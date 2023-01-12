%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Data-GUID
%define upstream_version 0.050

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    0.051
Release:    alt1

Summary:    Globally unique identifiers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/authors/id/R/RJ/RJBS/%{upstream_name}-%{version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Data/UUID.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Sub/Install.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(bytes.pm)
BuildRequires: perl(overload.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
Data::GUID provides a simple interface for generating and using globally
unique identifiers.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make_build

%check
%make_build test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml README
%{perl_vendor_privlib}/*

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 0.051-alt1
- automated CPAN update

* Mon Jul 05 2021 Igor Vlasenko <viy@altlinux.org> 0.050-alt1_1
- update by mgaimport

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.org> 0.050-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1_10
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1_6
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1_2
- update to new release by fcimport

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.049-alt1
- automated CPAN update

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2_2
- update to new release by fcimport

* Fri Mar 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.048-alt2_1
- moved to Sisyphus as dependency

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.048-alt1_1
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.047-alt2_2
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.047-alt2_1
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1_1
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.046-alt1_1
- converted for ALT Linux by srpmconvert tools

