# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(IO/File.pm) perl(Test/More.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-YAML-Meta
Version:        0.21
Release:        alt1
Summary:        Validation of the META.yml file in a distribution
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-YAML-Meta/
Source:        http://www.cpan.org/authors/id/B/BA/BARBIE/Test-YAML-Meta-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/YAML/Valid.pm)
BuildRequires:  perl(Test/CPAN/Meta/YAML.pm)
BuildRequires:  perl(YAML.pm)
BuildRequires:  perl(YAML/Syck.pm)
Source44: import.info

%description
This module was written to ensure that a META.yml file, provided with a
standard distribution uploaded to CPAN, meets the specifications that
slowly being introduced to module uploads, via the use of
ExtUtils::MakeMaker, Module::Build and Module::Install.

%prep
%setup -q -n Test-YAML-Meta-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}
mv LICENSE LICENSE.in
iconv -fiso88591 -tutf8 -oLICENSE LICENSE.in
rm LICENSE.in

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README examples
%dir %{perl_vendor_privlib}/Test/
%dir %{perl_vendor_privlib}/Test/YAML/
%{perl_vendor_privlib}/Test/YAML/Meta.pm

%changelog
* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_2
- fc import

