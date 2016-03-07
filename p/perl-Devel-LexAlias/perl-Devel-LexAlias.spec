# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DynaLoader.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Devel-LexAlias
Version:        0.05
Release:        alt2_9
Summary:        Alias lexical variables
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-LexAlias/
Source0:        http://www.cpan.org/authors/id/R/RC/RCLAMP/Devel-LexAlias-%{version}.tar.gz

BuildRequires:  perl(Devel/Caller.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

%prep
%setup -q -n Devel-LexAlias-%{version}

perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} +

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes t/
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Devel*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_9
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_8.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_8
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_6.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_4
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_3
- update to new release by fcimport

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt2
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_2
- Sisyphus build

* Fri Feb 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt4_14
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3_14
- update to new release by fcimport

* Wed Jun 06 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt3_12
- fixed provides

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- fc import

