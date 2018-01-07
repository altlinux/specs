# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Unicode/UCD.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl-Encode-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Encode-EUCJPASCII
Version:        0.03
Release:        alt8_20
Summary:        EucJP-ascii - An eucJP-open mapping
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Encode-EUCJPASCII/
Source0:        http://www.cpan.org/modules/by-module/Encode/Encode-EUCJPASCII-%{version}.tar.gz
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(XSLoader.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Encode/CJKConstants.pm)
BuildRequires:  perl(Encode/JP/JIS7.pm)
%if 0%{?el6}
BuildRequires:  perl-devel
%else
BuildRequires:  perl-Encode-devel
BuildRequires:  rpm-build-perl
%endif


Source44: import.info

%description
This module provides eucJP-ascii, one of eucJP-open mappings, and its
derivative.

%prep
%setup -q -n Encode-EUCJPASCII-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_archlib}/*
%exclude %dir %{perl_vendor_archlib}/auto/

%changelog
* Sun Jan 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt8_20
- to Sisyphus as biber dependency

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt7_20
- rebuild with perl 5.26

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt6_20
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt6_18
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt6_17
- update to new release by fcimport

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt6_16
- rebuild to get rid of unmets

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt5_16
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt5_14
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt5_13
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt4_13
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt4_11
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_11
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt3_9
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt3_8
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_7
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_6
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.03-alt2_4
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_4
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_2
- fc import

