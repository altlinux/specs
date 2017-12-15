# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DynaLoader.pm) perl(Encode.pm) perl(Exporter.pm) perl(utf8.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-String-Similarity
Version:        1.04
Release:        alt4_21.1
Summary:        Calculates the similarity of two strings
License:        GPLv2+
Group:          Development/Other
URL:            http://search.cpan.org/dist/String-Similarity/
Source0:        http://www.cpan.org/authors/id/M/ML/MLEHMANN/String-Similarity-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)


Source44: import.info

%description
The similarity function calculates the similarity index of its two arguments. 
A value of 0 means that the strings are entirely different. A value of 1 
means that the strings are identical. Everything else lies between 0 and 1 
and describes the amount of similarity between the strings.

%prep
%setup -q -n String-Similarity-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/String*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_21.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_21
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_18
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_17.1
- rebuild with new perl 5.24.1

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_17
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_16
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_15.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_15
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_13.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_11
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt4_10
- update to new release by fcimport

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt4
- built for perl 5.18

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3_9
- update to new release by fcimport

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3_8
- build for Sisyphus

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_8
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 1.04-alt2_7
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_7
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_5
- fc import

