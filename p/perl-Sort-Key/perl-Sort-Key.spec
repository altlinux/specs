# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(XSLoader.pm) perl(locale.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Sort-Key
Version:        1.32
Release:        alt4_4
Summary:        Fastest way to sort anything in Perl
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Sort-Key/
Source0:        http://www.cpan.org/authors/id/S/SA/SALVA/Sort-Key-%{version}.tar.gz
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
Sort::Key provides a set of functions to sort lists of values by some
calculated key value.

%prep
%setup -q -n Sort-Key-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Sort*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt4_4
- Sisyphus build

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.32-alt3_4
- rebuild to get rid of unmets

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt2_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt2_3
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt2_2
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.32-alt2_1
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1_1
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2_9
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_9
- fc import

