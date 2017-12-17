# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
#
# Rebuild option:
#
#   --with testsuite         - run the test suite
#

Name:           perl-GSSAPI
Version:        0.28
Release:        alt5_21.1
Summary:        Perl extension providing access to the GSSAPIv2 library
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/GSSAPI/
Source0:        http://www.cpan.org/authors/id/A/AG/AGROLMS/GSSAPI-%{version}.tar.gz
BuildRequires:  libkrb5-devel
BuildRequires:  which
%{?_with_testsuite:BuildRequires: perl(constant.pm)}
%{?_with_testsuite:BuildRequires: perl(Carp.pm)}
%{?_with_testsuite:BuildRequires: perl(Exporter.pm)}
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
%{?_with_testsuite:BuildRequires: perl(ExtUtils/testlib.pm)}
BuildRequires:  perl(Getopt/Long.pm)
%{?_with_testsuite:BuildRequires: perl(Test/More.pm)}
%{?_with_testsuite:BuildRequires: perl(Test/Pod.pm)}
%{?_with_testsuite:BuildRequires: perl(XSLoader.pm)}
Source44: import.info

%description
This module gives access to the routines of the GSSAPI library, as
described in rfc2743 and rfc2744 and implemented by the Kerberos-1.2
distribution from MIT.

%prep
%setup -q -n GSSAPI-%{version}
chmod -c a-x examples/*.pl

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} %{buildroot}/*

%check
# fails a couple of tests if network not available
%{?_with_testsuite:make test}

%files
%doc Changes README examples/
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/GSSAPI*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt5_21.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt5_21
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt5_19
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt5_17.1
- rebuild with new perl 5.24.1

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt5_17
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt4_17
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.28-alt4_16
- update to new release by fcimport

* Fri Nov 27 2015 Cronbuild Service <cronbuild@altlinux.org> 0.28-alt4_15
- rebuild to get rid of unmets

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt3_15
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.28-alt3_13
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_13
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt2_11
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.28-alt2_10
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_10
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_9
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_8
- initial fc import

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.26-alt1.1
- rebuilt with perl 5.12

* Tue Oct 07 2008 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.26-alt1
- new version
- fixed build

* Mon Jun 11 2007 Vladimir A. Svyatoshenko <svyt@altlinux.ru> 0.24-alt1
- first build for ALT Linux Sisyphus

