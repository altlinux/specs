%define _unpackaged_files_terminate_build 1
BuildRequires: libgmp-devel
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(Math/GMP.pm) perl(overload.pm) perl(subs.pm)
#BuildRequires: perl(Math/GMPf.pm) perl(Math/GMPz.pm) perl(Math/MPFR.pm)
# END SourceDeps(oneline)
%define module_name Math-GMPq
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.45
Release: alt1.1
Summary: perl interface to the GMP library's rational (mpq) functions..
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SI/SISYPHUS/%{module_name}-%{version}.tar.gz

%description
A bigrational module utilising the Gnu MP (GMP) library..
   Basically this module simply wraps all of the 'mpq'
   (rational number) functions provided by that library.
   The documentation below extensively plagiarises the GMP
   documentation (which can be found at http://gmplib.org).
   See also the Math::GMPq test suite for examples of usage.

   IMPORTANT:
    If your perl was built with '-Duse64bitint' you need to assign
    all integers larger than 52-bit in a 'use integer;' block. 
    Failure to do so can result in the creation of the variable as 
    an NV (rather than an IV) - with a resultant loss of precision.


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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1.1
- rebuild with new perl 5.26.1

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1.1
- rebuild with new perl 5.24.1

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1.1
- rebuild with new perl 5.20.1

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.36-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- initial import by package builder

