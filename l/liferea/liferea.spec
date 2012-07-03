Name: liferea
Version: 1.9.0
Release: alt1
Summary: A RSS News Reader for GNOME
License: GPLv2
Group: Networking/News
Url: http://%name.sf.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires(post,preun): GConf
Obsoletes: %name-gtkhtml < %version-%release %name-xulrunner < %version-%release
Provides: %name-backend = %version-%release %name-gtkhtml = %version-%release %name-xulrunner = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(Pre): libGConf-devel
BuildRequires: libSM-devel libICE-devel
BuildRequires: libnotify-devel
BuildRequires: libgtk+3-devel glib2-devel libgio-devel libpango-devel libxml2-devel libxslt-devel libsqlite3-devel
BuildRequires: libsoup-devel libunique3-devel libwebkitgtk3-devel libjson-glib-devel
BuildRequires: GConf gcc-c++ intltool

%description
Liferea is a simple FeedReader clone for Unix distributions with GTK2
(GNOME2 is optional). It is a news aggregator for RSS/RDF feeds which
also supports CDF channels, Atom/Echo/PIE feeds and OCS or OPML
directories. The problem with FeedReader: for now its only available
for Windows. There are some projects for GNU/Linux, but no solution for
GTK/GNOME, which does not require Python or Perl. Liferea tries to fill
this gap. Liferea is an abbreviation for Linux Feed Reader.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	-with-gtk=3.0 \
	--disable-schemas-install \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/*
%_datadir/liferea
%_datadir/applications/%name.desktop
%_datadir/icons/hicolor/*/apps/*
%_man1dir/%name.1*

%changelog
* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0
- build with gtk3

* Tue Aug 23 2011 Alexey Shabalin <shaba@altlinux.ru> 1.7.6-alt1
- unstable version 1.7.6

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.5-alt2
- rebuild with NM 0.9
- add ALTLinux feed list (ALT #25269)

* Fri Oct 08 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.5-alt1
- 1.6.5

* Mon Jul 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Tue Feb 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Mon Jan 25 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Sat Nov 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Fri Oct 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt3
- rebuild with NM-0.8

* Sun Aug 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt2
- updated Russian translation

* Sat Jul 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt1
- 1.6.0 release

* Tue Jul 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt0.rc7
- 1.6.0-rc7

* Tue Jun 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt0.rc6
- 1.6.0-rc6

* Sun Jun 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt0.rc5
- 1.6.0-rc5

* Sat Jun 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt0.rc4
- 1.6.0-rc4

* Sat May 30 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt0.rc3
- 1.6.0-rc3

* Tue May 26 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.6.0-alt0.rc2
- 1.6.0-rc2

* Fri May 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5.15-alt1
- 1.5.15

* Thu Apr 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.4.28-alt1
- 1.4.28

* Thu Nov 27 2008 Yuri N. Sedunov <aris@altlinux.org> 1.4.22d-alt1
- new version
- removed obsolete %%post{,un} scripts
- drop upsreamed patches
- nm support enabled

* Fri Oct 03 2008 Yuri N. Sedunov <aris@altlinux.org> 1.4.19-alt1
- new version

* Wed Aug 20 2008 Yuri N. Sedunov <aris@altlinux.org> 1.4.17-alt3
- Fixed crash during startup schema migration 
  (patch1 from ktirf@ -alt2 package).

* Sun Aug 17 2008 Yuri N. Sedunov <aris@altlinux.org> 1.4.17-alt1
- 1.4.17
- xulrunner plugin
- dbus support
- optional -lua subpackage
- move %%gconf2_uninstall from %%postun to %%preun
- spec cleanup

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.4.9-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for liferea

* Sun Dec 02 2007 Alex V. Myltsev <avm@altlinux.ru> 1.4.9-alt1
- Security fix (CVE-2005-4791).
- New version: more keyboard shortcuts, new translations, bug fixes.

* Tue Oct 16 2007 Alex V. Myltsev <avm@altlinux.ru> 1.4.5b-alt1
- major bug fixes

* Wed Sep 05 2007 Alex V. Myltsev <avm@altlinux.ru> 1.4.1-alt1
- 1.4.1: major bug fixes

* Sun Sep 02 2007 Alex V. Myltsev <avm@altlinux.ru> 1.4.0-alt1
- New stable version:
- - sqlite storage for feed entries
- - comment feed support
- - duplicate items detection support
- - better proxy configuration dialog
- - removed feedbag.xpi, upgrade to Firefox 2.0 if you were using it
- - UI/scripting enhancements, bug fixes, performance improvements
- - support for gwget as a download tool

* Thu Jul 05 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.19-alt1
- new version: less memory leaks, fixes digest auth (broken since 1.2.17).

* Tue Jun 19 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.17-alt1
- new version: decreased power consumption, bug fixes.

* Thu May 24 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.15b-alt1
- new version: less CPU usage, block file:// links, other fixes.

* Tue May 08 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.14-alt1
- 1.2.14: significant memory leak fix, other bug fixes.

* Thu Apr 26 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.12-alt1
- 1.2.12: speed improvements, bug fixes.

* Thu Mar 15 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.8-alt1
- 1.2.8: many bugfixes, duplicate entry detection, speed improvements

* Tue Feb 06 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.5-alt1
- 1.2.5: Russian translation, fixed possible crash on x86_64.

* Mon Jan 29 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.4-alt1
- New version.

* Fri Jan 12 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.3-alt1
- important bug fixes.

* Mon Dec 25 2006 Alex V. Myltsev <avm@altlinux.ru> 1.2.1-alt1
- 1.2.1: stable version.
- Rebuilding for the new libdbus.

* Tue Nov 28 2006 Alex V. Myltsev <avm@altlinux.ru> 1.2-alt0.rc3
- 1.2 RC3: list saving fixes, lower CPU load.

* Wed Nov 22 2006 Alex V. Myltsev <avm@altlinux.ru> 1.2-alt0.rc2
- 1.2 RC2: bug fixes, documentation updates.

* Sat Nov 04 2006 Alex V. Myltsev <avm@altlinux.ru> 1.1.9-alt1
- 1.1.9: lots of new features: updateable feed lists, social bookmarking,
  wide screen view, firefox 2.0 integration, scripting etc.

* Fri Nov 03 2006 Alex V. Myltsev <avm@altlinux.ru> 1.0.25-alt1
- 1.0.25: many bug fixes, builds against seamonkey.
- liferea-xulrunner does not work, disabled it by default.

* Fri Apr 28 2006 Vital Khilko <vk@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Mon Mar 06 2006 Vital Khilko <vk@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Fri Feb 03 2006 Vital Khilko <vk@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Wed Jan 25 2006 Vital Khilko <vk@altlinux.ru> 1.0.1-alt1
- 1.0.1
- all translated description data removed

* Thu Aug 04 2005 Vital Khilko <vk@altlinux.ru> 0.9.5-alt1.1
- 0.9.5

* Wed Jul 27 2005 Vital Khilko <vk@altlinux.ru> 0.9.4-alt1.1
- DBus support

* Wed Jul 27 2005 Vital Khilko <vk@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Thu Jul 21 2005 Vital Khilko <vk@altlinux.ru> 0.9.2-alt1.1
- DBus disabled

* Thu May 19 2005 Vital Khilko <vk@altlinux.ru> 0.9.2-alt1
- 0.9.2
- DBus support

* Fri Jan 28 2005 Vital Khilko <vk@altlinux.ru> 0.9.0b-alt1
- 0.9.0b
- remove mozilla library to separate package
- updated belarusian translation

* Mon Nov 15 2004 Vital Khilko <vk@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Fri Nov 05 2004 Vital Khilko <vk@altlinux.ru> 0.6.1-alt1
- 0.6.1
- updated belarusian translation

* Thu Sep 16 2004 Vital Khilko <vk@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Wed Aug 18 2004 Vital Khilko <vk@altlinux.ru> 0.5.3-alt1
- 0.5.3
- added belarusian translations

* Tue May 25 2004 Vital Khilko <vk@altlinux.ru> 0.4.9-alt1
- initial build for ALTLinux Sisyphus 
- added code for http proxy autorization
