# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

%define sover 2
%define libqupzilla libqupzilla%sover

Name: qupzilla
Version: 2.2.3
Release: alt1

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW
Url: http://qupzilla.com
Packager: Michael Shigorin <mike@altlinux.org>

PreReq(post,preun): alternatives >= 0.2
Provides: webclient

# https://github.com/QupZilla/qupzilla
Source: %name-%version.tar
# Automatically added by buildreq on Thu Apr 07 2016
# optimized out: fontconfig gcc-c++ libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel pkg-config python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel
BuildRequires: libssl-devel libxcbutil-devel qt5-multimedia-devel qt5-script-devel qt5-tools-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel
BuildRequires: rpm-build-kf5 kf5-kwallet-devel libgnome-keyring-devel

%description
QupZilla is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.

%package kde5
Group: Graphical desktop/KDE
Summary: QupZilla KDE integration
Requires: %name
%description kde5
QupZilla KDE integration.

%package gnome3
Group: Graphical desktop/GNOME
Summary: QupZilla GNOME integration
Requires: %name
%description gnome3
QupZilla GNOME integration.

%package -n %libqupzilla
Group: System/Libraries
Summary: %name library
#Requires: %name-common = %EVR
Conflicts: qupzilla <= 2.0.0-alt2
%description -n %libqupzilla
%name library

%prep
%setup
sed -i 's,бит/с,б/с,' translations/ru_RU.ts

%build
export DISABLE_UPDATES_CHECK="true"
export NONBLOCK_JS_DIALOGS="true"
export KDE_INTEGRATION="true"
export GNOME_INTEGRATION="true"
export USE_LIBPATH="%_libdir"
export SHARE_FOLDER="%_datadir"
%qmake_qt5 "QMAKE_LFLAGS += -L%_K5link"
%make_build

%install
make INSTALL_ROOT=%buildroot install

# install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_bindir/qupzilla      111
%_bindir/x-www-browser       %_bindir/qupzilla      111
__EOF__

%find_lang --all-name --with-qt %name

%files -f %name.lang
%lang(uz) %_datadir/%name/locale/uz@Latn.qm
%config /%_sysconfdir/alternatives/packages.d/%name
%doc AUTHORS FAQ
%_bindir/%name
%_libdir/%name/libAutoScroll.so
%_libdir/%name/libFlashCookieManager.so
%_libdir/%name/libGreaseMonkey.so
%_libdir/%name/libImageFinder.so
%_libdir/%name/libMouseGestures.so
%_libdir/%name/libPIM.so
%_libdir/%name/libStatusBarIcons.so
%_libdir/%name/libTabManager.so
%_desktopdir/*.desktop
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/*/*.png
%dir %_datadir/%name
%dir %_datadir/%name/locale
%_datadir/%name/themes
%_datadir/bash-completion/completions/qupzilla

%files kde5
%_libdir/%name/libKWalletPasswords.so

%files gnome3
%_libdir/%name/libGnomeKeyringPasswords.so

%files -n %libqupzilla
%_libdir/libQupZilla.so.%sover
%_libdir/libQupZilla.so.%sover.*

%changelog
* Wed Dec 20 2017 Michael Shigorin <mike@altlinux.org> 2.2.3-alt1
- 2.2.3

* Wed Dec 06 2017 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Nov 01 2017 Michael Shigorin <mike@altlinux.org> 2.2.1-alt1
- 2.2.1

* Sun Oct 08 2017 Michael Shigorin <mike@altlinux.org> 2.2.0-alt1
- 2.2.0

* Thu Mar 16 2017 Michael Shigorin <mike@altlinux.org> 2.1.2-alt1
- 2.1.2

* Tue Feb 14 2017 Michael Shigorin <mike@altlinux.org> 2.1.1-alt1
- 2.1.1

* Sat Feb 04 2017 Michael Shigorin <mike@altlinux.org> 2.1.0-alt1
- 2.1.0

* Tue Oct 25 2016 Michael Shigorin <mike@altlinux.org> 2.0.2-alt1
- 2.0.2

* Fri Jun 10 2016 Michael Shigorin <mike@altlinux.org> 2.0.1-alt1
- 2.0.1

* Fri Apr 15 2016 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt4
- fix alternatives

* Tue Apr 12 2016 Sergey V Turchin <zerg at altlinux dot org> 2.0.0-alt3
- build KDE and GNOME integration plugins (closes: #31959)
- package library separately
- provide webclient
- properly package translations
- fix build options

* Thu Apr 07 2016 Michael Shigorin <mike@altlinux.org> 2.0.0-alt2
- buildreq

* Thu Mar 31 2016 Michael Shigorin <mike@altlinux.org> 2.0.0-alt1
- 2.0.0

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
