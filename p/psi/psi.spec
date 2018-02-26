Name: psi
Version: 0.14
Release: alt3
Group: Networking/Instant messaging
Summary: Psi Jabber client
Summary(ru_RU.UTF-8): Jabber клиент Psi
License: GPL
Url: http://psi-im.org/
Source: %name-%version-%release.tar
Source1: iris.tar
Source2: libpsi.tar
Patch0: %name-%version-%release.patch

#BuildRequires: unzip
Requires: sound_handler ca-certificates
# Automatically added by buildreq on Tue Nov 25 2008
BuildRequires: gcc-c++ libXScrnSaver-devel libaspell-devel libcom_err-devel libqt4-devel libqca2-devel

Conflicts: qssl < 2.0 psi0.11
Obsoletes: psi0.11
Requires: libqt4-core >= %{get_version libqt4-core} sox qca2-ossl qca2-gnupg

%description 
Psi is a Jabber Instant Messaging client based on Qt.  Jabber supports
gateways (transports) to other IM systems, such as ICQ, MSN, Yahoo and
AIM.  Psi supports many Jabber features, such as simulatenous login to
several servers, conferences, cryptographic abilities (via SSL and
GnuPG), connection via HTTP(S) proxy, etc.

%description -l ru_RU.UTF-8
Psi - это удобный графический клиент сети быстрого обмена сообщениями
Jabber.  Jabber имеет шлюзы в другие сети, включая ICQ, MSN, Yahoo и
AIM.  Psi поддерживает такие возможности Jabber, как одновременная
работа с несколькими серверами, конференции, криптозащиту передаваемой
информации (через SSL и GnuPG), работу через HTTP(S) прокси-сервер и
т.д.

%prep
%setup -q -n %name-%version-%release -a1 -a2
%patch0 -p1
mv libpsi src/
mkdir -p lang/

%build
./configure \
    --prefix=%prefix \
    --bindir=%_bindir \
    --datadir=%_datadir \
    --qtdir=%_qt4dir \
    --disable-bundled-qca \
    --certstore-path=%_datadir/ca-certificates/ca-bundle.crt
%make

lrelease-qt4 psi_ru.ts

%install
%makeinstall INSTALL_ROOT=%buildroot
rm -f %buildroot%_bindir/psi.debug

install -Dm644 psi_ru.qm %buildroot%_datadir/psi/lang/psi_ru.qm

rm -Rf %buildroot%_datadir/psi/{README,COPYING,certs}

