## SPEC file for Perl module UNIVERSAL-can

Name: perl-UNIVERSAL-can
Version: 1.20110617
Release: alt1

Summary: Perl module UNIVERSAL::can

License: %perl_license
Group: Development/Perl

%define real_name UNIVERSAL-can
URL: http://search.cpan.org/dist/UNIVERSAL-can/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(Pre): perl-devel, perl-Module-Build, rpm-build-licenses

%description
Perl module UNIVERSAL::can attempts to work around people calling
UNIVERSAL::can() as a function, which it is not.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/UNIVERSAL/can.pm


%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.20110617-alt1
- New version 1.20110617

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Mar 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.16-alt1
- New version 1.16

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.15-alt1
- New version 1.15

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.12-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.12-alt0
- Initial build
