## SPEC file for Perl module Test::PerlTidy

%define real_name Test-PerlTidy

Name: perl-Test-PerlTidy
Version: 20130104
Release: alt2

Summary: Perl module to check that all project files are tidy

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-PerlTidy/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Mon Jun 27 2016
# optimized out: perl perl-Algorithm-Diff perl-Encode perl-parent python-base python-modules python3
BuildRequires: perl-File-Finder perl-File-Slurp perl-Perl-Tidy perl-Text-Diff perl-devel

%description
Perl module Test::PerlTidy provides a check during the tests that
that all the perl files included with the distribution are tidy.
If you make any changes please remember to tidy them.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_privlib/Test/PerlTidy*

%changelog
* Mon Jun 27 2016 Nikolay A. Fetisov <naf@altlinux.ru> 20130104-alt2
- Initial build for ALT Linux Sisyphus
