%define _kde_alternate_placement 1
%add_findpackage_path %_kde4_bindir
%def_disable nepomuk

%define rname plasma-mobile
Name: kde4-plasma-mobile
Version: 0.5
Release: alt4

Group: Graphical desktop/KDE
Summary: KDE mobile environment
License: GPLv2 / LGPLv2 / LGPLv2.1
Url: http://kde.org/

Requires: kde4-kactivities kde4base-runtime-core

Provides: kde4-contour = 0.4
Obsoletes:  kde4-contour < 0.4

Source: plasma-mobile-%version.tar
Patch1: plasma-mobile-0.4-alt-fix-compile.patch
Patch2: plasma-mobile-0.5-alt-cut-nepomuk.patch

# Automatically added by buildreq on Tue Oct 16 2012 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde-common-devel kde4-kactivities-devel kde4libs kde4libs-devel kde4pimlibs libGL-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-script libqt4-sql libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libssl-devel libstdc++-devel libxkbfile-devel phonon-devel pkg-config python-base rpm-build-gir ruby shared-desktop-ontologies shared-desktop-ontologies-devel soprano-backend-redland soprano-backend-virtuoso xorg-kbproto-devel xorg-renderproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: akonadi-devel boost-devel-headers gcc-c++ glib2-devel kde4-kactivities kde4base-workspace-devel kde4pimlibs-devel libqt3-devel python-module-distribute rpm-build-ruby soprano zlib-devel-static
BuildRequires: akonadi-devel boost-devel gcc-c++
BuildRequires: kde4base-workspace-devel kde4pimlibs-devel kde4-kactivities qt4-mobility-devel libqt4-webkit-devel
%if_enabled nepomuk
BuildRequires: libsoprano-devel shared-desktop-ontologies
BuildRequires: kde4-nepomuk-core kde4-nepomuk-core-devel
%endif
BuildRequires: kde-common-devel

%description
KDE mobile environment

%package -n libactiveapp4
Summary: %name library
Group: System/Libraries
#Requires: %name-common = %version-%release
%description -n libactiveapp4
%name library

%package -n libnepomukdatamodel4
Summary: %name library
Group: System/Libraries
#Requires: %name-common = %version-%release
%description -n libnepomukdatamodel4
%name library

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
#Requires: %name-common = %version-%release
%description devel
Devel stuff for %name


%prep
%setup -qn %rname-%version
%patch1 -p1
%if_disabled nepomuk
%patch2 -p1
%endif

sed -i \
    's|\(^cmake_minimum_required.*\)$|\1\n\nset(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules )|' \
    CMakeLists.txt
find ./ -type f -name CMakeLists.txt | \
find ./ -name CMakeLists.txt | \
while read f
do
sed -i 's|\(kext_onto_src.*\)\${CMAKE_INSTALL_PREFIX}|\1/usr|' $f
sed -i 's|\(kao_onto_src.*\)\${CMAKE_INSTALL_PREFIX}|\1/usr|' $f
done

%build
%K4build
#    -DKDE4_INCLUDE_DIR:PATH=%_K4includedir \
#    -DKDE4_LIB_DIR:PATH=%_K4link

%install
%K4install
%K4find_lang --with-kde %rname

# conflicts with kde4base-runtime-core
rm -rf %buildroot/%_K4lib/imports/org/kde/dirmodel/


%files -n libactiveapp4
%_K4libdir/libactiveapp.so.*

%if_enabled nepomuk
%files -n libnepomukdatamodel4
%_K4libdir/libnepomukdatamodel.so.*
%endif

%files -f %rname.lang
%if_enabled nepomuk
%_kde4_bindir/contour
%_K4conf_bin/*
%_K4conf_update/*
%_K4apps/active-webbrowser/
%_K4apps/contour/
%_K4start/*
%endif
%_kde4_bindir/active-*
%_kde4_bindir/plasma-*
%_K4exec/*
%_K4libdir/libkdeinit4_plasma-*.so
%_K4lib/imports/org/kde/*
%_K4lib/*.so
%_kde4_xdg_apps/*.desktop
%_kde4_iconsdir/plasmamobilemouse
%_kde4_iconsdir/hicolor/*/*/*.*
%_K4iconsdir/oxygen/*/*/*.*
%_K4wall/*
%_K4apps/desktoptheme/*
%_K4apps/plasma/packages/*
%_K4apps/plasma/plasmoids/*
%_K4apps/plasma/resourcedelegates/
%_K4apps/plasma/services/*
%_K4apps/plasma-widgetstrip/
%_K4apps/solid/actions/*
%_K4srv/*
%_K4srvtyp/*
%_K4dbus_system/org.kde.active.*.conf
%_K4dbus_sys_services/org.kde.active.*.service
%_datadir/polkit-1/actions/org.kde.active.*.policy

%files devel
%_K4apps/cmake/modules/*
%if_enabled nepomuk
%_libdir/cmake/NepomukDataModel/
%endif
%_K4includedir/*.h
%_K4link/lib*.so


%changelog
* Mon Feb 29 2016 Sergey V Turchin <zerg@altlinux.org> 0.5-alt4
- remove nepomuk support with stuff

* Fri Oct 16 2015 Sergey V Turchin <zerg@altlinux.org> 0.5-alt3
- fix build requires

* Mon May 18 2015 Sergey V Turchin <zerg@altlinux.org> 0.5-alt2
- rebuild with new qtwebkit

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 0.5-alt0.M70P.1
- built for M70P

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 0.5-alt1
- new version

* Thu Dec 13 2012 Sergey V Turchin <zerg@altlinux.org> 0.4-alt2
- add devel subpackage

* Tue Oct 16 2012 Sergey V Turchin <zerg@altlinux.org> 0.4-alt1
- new version

* Tue Apr 10 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt0.M60P.1
- built for M60P

* Tue Feb 28 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt2
- fix active-firstrun path to apps

* Wed Feb 08 2012 Sergey V Turchin <zerg@altlinux.org> 0.3-alt1
- initial specfile