%files
%defattr(0644,root,root,0755)
%doc README COPYING INSTALL TODO 
%attr(0755,root,root) %_bindir/psi
%dir %_datadir/psi
%_datadir/psi/*
%_datadir/applications/%name.desktop

%_iconsdir/hicolor/*/*/*.png

%changelog
* Thu Dec 24 2009 Anton Farygin <rider@altlinux.ru> 0.14-alt3
- updated URL in specfile (closes #21487)
- updated Russian translation (closes #21710)

* Thu Dec 24 2009 Anton Farygin <rider@altlinux.ru> 0.14-alt2
- add history dialog patch from dfo@

* Thu Dec 10 2009 Anton Farygin <rider@altlinux.ru> 0.14-alt1
- new version

* Fri Sep 04 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt4
- new version

* Mon Apr 27 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git11.487e3d4
- new snapshot

* Fri Apr 17 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git10.65d8d0c
- new snapshot

* Thu Apr 16 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git9.c25355e
- new snapshot

* Wed Apr 15 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt3.git8.36d25d7
- added workaround for threaded sender() and QT-4.5 in iris (closes #19391)
- added qca2-gnupg and qca2-ossl requires

* Sat Apr 11 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt2.git8.36d25d7
- revert broken patch from mike@ for drop psi-related cpu wakeups

* Sat Apr 11 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt1.git8.36d25d7
- new snapshot

* Sat Apr 04 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git8.f6760d1
- build with external libqca2

* Sat Apr 04 2009 Michael Shigorin <mike@altlinux.org> 0.13-alt0.git7.f6760d1
- NMU: applied crude patch to drop psi-related cpu wakeups
  (http://lists.affinix.com/pipermail/psi-devel-affinix.com/2008-September/008236.html)

* Sat Mar 28 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git6.f6760d1
- new snapshot
- disabled AVCALL
- disabled whiteboarding

* Tue Mar 03 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git4.561bb4f
- new snapshot
- translations fixed (#17788)

* Sat Feb 07 2009 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git3.57c98f2
- new snapshot

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 0.13-alt0.git1.20e6902
- updated to 0.13 snapshot
- removed post-scripts
- updated patches

* Mon Sep 01 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt2.svn1173
- fixed psi mainwindow options (hide/unhide from tray)

* Wed Jul 30 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1173
- new snapshot (0.12-release)
- updated translations

* Wed Jun 18 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1167
- new snapshot
- workaround for segfault with enabled spellchecker and QT-4.4.0: 
    don't use WaveUnderline in SpellHighlighter format

* Fri May 16 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1157
- new snapshot
- translation updates and fixes

* Tue May 13 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1148
- new snapshot

* Thu May 08 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1138
- new snapshot

* Mon Apr 28 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1131
- new snapshot
- updated translation

* Tue Apr 22 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1109
- new snapshot

* Thu Apr 17 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1104
- new snapshot

* Mon Apr 07 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1100
- new snapshot

* Thu Mar 20 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1086
- new snapshot
- dbus connection patch included to mainstream

* Wed Mar 05 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1069
- new snaphot
- trying to fix dbus connection with numeric profile

* Wed Feb 27 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1064
- new snapshot

* Tue Feb 26 2008 Anton Farygin <rider@altlinux.ru> 0.12-alt1.svn1061
- new snapshot

* Tue Sep 18 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt3svn20070918
- added requires to sox (#12427)

* Tue Sep 18 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070918
- updated from mainstream:
    Justin's SASL fix (auth with openfire servers)

* Mon Sep 17 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070917
- update from mainstream

* Fri Aug 03 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070803
-  update from mainstream, RC2
- added requires to libQT4 >= %{get_version libqt4-core}

* Mon Jul 09 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070709
- update from mainstream

* Tue Jun 05 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070605
- update from mainstream

* Wed May 23 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070523
- update from mainstream
- updated russian translation from Andrey Cherepanov

* Sun May 13 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070513
- update from mainstream

* Fri May 11 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070511
- update from mainstream

* Thu May 03 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070503
- update from mainstream

* Fri Apr 20 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070420
- update from mainstream repository
- added russian translation
- build with aspell
- use system locale for translation

* Mon Apr 16 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070416
- update from mainstream repository

* Fri Apr 13 2007 Anton Farygin <rider@altlinux.ru> 0.11-alt2svn20070413
- new version from subversion repository

* Mon Feb 20 2006 Anton Farygin <rider@altlinux.ru> 0.10-alt3cvs20051215
- NMU (rebuild for x86_64, without changes)

* Mon Dec 12 2005 Mikhail Yakshin <greycat@altlinux.org> 0.10-alt2cvs20051215
- 0.10 prerelease (based on current darcs snapshot)
- added muc-bundle patches from
  http://norman.rasmussen.co.za/darcs/psi-muc-bundle/
  http://norman.rasmussen.co.za/darcs/psi-muc/

* Sun Oct 02 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.10-alt1cvs20050312
- updated translation

* Sat Mar 12 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.10-alt0cvs20050312
- 0.9.3 + cvs changes on 20050312
- global accels went into upstream
- adhoc+rc patch applied

* Sat Jan 01 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.9.3-alt0.test2
- 0.9.3-test2, lots of bugfixes
- disabled global accels by default (one can enable by hand-editing config)

* Tue Dec 14 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.3-alt0.cvs20041214
- 0.9.3-test1, slightly fixed from cvs20041214 snapshot

* Mon Aug 02 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.2-alt2
- added default data proxy
- fixed "play" calls to use sound_handler wrapper scripts

* Fri Jun 11 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Sat May 15 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.2-alt0.test1
- 0.9.2-test1
- incomplete translation
- removed iconsets, they are in ancient non-supported format anyway

* Sat Jan  3 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.9.1-alt0.1
- 0.9.1
- all patches got into mainstream (doubting about mainwin patch)
- got translation from CVS

* Thu Sep 18 2003 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt3
- added psi dudes, aqualight, businessblack icon sets
- added gpg correction patch

* Fri Jul 11 2003 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt2
- removed all patches
- updated russian translation
- added tray icon patch (transparent background in kwin)
- added main window customized flag patch ("tool window" working)
- spec cleanup

* Wed Jun 25 2003 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt1
- 0.9 release
- removed all patches except for sysname (got into mainstream)
- updated russian translation
- spec cleanup
- added 4 more iconsets, several renewed

* Thu May 15 2003 Stanislav Ievlev <inger@altlinux.ru> 0.8.7-alt5.1
- fix closing in kde when program in dock

* Sun Dec 15 2002 Rider <rider@altlinux.ru> 0.8.7-alt5
- updated russian translation from Valentina

* Fri Dec 13 2002 Rider <rider@altlinux.ru> 0.8.7-alt4
- WhatsThis patch from Greycat

* Mon Nov 25 2002 Rider <rider@altlinux.ru> 0.8.7-alt3
- BuildRequires fix (unzip)

* Fri Nov 22 2002 Rider <rider@altlinux.ru> 0.8.7-alt2
- added iconset
- fixed bug for proxy port setup
- fixed URL

* Sun Nov 10 2002 Rider <rider@altlinux.ru> 0.8.7-alt1
- requires fix (libqt3)
- Russian language pack from Valentina Vaneeva <fattie at altlinux ru>

* Tue Nov 05 2002 Rider <rider@altlinux.ru> 0.8.7-alt0.1
- 0.8.7

* Wed Sep 25 2002 Rider <rider@altlinux.ru> 0.8.6-alt4
- requires fix

* Fri Sep 20 2002 Rider <rider@altlinux.ru> 0.8.6-alt3
- rebuild

* Thu Aug 08 2002 Rider <rider@altlinux.ru> 0.8.6-alt2
- proxy port fix and options helper (Mikhail Yakshin aka GreyCat)
- libqssl location fix (me)
- Russian langpack

* Tue Jul 09 2002 Rider <rider@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Mon Apr 01 2002 Rider <rider@altlinux.ru> 0.8.5-alt1
- first build for ALT Linux, based on MandrakeSoft package
- openssl patch

* Tue Feb  8 2002 Alexander Skwar <ASkwar@DigitalProjects.com> 0.8.4-1mdk
- 0.8.4

* Mon Jan 14 2002 Alexander Skwar <ASkwar@Linux-Mandrake.com> 0.8.3.1-1mdk
- First Mandrake release, based on the Conectiva pacakge

* Tue Dec 18 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.8.3.1-1cl
- New minor bugfix version

* Tue Nov 13 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.8.2-1cl
- Bug fix adn new features release
- Name changed. Author uses 0.8.x nomenclature, leaving 0.8x lost
- Epoch added

* Mon Nov 12 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-4cl
- Minor Spec changes
- Solved install dir problems

* Fri Nov 09 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-3cl
- Added description
- Added menu items
- Added icons

* Fri Nov 09 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-2cl
- Added patch to enable right datadir

* Fri Nov 09 2001 Helio Chissini de Castro <helio@conectiva.com.br>
+ psi-0.81-1cl
- First CL package
- Really bad way to install
