# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-Portability-Files
Version:        0.05
Release:        alt2_20
Summary:        Check file names portability
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Test-Portability-Files/
Source0:        http://www.cpan.org/authors/id/S/SA/SAPER/Test-Portability-Files-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Spec.pm)
#BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
This module is used to check the portability across operating systems of
the names of the files present in the distribution of a module. The tests
use the advices given in "Files and Filesystems" in perlport. The author of
a distribution can select which tests to execute.

%prep
%setup -q -n Test-Portability-Files-%{version}

%build
#%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
#./Build
make

%install

#./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
make install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
#./Build test
make test

%files
%doc Changes LICENSE LICENSE.Artistic LICENSE.GPL README
%{perl_vendor_privlib}/*

%changelog
* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_20
- Sisyphus build; switch to fc import

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_19
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_18
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_17
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_16
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_14
- fc import

