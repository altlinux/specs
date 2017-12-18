%define _unpackaged_files_terminate_build 1
%define module_name Math-Prime-Util-GMP
# BEGIN SourceDeps(oneline):
BuildRequires: libgmp-devel perl(Benchmark.pm) perl(Carp.pm) perl(Config.pm) perl(Devel/CheckLib.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/Util.pm) perl(Math/BigFloat.pm) perl(Math/BigInt.pm) perl(Math/Primality.pm) perl(Math/Prime/Util.pm) perl(Math/Prime/Util/ECAffinePoint.pm) perl(Test/More.pm) perl(Test/Perl/Critic.pm) perl(Text/ParseWords.pm) perl(Time/HiRes.pm) perl(XSLoader.pm) perl(base.pm) perl(threads.pm) perl(threads/shared.pm) perl(bigint.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.50
Release: alt1
Summary: Utilities related to prime numbers, using GMP
Group: Development/Perl
License: perl
URL: https://github.com/danaj/Math-Prime-Util-GMP

Source0: http://www.cpan.org/authors/id/D/DA/DANAJ/%{module_name}-%{version}.tar.gz

%description
A set of utilities related to prime numbers, using GMP.  This includes
primality tests, getting primes in a range, and factoring.

While it certainly can be used directly, the main purpose of this
module is for the Math::Prime::Util manpage.  That module will automatically
load this one if it is installed, greatly speeding up many of its
operations on big numbers.

Inputs and outputs for big numbers are via strings, so you do not need
to use a bigint package in your program.  However if you do use bigints,
inputs will be converted internally so there is no need to convert
before a call.  Output results are returned as either Perl scalars
(for native-size) or strings (for bigints).  the Math::Prime::Util manpage tries
to reconvert all strings back into the callers bigint type if possible,
which makes it more convenient for calculations.

The various `is_*_pseudoprime' tests are more appropriately called
`is_*_probable_prime' or `is_*_prp'.  They return 1 if the input is a
probable prime based on their test.  The naming convention is historical
and follows Pari, the Math::Primality manpage, and some other math packages.
The modern definition of pseudoprime is a *composite* that passes the
test, rather than any number.



%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes TODO examples
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Nov 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1.1
- automated CPAN update

* Wed Nov 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1.1
- rebuild with new perl 5.24.1

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1.1
- rebuild with new perl 5.22.0

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Jan 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- regenerated from template by package builder

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- regenerated from template by package builder

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- initial import by package builder

