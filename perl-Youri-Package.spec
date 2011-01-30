%define upstream_name       Youri-Package
%define upstream_version    0.2.2
%define _requires_exceptions perl(\\(URPM\\|RPM.*\\|RPM4.*\\))

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Abstract package class
License:	GPL or Artistic
Group:		Development/Other
Url:		http://youri.zarb.org
Source0:	http://youri.zarb.or/download/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl(Youri::Package::RPM::Generator)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Expect)
BuildRequires:  perl(RPM)
BuildRequires:  perl(URPM)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl-version
Requires:       perl-version
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
YOURI stands for "Youri Offers an Upload & Repository Infrastucture". It aims
to build tools making management of a coherent set of packages easier.

This class provides an uniform view over various kind of packages.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# a problem in the chroot prevent expect-based signature test to work
#%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*
