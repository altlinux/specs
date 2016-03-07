# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Perl-MinimumVersion
Version:        1.38
Release:        alt1_9
Summary:        Find a minimum required version of perl for Perl code
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Perl-MinimumVersion/
Source0:        http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/Perl-MinimumVersion-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
# Run-time and tests:
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(Params/Util.pm)
BuildRequires: perl(Perl/Critic/Utils.pm)
BuildRequires: perl(PPI.pm)
BuildRequires: perl(PPI/Util.pm)
BuildRequires: perl(PPIx/Regexp.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(vars.pm)
BuildRequires: perl(version.pm)
BuildRequires: perl(warnings.pm)
%if !%{defined perl_bootstrap}
BuildRequires: perl(File/Find/Rule.pm)
BuildRequires: perl(File/Find/Rule/Perl.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Script.pm)
%endif

# Remove under-specified dependencies



Source44: import.info
%filter_from_requires /^perl\\(version.pm\\)$/d
%filter_from_requires /^perl\\(Params.Util.pm\\)$/d
%filter_from_requires /^perl >= 0:5.005$/d

%description
Find a minimum required version of perl for Perl code

%prep
%setup -q -n Perl-MinimumVersion-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
make test
%endif

%files
%doc Changes
%doc LICENSE
%{_bindir}/*
%{perl_vendor_privlib}/Perl
%{_mandir}/man1/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_4
- update to new release by fcimport

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1_1
- update to new release by fcimport

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.37-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_3
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_2
- fc update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt3_8
- no bootstrap

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2_8
- moved to Sisyphus (bootstrap)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_7
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_4
- fc import

