%define _unpackaged_files_terminate_build 1
%define module_name Math-Decimal64
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(Math/LongDouble.pm) perl(overload.pm) perl(subs.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.16
Release: alt1.1
Summary: (alpha) perl interface to C's _Decimal64 operations.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SI/SISYPHUS/%{module_name}-%{version}.tar.gz

%description
Note that this module is alpha software. It seems to work ok
   for me on MS Windows (compiling with gcc-4.6.3, gcc-4.7.0)
   but, at time of release, is untested elsewhere.

   Math::Decimal64 supports up to 16 decimal digits of significand
   (mantissa) and an exponent range of -383 to +384.
   The smallest expressable value is -9.999999999999999e384 (which
   is also equivalent to -9999999999999999e369).
   The largest expressable value is 9.999999999999999e384 (which
   also equivalent to 9999999999999999e369).
   The closest we can get to zero is (plus or minus) 1e-384
   (which is also equivalent to 1000000000000000e-399).

   This module allows decimal floating point arithmetic via
   operator overloading - see "OVERLOADING".

   In the documentation that follows, "$mantissa" is a perl scalar
   holding a string of up to 16 decimal digits:
    $mantissa = '1234';
    $mantissa = '1234567890123456';

   For many values, it normally shouldn't matter if $mantissa is 
   assigned as a number:
    $mantissa = 1234;      # should work ok.

   But on some perls there are values that *need* to be assigned
   as a string. For example, on perls where nvtype is an 8 byte
   'double':
    $mantissa = '-9307199254740993'; # works fine
    $mantissa = -9307199254740993;   # will assign wrong value

   So ... where you see "$mantissa" in the following docs, think
   *string* of up to 16 decimal digits".


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- rebuild with new perl 5.24.1

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

