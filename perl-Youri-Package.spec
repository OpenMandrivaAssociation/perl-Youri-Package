%define upstream_name       Youri-Package
%define upstream_version    0.2.4
%define __noautoreq 'perl\\((URPM|RPM.*|RPM4.*)\\)'

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Abstract package class
License:	GPLv1+ or Artistic
Group:		Development/Other
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GR/GROUSSE/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl(Youri::Package::RPM::Generator)
BuildRequires:	perl-JSON-PP
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Expect)
BuildRequires:	perl(RPM)
BuildRequires:	perl(URPM)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl-version
BuildRequires:	perl-devel
BuildRequires:  gnupg
Requires:		perl-version
BuildArch:		noarch

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

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Youri
%{_mandir}/man3/*


%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.2.2-2mdv2011.0
+ Revision: 640784
- rebuild to obsolete old packages

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-1
+ Revision: 634184
- new version

* Sat Jan 29 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1
+ Revision: 633915
- new version

* Thu Jan 27 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-2
+ Revision: 633182
- disable tests as long as the chroot issue with /dev/tty exists
- no dependency on RPM bindings (only one is needed)

* Sat Jan 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.0-1
+ Revision: 632221
- new version
- dropped rpm5 patch, merged upstream

* Wed Jan 19 2011 Eugeni Dodonov <eugeni@mandriva.com> 0.1.1-8
+ Revision: 631702
- Rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - merge rpm5 branch

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.1-6mdv2011.0
+ Revision: 430673
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1.1-4mdv2009.0
+ Revision: 268886
- rebuild early 2009.0 package (before pixel changes)

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-3mdv2009.0
+ Revision: 210963
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-2mdv2008.0
+ Revision: 17200
- force dependency on perl-version

* Sun Apr 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-1mdv2008.0
+ Revision: 17031
- Import perl-Youri-Package

