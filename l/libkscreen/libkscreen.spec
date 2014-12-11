Name: libkscreen
Version: 1.0.5
Release: alt2

Group: System/Libraries
Summary: Display configuration library
Url: https://projects.kde.org/projects/playground/libs/libkscreen
License: GPLv2+

Requires: hwdatabase

Source: %name-%version.tar
Patch1: alt-pnp-ids-path.patch

# Automatically added by buildreq on Fri Sep 13 2013 (-bi)
# optimized out: automoc cmake cmake-modules elfutils fontconfig fontconfig-devel glibc-devel-static kde4libs libICE-devel libSM-devel libX11-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXcursor-devel libXdamage-devel libXdmcp-devel libXext-devel libXfixes-devel libXft-devel libXi-devel libXinerama-devel libXpm-devel libXrandr-devel libXrender-devel libXt-devel libXtst-devel libXv-devel libXxf86vm-devel libdbus-devel libdbusmenu-qt2 libfreetype-devel libpng-devel libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sql-sqlite libqt4-svg libqt4-test libqt4-xml libssl-devel libstdc++-devel libxcb-devel libxkbfile-devel phonon-devel pkg-config python-base python3 python3-base ruby ruby-stdlibs xorg-kbproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel zlib-devel
#BuildRequires: gcc-c++ glib2-devel kde4libs-devel libicu50 libxcb-render-util-devel libxcbutil-image-devel python-module-distribute qjson-devel rpm-build-python3 rpm-build-ruby xorg-xf86miscproto-devel zlib-devel-static
BuildRequires: gcc-c++ kde4libs-devel qjson-devel >= 0.8.1
BuildRequires: libxcb-render-util-devel libxcbutil-image-devel xorg-xf86miscproto-devel libXrandr-devel

%description
LibKScreen is a library that provides access to current configuration
of connected displays and ways to change the configuration.

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch1 -p1

%build
%K4build


%install
%K4install


%files
%_K4libdir/libkscreen.so.*
%_K4lib/plugins/kscreen/*.so

%files devel
%_K4includedir/kscreen/
%_K4link/libkscreen.so
%_K4libdir/cmake/LibKScreen/
%_K4libdir/pkgconfig/kscreen.pc

%changelog
* Thu Dec 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt2
- fix pnp.ids usage

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt0.M70P.1
- built for M70P

* Mon Aug 11 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.5-alt1
- new version

* Wed Jun 04 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt0.M70P.1
- built for M70P

* Thu May 29 2014 Sergey V Turchin <zerg@altlinux.org> 1.0.4-alt1
- new version

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt0.M70P.1
- built for M70P

* Wed Dec 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.2-alt1
- new version

* Fri Oct 04 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt0.M70P.1
- built for M70P

* Fri Sep 13 2013 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- initial build
