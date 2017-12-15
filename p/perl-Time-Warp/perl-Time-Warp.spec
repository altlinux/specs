Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       perl-Time-Warp 
Version:    0.52
Release:    alt1_8.1
License:    GPL+ or Artistic 
Summary:    Control over the flow of time
Source:     http://search.cpan.org/CPAN/authors/id/S/SZ/SZABGAB/Time-Warp-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Time-Warp
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
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
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} +
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_8.1
- rebuild with new perl 5.26.1

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_8
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_5
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_4.1
- rebuild with new perl 5.24.1

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_4
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_3
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_2.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_2
- update to new release by fcimport

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

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

