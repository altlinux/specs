%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtwayland

Name: qt6-wayland
Version: 6.4.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Wayland platform support and QtCompositor module
Url: http://qt.io/
License:  GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake fontconfig-devel zlib-devel glib2-devel
BuildRequires: libEGL-devel libGLES-devel libvulkan-devel
BuildRequires: libdrm-devel
BuildRequires: libX11-devel libXcomposite-devel libXext-devel libXrender-devel libxkbcommon-devel
BuildRequires: libinput-devel libts-devel libmtdev-devel
BuildRequires: libudev-devel
BuildRequires: wayland-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: qt6-base-devel qt6-declarative-devel qt6-tools-devel

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common = %EVR
Requires: qt6-base-devel
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
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-compositor
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-compositor
%summary

%package -n libqt6-waylandcompositor
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandcompositor
%summary

%package -n libqt6-waylandclient
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandclient
%summary

%package -n libqt6-waylandeglclienthwintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandeglclienthwintegration
%summary

%package -n libqt6-waylandeglcompositorhwintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandeglcompositorhwintegration
%summary

%package -n libqt6-wlshellintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-wlshellintegration
%summary


%prep
%setup -qn %qt_module-everywhere-src-%version
#for d in gl nogl; do
#mkdir $d
#done

%build
%Q6build \
    -DFEATURE_wayland_client:BOOL=ON \
    -DFEATURE_wayland_server:BOOL=ON \
    #

%if %qdoc_found
%make -C BUILD docs
%endif

%install
%Q6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot install_docs ||:
%endif

%files common
%doc LICENSES/*

%files
%_qt6_plugindir/platforms/*
%_qt6_plugindir/wayland-decoration-client/
%_qt6_plugindir/wayland-graphics-integration-server/
%_qt6_plugindir/wayland-graphics-integration-client/
%_qt6_plugindir/wayland-shell-integration/
%dir %_qt6_qmldir/QtWayland/
%_qt6_qmldir/QtWayland/Compositor/
%dir %_qt6_qmldir/QtWayland/Client/
%_qt6_qmldir/QtWayland/Client/TextureSharing/

#%files -n libqt6-compositor
#%_qt6_libdir/libQt?Compositor.so.*
%files -n libqt6-waylandcompositor
%_qt6_libdir/libQt?WaylandCompositor.so.*
%files -n libqt6-waylandclient
%_qt6_libdir/libQt?WaylandClient.so.*
%files -n libqt6-waylandeglclienthwintegration
%_qt6_libdir/libQt?WaylandEglClientHwIntegration.so.*
%files -n libqt6-waylandeglcompositorhwintegration
%_qt6_libdir/libQt?WaylandEglCompositorHwIntegration.so.*
%files -n libqt6-wlshellintegration
%_qt6_libdir/libQt?WlShellIntegration.so.*

%files devel
%doc LICENSES/*
%_qt6_libexecdir/qtwaylandscanner
%_qt6_headerdir/Qt*/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/*.pri
%_qt6_libdir/metatypes/qt6*.json
%_qt6_datadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed Jun 01 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
