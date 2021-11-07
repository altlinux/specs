## SPEC file for Perl module Test::TrailingSpace
%define _unpackaged_files_terminate_build 1
%define real_name Test-TrailingSpace

Name: perl-Test-TrailingSpace
Version: 0.0601
Release: alt1

Summary: test for trailing space in source files

License: %mit
Group: Development/Perl

URL: https://metacpan.org/dist/Test-TrailingSpace/

Packager: Nikolay A. Fetisov <naf@altlinux.org>
BuildArch: noarch

Source: %real_name-%version.tar

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Nov 07 2021
# optimized out: libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Class-XSAccessor perl-Encode perl-File-Find-Object perl-JSON-PP perl-Module-Metadata perl-Number-Compare perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-Text-Glob perl-Tie-RefHash perl-autodie perl-devel perl-parent perl-podlators python3-base sh4
BuildRequires: perl-File-Find-Object-Rule perl-File-TreeCreate perl-HTML-Parser perl-Module-Build

%description
Perl module Test::TrailingSpace  is used to test for lack
of trailing space.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Test/TrailingSpace*

%changelog
* Sun Nov 07 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.0601-alt1
- New version
- Update URL

* Mon Jun 08 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.0600-alt1
- New version

* Sun May 24 2020 Nikolay A. Fetisov <naf@altlinux.org> 0.0400-alt1
- New version

* Wed Sep 04 2019 Nikolay A. Fetisov <naf@altlinux.org> 0.0302-alt1
- New version

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.0301-alt1
- New version

* Tue Jun 21 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.0300-alt1
- New version

* Sat Jun 06 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.0205-alt1
- New version

* Mon Sep 08 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.0204-alt3
- Rising release to override package from Autoimports/Sisyphus repository

* Sun Aug 31 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.0204-alt1
- Initial build

