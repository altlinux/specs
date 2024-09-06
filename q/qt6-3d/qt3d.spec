%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qt3d

Name: qt6-3d
Version: 6.7.2
Release: alt1

Group: System/Libraries
Summary: Qt6 - Qt3D QML bindings and C++ APIs
Url: http://qt.io/
License: LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)

Requires: qt6-imageformats

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-base-devel qt6-declarative-devel qt6-shadertools-devel qt6-multimedia-devel
BuildRequires: zlib-devel libminizip-devel libpoly2tri-devel pkgconfig(assimp)
BuildRequires: libxkbcommon-devel

%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications).

%package common
Summary: Common package for %name
Group: System/Configuration/Other
Requires: qt6-base-common
%description common
Common package for %name

%package devel
Group: Development/KDE and QT
Summary: Development files for %name
Requires: %name-common
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
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-3dcore
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dcore
%summary

%package -n libqt6-3dinput
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dinput
%summary

%package -n libqt6-3dlogic
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dlogic
%summary

%package -n libqt6-3dquick
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dquick
%summary

%package -n libqt6-3dquickinput
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dquickinput
%summary

%package -n libqt6-3dquickrender
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dquickrender
%summary

%package -n libqt6-3drender
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3drender
%summary

%package -n libqt6-3dextras
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dextras
%summary

%package -n libqt6-3dquickextras
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
Provides: %name = %EVR
Obsoletes: %name < %EVR
%description -n libqt6-3dquickextras
%summary

%package -n libqt6-3danimation
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3danimation
%summary

%package -n libqt6-3dquickanimation
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dquickanimation
%summary

%package -n libqt6-3dquickscene2d
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-3dquickscene2d
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

cat >>src/plugins/renderers/rhi/CMakeLists.txt <<__EOF__
find_package(Qt6 COMPONENTS ShaderTools)
__EOF__

%build
%ifarch %e2k
%add_optflags -mno-sse
%endif
%Q6build \
    -DFEATURE_qt3d_rhi_renderer:BOOL=ON \
    -DQT_FEATURE_qt3d_assimp:BOOL=ON \
    -DQT_FEATURE_qt3d_system_assimp:BOOL=ON \
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
%dir %_qt6_plugindir/geometryloaders/
%dir %_qt6_plugindir/sceneparsers
%dir %_qt6_plugindir/renderplugins/
%dir %_qt6_plugindir/renderers/
%dir %_qt6_qmldir/Qt3D/

%files -n libqt6-3dcore
%_qt6_libdir/libQt?3DCore.so.*
%files -n libqt6-3dinput
%_qt6_libdir/libQt?3DInput.so.*
%files -n libqt6-3dlogic
%_qt6_libdir/libQt?3DLogic.so.*
%_qt6_qmldir/Qt3D/Logic/
%files -n libqt6-3dquick
%_qt6_libdir/libQt?3DQuick.so.*
%_qt6_qmldir/Qt3D/Core/
%files -n libqt6-3dquickinput
%_qt6_libdir/libQt?3DQuickInput.so.*
%_qt6_qmldir/Qt3D/Input/
%files -n libqt6-3dquickrender
%_qt6_libdir/libQt?3DQuickRender.so.*
%_qt6_qmldir/Qt3D/Render/
%files -n libqt6-3drender
%_qt6_libdir/libQt?3DRender.so.*
%_qt6_plugindir/geometryloaders/*.so
%_qt6_plugindir/renderers/*.so
%files -n libqt6-3dextras
%_qt6_libdir/libQt?3DExtras.so.*
%_qt6_plugindir/sceneparsers/*.so
%files -n libqt6-3dquickextras
%_qt6_libdir/libQt?3DQuickExtras.so.*
%_qt6_qmldir/Qt3D/Extras/
%files -n libqt6-3danimation
%_qt6_libdir/libQt?3DAnimation.so.*
%files -n libqt6-3dquickanimation
%_qt6_libdir/libQt?3DQuickAnimation.so.*
%_qt6_qmldir/Qt3D/Animation/
%_qt6_qmldir/QtQuick/Scene3D/
%files -n libqt6-3dquickscene2d
%_qt6_libdir/libQt?3DQuickScene2D.so.*
%_qt6_plugindir/renderplugins/*.so
%_qt6_qmldir/QtQuick/Scene2D/

%files devel
%_qt6_headerdir/Qt*/
%_qt6_libdatadir/libQt*.so
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_archdatadir/metatypes/qt6*.json
%_qt6_archdatadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version
- build with sstem assimp (closes: 51214)

* Fri Feb 23 2024 Michael Shigorin <mike@altlinux.org> 6.6.2-alt1.1
- E2K: disable SSE due to core header missing

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

* Tue Jun 13 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt2
- fixed build with GCC 13 (thanks asheplyakov@alt) (closes: 46479)

* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Thu Jun 09 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- initial build
