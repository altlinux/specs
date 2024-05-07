%define real_name Crypt-SMIME

Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-podlators
# END SourceDeps(oneline)
BuildRequires: openssl
Name:           perl-%real_name
Version:        0.30
Release:        alt1
Summary:        S/MIME message signing, verification, encryption and decryption
License:        %perl_license
URL:            https://metacpan.org/release/%real_name
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/%real_name-%{version}.tar
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libssl-devel
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/CChecker.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(XSLoader.pm)
# Tests
BuildRequires:  openssl
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/PkgConfig.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Taint/Util.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Taint.pm)
BuildRequires:  perl(Test/More.pm)

#Add a test sub package.
%{?perl_default_subpackage_tests}

%description
This module provides a class for handling S/MIME messages. It can sign,
verify, encrypt and decrypt messages. It requires libcrypto
(http://www.openssl.org) to work.

%prep
%setup -q -n Crypt-SMIME-%{version}
# As part of the rpm process we generate some .list files which
# then cause t/manifest.t to fail.
echo '\.list$' >> MANIFEST.SKIP
echo '\.perl.req$' >> MANIFEST.SKIP

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/auto/*
%perl_vendor_archlib/Crypt*

%changelog
* Tue May 07 2024 L.A. Kostis <lakostis@altlinux.ru> 0.30-alt1
- 0.30.

* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 0.28-alt2
- Rebuild by human.

* Tue Nov 02 2021 Igor Vlasenko <viy@altlinux.org> 0.28-alt1_1
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.27-alt3_4
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.27-alt3_3
- update to new release by fcimport

* Wed Jun 16 2021 Cronbuild Service <cronbuild@altlinux.org> 0.27-alt3_2
- rebuild to get rid of unmets

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.27-alt2_2
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.27-alt2_1
- update to new release by fcimport

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1_1
- update to new release by fcimport

* Thu Oct 01 2020 Cronbuild Service <cronbuild@altlinux.org> 0.26-alt3_1
- rebuild to get rid of unmets

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt2_1
- rebuild with perl 5.30

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_1
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3_8
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3_7
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3_6
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3_5
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3_4
- update to new release by fcimport

* Tue Jan 29 2019 Cronbuild Service <cronbuild@altlinux.org> 0.25-alt3_3
- rebuild to get rid of unmets

* Tue Jan 29 2019 Cronbuild Service <cronbuild@altlinux.org> 0.25-alt2_3
- rebuild to get rid of unmets

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_3
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_2
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_5
- rebuild with perl 5.26

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_3
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_2
- update to new release by fcimport

* Sun Feb 12 2017 Cronbuild Service <cronbuild@altlinux.org> 0.18-alt2_1
- rebuild to get rid of unmets

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_1
- update to new release by fcimport

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1_1
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt2_2
- update to new release by fcimport

* Sun Nov 29 2015 Cronbuild Service <cronbuild@altlinux.org> 0.16-alt2_1
- rebuild to get rid of unmets

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- update to new release by fcimport

* Sat Dec 13 2014 Cronbuild Service <cronbuild@altlinux.org> 0.10-alt4_9
- rebuild to get rid of unmets

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_9
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt3_7
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.10-alt3_6
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_5
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2_4
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.10-alt2_3
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- fc import

