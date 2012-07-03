
Name: knights
Version: 2.4.2
Release: alt1

Group: Games/Boards
Summary: Chess board for KDE SC 4
Url: http://kde-apps.org/content/show.php/Knights?content=122046
# http://projects.kde.org/projects/extragear/games/knights
License: GPLv2+

Requires: chess

# Automatically added by buildreq on Thu Feb 03 2011 (-bi)
#BuildRequires: gcc-c++ glib2-devel kde4games-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel qt4-designer zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4games-devel libqt4-devel zlib-devel
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
* Mon May 14 2012 Sergey V Turchin <zerg@altlinux.org> 2.4.2-alt1
- new version

* Fri Apr 22 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt2
- fix build requires

* Thu Feb 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.2.0-alt1
- initial build
