## SPEC file for Perl module Encode-Escape

%define version    0.14
%define release    alt1
%define real_name  Encode-Escape

Name: perl-Encode-Escape
Version: %version
Release: alt1.1

Summary: Perl extension for Encodings of various escape sequences

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~you/Encode-Escape/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/Y/YO/YOU/%real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Dec 15 2008
BuildRequires: perl-Encode perl-Module-Build

%description
Encode::Escape  Perl module is  a wrapper class  for encodings
of escape sequences in strings.  It is NOT for an escape-based
encoding (eg. ISO-2022-JP). It is for encoding/decoding escape
sequences, generally used in source codes.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Encode/Escape*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt1
- Initial build for ALT Linux Sisyphus
