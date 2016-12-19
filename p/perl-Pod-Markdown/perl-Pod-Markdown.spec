# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Usage.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Pod-Markdown
Version:        3.005
Release:        alt1_2
Summary:        Convert POD to Markdown
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Pod-Markdown/
Source0:        http://www.cpan.org/authors/id/R/RW/RWSTAUNER/Pod-Markdown-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(Pod/Simple.pm)
BuildRequires:  perl(Pod/Simple/Methody.pm)
# Tests:
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Symbol.pm)
BuildRequires:  perl(Test/Differences.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(version.pm)
Source44: import.info

%description
This module subclasses Pod::Parser and converts POD to Markdown.

%prep
%setup -q -n Pod-Markdown-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/*
%{_mandir}/man[13]/*
%{_bindir}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 3.005-alt1_2
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 3.005-alt1_1
- update to new release by fcimport

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 3.005-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1_1
- update to new release by fcimport

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.003-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.002-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1_1
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.002-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.001-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.001-alt1_1
- update to new release by fcimport

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.001-alt1
- automated CPAN update

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1_1
- update to new release by fcimport

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1
- automated CPAN update

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.500-alt1_1
- update to new release by fcimport

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.500-alt1
- automated CPAN update

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.401-alt1_1
- update to new release by fcimport

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.401-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.400-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt2_4
- Sisyphus build; switch to fc import

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1_2
- initial fc import

