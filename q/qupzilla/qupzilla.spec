# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

Name: qupzilla
Version: 1.8.9
Release: alt2

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW

Url: http://qupzilla.com
# https://github.com/QupZilla/qupzilla
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon Feb 09 2015
# optimized out: libGL-devel libX11-devel libcloog-isl4 libgst-plugins1.0 libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-opengl libqt5-printsupport libqt5-qml libqt5-quick libqt5-script libqt5-sql libqt5-webkit libqt5-webkitwidgets libqt5-widgets libqt5-xml libstdc++-devel pkg-config qt5-base-devel qt5-declarative-devel qt5-tools xorg-xproto-devel
BuildRequires: gcc-c++ libssl-devel qt5-multimedia-devel qt5-script-devel qt5-tools-devel qt5-webkit-devel qt5-websockets-devel
BuildRequires: qt5-x11extras-devel

BuildRequires: pkgconfig(Qt5Concurrent)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Sql)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Widgets)

BuildRequires: fontconfig
BuildRequires: gdb

%description
QupZilla is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.

%prep
%setup
sed -i 's,бит/с,б/с,' translations/ru_RU.ts

%build
export USE_WEBGL="true"
export NONBLOCK_JS_DIALOGS="true"
export KDE="false"
export USE_LIBPATH="%_libdir"
echo "CONFIG += debug" >> src/defines.pri
qmake-qt5
%make_build

%install
make INSTALL_ROOT=%buildroot install

%files
%doc AUTHORS FAQ
%_bindir/%name
%_libdir/%name
%_libdir/*.so.*
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/*/*.png
%dir %_datadir/%name
%_datadir/%name/locale
%exclude %_datadir/%name/locale/uz@Latn.qm
%_datadir/%name/themes
%_datadir/bash-completion/completions/qupzilla
%_datadir/appdata/*

# TODO:
# - move shared libraries to a subpackage?

%changelog
* Thu Feb 04 2016 Michael Shigorin <mike@altlinux.org> 1.8.9-alt2
- tweaked Russian translation (sent upstream)

* Sun Nov 15 2015 Michael Shigorin <mike@altlinux.org> 1.8.9-alt1
- 1.8.9

* Thu Oct 29 2015 Michael Shigorin <mike@altlinux.org> 1.8.8-alt1
- 1.8.8

* Fri Oct 09 2015 Michael Shigorin <mike@altlinux.org> 1.8.7-alt1
- 1.8.7

* Wed Sep 16 2015 Michael Shigorin <mike@altlinux.org> 1.8.6-alt3
- amended BR:

* Mon Feb 09 2015 Michael Shigorin <mike@altlinux.org> 1.8.6-alt2
- rebuilt against qt5

* Mon Jan 26 2015 Michael Shigorin <mike@altlinux.org> 1.8.6-alt1
- 1.8.6

* Tue Dec 23 2014 Michael Shigorin <mike@altlinux.org> 1.8.5-alt1
- 1.8.5

* Wed Nov 05 2014 Michael Shigorin <mike@altlinux.org> 1.8.4-alt1
- 1.8.4

* Sat Oct 25 2014 Michael Shigorin <mike@altlinux.org> 1.8.3-alt1
- 1.8.3 (closes: #30415)
- added appdata just in case

* Sun Oct 05 2014 Michael Shigorin <mike@altlinux.org> 1.8.1-alt1
- 1.8.1
- added missing dependency (closes: #30370)

* Fri Sep 26 2014 Michael Shigorin <mike@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 1.6.6-alt1
- 1.6.6

* Fri Apr 25 2014 Michael Shigorin <mike@altlinux.org> 1.6.5-alt1
- 1.6.5

* Mon Apr 14 2014 Michael Shigorin <mike@altlinux.org> 1.6.4-alt1
- 1.6.4

* Sat Feb 15 2014 Michael Shigorin <mike@altlinux.org> 1.6.3-alt1
- 1.6.3

* Mon Jan 27 2014 Michael Shigorin <mike@altlinux.org> 1.6.1-alt2
- BR: gdb (https://github.com/QupZilla/qupzilla/issues/1180)
- disabled KDE integration, I prefer qupzilla package
  to stay relatively lean and mean regarding R:

* Mon Jan 27 2014 Michael Shigorin <mike@altlinux.org> 1.6.1-alt1
- 1.6.1

* Thu Jan 02 2014 Michael Shigorin <mike@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Nov 22 2013 Michael Shigorin <mike@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Mar 12 2013 Michael Shigorin <mike@altlinux.org> 1.4.0-alt1
- 1.4.0

* Mon Jul 16 2012 Michael Shigorin <mike@altlinux.org> 1.3.1-alt1
- 1.3.1
  + dropped desktop file patch (merged upstream)
- fixed x86_64 build (thx led@ for a hint)

* Sun Jul 15 2012 Michael Shigorin <mike@altlinux.org> 1.3.0-alt1
- 1.3.0
  + enabled nonblocking js dialogs
  + added desktop file patch from gentoo

* Tue Mar 13 2012 Michael Shigorin <mike@altlinux.org> 1.1.8-alt1
- initial build for ALT Linux Sisyphus (based on opensuse package)
- considerable cleanup of otherwise quite nice spec
- buildreq

* Tue Feb 14 2012 fisiu@opensuse.org
- Update to 1.1.8:
  + new translations: Swedish, Serbian and Traditional Chinese
  + option to use external download manager
  + import/export passwords into xml file
  + option to change user agent
  + support for JavaScript Popup windows
  + allow changing background in Speed Dial
  + many bugfixes, details in Changelog file
- Drop qupzilla-1.1.5-remove-date-time.patch: sed'ed in .spec
* Sun Jan  8 2012 fisiu@opensuse.org
- Update to 1.1.5:
  + new translations: Portuguese, French, Greek
  + add support for js printing with window.print()
  + improved commandline options
  + improved performance of history delete
  + many bugfixes
- Rebase remove_date-time.patch
* Thu Dec 22 2011 fisiu@opensuse.org
- Add fedora and mandriva items
* Mon Dec 19 2011 fisiu@opensuse.org
- Upstream update to 1.1.0:
  + speed dial
  + import bookmarks from html file
  + option to turn on XSS Auditing
  + many bugfixes
- Set variable KDE to "true" to enable better integration
  (atm only incons, nepomuk is planned)
* Tue Nov  1 2011 fisiu@opensuse.org
- enable webgl only for openSUSE >= 12.1
* Tue Nov  1 2011 fisiu@opensuse.org
- initial package
