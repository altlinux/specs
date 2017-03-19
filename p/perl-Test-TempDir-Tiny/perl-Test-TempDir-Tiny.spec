## SPEC file for Perl module Test::TempDir::Tiny

%define real_name Test-TempDir-Tiny

Name: perl-Test-TempDir-Tiny
Version: 0.016
Release: alt2

Summary: Perl module to keep test directories if tests fail

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-TempDir-Tiny/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

%description
Perl module Test::TempDir::Tiny works with Test::More to create
temporary directories that stick around if tests fail.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/TempDir/Tiny*

%changelog
* Sun Mar 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.016-alt2
- Initial build for ALT Linux Sisyphus
