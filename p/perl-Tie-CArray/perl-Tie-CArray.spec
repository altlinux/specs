## SPEC file for Perl module Tie::CArray

%define real_name Tie-CArray

Name: perl-Tie-CArray
Version: 0.15
Release: alt3.1.1.1

Summary: space-efficient, typed, external C Arrays

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Tie-CArray/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

%description
Perl module Tie::CArray provides several XS classes and methods
to deal with typed, space-efficient C arrays.

For the three basic C-types array of INT, DOUBLE and STRING
and some sequential aggregate types int[2][], int[3][], int[4][],
double[2][], double[3][] hand-optimized, fast XS versions
are provided.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Tie/CArray*
%perl_vendor_autolib/Tie/CArray*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt3.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt3.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt3.1
- rebuild with new perl 5.22.0

* Mon Jun 08 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.15-alt3
- Initial build for ALT Linux Sisyphus
