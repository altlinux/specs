%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(Exporter.pm) perl(FindBin.pm) perl(Math/BigInt.pm) perl(Math/BigRat.pm) perl(Math/Complex.pm) perl(Math/Symbolic.pm) perl(Math/Symbolic/Derivative.pm) perl(Test.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_name Math-Polynomial
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.014
Release: alt1
Summary: Perl class for polynomials in one variable
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MH/MHASCH/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/M*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.013-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.011-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.009-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.008-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.007-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.005-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1
- initial import by package builder

