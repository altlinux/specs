
Name: knights
Version: 2.5.0
Release: alt1

Group: Games/Boards
Summary: Chess board for KDE SC 4
Url: http://kde-apps.org/content/show.php/Knights?content=122046
# http://projects.kde.org/projects/extragear/games/knights
License: GPLv2+

Requires: chess

# Automatically added by buildreq on Fri Oct 12 2012 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel libicu libkdegames4-devel libqt3-devel zlib-devel-static
BuildRequires: gcc-c++ libkdegames4-devel
BuildRequires: kde-common-devel

Source: %name-%version.tar

%description
Knights supports local and Internet play against a human being or a computer engine.

%prep
%setup -n %name-%version -q


%build
%K4build

%install
%K4install
%K4find_lang --with-kde %name


%files -f %name.lang
%doc README README.themes
%_K4bindir/knights
%_K4apps/knights
%_K4iconsdir/hicolor/*/apps/knights.*
%_K4cfg/knights.kcfg
%_K4conf/knights.knsrc
%_K4xdg_apps/knights.desktop
%_K4dbus_interfaces/org.kde.Knights.xml

%changelog
* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 2.5.0-alt1
- new version

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt0.M60P.1
- build for M60P

* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt1
- new version

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt2
- fix build requires

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- initial build
