%define _unpackaged_files_terminate_build 1
%define module_name Math-MPFR
# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel libmpfr-devel perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(Math/GMP.pm) perl(Math/GMPf.pm) perl(Math/GMPq.pm) perl(Math/GMPz.pm) perl(Math/LongDouble.pm) perl(Math/Trig.pm) perl(overload.pm) perl(subs.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators
%ifnarch %e2k %arm aarch64 loongarch64 riscv64
BuildRequires: perl(Math/Decimal64.pm)
%endif
# see the latest GCC spec
%define libquadmath_arches	%ix86 x86_64 ppc64le
# not needed for now, but safe due to -Wl,as-needed
%ifarch %libquadmath_arches
BuildRequires: libquadmath-devel
%endif

Packager: Igor Vlasenko <viy@altlinux.org>

Name: perl-%module_name
Version: 4.38
Release: alt1.1
Summary: perl interface to the MPFR (floating point) library..
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SI/SISYPHUS/%{module_name}-%{version}.tar.gz

%description
A bigfloat module utilising the MPFR library. Basically.
   this module simply wraps the 'mpfr' floating point functions
   provided by that library.
   Operator overloading is also available.
   The following documentation heavily plagiarises the mpfr
   documentation.
   See also the Math::MPFR test suite for some examples of usage.

%prep
%setup -q -n %{module_name}-%{version}

%ifnarch libquadmath_arches
# These test don't try to detect long double presence
# and just fail. Skip them when libquadmath is not available.
rm -vf t/LongDouble.t t/uselongdouble.t
%endif

# todo: MPFR?
%ifarch ppc64le
#expected 1.00000000000000000000000000000001, got 9.99999999999999999999999999999991
rm t/LongDouble.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Fri Apr 04 2025 Ivan A. Melnikov <iv@altlinux.org> 4.38-alt1.1
- NMU: fix FTBFS on loongarch64 and riscv64
  + disable Math/Decimal64 BR on loongarch64 and riscv64,
    as decimal floating-point not supported by GCC on
    these platforms
  + copy libquadmath_arches definition from gcc14 spec
    and skip BR on libquadmath-devel and long double
    tests there
  + enable building on aarch64, as now it should work, too.

* Thu Apr 03 2025 Igor Vlasenko <viy@altlinux.org> 4.38-alt1
- automated CPAN update

* Mon Jan 15 2024 Igor Vlasenko <viy@altlinux.org> 4.28-alt1
- automated CPAN update

* Thu Jun 22 2023 Igor Vlasenko <viy@altlinux.org> 4.27-alt1
- automated CPAN update

* Mon Mar 20 2023 Igor Vlasenko <viy@altlinux.org> 4.26-alt1
- automated CPAN update

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 4.25-alt1
- automated CPAN update

* Wed Jun 15 2022 Igor Vlasenko <viy@altlinux.org> 4.24-alt1
- automated CPAN update

* Fri May 20 2022 Igor Vlasenko <viy@altlinux.org> 4.23-alt1
- automated CPAN update

* Mon Apr 11 2022 Igor Vlasenko <viy@altlinux.org> 4.22-alt1
- automated CPAN update

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 4.21-alt1
- automated CPAN update

* Tue Feb 08 2022 Igor Vlasenko <viy@altlinux.org> 4.19-alt1
- automated CPAN update

* Tue Nov 23 2021 Igor Vlasenko <viy@altlinux.org> 4.18-alt1
- automated CPAN update

* Fri Sep 17 2021 Igor Vlasenko <viy@altlinux.org> 4.17-alt1
- automated CPAN update

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 4.16-alt1
- automated CPAN update

* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 4.14-alt2
- ppc64le build

* Mon Sep 21 2020 Igor Vlasenko <viy@altlinux.ru> 4.14-alt1
- updated exlusive arch
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.12-alt1
- automated CPAN update

* Sat Apr 13 2019 Michael Shigorin <mike@altlinux.org> 4.11-alt2
- support e2kv4 through %%e2k macro use

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 4.11-alt1
- automated CPAN update

* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 4.09-alt1
- automated CPAN update

* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 4.08-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 4.06-alt1.1
- rebuild with new perl 5.28.1

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 4.06-alt1
- automated CPAN update

* Sun Oct 28 2018 Igor Vlasenko <viy@altlinux.ru> 4.05-alt1
- automated CPAN update

* Wed May 09 2018 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- automated CPAN update

* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 4.03-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 4.02-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 4.01-alt1
- automated CPAN update

* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1
- automated CPAN update

* Sat Dec 23 2017 Michael Shigorin <mike@altlinux.org> 3.36-alt2
- E2K: avoid gcc-specific BR: perl-Math-Decimal64 (closes: #34380)

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.36-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 3.36-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 3.35-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 3.34-alt1.1
- rebuild with new perl 5.24.1

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 3.34-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 3.33-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 3.32-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 3.30-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 3.29-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 3.28-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 3.25-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.25-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 3.24-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 3.22-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.21-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 3.21-alt1
- regenerated from template by package builder

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 3.18-alt1
- initial import by package builder

