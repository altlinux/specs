## SPEC file for Perl module Test::File

Name: perl-Test-File
Version: 1.992
Release: alt1

Summary: Perl module to test file attributes

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Test-File/
#URL: http://github.com/briandfoy/test-file/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

%define real_name Test-File
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Devel-Symdump perl-Encode perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel perl-parent perl-unicore python-base python-modules python3-base
BuildRequires: libnss-mymachines perl-Test-Manifest perl-Test-Pod perl-Test-Pod-Coverage perl-Test-utf8

## REMOVE THESE:
# We need Builder.pm >= 1.001.016. Wait for it.
BuildRequires: perl-devel >= 5.20

%description
Test::File provides a collection of test utilities for
file attributes.

%prep
%setup  -n %real_name-%version
%patch0 -p1

rm -f -- t/win32.t t/normalize.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.pod
%perl_vendor_privlib/Test


%changelog
* Mon Dec 05 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.992-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 1.991-alt1
- New version

* Sat Mar 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.448-alt1
- New version

* Tue Mar 09 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.447-alt1
- New version

* Tue Apr 25 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.443-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.442-alt1
- New version

* Sun Oct 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.44-alt1
- New version

* Sat Oct 12 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.35-alt1
- New version

* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.34-alt1
- Initial build for ALT Linux Sisyphus

