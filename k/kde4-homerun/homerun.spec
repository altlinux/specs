%define _kde_alternate_placement 1

%define homerun_sover 0
%define libhomerun libhomerun%homerun_sover

%define rname homerun
Name: kde4-homerun
Version: 1.2.4
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE Application Launcher
Url: http://userbase.kde.org/Homerun
License: GPLv2 / GPLv3

Source: %rname-%version.tar
Patch1: alt-install-includes.patch

# Automatically added by buildreq on Tue Apr 15 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby ruby-stdlibs xorg-kbproto-devel xorg-xproto-devel zlib-devel
BuildRequires: gcc-c++ kde4base-devel kde4base-workspace-devel kde-common-devel

%description
Homerun is an alternative modern launcher for KDE.

%package -n %libhomerun
Group: System/Libraries
Summary: Library files of homerun launcher
%description -n %libhomerun
This package provides the library files of the homerun launcher.

%package devel
Group: Development/KDE and QT
Summary: Development files for homerun
%description devel
The homerun-devel package contains all the development files
of the homerun launcher.

%prep
%setup -qn %rname-%version
%patch1 -p1

%build
%K4build

%install
%K4install
%K4find_lang --with-kde %rname
%K4find_lang --with-kde --append --output=%rname.lang plasma_applet_org.kde.homerun

%files -n %libhomerun
%_K4libdir/libhomerun.so.%homerun_sover
%_K4libdir/libhomerun.so.%homerun_sover.*

%files -f %rname.lang
%_kde4_bindir/homerunviewer
%_K4apps/plasma/plasmoids/org.kde.homerun/
%_K4apps/plasma/plasmoids/org.kde.homerun-kicker/
%_K4apps/homerun/
%_K4lib/homerun_source_recentdocuments.so
%_K4lib/plasma_applet_homerunlauncher.so
%_K4lib/imports/org/kde/homerun/
%_kde4_iconsdir/hicolor/*/*/*.*
%_K4srv/homerun-source-recentdocuments.desktop
%_K4srv/homerunviewer.desktop
%_K4srv/plasma-applet-homerun.desktop
%_K4srv/plasma-applet-homerunlauncher.desktop
%_K4srv/plasma-applet-homerun-kicker.desktop
%_K4srvtyp/homerun-source.desktop
%_K4conf/homerunrc
%_K4conf/homerunkickerrc


%files devel
%_K4link/lib*.so
%_K4includedir/homerun/
%_K4libdir/cmake/Homerun/

%changelog
* Mon May 12 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.4-alt1
- new version

* Wed Apr 16 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1.M70P.1
- built for M70P

* Wed Apr 16 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt2
- move to kde-specific place

* Tue Apr 15 2014 Sergey V Turchin <zerg@altlinux.org> 1.2.3-alt1
- initial build
