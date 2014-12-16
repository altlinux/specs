
%global qt_module qtwayland

Name: qt5-wayland
Version: 5.4.0
Release: alt1

Group: System/Libraries
Summary: Qt5 - Wayland platform support and QtCompositor module
Url: http://qt-project.org/
License: LGPLv2 / GPLv3

Source: %qt_module-opensource-src-%version.tar

# Automatically added by buildreq on Thu Jul 17 2014 (-bi)
# optimized out: elfutils fontconfig glibc-devel-static libGL-devel libX11-devel libXfixes-devel libcloog-isl4 libfreetype-devel libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-qml libqt5-quick libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server pkg-config python-base qt5-base-devel qt5-declarative-devel qt5-script-devel ruby ruby-stdlibs wayland-devel xorg-compositeproto-devel xorg-fixesproto-devel xorg-xproto-devel
#BuildRequires: fontconfig-devel gcc-c++ git-core glib2-devel libEGL-devel libXcomposite-devel libXext-devel libXrender-devel libudev-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libxkbcommon-devel python-module-protobuf qt5-base-devel-static qt5-phonon-devel qt5-quick1-devel qt5-tools-devel qt5-webkit-devel qt5-xmlpatterns-devel rpm-build-ruby
BuildRequires: fontconfig-devel gcc-c++ git-core glib2-devel libEGL-devel libXcomposite-devel libXext-devel libXrender-devel
BuildRequires: libudev-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel libxkbcommon-devel
BuildRequires: qt5-base-devel-static qt5-tools-devel
#BuildRequires: gcc-c++ glibc-devel qt5-base-devel qt5-base-devel-static qt5-tools

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt5-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt5-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt5 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt5 %qt_module

%package -n libqt5-compositor
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-compositor
%summary

%package -n libqt5-waylandclient
Summary: Qt5 library
Group: System/Libraries
Requires: %name-common = %EVR
%description -n libqt5-waylandclient
%summary

%prep
%setup -qn %qt_module-opensource-src-%version
#syncqt.pl-qt5 \
#	-version %version \
#	-private \
#	-module QtWaylandClient \
#	-module QtCompositor \
#    #

%build
# Presence of repository tricks qmake into invoking syncqt for us with
# correct arguments at make time.
git init

%qmake_qt5 -o gl/Makefile CONFIG+=wayland-compositor
%qmake_qt5 -o nogl/Makefile QT_WAYLAND_GL_CONFIG=nogl
%make_build -C nogl
%make_build -C gl
%make -C gl docs

%install
%install_qt5 -C nogl
%install_qt5 -C gl
%make -C gl INSTALL_ROOT=%buildroot install_docs ||:

%files common

%files
%_qt5_plugindir/platforms/*
%_qt5_plugindir/wayland-decoration-client/
%_qt5_plugindir/wayland-graphics-integration-server/
%_qt5_plugindir/wayland-graphics-integration-client/

%files -n libqt5-compositor
%_qt5_libdir/libQt?Compositor.so.*
%files -n libqt5-waylandclient
%_qt5_libdir/libQt?WaylandClient.so.*

%files devel
%doc LGPL_EXCEPTION.txt
%_qt5_bindir/qtwaylandscanner*
%_bindir/qtwaylandscanner*
%_qt5_headerdir/Qt*/
%_qt5_libdir/libQt*.so
%_qt5_libdir/libQt*.prl
%_qt5_libdir/cmake/Qt*/
%_qt5_libdir/pkgconfig/Qt*.pc
%_qt5_archdatadir/mkspecs/modules/*.pri

%files doc
#%_qt5_docdir/*

%changelog
* Tue Dec 16 2014 Sergey V Turchin <zerg@altlinux.org> 5.4.0-alt1
- new version

* Thu Jul 17 2014 Sergey V Turchin <zerg@altlinux.org> 5.3.0-alt1
- initial build
