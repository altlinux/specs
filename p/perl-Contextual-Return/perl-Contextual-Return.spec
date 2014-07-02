# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Scalar/Util.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Contextual-Return
Version:        0.004007
Release:        alt2_5
Summary:        Create context-sensitive return values
Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Contextual-Return
Source0:        http://search.cpan.org/CPAN/authors/id/D/DC/DCONWAY/Contextual-Return-%{version}.tar.gz
BuildArch:      noarch 
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(Want.pm)


Source44: import.info


%description
This module allows you to define return values of a perl sub that are
appropriate given the calling context.


%prep
%setup -q -n Contextual-Return-%{version}


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor 
make %{?_smp_mflags}


%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} ';' 2>/dev/null
# %{_fixperms} %{buildroot}


%check
make test


%files
%doc Changes README
%{perl_vendor_privlib}/Contextual/


%changelog
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

