## SPEC file for Perl module Test::LectroTest

%define real_name Test-LectroTest

Name: perl-Test-LectroTest
Version: 0.5001
Release: alt3

Summary: Perl module for easy, automatic, specification-based tests

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Test-LectroTest

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Thu Aug 16 2018
# optimized out: perl perl-CPAN-Meta-Requirements perl-Devel-Symdump perl-Encode perl-Filter perl-JSON-PP perl-Parse-CPAN-Meta perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-parent python-base python-modules python3 python3-base python3-dev ruby sh3
BuildRequires: perl-CPAN-Meta perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module Test::LectroTest provides a simple (yet full featured)
interface to LectroTest, an automated, specification-based testing
system for Perl. To use it, declare properties that specify the
expected behavior of your software. LectroTest then checks your
software to see whether those properties hold.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/LectroTest*

%changelog
* Thu Aug 16 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.5001-alt3
- Initial build for ALT Linux Sisyphus
