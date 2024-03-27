## SPEC file for Perl module Test::Regexp

%define real_name Test-Regexp

%define _unpackaged_files_terminate_build 1

Name: perl-Test-Regexp
Version: 2017040101
Release: alt2

Summary: Perl module to test regular expressions

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Test-Regexp

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Wed Mar 27 2024
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Devel-Symdump perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-parent python-modules python2-base python3 python3-base python3-dev sh5
BuildRequires: perl-CPAN-Meta perl-Test-Pod perl-Test-Pod-Coverage perl-unicore

%description
Perl module Test::Regexp is intended to test your regular expressions.
Given a subject string and a regular expression (aka pattern),
the module not only tests whether the regular expression complete
matches the subject string, it performs a utf8::upgrade or
utf8::downgrade on the subject string and performs the tests again,
if necessary. Furthermore, given a pattern with capturing parenthesis,
it checks whether all captures are present, and in the right order.
Both named and unnamed captures are checked.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Test/Regexp*

%changelog
* Wed Mar 27 2024 Nikolay A. Fetisov <naf@altlinux.org> 2017040101-alt2
- Bump release to override autoimports package

* Wed Mar 27 2024 Nikolay A. Fetisov <naf@altlinux.org> 2017040101-alt1
- Initial build for ALT Linux Sisyphus
