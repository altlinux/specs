## SPEC file for Perl module UNIVERSAL-isa

Name: perl-UNIVERSAL-isa
Version: 1.20110614
Release: alt1

Summary: Perl module UNIVERSAL::isa

License: %perl_license
Group: Development/Perl

%define real_name UNIVERSAL-isa
URL: http://search.cpan.org/dist/UNIVERSAL-isa/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jun 21 2011
BuildRequires: perl-CGI perl-devel

%description
Perl module UNIVERSAL::isa attempts to work around people calling
UNIVERSAL::isa() as a function, which it is not.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/UNIVERSAL/isa.pm


%changelog
* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.20110614-alt1
- New version 1.20110614

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt1
- New version 1.03

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.01-alt1
- New version 1.01

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt0
- Initial build
