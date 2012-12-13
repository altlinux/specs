%define _kde_alternate_placement 1
%define sover_kactivities 6
%define sover_models 1

%define rname kactivities
Name: kde4-kactivities
%define major 4
%define minor 10
%define bugfix 0
Version: %major.%minor.%bugfix
Release: alt0.1

Group: Graphical desktop/KDE
Summary: KDE activity manager
Url: http://kde.org/
License: LGPLv2+

Conflicts: kde4base-runtime-core <= 4.7.4-alt1

Source: %rname-%version.tar
Patch1: alt-fix-install.patch
Patch2: alt-ontologies-dir.patch

# Automatically added by buildreq on Wed Dec 07 2011 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel kde-common-devel
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano
BuildRequires: kde4-nepomuk-core-devel

%description
KDE activity manager

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
%description common
Common package for %name

%package -n libkactivities%sover_kactivities
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkactivities%sover_kactivities
%name library

%package -n libkactivities-models%sover_models
Group: System/Libraries
Summary: %name library
Requires: %name-common = %version-%release
%description -n libkactivities-models%sover_models
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
%patch2 -p1
sed -i 's|^\(INCLUDE.*KDE4Defaults.*\)|\1\ninclude(SopranoAddOntology)|' CMakeLists.txt


%build
%K4build


%install
%K4install


%files common
%files
%_kde4_bindir/kactivitymanagerd
%_K4lib/*activitymanager*.so
%_K4lib/kio_activities.so
%_K4lib/kcm_activities.so
%_K4lib/imports/org/kde/activities/models/
%_K4srv/activitymanager-plugin-*.desktop
%_K4srv/kactivitymanagerd.desktop
%_K4apps/plasma/packages/org.kde.ActivityManager.UiHandler/
%_K4apps/activitymanager/
#%_K4srv/kded/activitymanager.desktop
%_K4srv/activities.protocol
%_K4srv/kactivitymanagerd_fileitem_linking_plugin.desktop
%_K4srv/kcm_activities.desktop
%_K4srvtyp/activitymanager-plugin.desktop
%_datadir/ontology/kde/*

%files -n libkactivities%sover_kactivities
%_K4libdir/libkactivities.so.%sover_kactivities
%_K4libdir/libkactivities.so.%sover_kactivities.*

%files -n libkactivities-models%sover_models
%_K4libdir/libkactivities-models.so.%sover_models
%_K4libdir/libkactivities-models.so.%sover_models.*

%files devel
%_libdir/cmake/KActivities/
%_libdir/cmake/KActivities-Models/
%_libdir/pkgconfig/*
%_K4includedir/*
%_K4link/*.so

%changelog
* Mon Dec 10 2012 Sergey V Turchin <zerg@altlinux.org> 4.10.0-alt0.1
- new beat version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Wed Sep 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- new version

* Thu Aug 02 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt0.M60P.1
- built for M60P

* Wed Aug 01 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.5-alt1
- new version

* Mon Jun 18 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.4-alt0.M60P.1
- built for M60P

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
