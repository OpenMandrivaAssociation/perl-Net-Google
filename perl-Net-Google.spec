%define module	Net-Google
%define name	perl-%{module}
%define version 1.0.1
%define release 9

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simple OOP-ish interface to the Google SOAP API
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Module::Build)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Provides a simple OOP-ish interface to the Google SOAP API

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
# checking requires a Google API key

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2010.0
+ Revision: 430510
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 241773
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdv2008.0
+ Revision: 25450
- rebuild

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-3mdv2008.0
+ Revision: 25277
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.0.1-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Wed Jan 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdk
- New release 1.0.1

* Mon Dec 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-1mdk
- New release 1.0
- spec cleanup
- better URL
- fix directory ownership
- switch to Module::Build

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.62-1mdk
- initial Mandriva package

