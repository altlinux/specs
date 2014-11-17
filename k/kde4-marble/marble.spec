
%add_findpackage_path %_kde4_bindir

%define rname marble
%define major 4
%define minor 14
%define bugfix 3
Name: kde4-marble
Version: %major.%minor.%bugfix
Release: alt1

Group: Education
Summary: A virtual globe and world atlas
Url: http://edu.kde.org/marble
License: LGPLv2+

Requires: xplanet
Provides: kde4edu-marble = %version-%release
Obsoletes: kde4edu-marble < %version-%release

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Sep 11 2014 (-bi)
# optimized out: automoc cmake cmake-modules docbook-dtds docbook-style-xsl elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgpg-error libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-location libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libstdc++-devel libxkbfile-devel openssh-common phonon-devel pkg-config python-base qextserialport ruby ruby-stdlibs shared-mime-info xml-common xml-utils xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: cvs gcc-c++ git-core glib2-devel kde4base-runtime-core kde4libs-devel libXxf86misc-devel libgps-devel libicu50 libqt3-devel libquazip-devel libshape-devel python-module-google qextserialport-devel qt4-designer qt4-mobility-devel rpm-build-ruby subversion valgrind zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel libgps-devel libquazip-devel libshape-devel qextserialport-devel qt4-mobility-devel
BuildRequires: kde-common-devel

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective
Wikipedia article.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common >= %major.%minor
Conflicts: kde4edu-common <= 4.14.0-alt1
%description common
Common package for %name

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
#Requires: libkdeedu4-devel
Requires: %name-common = %version-%release
%description devel
Files needed to build applications based on %name.

%package -n libmarblewidget4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libmarblewidget4
KDE 4 library

%package -n libastro4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libastro4
KDE 4 library

%prep
%setup -q -n %rname-%version
#patch1 -p1

%build
%K4build \
    -DBoostPython_FOUND=ON \
    -DKDE4_BUILD_TESTS:BOOL=OFF \
    -DNOVA_INCLUDE_DIR=%_includedir/libnova \
    -DNOVA_LIBRARIES="-lnova" \
    -DINDI_INCLUDE_DIR=%_includedir/libindi \
    -DNOVA_FUNCTION_COMPILE:BOOL=true \
    -DWITH_DESIGNER_PLUGIN:BOOL=ON \
    #

%install
%K4install

%files common
%_K4xdg_mime/geo.xml

%files
%_K4bindir/marble
%_K4bindir/marble-qt
%_K4bindir/marble-touch
%_K4bindir/marble-mobile
%_K4xdg_apps/marble*.desktop
%dir %_qt4dir/imports/org/
%dir %_qt4dir/imports/org/kde
%dir %_qt4dir/imports/org/kde/edu
%_qt4dir/imports/org/kde/edu/marble/
%_K4lib/libmarble_part.*
%_K4lib/marblethumbnail.so
%_K4lib/plugins/marble
%_K4lib/plasma_applet_worldclock.so
%_K4lib/plasma_runner_marble.so
%_K4iconsdir/hicolor/*/apps/marble.*
%_K4apps/marble
%_K4cfg/marble.kcfg
%_K4srv/marble_part*.desktop
%_K4srv/marble_thumbnail_*.desktop
%_K4srv/plasma-applet-kworldclock.desktop
%_K4srv/plasma-runner-marble.desktop
%_K4doc/*/marble
# tools
#%_kde4_bindir/tilecreator
#%_kde4_bindir/routing-instructions

%files -n libmarblewidget4
%_K4libdir/libmarblewidget.so.*
%files -n libastro4
%_K4libdir/libastro.so.*

%files devel
%_includedir/marble/
%_K4link/*.so
%_includedir/astro/
%_K4apps/cmake/modules/*
%_K4lib/plugins/designer/*.so


%changelog
* Mon Nov 17 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.3-alt1
- new version

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.2-alt1
- new version

* Thu Sep 11 2014 Sergey V Turchin <zerg@altlinux.org> 4.14.0-alt10
- split from kde4edu
