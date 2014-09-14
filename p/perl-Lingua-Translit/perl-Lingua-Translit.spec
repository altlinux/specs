## SPEC file for Perl module Lingua::Translit

%define real_name Lingua-Translit

Name: perl-Lingua-Translit
Version: 0.20
Release: alt1

Summary: Perl module to transliterate text between writing systems

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Lingua-Translit/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Aug 04 2012
BuildRequires: perl-Encode perl-devel

%description
Perl module Lingua::Translit can be used to convert text from one
writing system to another, based on national or international
transliteration tables. Where possible a reverse transliteration
is supported.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Lingua/Translit*
%_bindir/translit

%changelog
* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version

* Sat Aug 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- Initial build for ALT Linux Sisyphus
