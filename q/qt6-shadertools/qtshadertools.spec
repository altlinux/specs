%global qt_module qtshadertools

Name: qt6-shadertools
Version: 6.4.2
Release: alt1
%if "%version" == "%{get_version qt6-tools-common}"
%def_disable bootstrap
%else
%def_enable bootstrap
%endif

Group: System/Libraries
Summary: Qt6 - QtShaderTools component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar

BuildRequires(pre): rpm-macros-qt6 qt6-tools-common
%if_disabled bootstrap
BuildRequires: qt6-tools
%endif
BuildRequires: cmake gcc-c++ glibc-devel qt6-base-devel
BuildRequires: glslang libGLU-devel libxkbcommon-devel

%description
APIs and tools in this module provide the producer functionality for the shader pipeline
that allows Qt Quick to operate on Vulkan, Metal, and Direct3D, in addition to OpenGL.

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
Summary: Document for developing apps which will use Qt6 %qt_module
Group: Development/KDE and QT
Requires: %name-common = %EVR
%description doc
This package contains documentation for Qt6 %qt_module

%package -n libqt6-shadertools
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libqt6-core = %_qt6_version
%description -n libqt6-shadertools
%summary

%prep
%setup -n %qt_module-everywhere-src-%version

%build
%define qdoc_found %{expand:%%(if [ -e %_qt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}

%Q6build
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
%files -n libqt6-shadertools
%_qt6_libdir/libQt?ShaderTools.so.*

%files devel
%_bindir/qsb*
%_qt6_bindir/qsb
%_qt6_headerdir/Qt*/
%_qt6_libdir/libQt*.so
%_qt6_libdatadir/libQt*.so
%_qt6_libdir/libQt*.prl
%_qt6_libdatadir/libQt*.prl
%_qt6_libdir/cmake/Qt*/
#%_qt6_libdir/pkgconfig/Qt*.pc
%_qt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_qt6_datadir/modules/*.json
%_qt6_libdir/metatypes/qt*.json
%_pkgconfigdir/Qt?*.pc

%files doc
%if %qdoc_found
%_qt6_docdir/*
%endif
#%_qt6_examplesdir/*

%changelog
* Wed Feb 15 2023 Sergey V Turchin <zerg@altlinux.org> 6.4.2-alt1
- new version

* Wed Oct 19 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt3
- fix automatic package bootstrap mode

* Thu Oct 13 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt2
- add automatic package bootstrap mode

* Wed May 25 2022 Sergey V Turchin <zerg@altlinux.org> 6.2.4-alt1
- new version

* Tue Dec 07 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.2-alt1
- new version

* Mon Nov 29 2021 Sergey V Turchin <zerg@altlinux.org> 6.2.1-alt0.1
- initial build

