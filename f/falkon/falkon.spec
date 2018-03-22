# spec file for package qupzilla
# Original author: Mariusz Fik (Fisiu)
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself.

%define sover 3
%define libfalkonprivate libfalkonprivate%sover

Name: falkon
Version: 3.0.0
Release: alt2
%K5init no_altplace

Summary: A very fast open source browser based on WebKit core
License: GPLv3+
Group: Networking/WWW
Url: https://github.com/KDE/falkon

PreReq(post,preun): alternatives >= 0.2
Provides: webclient

Source: %name-%version.tar
# Automatically added by buildreq on Thu Apr 07 2016
# optimized out: fontconfig gcc-c++ libGL-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-positioning libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-sql libqt5-webchannel libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-x11extras libqt5-xml libstdc++-devel libxcb-devel pkg-config python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel
BuildRequires(pre): rpm-build-kf5 rpm-build-ubt
BuildRequires: extra-cmake-modules
BuildRequires: libssl-devel libxcbutil-devel qt5-multimedia-devel qt5-script-devel qt5-tools-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel
BuildRequires: kf5-kwallet-devel libgnome-keyring-devel

%description
Falkon is a new and very fast World Wide Web Browser
which uses Qt Framework and its QtWebKit rendering core.
It is a lightweight browser with some advanced functions
like integrated AdBlock, Search Engines Manager, Theming
support, Speed Dial and SSL Certificate manager.

%package kde5
Group: Graphical desktop/KDE
Summary: Falkon KDE integration
Requires: %name
%description kde5
Falkon KDE integration.

%package gnome3
Group: Graphical desktop/GNOME
Summary: Falkon GNOME integration
Requires: %name
%description gnome3
Falkon GNOME integration.

%package -n %libfalkonprivate
Group: System/Libraries
Summary: %name library
#Requires: %name-common = %EVR
%description -n %libfalkonprivate
%name library

%prep
%setup

%build
%K5build

%install
%K5install

#install alternatives
install -d %buildroot/%_sysconfdir/alternatives/packages.d
cat > %buildroot/%_sysconfdir/alternatives/packages.d/%name <<__EOF__
%_bindir/xbrowser       %_K5bin/falkon      111
%_bindir/x-www-browser       %_K5bin/falkon      111
__EOF__

%find_lang --all-name --with-qt %name

%files -f %name.lang
%config /%_sysconfdir/alternatives/packages.d/%name
%_K5bin/%name
%dir %_K5plug/%name/
%_K5plug/%name/AutoScroll.so
%_K5plug/%name/FlashCookieManager.so
%_K5plug/%name/GreaseMonkey.so
%_K5plug/%name/ImageFinder.so
%_K5plug/%name/MouseGestures.so
%_K5plug/%name/PIM.so
%_K5plug/%name/StatusBarIcons.so
%_K5plug/%name/TabManager.so
%_K5plug/%name/VerticalTabs.so
%_K5xdgapp/org.kde.falkon.desktop
%_pixmapsdir/%name.png
%_K5icon/hicolor/*/*/*.png
%_K5icon/hicolor/*/*/*.svg
#%_datadir/locale/*/*/*.qm
%_datadir/%name/
%_datadir/bash-completion/completions/falkon

%files kde5
%_K5plug/%name/KWalletPasswords.so

%files gnome3
%_K5plug/%name/GnomeKeyringPasswords.so

%files -n %libfalkonprivate
%_K5lib/libFalkonPrivate.so.%sover
%_K5lib/libFalkonPrivate.so.%sover.*

%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt2
- NMU: added URL (closes: #34686)

* Tue Mar 20 2018 Oleg Solovyov <mcpain@altlinux.org> 3.0.0-alt1%ubt
- initial build for ALT
