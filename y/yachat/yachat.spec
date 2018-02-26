%define svnnumber svn8990

Name: yachat
Version: 3.2.2
Release: alt2
Group: Networking/Instant messaging
Summary: Yandex jabber client based on Qt

Summary(ru_RU.UTF-8): Яндекс Jabber клиент
License: GPL
Url: http://online.yandex.ru

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar
Patch: yachat-version-5067-alt1.patch
Patch1: yachat-whirpool.2.1.patch
Patch2: yachat-3.0.5-fix.alt2.patch
Patch3: yachat-3.2-alt-qt4.8.0-private.patch

Provides: yapsi = %version-%release
Obsoletes: yapsi  < %version-%release

Requires: sound_handler ca-certificates
Requires: sox-base gnupg

BuildPreReq: fontconfig libqt4-sql libsasl2-devel libstdc++-devel
BuildPreReq: libSM-devel libssl-devel libXScrnSaver-devel libaspell-devel

# Automatically added by buildreq on Mon Apr 26 2010
BuildRequires: gcc-c++ libXScrnSaver-devel libaspell-devel libqt4-devel
BuildRequires: libcom_err-devel

Requires: libqt4-core sox

%description
YaChat is the premiere Instant Messaging application designed for Microsoft
Windows, Apple Mac OS X and GNU/Linux. Built upon an open protocol named
Jabber, YaChat is a fast and lightweight messaging client that utilises the best
in open source technologies.

%description -l ru_RU.UTF-8
Yandex chat - это программа, ориентированный для работы с сервером Яндекс-онлайн
Psi - это удобный графический клиент сети быстрого обмена сообщениями
Jabber.  Jabber имеет шлюзы в другие сети, включая ICQ, MSN, Yahoo и
AIM.  Psi поддерживает такие возможности Jabber, как одновременная
работа с несколькими серверами, конференции, криптозащиту передаваемой
информации (через SSL и GnuPG), работу через HTTP(S) прокси-сервер и
т.д.

%prep
%setup -q -n %name-%version
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
./configure --prefix=%prefix --bindir=%_bindir --datadir=%_datadir --qtdir=%_qt4dir
lrelease-qt4 lang/qt_ru.ts
lrelease-qt4 lang/psi_ru.ts
%make

%install
%makeinstall INSTALL_ROOT=%buildroot
install -dm755 %buildroot%_datadir/yachat/lang/
install -Dm644 lang/*.qm %buildroot%_datadir/yachat/lang/

install -dm755 %buildroot%_datadir/yachat/iconsets/roster/default
install -p -m644 iconsets/roster/default/*  %buildroot%_datadir/yachat/iconsets/roster/default
install -p -m644 iconsets/roster/*.jisp  %buildroot%_datadir/yachat/iconsets/roster
install -dm755 %buildroot%_datadir/yachat/iconsets/system/default/whiteboarding/
install -p -m644 iconsets/system/default/whiteboarding/* %buildroot%_datadir/yachat/iconsets/system/default/whiteboarding
install -p -m644 iconsets/system/default/*.{png,xml} %buildroot%_datadir/yachat/iconsets/system/default
#mv iconsets/system/README iconsets/system/README.iconset

%files
%doc README COPYING INSTALL
# iconsets/system/README.iconset
%dir %_datadir/yachat
%_datadir/yachat/*
%exclude %_datadir/yachat/COPYING
%_desktopdir/*.desktop
%_bindir/*
%_iconsdir/hicolor/*/*/*.png


%changelog
* Wed May 23 2012 Sergey V Turchin <zerg@altlinux.org> 3.2.2-alt2
- fix requires

* Sat Mar 03 2012 Sergey V Turchin <zerg@altlinux.org> 3.2.2-alt1
- new version

* Wed May 25 2011 Repocop Q. A. Robot <repocop@altlinux.org> 3.2.0-alt1.svn8990.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * specfile-macros-get_dep-is-deprecated for yachat

* Sun May 22 2011 Hihin Ruslan <ruslandh@altlinux.ru> 3.2.0-alt1.svn8990
- new version

* Fri Feb 04 2011 Sergey V Turchin <zerg@altlinux.org> 3.2.0-alt1.svn8829
- new version

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 3.1.0-alt0.1.svn8188.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Fri Jul 23 2010 Sergey V Turchin <zerg@altlinux.org> 3.1.0-alt0.1.svn8188
- update to 3.1.0 svn8188
- fix obsoletes
- update private Qt headers to fix compile

* Thu May 27 2010 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.5-alt2.svn7959
- New version

* Tue Apr 27 2010 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.5-alt2
- Correction 

* Mon Apr 26 2010 Hihin Ruslan <ruslandh@altlinux.ru> 3.0.5-alt1
- New Version

* Mon Jun 01 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.9-alt1
- New version

* Sat Apr 04 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt3
- add yachat-yastuff-2.1.patch

* Tue Feb 17 2009 Hihin Ruslan <ruslandh@altlinux.ru> 2.1-alt2
- New version

* Sat Dec 13 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.00-alt2
- correct spec
- dissable whirlpool

* Sun Sep 07 2008 Hihin Ruslan <ruslandh@altlinux.ru> 2.00-alt1
- init version Yandex-chat
- spec based on yapsi.spec

* Mon Sep 01 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt2.svn1173
- fixed psi mainwindow options (hide/unhide from tray)
