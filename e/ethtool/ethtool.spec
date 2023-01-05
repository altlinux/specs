%def_with check
Name: ethtool
Version: 6.1
Release: alt1
Epoch: 1
Summary: Ethernet settings tools for network cards
License: GPLv2
Group: System/Configuration/Networking
Url: http://sourceforge.net/projects/gkernel/

# http://git.kernel.org/?p=network/ethtool/ethtool.git;a=summary
# git://git.kernel.org/pub/scm/network/ethtool/ethtool.git
Source: %name-%version-%release.tar
BuildRequires: libmnl-devel

Summary(ru_RU.UTF-8): утилита настройки Ethernet-карт
Summary(uk_UA.UTF-8): утил╕та налаштування Ethernet-карток

Conflicts: net-tools <= 1.60-alt15

%description
This utility allows querying and changing of ethernet card settings,
such as speed, port, and autonegotiation.
Not all ethernet drivers support ethtool yet, but it is getting better.

%description -l ru_RU.UTF-8
Эта утилита позволяет запрос и изменение параметров
Ethernet-карты, таких как скорость, порт, autonegotiation.

%description -l uk_UA.UTF-8
Ця утил╕та дозволя╓ опитування та зм╕нювання параметр╕в
Ethernet-картки, таких як швидк╕сть, порт, autonegotiation.

%prep
%setup -n %name-%version-%release

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%check
make check

%files
%doc AUTHORS NEWS
%_sbindir/*
%_man8dir/*
%_datadir/bash-completion

%changelog
* Thu Jan 05 2023 Anton Farygin <rider@altlinux.ru> 1:6.1-alt1
- 6.1

* Sun Oct 16 2022 Anton Farygin <rider@altlinux.ru> 1:6.0-alt1
- 6.0

* Sun Sep 25 2022 Anton Farygin <rider@altlinux.ru> 1:5.19-alt1
- 5.19

* Mon Apr 11 2022 Anton Farygin <rider@altlinux.ru> 1:5.17-alt1
- 5.17

* Sat Jan 29 2022 Anton Farygin <rider@altlinux.ru> 1:5.16-alt1
- 5.16

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 1:5.15-alt1
- 5.15
- removed README.ALT (closes: #41460)

* Sun Oct 17 2021 Anton Farygin <rider@altlinux.ru> 1:5.14-alt1
- 5.14

* Mon Aug 16 2021 Anton Farygin <rider@altlinux.ru> 1:5.13-alt1
- 5.13

* Tue Jun 15 2021 Anton Farygin <rider@altlinux.ru> 1:5.12-alt2
- removed initscript (unusable in modern ALT environment)

* Wed May 12 2021 Anton Farygin <rider@altlinux.ru> 1:5.12-alt1
- 5.12

* Fri Jan 22 2021 Anton Farygin <rider@altlinux.org> 1:5.10-alt1
- 5.10

* Wed Aug 19 2020 Anton Farygin <rider@altlinux.ru> 1:5.8-alt1
- 5.8

* Sat Jun 27 2020 Anton Farygin <rider@altlinux.ru> 1:5.7-alt1
- 5.7
- enabled tests

* Wed Sep 25 2019 Anton Farygin <rider@altlinux.ru> 1:5.3-alt1
- 5.3
- added bash-completion

* Wed Aug 07 2019 Anton Farygin <rider@altlinux.ru> 1:5.2-alt1
- 5.2

* Tue Oct 10 2017 Anton Farygin <rider@altlinux.ru> 1:4.11-alt1
- 4.11

* Sat May 23 2015 Denis Pynkin <dans@altlinux.org> 1:3.18-alt1
- 3.18

* Sat Apr 21 2012 Michael Shigorin <mike@altlinux.org> 1:3.2-alt1
- 3.2

* Mon Sep 26 2011 Michael Shigorin <mike@altlinux.org> 1:3.0-alt1
- 3.0 (thx ldv@)

* Wed Feb 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1:2.6.33-alt0.1
- Updated to 2.6.33-pre1.
- Moved ether-wake to separate package.
- Moved obsolete mii-tool back to net-tools.

* Wed Aug 20 2008 Michael Shigorin <mike@altlinux.org> 6-alt1
- 6
  + several years of silent development
  + two security-related fixes in versions 5 and 6
- spec cleanup

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 3-alt5.0
- Automated rebuild.

* Thu Dec 22 2005 Denis Ovsienko <pilot@altlinux.ru> 3-alt5
- fixing #8656 (initscript and %_sysconfdir/net)

* Wed Aug 10 2005 Denis Ovsienko <pilot@altlinux.ru> 3-alt4
- fixed #7638 (mii-tool is broken)

* Tue May 17 2005 Denis Ovsienko <pilot@altlinux.ru> 3-alt3
- one more #6360 fix attempt

* Mon May 16 2005 Denis Ovsienko <pilot@altlinux.ru> 3-alt2
- #6360 adjustment

* Fri May 13 2005 Denis Ovsienko <pilot@altlinux.ru> 3-alt1
- new ethtool version
- adopted ether-wake and mii-tool from net-tools

* Tue Oct 29 2002 Michael Shigorin <mike@altlinux.ru> 1.7-alt1
- 1.7
- built with gcc 3.2

* Wed Jun 05 2002 Michael Shigorin <mike@altlinux.ru> 1.5-alt1
- built for ALT Linux
- spec adapted from Cooker/PLD and largely cleaned up
- new and shiny sysconfig-driven wrapper initscript added
