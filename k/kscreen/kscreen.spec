%define _kde_alternate_placement 1

Name: kscreen
Version: 1.0.1
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE Display Management software
Url: https://projects.kde.org/projects/playground/base/kscreen
License: GPLv2 / GPLv3

Source: %name-%version.tar

# Automatically added by buildreq on Mon Sep 16 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base python3 python3-base rpm-build-gir ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu50 libkscreen-devel python-module-distribute qjson-devel rpm-build-python3 rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel libkscreen-devel qjson-devel >= 0.8.1 gettext

%description
KCM and KDED modules for managing displays in KDE.


%prep
%setup


%build
%K4build


%install
%K4install

%K4find_lang --with-kde %name
%K4find_lang --with-kde --append --output=%name.lang kcm_displayconfiguration
%K4find_lang --with-kde --append --output=%name.lang plasma_applet_org.kde.plasma.kscreen


%files -f %name.lang
%doc COPYING
%_kde4_bindir/kscreen-console
%_K4lib/kcm_kscreen.so
%_K4lib/kded_kscreen.so
%_K4lib/plasma_applet_kscreen.so
%_K4apps/kcm_kscreen/
%_K4apps/plasma/packages/org.kde.plasma.kscreen.qml/
%_K4srv/kcm_kscreen.desktop
%_K4srv/kded/kscreen.desktop
%_K4srv/plasma-applet-kscreen-qml.desktop
%_K4srv/plasma-applet-kscreen.desktop
%_kde4_iconsdir/hicolor/*/actions/*


%changelog
* Fri Sep 13 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build

