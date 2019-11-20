Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Perl-MinimumVersion
Version:        1.38
Release:        alt1_23
Summary:        Find a minimum required version of perl for Perl code
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl-MinimumVersion
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Perl-MinimumVersion-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: rpm-build-perl
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
%filter_from_requires /^perl(version.pm)/d
%filter_from_requires /^perl(Params.Util.pm)/d
%filter_from_requires /^perl >= 0:5.005$/d

%description
Find a minimum required version of perl for Perl code

%prep
%setup -q -n Perl-MinimumVersion-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
make test
%endif

%files
%doc Changes
%doc --no-dereference LICENSE
%{_bindir}/*
%{perl_vendor_privlib}/Perl
%{_mandir}/man1/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_23
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_18
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_15
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1_11
- update to new release by fcimport

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

