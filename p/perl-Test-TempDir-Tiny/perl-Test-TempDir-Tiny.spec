## SPEC file for Perl module Test::TempDir::Tiny

%define real_name Test-TempDir-Tiny

Name: perl-Test-TempDir-Tiny
Version: 0.018
Release: alt1

Summary: Perl module to keep test directories if tests fail

License: %asl 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/Test-TempDir-Tiny/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 10 2019
# optimized out: gem-power-assert perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-parent python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4
BuildRequires: perl-CPAN-Meta perl-Capture-Tiny

%description
Perl module Test::TempDir::Tiny works with Test::More to create
temporary directories that stick around if tests fail.

%prep
%setup -q -n %real_name-%version

# Low required File::Temp version: no need in code,
# and we don't have 0.2308:
sed -e 's/0\.2308/0.2304/' -i lib/Test/TempDir/Tiny.pm
sed -e 's/0\.2308/0.2304/' -i t/00-report-prereqs.dd
sed -e 's/0\.2308/0.2304/' -i Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/TempDir/Tiny*

%changelog
* Fri May 10 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.018-alt1
- New version

* Wed May 09 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.017-alt1
- New version

* Sun Mar 19 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.016-alt2
- Initial build for ALT Linux Sisyphus
