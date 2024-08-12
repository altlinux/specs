%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%global qt_module qtquick3d

%define optflags_lto -ffat-lto-objects

Name: qt6-quick3d
Version: 6.6.2
Release: alt2

Group: System/Libraries
Summary: Qt6 - 3D content in Qt Quick
Url: http://qt.io/
License: GPL-3.0-or-later

Requires: qt6-declarative

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools
BuildRequires: cmake qt6-base-devel qt6-declarative-devel qt6-shadertools-devel qt6-quicktimeline-devel
BuildRequires: libassimp-devel

%description
A new module and API for defining 3D content in Qt Quick.

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

%package -n libqt6-quick3dassetimport
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dassetimport
%summary

%package -n libqt6-quick3dassetutils
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dassetutils
%summary

%package -n libqt6-quick3deffects
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3deffects
%summary

%package -n libqt6-quick3dglslparser
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dglslparser
%summary

%package -n libqt6-quick3dhelpersimpl
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dhelpersimpl
%summary

%package -n libqt6-quick3dhelpers
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dhelpers
%summary

%package -n libqt6-quick3diblbaker
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3diblbaker
%summary

%package -n libqt6-quick3dparticleeffects
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dparticleeffects
%summary

%package -n libqt6-quick3dparticles
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dparticles
%summary

%package -n libqt6-quick3druntimerender
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3druntimerender
%summary

%package -n libqt6-quick3d
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3d
%summary

%package -n libqt6-quick3dutils
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common
Requires: libqt6-core = %_qt6_version
%description -n libqt6-quick3dutils
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%ifarch %e2k
# error: constant is inaccessible
sed -i 's/enum Dirty :/public: &/' \
  src/quick3d/qquick3dcustommaterial_p.h
%endif

%build
%Q6build \
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
%dir %_qt6_plugindir/assetimporters/

%files
%_bindir/*-qt6
%_qt6_bindir/*
%_qt6_qmldir/QtQuick3D/
%_qt6_plugindir/assetimporters/*.so
%_qt6_plugindir/qmltooling/*.so

%files -n libqt6-quick3dassetimport
%_qt6_libdir/libQt?Quick3DAssetImport.so.*
%files -n libqt6-quick3dassetutils
%_qt6_libdir/libQt?Quick3DAssetUtils.so.*
%files -n libqt6-quick3deffects
%_qt6_libdir/libQt?Quick3DEffects.so.*
%files -n libqt6-quick3dglslparser
%_qt6_libdir/libQt?Quick3DGlslParser.so.*
%files -n libqt6-quick3dhelpersimpl
%_qt6_libdir/libQt?Quick3DHelpersImpl.so.*
%files -n libqt6-quick3dhelpers
%_qt6_libdir/libQt?Quick3DHelpers.so.*
%files -n libqt6-quick3diblbaker
%_qt6_libdir/libQt?Quick3DIblBaker.so.*
%files -n libqt6-quick3dparticleeffects
%_qt6_libdir/libQt?Quick3DParticleEffects.so.*
%files -n libqt6-quick3dparticles
%_qt6_libdir/libQt?Quick3DParticles.so.*
%files -n libqt6-quick3druntimerender
%_qt6_libdir/libQt?Quick3DRuntimeRender.so.*
%files -n libqt6-quick3d
%_qt6_libdir/libQt?Quick3D.so.*
%files -n libqt6-quick3dutils
%_qt6_libdir/libQt?Quick3DUtils.so.*

%files devel
%_qt6_headerdir/Qt*/
%ifnarch ppc64le %ix86 %e2k
%_qt6_libdatadir/libQt*.a
%_qt6_libdir/libQt*.a
%endif
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
* Mon Aug 12 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 6.6.2-alt2
- e2k build fix

* Tue Jul 09 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- initial build
