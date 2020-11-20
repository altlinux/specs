%define to_utf8(f:) iconv -f %{-f:%{-f*}}%{!-f:iso-8859-1} -t utf-8 < %1 > %1. && touch -r %1 %1. && mv -f %1. %1

Name: swaks
Version: 20201014.0
Release: alt1

Summary: Command-line SMTP transaction tester

License: GPLv2+
Group: Networking/WWW
Url: http://www.jetmore.org/john/code/swaks

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://www.jetmore.org/john/code/swaks/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-perl
BuildRequires: perl-podlators
BuildRequires: perl(Config.pm)

# TODO: where is AutoReq?
Requires:   perl(Authen/DigestMD5.pm)
Requires:   perl(Authen/NTLM.pm)
Requires:   perl(Authen/SASL.pm)
Requires:   perl(Config.pm)
Requires:   perl(Digest/SHA.pm)
Requires:   perl(IO/Socket/INET6.pm)
Requires:   perl(Net/DNS.pm)
Requires:   perl(Net/SSLeay.pm)
Requires:   perl(Time/HiRes.pm)

%description
Swiss Army Knife SMTP: A command line SMTP tester.  Swaks can test
various aspects of your SMTP server, including TLS and AUTH.

%prep
%setup
%to_utf8 doc/Changes.txt

%install
install -D -p -m 0755 swaks %buildroot/%_bindir/swaks
mkdir -p %buildroot/%_man1dir
%_bindir/pod2man swaks > %buildroot/%_man1dir/swaks.1

%files
%_bindir/swaks
%_man1dir/swaks.*
%doc README.txt doc/Changes.txt doc/recipes.txt doc/ref.txt

%changelog
* Thu Nov 19 2020 Vitaly Lipatov <lav@altlinux.ru> 20201014.0-alt1
- new version 20201014.0 (with rpmrb script)

* Thu Nov 19 2020 Vitaly Lipatov <lav@altlinux.ru> 20190914.0-alt2
- manual build to ALT Sisyphus

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 20190914.0-alt1_3
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 20190914.0-alt1_2
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 20190914.0-alt1_1
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 20181104.0-alt1_4
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 20181104.0-alt1_3
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 20181104.0-alt1_2
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 20170101.0-alt1_5
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 20170101.0-alt1_4
- update to new release by fcimport

* Mon Oct 09 2017 Igor Vlasenko <viy@altlinux.ru> 20170101.0-alt1_3
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 20130209.0-alt1_5
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 20130209.0-alt1_4
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 20130209.0-alt1_3
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 20130209.0-alt1_2
- update to new release by fcimport

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 20130209.0-alt1_1
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 20120320.0-alt1_4
- initial fc import

