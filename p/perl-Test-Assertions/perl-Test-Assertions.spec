# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/Spec/Functions.pm) perl(Test/More.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Assertions
Version:        1.054
Release:        alt2_11
Summary:        Simple set of building blocks for both unit and runtime testing
License:        GPLv2
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Assertions/
Source0:        http://www.cpan.org/authors/id/B/BB/BBC/Test-Assertions-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Log/Trace.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
Test::Assertions provides a convenient set of tools for constructing tests,
such as unit tests or run-time assertion checks (like C's ASSERT macro).
Unlike some of the Test:: modules available on CPAN, Test::Assertions is
not limited to unit test scripts; for example it can be used to check
output is as expected within a benchmarking script. When it is used for
unit tests, it generates output in the standard form for CPAN unit testing
(under Test::Harness).

%prep
%setup -q -n Test-Assertions-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.054-alt2_11
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.054-alt1_11
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.054-alt1_9
- fc import

