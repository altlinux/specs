# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Sys-MemInfo
Version:        0.99
Release:        alt3_5.1
Summary:        Memory information as Perl module
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Sys-MemInfo/
Source0:        http://www.cpan.org/authors/id/S/SC/SCRESTO/Sys-MemInfo-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Copy.pm)
# Run-time:
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Data/Dumper.pm)


Source44: import.info

%description
Sys::MemInfo returns the total amount of free and used physical memory in
bytes in totalmem and freemem variables.

%prep
%setup -q -n Sys-MemInfo-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Sys*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt3_5.1
- rebuild with new perl 5.26.1

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt3_5
- to Sisyphus by requst of lex.shen@yandex (closes: #34089)

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt2_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt2_3
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.99-alt2_2
- update to new release by fcimport

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.99-alt2_1
- rebuild to get rid of unmets

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.99-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.98-alt2_2
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.98-alt2_1
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1_1
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.91-alt4_11
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_11
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt3_9
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.91-alt3_8
- rebuild to get rid of unmets

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt2_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.91-alt2_6
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt2_5
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.91-alt2_3
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.91-alt1_1
- fc import

