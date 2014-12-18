# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-Time-Warp 
Version:    0.51
Release:    alt1.1_1
# Warp.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Perl
Summary:    Control over the flow of time
Source:     http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/Time-Warp-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Time-Warp
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Optional run-time:
BuildRequires:  perl(Time/HiRes.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info

%description
Our external experience unfolds in 3 1/2 dimensions (time has a
dimensionality of 1/2). The Time::Warp module offers developers control
over the measurement of time.

%prep
%setup -q -n Time-Warp-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/*

%changelog
* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1.1_1
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1.1
- rebuild with new perl 5.20.1

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt5_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt5_15
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt5_14
- update to new release by fcimport

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 0.5-alt5
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_14
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_13
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_12
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt4_11
- moved to Sisyphus (Tapper dep)

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.5-alt3_11
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_11
- update to new release by fcimport

* Tue Jun 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_9
- fixed provides

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_9
- fc import

