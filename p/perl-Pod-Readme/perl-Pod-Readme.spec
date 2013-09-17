# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(IO/File.pm) perl(Pod/PlainText.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define module_version 0.11

Name:           perl-Pod-Readme
Version:        0.110
Release:        alt3_9
Summary:        Convert POD to README file
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Pod-Readme/
Source0:        http://www.cpan.org/authors/id/B/BI/BIGPRESH/Pod-Readme-%{module_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Regexp/Common.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Portability/Files.pm)
Source44: import.info

%description
This module is a subclass of Pod::PlainText which provides additional POD
markup for generating README files.

%prep
%setup -q -n Pod-Readme-%{module_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install

make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
DEVEL_TESTS=1 make test

%files
%doc Changes README
%{_bindir}/*
%{perl_vendor_privlib}/*
%{_mandir}/man1/*

%changelog
* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt3_9
- Sisyphus build; switch to fc import

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.110-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.110-alt1_4
- fc import

