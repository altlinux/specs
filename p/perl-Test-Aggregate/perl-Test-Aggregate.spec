%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Builder.pm) perl(Test/Builder/Module.pm) perl-devel perl-podlators perl(Test/Trap.pm)
# END SourceDeps(oneline)
Name:       perl-Test-Aggregate
Version:    0.371
Release:    alt1
# lib/Test/Aggregate.pm -> GPL+ or Artistic
# lib/Test/Aggregate/Builder.pm -> GPL+ or Artistic
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Aggregate C<*.t> tests to make them run faster
Source:     http://www.cpan.org/authors/id/R/RW/RWSTAUNER/Test-Aggregate-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Test-Aggregate
BuildArch:  noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(FindBin.pm)
BuildRequires: perl(Module/Build/Compat.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/NoWarnings.pm)
BuildRequires: perl(Test/Simple.pm)
# optional tests
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Pod/Coverage.pm)

### auto-added reqs!
Requires:       perl(FindBin.pm) >= 1.47
Requires:       perl(Test/Harness.pm) >= 3.09
Requires:       perl(Test/NoWarnings.pm)

### auto-added brs!
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/Most.pm)


Source44: import.info

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

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
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

