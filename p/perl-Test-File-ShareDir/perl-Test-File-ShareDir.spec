## SPEC file for Perl module Test::File::ShareDir

Name: perl-Test-File-ShareDir
Version: 1.001002
Release: alt1

Summary: Create a Fake ShareDir for your modules for testing

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Test-File-ShareDir/
#URL: https://github.com/kentfredric/Test-File-ShareDir

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Test-File-ShareDir
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses perl-devel

# Automatically added by buildreq on Sat Jun 06 2015
# optimized out: perl-CPAN-Meta-Requirements perl-Class-Inspector perl-Parse-CPAN-Meta perl-Try-Tiny perl-devel perl-parent
BuildRequires: perl-CPAN-Meta perl-Class-Tiny perl-File-Copy-Recursive perl-File-ShareDir perl-Path-Tiny perl-Scope-Guard perl-Sub-Name perl-Test-Fatal

%description
Test::File::ShareDir is a Perl module to create a Fake ShareDir
for your modules for testing.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test/File/ShareDir*


%changelog
* Sat Mar 18 2017 Nikolay A. Fetisov <naf@altlinux.org> 1.001002-alt1
- New version

* Sat Jun 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.001001-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.000005-alt1
- New version

* Sun Oct 06 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.3-alt1
- New version

* Sun Nov 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux Sisyphus

