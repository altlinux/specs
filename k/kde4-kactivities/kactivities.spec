%define _kde_alternate_placement 1
%define sover 6

%define rname kactivities
Name: kde4-kactivities
Version: 4.8.4
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE activity manager
Url: http://kde.org/
License: LGPLv2+

Requires: libkactivities%sover
Conflicts: kde4base-runtime-core <= 4.7.4-alt1

Source: %rname-%version.tar
Patch1: alt-fix-install.patch

# Automatically added by buildreq on Wed Dec 07 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel kde-common-devel
#BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano

%description
KDE activity manager


%package -n libkactivities%sover
Group: System/Libraries
Summary: %name library
#Conflicts: kde4libs <= 4.7.4-alt1
%description -n libkactivities%sover
%name library

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: kde4libs-devel <= 4.7.4-alt1
%description devel
Development files for %name


%prep
%setup -qn %rname-%version
#%patch1 -p1
sed -i 's|^\(INCLUDE.*KDE4Defaults.*\)|\1\ninclude(SopranoAddOntology)|' CMakeLists.txt


%build
%K4build


%install
%K4install


%files
%_kde4_bindir/kactivitymanagerd
%_K4lib/activitymanager_plugin_*.so
%_K4srv/activitymanager-plugin-*.desktop
%_K4srv/kactivitymanagerd.desktop
%_K4srv/kded/activitymanager.desktop
%_K4srvtyp/activitymanager-plugin.desktop

%files -n libkactivities%sover
%_K4libdir/libkactivities.so.%sover
%_K4libdir/libkactivities.so.%sover.*

%files devel
%_libdir/cmake/KActivities/
%_libdir/pkgconfig/*
%_K4includedir/*
%_K4link/*.so

%changelog
* Tue Jun 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt1
- new version

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt0.M60P.1
- build for M60P

* Wed May 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 06 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Wed Jan 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3.M60P.1
- built for M60P

* Tue Jan 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt4
- built without nepomuk

* Tue Dec 27 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2.M60P.1
- built for M60P

* Tue Dec 20 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt3
- update code from master branch

* Thu Dec 15 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt2
- fix package description

* Mon Dec 12 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- built for M60P

* Fri Dec 09 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- initial build
