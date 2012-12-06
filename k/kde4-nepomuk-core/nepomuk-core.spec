%define _kde_alternate_placement 1

%define rname nepomuk-core
Name: kde4-nepomuk-core
%define major  4
%define minor  9
%define bugfix 4
Version: %major.%minor.%bugfix
Release: alt1
%define sover %major

Group: Graphical desktop/KDE
Summary: Nepomuk Server and core services
Url: http://kde.org/
License: LGPLv2+

Requires: %name-common >= %version-%release

Source: %rname-%version.tar
# ALT
Patch1: kdebase-runtime-4.8.0-alt-def-nepomuk.patch
Patch2: kdebase-runtime-4.8.0-alt-nepomuk-backup-on.patch
Patch3: nepomuk-core-4.9.1-alt-ontology-dir.patch

# Automatically added by buildreq on Wed Sep 26 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-test libqt4-xml libsoprano-devel libssl-devel libstdc++-devel libstrigi-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: doxygen gcc-c++ glib2-devel graphviz kde4libs-devel libicu libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: gcc-c++ glib2-devel kde4libs-devel
#BuildRequires: doxygen graphviz
BuildRequires: soprano-backend-redland soprano-backend-virtuoso soprano
BuildRequires: kde-common-devel

%description
This package contains Nepomuk Server providing Storage services, strigi controlling,
file indexer service, monitoring file changes.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kde4base-runtime-common < 4.9
%description common
%name common package

%package -n libnepomukcore4
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %version-%release
%description -n libnepomukcore4
%name library

%package -n libnepomuksync4
Group: System/Libraries
Summary: %name library
Requires: %name-common >= %version-%release
%description -n libnepomuksync4
%name library

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Conflicts: kde4libs-devel <= 4.7.4-alt1
Requires: %name-common >= %version-%release
%description devel
Development files for %name


%prep
%setup -qn %rname-%version
%patch1 -p2
%patch2 -p2
%patch3 -p1

sed -i 's|^\(include.*KDE4Defaults.*\)|\1\ninclude(SopranoAddOntology)|' CMakeLists.txt


%build
%K4build


%install
%K4install


%files
%_kde4_bindir/nepomuk-simpleresource-rcgen
%_kde4_bindir/nepomukbackup
%_kde4_bindir/nepomukindexer
%_kde4_bindir/nepomukserver
%_kde4_bindir/nepomukservicestub
%_K4libdir/libkdeinit4_nepomukserver.so
%_K4libdir/libnepomukcommon.so
%_K4lib/nepomukbackupsync.so
%_K4lib/nepomukfileindexer.so
%_K4lib/nepomukfilewatch.so
%_K4lib/nepomukqueryservice.so
%_K4lib/nepomukstorage.so
%_kde4_xdg_apps/nepomukbackup.desktop
%_K4apps/fileindexerservice/nepomukfileindexer.notifyrc
%_K4apps/nepomukfilewatch/nepomukfilewatch.notifyrc
%_K4apps/nepomukstorage/nepomukstorage.notifyrc
%_K4start/nepomukserver.desktop
%_K4srv/nepomukactivitiesservice.desktop
%_K4srv/nepomukbackupsync.desktop
%_K4srv/nepomukfileindexer.desktop
%_K4srv/nepomukfilewatch.desktop
%_K4srv/nepomukontologyloader.desktop
%_K4srv/nepomukqueryservice.desktop
%_K4srv/nepomukremovablestorageservice.desktop
%_K4srv/nepomukstorage.desktop
%_K4srv/nepomukstrigiservice.desktop
%_K4srvtyp/nepomukservice.desktop

%files common
%_datadir/ontology/kde/*

%files -n libnepomukcore4
%_K4libdir/libnepomukcore.so.*

%files -n libnepomuksync4
%_K4libdir/libnepomuksync.so.*

%files devel
%_K4dbus_interfaces/org.kde.*
%_libdir/cmake/NepomukCore/
#%_libdir/pkgconfig/*
%_K4includedir/*
%_K4link/*.so

%changelog
* Wed Dec 05 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.4-alt1
- new version

* Wed Nov 07 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.3-alt1
- new version

* Fri Oct 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.2-alt1
- new version

* Wed Sep 26 2012 Sergey V Turchin <zerg@altlinux.org> 4.9.1-alt1
- initial build
