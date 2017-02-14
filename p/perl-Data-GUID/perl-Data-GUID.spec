%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Data-GUID
Version:        0.049
Release:        alt1
Summary:        Globally unique identifiers
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Data-GUID/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Data-GUID-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/UUID.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Sub/Exporter.pm)
BuildRequires:  perl(Sub/Install.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

# tests
BuildRequires:  perl(Test/More.pm)
Source44: import.info


%description
Data::GUID provides a simple interface for generating and using globally
unique identifiers.

%prep
%setup -q -n Data-GUID-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%doc LICENSE
%{perl_vendor_privlib}/*

%changelog
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

