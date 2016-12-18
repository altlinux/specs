%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Contextual-Return
Version:        0.004010
Release:        alt1
Summary:        Create context-sensitive return values
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Contextual-Return
Source:        http://www.cpan.org/authors/id/D/DC/DCONWAY/Contextual-Return-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Runtime
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Want.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)
# Optional tests only
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(Data/Dumper.pm)


Source44: import.info
%filter_from_provides /^perl\\(DB.pm\\)$/d

%description
This module allows you to define return values of a perl sub that are
appropriate given the calling context.

%prep
%setup -q -n Contextual-Return-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.004010-alt1
- automated CPAN update

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.004009-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.004008-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.004008-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt2_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt2_5
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt2_4
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt1_3
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt1_2
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.004007-alt1_1
- update to new release by fcimport

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.004005-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.004003-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.004003-alt1_1
- fc import

