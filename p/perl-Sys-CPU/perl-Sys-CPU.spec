Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
BuildRequires: /proc
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Sys-CPU
Version:        0.61
Release:        alt5_13.1
Summary:        Getting CPU information

# Some code was copied from Unix::Processors, which is LGPLv3 or Artistic 2.0
# The rest of the code is under the standard Perl license (GPL+ or Artistic).
# See <https://bugzilla.redhat.com/show_bug.cgi?id=585336>.
License:        (GPL+ or Artistic) and (LGPLv3 or Artistic 2.0)
URL:            http://search.cpan.org/~mzsanford/Sys-CPU/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MZ/MZSANFORD/Sys-CPU-%{version}.tar.gz
# Support cpu_type on ARM and AArch64, bug #1093266, CPAN RT#95400
Patch0:         Sys-CPU-0.61-Add-support-for-cpu_type-on-ARM-and-AArch64-Linux-pl.patch
# Accept undefined cpu_clock on ARM and AArch64, bug #1093266, CPAN RT#95400
Patch1:         Sys-CPU-0.61-cpu_clock-can-be-undefined-on-an-ARM.patch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(DynaLoader.pm)
BuildRequires:  perl(Exporter.pm)


Source44: import.info

%description
Perl extension for getting CPU information. 
Currently only number of CPU's supported.

%prep
%setup -q -n Sys-CPU-%{version}
%patch0 -p1
%patch1 -p1
sed -i 's/\r//' Changes README

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%check
make test TEST_VERBOSE=1

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name CPU.bs -exec rm -f {} ';'
# %{_fixperms} %{buildroot}/*

%files
%doc Changes README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Sys/*


%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.61-alt5_13.1
- rebuild with new perl 5.26.1

* Sun Oct 29 2017 Igor Vlasenko <viy@altlinux.ru> 0.61-alt5_13
- to Sisyphus by requst of lex.shen@yandex (closes: #34088)

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.61-alt4_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.61-alt4_11
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.61-alt4_10
- update to new release by fcimport

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.61-alt4_9
- rebuild to get rid of unmets

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.61-alt3_9
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.61-alt3_7
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.61-alt2_7
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.61-alt2_5
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1_5
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1_2
- update to new release by fcimport

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1_1
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.54-alt2_5
- rebuild to get rid of unmets

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1_4
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1_3
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1_2
- update to new release by fcimport

* Thu Dec 13 2012 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1_1
- new fc rel

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.51-alt2_10
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1_10
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1_8
- fc import

