## SPEC file for Perl module Perl::Version

%define real_name Perl-Version

Name: perl-Perl-Version
Version: 1.011
Release: alt1

Summary: Perl module to parse and manipulate Perl version strings

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Perl-Version/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Devel-Symdump perl-Encode perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-podlators
BuildRequires: perl-File-Slurp perl-Test-Pod perl-Test-Pod-Coverage

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
%doc README Changes
%perl_vendor_privlib/Perl/Version*

%_bindir/perl-reversion

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.011-alt1
- Initial build for ALT Linux Sisyphus
