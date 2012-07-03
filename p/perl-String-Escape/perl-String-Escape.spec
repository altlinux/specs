## SPEC file for Perl module String-Escape

%define version    2010.002
%define release    alt1
%define real_name  String-Escape

Name: perl-String-Escape
Version: %version
Release: %release

Summary: Perl module that provides conversion functions for escaped strings

License: %artistic_license
Group: Development/Perl
URL: http://search.cpan.org/~evo/String-Escape/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/E/EV/EVO/%real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

%description
String::Escape Perl module provides a flexible calling interface
to some frequently-performed string conversion functions,
including applying and expanding standard C/Unix-style backslash
escapes like \n and \t, wrapping and removing double-quotes, and
truncating to fit within a desired length.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/String/Escape*

%changelog
* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 2010.002-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2002.001-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2002.001-alt1
- Initial build for ALT Linux Sisyphus
