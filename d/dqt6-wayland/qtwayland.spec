%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module dqtwayland

Name: dqt6-wayland
Version: 6.7.2
Release: alt0.dde.1

Group: System/Libraries
Summary: Qt6 - Wayland platform support and QtCompositor module
Url: http://qt.io/
License:  GPL-3.0-or-later AND (LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-or-later)

Source: %qt_module-everywhere-src-%version.tar

# find librares
%add_findprov_lib_path %_dqt6_libdir

Requires: libdqt6-waylandcompositor
Requires: libdqt6-waylandclient
Requires: libdqt6-waylandeglclienthwintegration
Requires: libdqt6-waylandeglcompositorhwintegration
Requires: libdqt6-wlshellintegration

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools rpm-build-ninja
BuildRequires: cmake fontconfig-devel zlib-devel glib2-devel
BuildRequires: libEGL-devel libGLES-devel libvulkan-devel
BuildRequires: libdrm-devel
BuildRequires: libX11-devel libXcomposite-devel libXext-devel libXrender-devel libxkbcommon-devel
BuildRequires: libinput-devel libts-devel libmtdev-devel
BuildRequires: libudev-devel
BuildRequires: wayland-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel libwayland-server-devel
BuildRequires: dqt6-base-devel dqt6-declarative-devel dqt6-tools-devel

%description
%summary.

%package common
Summary: Common package for %name
Group: System/Configuration/Other
BuildArch: noarch
Requires: dqt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
Requires: libwayland-client-devel libwayland-cursor-devel
Requires: dqt6-base-devel
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

%package -n libdqt6-compositor
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-compositor
%summary

%package -n libdqt6-waylandcompositor
Summary: Qt6 library
Group: System/Libraries
AutoProv: no,lib
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-waylandcompositor
%summary

%package -n libdqt6-waylandclient
Summary: Qt6 library
Group: System/Libraries
AutoProv: no,lib
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-waylandclient
%summary

%package -n libdqt6-waylandeglclienthwintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-waylandeglclienthwintegration
%summary

%package -n libdqt6-waylandeglcompositorhwintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-waylandeglcompositorhwintegration
%summary

%package -n libdqt6-wlshellintegration
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-wlshellintegration
%summary


%prep
%setup -qn %qt_module-everywhere-src-%version
#for d in gl nogl; do
#mkdir $d
#done

%build
%DQ6build \
    -DFEATURE_wayland_client:BOOL=ON \
    -DFEATURE_wayland_server:BOOL=ON \
    -DCMAKE_MAKE_PROGRAM=ninja \
    #

%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
mkdir -p %buildroot%_dqt6_docdir
cp -a BUILD/share/doc/dqt6/* %buildroot%_dqt6_docdir ||:
%endif

# relax depends on plugins files
for f in %buildroot/%_dqt6_libdir/cmake/Qt?*/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files

%files -n libdqt6-waylandcompositor
%_dqt6_libdir/libQt?WaylandCompositor.so.*
%_dqt6_qmldir/QtWayland/Compositor/
%dir %_dqt6_plugindir/wayland-graphics-integration-server/
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-dmabuf-server-buffer.so
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-drm-egl-server-buffer.so
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-linux-dmabuf-unstable-v1.so
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-shm-emulation-server.so
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-vulkan-server.so
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-eglstream-controller.so
%files -n libdqt6-waylandclient
%dir %_dqt6_qmldir/QtWayland/
%_dqt6_libdir/libQt?WaylandClient.so.*
%dir %_dqt6_plugindir/platforms/
%_dqt6_plugindir/platforms/libqwayland-generic.so
%_dqt6_plugindir/wayland-decoration-client/
%_dqt6_plugindir/wayland-shell-integration/libfullscreen-shell-v1.so
%_dqt6_plugindir/wayland-shell-integration/libivi-shell.so
%_dqt6_plugindir/wayland-shell-integration/libqt-shell.so
%_dqt6_plugindir/wayland-shell-integration/libxdg-shell.so
%_dqt6_qmldir/QtWayland/Client/
%dir %_dqt6_plugindir/wayland-graphics-integration-client/
%_dqt6_plugindir/wayland-graphics-integration-client/lib*server*.so
%files -n libdqt6-waylandeglclienthwintegration
%_dqt6_libdir/libQt?WaylandEglClientHwIntegration.so.*
%_dqt6_plugindir/platforms/libqwayland-egl.so
%_dqt6_plugindir/wayland-graphics-integration-client/lib*plugin*.so
%files -n libdqt6-waylandeglcompositorhwintegration
%_dqt6_libdir/libQt?WaylandEglCompositorHwIntegration.so.*
%_dqt6_plugindir/wayland-graphics-integration-server/libqt-wayland-compositor-wayland-egl.so
%files -n libdqt6-wlshellintegration
%_dqt6_libdir/libQt?WlShellIntegration.so.*
%_dqt6_plugindir/wayland-shell-integration/libwl-shell-plugin.so

%files devel
%doc LICENSES/*
%_dqt6_libexecdir/qtwaylandscanner
%_dqt6_headerdir/Qt*/
%_dqt6_libdir/libQt*.so
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/cmake/Qt*/
%_dqt6_archdatadir/mkspecs/modules/*.pri
%_dqt6_archdatadir/metatypes/qt6*.json
%_dqt6_archdatadir/modules/*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc
%_dqt6_examplesdir/*

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif

%changelog
* Thu Oct 03 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

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
