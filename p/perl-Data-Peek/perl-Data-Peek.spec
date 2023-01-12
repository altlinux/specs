%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run optional test
%{bcond_without perl_Data_Peek_enables_option_test}

Name:           perl-Data-Peek
Version:        0.52
Release:        alt1
Summary:        Collection of low-level debug facilities
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Data-Peek
Source0:        http://www.cpan.org/authors/id/H/HM/HMBRAND/Data-Peek-%{version}.tgz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
# Run-time:
BuildRequires:  perl(bytes.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(XSLoader.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Warnings.pm)
%if %{with perl_Data_Peek_enables_option_test}
# Optional tests:
BuildRequires:  perl(Perl/Tidy.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%endif


Source44: import.info

%description
Data::Peek started off as DDumper being a wrapper module over Data::Dumper,
but grew out to be a set of low-level data introspection utilities that no
other module provided yet, using the lowest level of the perl internals API
as possible.

%prep
%setup -q -n Data-Peek-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{make_build}

%install
%{makeinstall_std}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README CONTRIBUTING.md examples
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Data*
%{perl_vendor_archlib}/DP.pm

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.52-alt1
- automated CPAN update

* Thu Apr 07 2022 Igor Vlasenko <viy@altlinux.org> 0.51-alt2_2
- to Sisyphus as IO-Compress dep

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.51-alt1_2
- update to new release by fcimport

* Thu Jan 20 2022 Igor Vlasenko <viy@altlinux.org> 0.51-alt1_1
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.50-alt3_4
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.50-alt3_3
- update to new release by fcimport

* Wed Jun 16 2021 Cronbuild Service <cronbuild@altlinux.org> 0.50-alt3_2
- rebuild to get rid of unmets

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.50-alt2_2
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.50-alt2_1
- update to new release by fcimport

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1_1
- update to new release by fcimport

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.49-alt2_3
- rebuild with perl 5.30

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_3
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_2
- update to new release by fcimport

* Thu Feb 27 2020 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1_1
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.48-alt3_7
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.48-alt3_6
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.48-alt3_5
- update to new release by fcimport

* Tue Jan 29 2019 Cronbuild Service <cronbuild@altlinux.org> 0.48-alt3_4
- rebuild to get rid of unmets

* Tue Jan 29 2019 Cronbuild Service <cronbuild@altlinux.org> 0.48-alt2_4
- rebuild to get rid of unmets

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1_4
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1_3
- update to new release by fcimport

* Thu Mar 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1_2
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1_3
- update to new release by fcimport

* Mon Feb 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1_2
- update to new release by fcimport

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.46-alt3_3
- rebuild with perl 5.26

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.46-alt2_3
- update to new release by fcimport

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.46-alt2_2
- rebuild to get rid of unmets

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1_2
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_1
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.44-alt2_3
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1_3
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1_1
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.41-alt2_1
- rebuild to get rid of unmets

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_4
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_2
- update to new release by fcimport

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_1
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.39-alt2_1
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_3
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_2
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.33-alt2_5
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1_5
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1_3
- fc import

