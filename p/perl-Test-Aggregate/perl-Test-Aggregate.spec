%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test/NoWarnings.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-Test-Aggregate
Version:    0.372
Release:    alt1
# lib/Test/Aggregate.pm -> GPL+ or Artistic
# lib/Test/Aggregate/Builder.pm -> GPL+ or Artistic
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Aggregate *.t tests to make them run faster
Source:     http://www.cpan.org/authors/id/R/RW/RWSTAUNER/Test-Aggregate-%{version}.tar.gz
# Do not touch Test::Builder internals that will change in 2.0, CPAN RT#64604
Patch0:     Test-Aggregate-0.371-Don-t-grab-at-Test-Builder-hash-keys.patch
Url:        http://search.cpan.org/dist/Test-Aggregate
BuildArch:  noarch

BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Builder/Module.pm)
BuildRequires:  perl(Test/More.pm)
# Test::NoWarnings not used at tests
BuildRequires:  perl(vars.pm)
# Optional run-time:
BuildRequires:  perl(Data/Dump/Streamer.pm)
# Tests:
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Trap.pm)
Requires:       perl(FindBin.pm) >= 1.47
Requires:       perl(Test/NoWarnings.pm)


# Filter under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\(FindBin.pm\\)$/d

%description
*WARNING*: this is ALPHA code. The interface is not guaranteed to be
stable.

A common problem with many test suites is that they can take a
long time to run. The longer they run, the less likely you are to run
the tests. This module borrows a trick from 'Apache::Registry' to load
up your tests at once, create a separate package for each test and wraps
each package in a method named 'run_the_tests'. This allows us to load
perl only once and related modules only once. If you have modules which
are expensive to load, this can dramatically speed up a test suite.

%prep
%setup -q -n Test-Aggregate-%{version}
%patch0 -p1

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install 'destdir=%{buildroot}' create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.372-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.371-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.371-alt1_3
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.371-alt1_2
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.371-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.370-alt1
- automated CPAN update

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.369-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.366-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.364-alt3_6
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.364-alt3_5
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.364-alt2_5
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.364-alt2_3
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.364-alt1_3
- fc import

