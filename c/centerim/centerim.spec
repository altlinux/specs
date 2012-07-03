Name: centerim
Version: 4.22.10
Release: alt1.qa2

Summary: Console ncurses based IM client. ICQ, Yahoo!, AIM, IRC, MSN, Gadu-Gadu and Jabber protocols are supported. Internal RSS reader is also provided
Summary(ru_RU.KOI8-R): Клиентская программа для IM (быстрого общения). Поддержка протоколов:  ICQ, Yahoo!, AIM, IRC, MSN, Gadu-Gadu и Jabber. Клиент для LiveJournal и RSS.
License: GPL
Group: Networking/Instant messaging
Source0: %name-%version.tar.gz
Patch0:         centericq-libyahoo.patch
Patch1:         centericq-kkconsui.patch
Patch2:         centericq-kkstrtext.patch
Patch3:         centericq-src.patch

# the next two fix CVE-2005-3694
# http://www.gentoo.org/cgi-bin/viewcvs.cgi/net-im/centericq/files/
# see redhat bugzilla #174611
Patch4:         centericq-4.21.0-icq-short-read.diff.bz2
Patch5:         centericq-4.21.0-memory-handling.diff.bz2
# and see http://www.gentoo.org/security/en/glsa/glsa-200512-11.xml 
# and redhat bugzilla #176451
Patch6:         centericq-4.21.0-kkstrtext.patch
# Fix libmsn 
Patch7:       http://centericq.de/archive/contrib/patches/centericq-4.21.0.msn.patch

#new for alt3:

# Fix ljhook
Patch8:       http://www.crystalowl.net/patches/centericq-4.20.0-ljtags.patch
Patch9:       centericq-ljtypo.patch

## feature enh
# improve utf8 handling
Patch10:       centericq-ncursesw.patch
# provided by Andy Shevchenko... will ask before quit
Patch11:       centericq-quitask.patch

# CVE-2007-0160
# http://mailman.linuxpl.org/pipermail/cicq/2007-January/004866.html
# see redhat bugzilla #227791
Patch12:         centericq-ijhook.patch
Patch13:         centericq-libjab-segv.patch


# fix connect to Jabber on 64-bit
Patch14:	centericq-4.21.0-amd64jabber.patch

Patch15: centerim-4.22.10-alt-gcc4.6.patch


Url: http://www.centerim.org

Packager: Ilya Mashkin <oddity at altlinux dot ru>

Provides: centericq
Obsoletes: centericq

BuildRequires: gcc-c++ libcurl-devel libgpgme-devel libidn-devel libjpeg-devel libncurses-devel libssl-devel libstdc++-devel libtinfo-devel zlib-devel
BuildRequires: ncurses libncursesw-devel libncurses libncursesw

# Automatically added by buildreq on Tue Sep 09 2008
BuildRequires: glibc-devel-static  libgpg-error-devel 

%description
Centerim is a fork of the centericq instant messaging client
centerim is a text mode menu- and window-driven IM interface. Currently
ICQ2000, Yahoo!, AIM TOC, IRC, MSN, Gadu-Gadu and Jabber protocols are supported. It allows
you to send, receive, and forward messages, URLs and, SMSes, mass
message send, search for users (including extended "whitepages search"),
view users' details, maintain your contact list directly from the
program (including non-icq contacts), view the messages history,
register a new UIN and update your details, be informed on receiving
email messages, automatically set away after the defined period of
inactivity (on any console), and have your own ignore, visible and
invisible lists. It can also associate events with sounds, has support
for Hebrew and Arabic languages and allows to arrange contacts into
groups. Internal RSS reader is provided.

%description -l ru_RU.KOI8-R
Centerim - это форк клиента centericq 
Centerim - клиентская программа для IM (быстрого общения) под Linux. ICQ2000, Yahoo, AIM, IRC, MSN, Gadu-Gadu и Jabber протоколы поддерживаются на сегодняшний день.
Плюс к этому:
- Поддержка IRC.
- Встроенный клиент LiveJournal.
- Встроенный интерфейс для чтения RSS
- Компилируется и работает под Linux, FreeBSD, NetBSD, OpenBSD, Sun Solaris, Windows и MacOS X/Darwin
- Скрипт для миграции списка контактов (включая историю) из licq, kxicq2, gnomeicu и micq
- Ведение журнала работы программы
- Обширная и довольно интересная документация
- Дружественное и активное сообщество пользователей

%prep
%setup -q
#patch0
#patch1
#patch2
#patch3
#patch4 -p1
#patch5 -p1
#patch6 -p1
#patch7 -p1
#patch8 -p1
#patch9 -p1
#patch10 -p1
#patch11 -p1
#patch12 -p1
#patch13 -p1
#patch14 -p1
%patch15 -p2


%build

%set_automake_version 1.9
%set_autoconf_version 2.5

