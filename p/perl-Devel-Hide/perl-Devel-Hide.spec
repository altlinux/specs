# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/Temp.pm) perl(Module/CoreList.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Devel-Hide
Version:        0.0009
Release:        alt1_8
Summary:        Forces the unavailability of specified Perl modules (for testing)
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-Hide/
Source0:        http://www.cpan.org/authors/id/F/FE/FERREIRA/Devel-Hide-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
Given a list of Perl modules/filenames, this module makes require and
use statements fail (no matter the specified files/modules are
installed or not).

%prep
%setup -q -n Devel-Hide-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_2
- update to new release by fcimport

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.0009-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt2_13
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt2_9
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.0008-alt1_9
- fc import

