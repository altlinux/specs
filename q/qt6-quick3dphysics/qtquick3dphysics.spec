%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtquick3dphysics
%global optflags_lto %optflags_lto -ffat-lto-objects

Name: qt6-quick3dphysics
Version: 6.10.3
Release: alt1

Group: System/Libraries
Summary: Qt6 - Support for rendering and displaying SVG
Url: http://qt.io/
License: GPL-3.0-only WITH Qt-GPL-exception-1.0

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: qt6-base-devel
BuildRequires: cmake qt6-declarative-devel qt6-shadertools-devel qt6-quick3d-devel

%description
Scalable Vector Graphics (SVG) is an XML-based language for describing
two-dimensional vector graphics. Qt provides classes for rendering and
displaying SVG drawings in widgets and on other paint devices.

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

%package -n libqt6-quick3dphysics
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dphysics
%summary

%package -n libqt6-quick3dphysicshelpers
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Provides: %name = %EVR
Obsoletes: %name < %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dphysicshelpers
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%ifarch %ix86
%add_optflags -msse3
%endif
%Q6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #
%if %qdoc_found
%Q6make --target docs
%endif

%install
%Q6install_qt
%if %qdoc_found
#Q6install_qt --target install_docs
mkdir -p %buildroot/%_docdir/qt6/
cp -ar BUILD/share/doc/qt6/* %buildroot/%_docdir/qt6/
%endif

# relax depends on plugins files
for f in %buildroot/%_libdir/cmake/Qt?*/Qt*Targets.cmake ; do
    sed -i '/message.*FATAL_ERROR.*target.* references the file/s|FATAL_ERROR|WARNING|' $f
done

%files common
%doc LICENSES/*

%files -n libqt6-quick3dphysics
%doc *LICENSE*
%_qt6_libdir/libQt?Quick3DPhysics.so.*
%dir %_qt6_qmldir/QtQuick3D/
%dir %_qt6_qmldir/QtQuick3D/Physics/
%_qt6_qmldir/QtQuick3D/Physics/*3dphysics*.so
%_qt6_qmldir/QtQuick3D/Physics/plugins.qmltypes
%_qt6_qmldir/QtQuick3D/Physics/qmldir
%_qt6_qmldir/QtQuick3D/Physics/designer/
%files -n libqt6-quick3dphysicshelpers
%_qt6_libdir/libQt?Quick3DPhysicsHelpers.so.*
%_qt6_qmldir/QtQuick3D/Physics/Helpers/

%files devel
%_bindir/cooker*
%_qt6_bindir/cooker*
%_qt6_headerdir/QtQuick3DPhysics/
%_qt6_headerdir/QtQuick3DPhysicsHelpers/
%_qt6_libdir/lib*.so
%_qt6_libdir/lib*.a
%_qt6_libdir/lib*.prl
%_qt6_libdatadir/lib*.so
%_qt6_libdatadir/lib*.a
%_qt6_libdatadir/lib*.prl
%_qt6_libdir/cmake/Qt?/*PhysX*.cmake
%_qt6_libdir/cmake/Qt?*Phys*/
%_qt6_libdir/cmake/Qt?Qml/QmlPlugins/*3dphysics*.cmake
%_qt6_libdir/cmake/Qt?BuildInternals/StandaloneTests/*Quick3DPhysics*.cmake
%_qt6_archdatadir/mkspecs/modules/*quick3dphysics*.pri
%_qt6_archdatadir/metatypes/qt6*.json
%_qt6_archdatadir/modules/*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
%_qt6_examplesdir/*

%changelog
* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Tue Mar 24 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- initial build
