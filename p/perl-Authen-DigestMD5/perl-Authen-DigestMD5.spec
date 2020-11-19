Name: perl-Authen-DigestMD5
Version: 0.04
Release: alt2

Summary: SASL DIGEST-MD5 authentication (RFC2831)

License: GPL+ or Artistic
Group: Development/Other
Url: https://metacpan.org/release/Authen-DigestMD5
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://cpan.metacpan.org/modules/by-module/Authen/Authen-DigestMD5-%version.tar.gz
Source: %name-%version.tar
Patch0: Authen-DigestMD5-0.04-UTF8.patch
Patch1: Authen-DigestMD5-0.04-shellbang.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators

# Build
BuildRequires: su
BuildRequires: findutils
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils/MakeMaker.pm)

# Runtime
Requires: perl(Carp.pm)
Requires: perl(Digest/MD5.pm)
Requires: perl(strict.pm)
Requires: perl(warnings.pm)

# Test Suite
BuildRequires: perl(Test/More.pm)

%description
This module supports DIGEST-MD5 SASL authentication as defined in RFC-2831.

%prep
%setup

# Fix wrong script interpreter, and set permissions to avoid extra deps
%patch1
chmod -c 644 digest-md5-auth.pl

# Fix character encoding
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%buildroot
find %buildroot -type f -name .packlist -delete
# %_fixperms -c %buildroot

# Get rid of sample code that introduces additional dep on perl(OpenLDAP)
rm -f %buildroot%perl_vendor_privlib/Authen/digest-md5-auth.pl

%check
make test

%files
%doc Changes README digest-md5-auth.pl
%perl_vendor_privlib/Authen/

%changelog
* Thu Nov 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt2
- manual build to ALT Sisyphus

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_37
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_36
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_35
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_34
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_33
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_32
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_31
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_30
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_28
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_27
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_26
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_25
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_24
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_23
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_22
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_20
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_19
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_18
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_17
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_16
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_15
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_13
- fc import

