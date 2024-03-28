## SPEC file for Perl module Perl::Version

%define real_name Perl-Version

Name: perl-Perl-Version
Version: 1.017
Release: alt1

Summary: Perl module to parse and manipulate Perl version strings

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Perl-Version/
#URL: https://github.com/briandfoy/perl-version

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: perl-Devel-Symdump perl-Encode perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-Pod-Usage perl-devel perl-podlators
BuildRequires: perl-File-Slurp-Tiny perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Perl::Version provides a simple interface for parsing,
manipulating and formatting Perl version strings.

Unlike version.pm (which concentrates on parsing and comparing
version strings) Perl::Version is designed for cases where you'd
like to parse a version, modify it and get back the modified
version formatted like the original.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod Changes
%perl_vendor_privlib/Perl/Version*

%_bindir/perl-reversion
%_man1dir/perl-reversion*

%changelog
* Thu Mar 28 2024 Nikolay A. Fetisov <naf@altlinux.org> 1.017-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.013-alt1
- New version

* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.011-alt1
- Initial build for ALT Linux Sisyphus
