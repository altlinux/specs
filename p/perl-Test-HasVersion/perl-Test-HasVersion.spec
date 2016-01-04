%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-HasVersion
Version:        0.014
Release:        alt1
Summary:        Check Perl modules have version numbers
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-HasVersion/
Source:        http://www.cpan.org/authors/id/F/FE/FERREIRA/Test-HasVersion-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


Source44: import.info

%description
Do you wanna check that every one of your Perl modules in a distribution
has a version number? You wanna make sure you don't forget the brand new
modules you just added? Well, that's the module you have been looking
for. Use it!

%prep
%setup -q -n Test-HasVersion-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendor_privlib}/*

%changelog
* Mon Jan 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_13
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_10
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt3_9
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_4
- fc import

