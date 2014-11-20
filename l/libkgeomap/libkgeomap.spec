Name: libkgeomap
Version: 3.0.0
Release: alt1

Group: System/Libraries
Summary: Libkgeomap is a wrapper around different world-map components
Url: https://projects.kde.org/projects/extragear/libs/libkgeomap
License: GPL2

Requires: %name-common >= %EVR
Conflicts: libkmap

Source: %name-%version.tar
Source1: po.tar

# Automatically added by buildreq on Mon Sep 15 2014 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs kde4libs-devel libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libcloog-isl4 libdbus-devel libdbusmenu-qt2 libfreetype-devel libgst-plugins libpng-devel libqt4-core libqt4-dbus libqt4-declarative libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-webkit libqt4-xml libqt4-xmlpatterns libsoprano-devel libstdc++-devel libxkbfile-devel openssh-common phonon-devel pkg-config python-base rpm-build-gir ruby ruby-stdlibs xorg-kbproto-devel xorg-xf86miscproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: boost-devel-headers cvs gcc-c++ git-core glib2-devel kde4edu-devel libXxf86misc-devel libkexiv24-devel libqt3-devel python-module-google qt4-designer rpm-build-ruby subversion valgrind zlib-devel-static
BuildRequires(pre): kde-common-devel
BuildRequires: boost-devel gcc-c++ kde4libs-devel kde4edu-devel libkexiv24-devel

%description
Libkgeomap is a wrapper around different world-map components, to browse and arrange photos over a map.
Currently supported map engine are:
- Marble,
- OpenstreetMap (via Marble),
- GoogleMap.

%package common
BuildArch: noarch
Group: Graphical desktop/KDE
Summary: Common files for %name package
%description common
Common files for %name package

%package devel
Group: Development/KDE and QT
Summary: Devel files for %name
%description devel
Devel files for %name

%prep
%setup -a1
if ! grep -qe '^add_subdirectory([[:space:]]*po[[:space:]]*)' CMakeLists.txt
then
cat >> CMakeLists.txt <<__EOF__
find_package(Msgfmt REQUIRED)
find_package(Gettext REQUIRED)
add_subdirectory( po )
__EOF__
fi

%build
%K4build

%install
%K4install

rm -rf %buildroot/%_K4i18n/*/*/*kipi*
rm -rf %buildroot/%_K4i18n/*/*/digikam*
%K4find_lang %name

%files common -f %name.lang
%files
#%_K4bindir/*
%_K4libdir/%name.so*
%_K4apps/%name

%files devel
%_pkgconfigdir/%name.pc
%_K4includedir/*
%_K4link/*.so
%_K4apps/cmake/modules/FindKGeoMap.cmake


%changelog
* Thu Nov 20 2014 Sergey V Turchin <zerg@altlinux.org> 3.0.0-alt1
- new version

* Mon Sep 15 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt12
- digikam-4.2.0

* Fri Aug 15 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt11
- rebuilt with new KDE

* Mon May 19 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt10
- digikam-4.0.0

* Wed Apr 23 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt9
- rebuilt with new KDE

* Fri Mar 14 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt7.M70P.1
- built for M70P

* Tue Mar 11 2014 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt8
- rebuilt with new KDE

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt6.M70P.1
- built for M70P

* Tue Sep 10 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt7
- update from digikam-3.4.0

* Tue May 21 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt6
- update from digikam-3.2.0

* Thu Apr 18 2013 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt5
- update from digikam-3.1.0
- package translatons (ALT#26565)

* Tue Dec 18 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt4
- update from digikam-3.0.0-beta3

* Fri Oct 05 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt3
- rebuilt with KDE-4.9

* Sat Apr 07 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.3
- rebuilt with KDE-4.8

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt2
- rebuilt with new kde

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 2.0.0-alt0.M60P.2
- rebuilt with KDE-4.7

* Tue Oct 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt0.M60P.1
- backport to ALTLinux 6.0P (by rpmbph script)

* Tue Oct 04 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 2.0.0-alt1
- Update to 2.0.0
  + Rename to libkgeomap

* Thu Jun 30 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 1.0.0-alt1
- Initial build for sysiphus

