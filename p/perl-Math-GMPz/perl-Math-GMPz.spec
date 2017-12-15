%define _unpackaged_files_terminate_build 1
BuildRequires: libgmp-devel
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(overload.pm) perl(subs.pm)
#BuildRequires: perl(Math/GMPf.pm) perl(Math/GMPq.pm) perl(Math/MPFR.pm)
# END SourceDeps(oneline)
%define module_name Math-GMPz
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.46
Release: alt1.1
Summary: perl interface to the GMP library's integer (mpz) functions..
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/S/SI/SISYPHUS/%{module_name}-%{version}.tar.gz

%description
A bignum module utilising the Gnu MP (GMP) library..
   Basically this module simply wraps nearly all of
   the integer functions provided by that library.
   The documentation below extensively plagiarises
   the documentation at http://gmplib.org.
   See the Math::GMPz test suite for examples of
   usage.


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
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1.1
- rebuild with new perl 5.26.1

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1.1
- rebuild with new perl 5.24.1

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1
- automated CPAN update

* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1.1
- rebuild with new perl 5.22.0

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1.1
- rebuild with new perl 5.20.1

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- initial import by package builder

