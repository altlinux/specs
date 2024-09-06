%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtwayland

Name: qt6-wayland
Version: 6.7.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Wayland platform support and QtCompositor module
Url: http://qt.io/
License:  GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)

Requires: libqt6-waylandcompositor
Requires: libqt6-waylandclient
Requires: libqt6-waylandeglclienthwintegration
Requires: libqt6-waylandeglcompositorhwintegration
Requires: libqt6-wlshellintegration

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
Requires: %name-common
Requires: libwayland-client-devel libwayland-cursor-devel
Requires: qt6-base-devel
%description devel
%summary.

%package devel-static
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: %name-devel
%description devel-static
%summary.

%package doc
BuildArch: noarch
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-compositor
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-compositor
%summary

%package -n libqt6-waylandcompositor
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandcompositor
%summary

%package -n libqt6-waylandclient
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandclient
%summary

%package -n libqt6-waylandeglclienthwintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandeglclienthwintegration
%summary

%package -n libqt6-waylandeglcompositorhwintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-waylandeglcompositorhwintegration
%summary

%package -n libqt6-wlshellintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
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

# relax depends on plugins files
for f in %buildroot/%_libdir/cmake/Qt?*/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files

%files -n libqt6-waylandcompositor
%_qt6_libdir/libQt?WaylandCompositor.so.*
%_qt6_qmldir/QtWayland/Compositor/
%dir %_qt6_plugindir/wayland-graphics-integration-server/
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-dmabuf-server-buffer.so
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-drm-egl-server-buffer.so
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-linux-dmabuf-unstable-v1.so
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-shm-emulation-server.so
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-vulkan-server.so
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-eglstream-controller.so
%files -n libqt6-waylandclient
%dir %_qt6_qmldir/QtWayland/
%_qt6_libdir/libQt?WaylandClient.so.*
%dir %_qt6_plugindir/platforms/
%_qt6_plugindir/platforms/libqwayland-generic.so
%_qt6_plugindir/wayland-decoration-client/
%_qt6_plugindir/wayland-shell-integration/libfullscreen-shell-v1.so
%_qt6_plugindir/wayland-shell-integration/libivi-shell.so
%_qt6_plugindir/wayland-shell-integration/libqt-shell.so
%_qt6_plugindir/wayland-shell-integration/libxdg-shell.so
%_qt6_qmldir/QtWayland/Client/
%dir %_qt6_plugindir/wayland-graphics-integration-client/
%_qt6_plugindir/wayland-graphics-integration-client/lib*server*.so
%files -n libqt6-waylandeglclienthwintegration
%_qt6_libdir/libQt?WaylandEglClientHwIntegration.so.*
%_qt6_plugindir/platforms/libqwayland-egl.so
%_qt6_plugindir/wayland-graphics-integration-client/lib*plugin*.so
%files -n libqt6-waylandeglcompositorhwintegration
%_qt6_libdir/libQt?WaylandEglCompositorHwIntegration.so.*
%_qt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-egl.so
%files -n libqt6-wlshellintegration
%_qt6_libdir/libQt?WlShellIntegration.so.*
%_qt6_plugindir/wayland-shell-integration/libwl-shell-plugin.so

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
%_qt6_archdatadir/metatypes/qt6*.json
%_qt6_archdatadir/modules/*.json
%_pkgconfigdir/Qt?*.pc
%_qt6_examplesdir/*

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif

%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Tue Apr 16 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt2
- update requires

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed Jun 01 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
