## SPEC file for Perl module Lingua::Translit

%define real_name Lingua-Translit

Name: perl-Lingua-Translit
Version: 0.29
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

# Automatically added by buildreq on Sun Aug 30 2015
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple
BuildRequires: perl-devel perl-podlators perl-unicore

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
%_man1dir/translit*

%changelog
* Sun Dec 04 2022 Nikolay A. Fetisov <naf@altlinux.org> 0.29-alt1
- New version

* Sun Nov 12 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.28-alt1
- New version

* Mon May 01 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.27-alt1
- New version

* Sat May 28 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.26-alt1
- New version

* Sun Nov 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.24-alt1
- New version

* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.22-alt1
- New version

* Wed Oct 29 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.21-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- New version

* Sat Aug 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.19-alt1
- Initial build for ALT Linux Sisyphus