CFLAGS="$RPM_OPT_FLAGS" \
./configure --with-ssl


#configure --with-ssl --with-included-gettext
%make_build

%install
%make_install

install -D -pm 755 src/%name %buildroot%_bindir/%name
install -D -pm 755 misc/cimconv %buildroot%_bindir/cimconv
#install -D -pm 755 misc/cicqsync %buildroot%_bindir/cicqsync

install -D -pm 644 %name.1 %buildroot%_man1dir/%name.1
install -D -pm 644 misc/cimconv.1 %buildroot%_man1dir/cimconv.1
#install -D -pm 644 misc/cicqsync.1 %buildroot%_man1dir/cicqsync.1

%__mkdir_p %buildroot%_datadir/%name
install -D -pm 644 share/*.wav %buildroot%_datadir/%name/
install -D -pm 644 po/ru.gmo %buildroot%_datadir/locale/ru/LC_MESSAGES/%name.mo

install -D -pm 644 po/uk.gmo %buildroot%_datadir/locale/uk/LC_MESSAGES/%name.mo
install -D -pm 644 po/fr.gmo %buildroot%_datadir/locale/fr/LC_MESSAGES/%name.mo
install -D -pm 644 po/de.gmo %buildroot%_datadir/locale/de/LC_MESSAGES/%name.mo
install -D -pm 644 po/bg.gmo %buildroot%_datadir/locale/bg/LC_MESSAGES/%name.mo
install -D -pm 644 po/pl.gmo %buildroot%_datadir/locale/pl/LC_MESSAGES/%name.mo

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Centerim
Comment=Centerim -  A text mode IM client
GenericName=
Icon=%name
Exec=%name
Terminal=true
Categories=Network;InstantMessaging;
EOF

%find_lang %name

%files -f %name.lang
%doc README COPYING INSTALL TODO ChangeLog FAQ AUTHORS THANKS ABOUT-NLS
%_bindir/*
%_man1dir/*
#_datadir/%name/*.wav
%_datadir/%name
%_desktopdir/%name.desktop

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.22.10-alt1.qa2
- Fixed build

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 4.22.10-alt1.qa1
- NMU: converted menu to desktop file

* Wed Nov 24 2010 Ilya Mashkin <oddity@altlinux.ru> 4.22.10-alt1
- fix CVE-2009-3720
- fix yahoo connectivity

* Sat Oct 30 2010 Ilya Mashkin <oddity@altlinux.ru> 4.22.9.49-alt1
- 4.22.9.49

* Sat Dec 19 2009 Ilya Mashkin <oddity@altlinux.ru> 4.22.9-alt1
- 4.22.9

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 4.22.8-alt1
- 4.22.8
- fix connection to the Yahoo messanger protocol
- fix CVE-2008-4776

* Tue Feb 24 2009 Ilya Mashkin <oddity@altlinux.org> 4.22.7-alt1
- 4.22.7

* Sun Dec 28 2008 Ilya Mashkin <oddity@altlinux.org> 4.22.6-alt2
- now provides centericq
- remove unneeded post scripts

* Tue Nov 04 2008 Ilya Mashkin <oddity@altlinux.ru> 4.22.6-alt1
- 4.22.6

* Sat Sep 13 2008 Ilya Mashkin <oddity@altlinux.ru> 4.22.5-alt0.2
- correct url

* Tue Sep 09 2008 Ilya Mashkin <oddity@altlinux.ru> 4.22.5-alt0.1
- first build Centerim for Sisyphus based on centericq spec 

* Mon Feb 25 2008 Ilya Mashkin <oddity@altlinux.ru> 4.21.0-alt6
- rebuild with automake 1.9 and autoconf 2.5

* Fri Feb 16 2007 Ilya Mashkin <oddity@altlinux.ru> 4.21.0-alt5
- fix #10786 (connect to Jabber on 64-bit systems)
- fix CVE-2007-0160

* Thu Dec 28 2006 Ilya Mashkin <oddity@altlinux.ru> 4.21.0-alt4
- fix #10500

* Sun Dec 16 2006 Ilya Mashkin <oddity at altlinux dot ru> 4.21.0-alt3
- add some patches:
  + ask before quit
  + fixes lj hook
  + improve utf8 support

* Mon Jan 09 2006 Ilya Mashkin <oddity at altlinux dot ru> 4.21.0-alt2
- fixed ktools Buffer Overflow Vulnerability #8701
- small fixes

* Sun Sep 03 2005 Ilya Mashkin <oddity at altlinux dot ru> 4.21.0-alt1
- New version 4.21.0:
- AIM changed its protocol again, so all TOC clients did not work. This release fixes the inability to connect to the AIM network.
- Some Jabber bugs were fixed. PGP works better, and it's also possible to connect to Google Talk.
- Some other changes, see ChangeLog file for details

* Sun Feb 06 2005 Ilya Mashkin <oddity at altlinux dot ru> 4.20.0-alt1
- Included gettext support
- New version 4.20.0:
- PGP encryption support was implemented for the Jabber module. (disable in this -alt1 build)
- Fixed the RTF parser that takes charge when a message from a Windows ICQ client is received. 
- After ICQ dual login detection centericq used to try re-connecting, though it wasn't supposed to. Fixed.
- Fixed libicq2000 headers etc.
- For details and more changes see ChangeLog file 

* Wed Jan 19 2005 Ilya Mashkin <oddity at altlinux dot ru> 4.14.0-alt1
- New version 4.14.0:
- A memory leak problem when checking RSS was fixed.
- fixed segfault in Gadu-Gadu module
- fixed eating all 'u' characters  in RTF parser
- For details see ChangeLog file 

* Sun Dec 26 2004 Ilya Mashkin <oddity at altlinux dot ru> 4.13.0-alt1
- New version 4.13.0:
- Centericq now builds fine with gcc 3.4.
- A new command-line parameter, --debug, was added.
- There are two passwords for an IRC account now. One is for Nickserv and the other one is for regular IRC authentification, which wasn't supported before.
- Online and free-for-chat mode have the same priority now.
- Unicode characters in rtf-encoded icq messages aren't lost anymore. Instead, they are recoded into the primary charset. 
- For details see ChangeLog file 

* Wed Oct 20 2004 Ilya Mashkin <oddity at altlinux dot ru> 4.12.0-alt2
- force add Ukrainian, Polish, French, Deutsch and Bulgarian translations
- spec cleanup

* Tue Sep 28 2004 Ilya Mashkin <oddity at altlinux dot ru> 4.12.0-alt1
- New version 4.12.0: fixes in MSN, SSL & LJ

* Fri Aug 06 2004 Ilya Mashkin <oddity@altlinux.ru> 4.11.0-alt1
- many fixes. See ChangeLog file for detailes
- update description  

* Sun Jul 04 2004 Ilya Mashkin <oddity@altlinux.ru> 4.10.0-alt1
- update version (4.10.0)
- Problems with displaying national characters that used to happen on some systems were fixed.
- libmsn rewriten
- Applied patch by Iulian Ciorascu that made Jabber not to block when establishing an SSL connection.
- other fixes and small addons (see CHANGELOG file)

* Fri Apr 16 2004 Ilya Mashkin <oddity@altlinux.ru> 4.9.12-alt1

- Version 4.9.12:
- It was impossible to turn on character set conversion for the LJ protocol. Fixed.
- Another nasty bug was related to the new configurable keybindings
 feature. Default configuration files were not created on a fresh run and
 also in case the program couldn't find them, so it was a real trouble.

- Now, invoking the multi-contacts selection dialog, you'll see groups and be able to select/deselect whole groups as well.
- The "Enter key sends" feature lost its functionality in the previous version. Fixed.
- MSN used to crash on long messages. Fixed as well.
- Jabber module now sends keepalive packets from time to time.

* Tue Mar 23 2004 Ilya Mashkin <oddity@altlinux.ru> 4.9.11-alt1
- Update version to 4.9.11, many changes include:
- MSN protocol is back.
- LiveJournal can now use the http proxy setting from configuration.
- Support for the Polish Gadu-Gadu IM
- Server-side groups were implemented for the ICQ protocol.
- A problem with Jabber conferences was fixed. In the "Join Channel" dialog the service textual description was used instead of chat service name.
- Codepages conversion was extended. Now it's possible to specify charsets from and to which you'd like your messages to be (de-/en-)coded. Must be of great use for those languages that use different charsets on different platforms, just like koi8 and cp1251 for Russian.
- A bug was fixed that caused centericq not to work properly with eJabberd servers.
- Now it's possible to scroll a message in the full-screen mode invoked with F9.
- and others, see ChangeLog

* Tue Feb 17 2004 Ilya Mashkin <oddity@altlinux.ru> 4.9.10-alt2
- Corrected menu support (#3704)

* Sat Jan 17 2004 Ilya Mashkin <oddity@altlinux.ru> 4.9.10-alt1
- Update version to 4.9.10:
- Survived another Yahoo! protocol change. 
- new "Mass group move" feature
- IRC /raw command was implemented.
- another changes

* Sun Nov 23 2003 Ilya Mashkin <oddity@altlinux.ru> 4.9.9-alt1
- Add menus and russian description
- Update to version 4.9.9:
- Yahoo! search was implemented,
- Yahoo! and Jabber server-side groups are now reflected on the contact list.
- LiveJournal support was improved
- The RDF support got broken somehow in the previous release. Fixed.
- Other changes

* Sat Oct 25 2003 Ilya Mashkin <oddity@altlinux.ru> 4.9.8-alt1
- Initial build
