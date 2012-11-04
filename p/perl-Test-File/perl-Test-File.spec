## SPEC file for Perl module Test::File

Name: perl-Test-File
Version: 1.34
Release: alt1

Summary: Perl module to test file attributes

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Test-File/
#URL: http://github.com/briandfoy/test-file/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Test-File
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch
Patch1: %real_name-1.34-alt-fix_tests.patch

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Nov 04 2012
# optimized out: perl-Devel-Symdump perl-Encode perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-podlators
BuildRequires: perl-Test-Manifest perl-Test-Pod perl-Test-Pod-Coverage

%description
Test::File provides a collection of test utilities for
file attributes.

%prep
%setup  -n %real_name-%version
%patch0 -p1

%patch1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test


%changelog
* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.34-alt1
- Initial build for ALT Linux Sisyphus

