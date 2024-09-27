%define rdn_name net.sourceforge.liferea

Name: liferea
Version: 1.15.8
Release: alt1

Summary: A RSS News Reader for GNOME
License: GPL-2.0-or-later
Group: Networking/News
Url: https://lzone.de/liferea

Obsoletes: %name-gtkhtml < %version-%release %name-xulrunner < %version-%release
Provides: %name-backend = %version-%release %name-gtkhtml = %version-%release %name-xulrunner = %version-%release

Vcs: https://github.com/lwindolf/liferea.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: dconf gnome-icon-theme
Requires: typelib(Gtk) = 3.0 libpeas-python3-loader

%add_python3_path %_libdir/%name/plugins
%add_typelib_req_skiplist typelib(AppIndicator3)

BuildRequires(pre): gobject-introspection-devel rpm-build-gir >= 0.7.3-alt3
BuildRequires(pre): rpm-build-python3 python3-devel
BuildRequires: python3-module-pygobject3-devel
BuildRequires: xvfb-run gcc-c++ intltool
BuildRequires: pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires: pkgconfig(glib-2.0) >= 2.50.0 pkgconfig(gio-2.0) >= 2.50.0 pkgconfig(gmodule-2.0) >= 2.0.0 pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(pango) >= 1.4.0
BuildRequires: pkgconfig(libxml-2.0) >= 2.6.27 pkgconfig(libxslt) >= 1.1.19
BuildRequires: pkgconfig(sqlite3) >= 3.7.0
BuildRequires: pkgconfig(libsoup-3.0) >= 3.2 pkgconfig(webkit2gtk-4.1) pkgconfig(json-glib-1.0) pkgconfig(webkit2gtk-web-extension-4.1)
BuildRequires: pkgconfig(gobject-introspection-1.0) gir(Gtk) = 3.0
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(libpeas-1.0) >= 1.0.0 pkgconfig(libpeas-gtk-1.0) >= 1.0.0

%set_typelibdir %_libdir/%name/girepository-1.0

%description
Liferea is a desktop feed reader/news aggregator that brings together
all of the content from your favorite subscriptions into a simple interface
that makes it easy to organize and browse feeds.
Its GUI is similar to a desktop mail/newsclient, with an embedded graphical browser.

%package plugins-gnome-keyring
Summary: GNOME Keyring Support for the %name
Group: Networking/News
Requires: %name = %EVR

%description plugins-gnome-keyring
Allow Liferea to use GNOME keyring as password store

%prep
%setup
%patch -p1

%build
%autoreconf
%configure \
	--enable-introspection \
	--disable-static
xvfb-run %make_build

%install
%makeinstall_std

%find_lang --with-gnome --with-man %name

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog
%_bindir/*
%_libdir/%name/girepository-1.0/*.typelib
%_datadir/%name/
%_datadir/glib-2.0/schemas/*.xml
%_datadir/GConf/gsettings/%name.convert
%_datadir/metainfo/%rdn_name.appdata.xml
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/icons/hicolor/*/apps/*
%_man1dir/%name.*
%_libdir/%name/web-extension/*.so
%exclude  %_libdir/%name/web-extension/*.la

%dir %_libdir/%name/plugins
%dir %_libdir/%name/plugins/__pycache__

# plugins. may be separated packages?
%_libdir/%name/plugins/bold-unread.*
%_libdir/%name/plugins/__pycache__/bold-unread.*
%_libdir/%name/plugins/getfocus.*
%_libdir/%name/plugins/__pycache__/getfocus.*
%_libdir/%name/plugins/headerbar.*
%_libdir/%name/plugins/__pycache__/headerbar.*
%_libdir/%name/plugins/libnotify.*
%_libdir/%name/plugins/__pycache__/libnotify.*
%_libdir/%name/plugins/plugin-installer.*
%_libdir/%name/plugins/__pycache__/plugin-installer.*
%_libdir/%name/plugins/trayicon.*
%_libdir/%name/plugins/__pycache__/trayicon.*
%_libdir/%name/plugins/add-bookmark-site*
%_libdir/%name/plugins/__pycache__/add-bookmark-site.*

%files plugins-gnome-keyring
%_libdir/%name/plugins/gnome-keyring.*
%_libdir/%name/plugins/__pycache__/gnome-keyring.*

%changelog
* Fri Sep 27 2024 Yuri N. Sedunov <aris@altlinux.org> 1.15.8-alt1
- 1.15.8

* Sat Jun 22 2024 Yuri N. Sedunov <aris@altlinux.org> 1.15.7-alt1
- updated to v1.15.7-3-dea9940bc7

* Sun Mar 17 2024 Yuri N. Sedunov <aris@altlinux.org> 1.15.6-alt1
- updated to v1.15.6-3-g9c2d2499f

* Fri Jan 05 2024 Yuri N. Sedunov <aris@altlinux.org> 1.15.5-alt1
- 1.15.5

* Sat Dec 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.4-alt1.2
- fixed build with libxml2-2.12.x

* Tue Oct 24 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.4-alt1.1
- skip AppIndicator3 typelib dependency

* Tue Oct 24 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.4-alt1
- 1.15.4

* Mon Sep 18 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.3-alt1
- 1.15.3

* Fri Sep 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Mon Aug 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.1-alt1
- updated to v1.15.1-3-g4584e0947

* Sat Jul 22 2023 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- updated to v1.15.0-51-g3acb5bc16 (ported to libsoup-3.0/webkitgtk-4.1,
  fixed CVE-2023-1350)

* Thu May 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.5-alt2
- explicitly required typelib(Gtk) = 3.0 libpeas-python3-loader

* Tue Apr 11 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.5-alt1
- updated to v1.14.5-3-g201ac9fed

* Wed Mar 22 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Mon Mar 13 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1 (fixed CVE-2023-1350)

* Wed Jan 11 2023 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Oct 05 2022 Yuri N. Sedunov <aris@altlinux.org> 1.13.9-alt1
- updated to v1.13.9-41-g49174d5cd

* Sun Jun 28 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.1-alt1
- 1.13.1

* Fri Mar 13 2020 Alexey Shabalin <shaba@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Dec 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.12.7-alt2
- run make via xvfb-run as a workaround to build Liferea-3.0.gir

* Tue Aug 13 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.7-alt1
- 1.12.7

* Thu Jan 03 2019 Alexey Shabalin <shaba@altlinux.org> 1.12.6-alt1
- 1.12.6

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.5-alt1
- new version 1.12.5

* Sat Aug 18 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.4-alt1
- 1.12.4

* Wed May 23 2018 Alexey Shabalin <shaba@altlinux.ru> 1.12.3-alt1
- 1.12.3

* Mon Apr 02 2018 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Wed Jan 10 2018 Alexey Shabalin <shaba@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Mon Apr 25 2016 Alexey Shabalin <shaba@altlinux.ru> 1.10.19-alt1
- 1.10.19

* Fri Jul 03 2015 Alexey Shabalin <shaba@altlinux.ru> 1.10.16-alt1
- 1.10.16

* Thu Nov 13 2014 Alexey Shabalin <shaba@altlinux.ru> 1.10.12-alt1
- 1.10.12

* Thu Aug 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.10.11-alt1
- 1.10.11

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 1.10.9-alt1
- 1.10.9

* Thu Jan 23 2014 Alexey Shabalin <shaba@altlinux.ru> 1.10.5-alt1
- 1.10.5

* Sat May 11 2013 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10-RC1
- add plugin packages

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
