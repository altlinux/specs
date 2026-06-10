%global qt_module dqtshadertools
%def_enable glslang_bundle

Name: dqt6-shadertools
Version: 6.10.3
Release: alt0.dde.1
%if "%version" == "%{get_version dqt6-tools-common}"
%def_disable bootstrap
%else
%def_enable bootstrap
%endif

Group: System/Libraries
Summary: Qt6 - QtShaderTools component
Url: http://qt.io/
License: GPL-3.0-or-later

Source: %qt_module-everywhere-src-%version.tar
Patch1: qtshadertools-unbundle-glslang.patch

# find librares
%add_findprov_lib_path %_dqt6_libdir

BuildRequires(pre): rpm-macros-dqt6 dqt6-tools-common
%if_disabled bootstrap
BuildRequires: dqt6-tools
%endif
BuildRequires: /proc
BuildRequires: cmake glibc-devel dqt6-base-devel
BuildRequires: libdqt6-gui
%if_disabled glslang_bundle
BuildRequires: glslang glslang-devel libspirv-tools-devel
%else
BuildRequires: glslang
%endif
BuildRequires: libGLU-devel libxkbcommon-devel

%description
APIs and tools in this module provide the producer functionality for the shader pipeline
that allows Qt Quick to operate on Vulkan, Metal, and Direct3D, in addition to OpenGL.

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
Requires: %name-common = %EVR
Requires: dqt6-base-devel
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

%package -n libdqt6-shadertools
Summary: Qt6 library
Group: System/Libraries
Requires: %name-common = %EVR
Requires: libdqt6-core = %_dqt6_version
%description -n libdqt6-shadertools
%summary

%prep
%setup -n %qt_module-everywhere-src-%version
%if_disabled glslang_bundle
%patch1 -p1
%endif

%build
%if_enabled bootstrap
%define qdoc_found %{expand:%%(if [ -e %_dqt6_bindir/qdoc ]; then echo 1; else echo 0; fi)}
%else
%define qdoc_found 0
%endif
%DQ6build \
    -DQT_GENERATE_SBOM:BOOL=OFF \
    #
%if %qdoc_found
%DQ6make --target docs
%endif

%install
%DQ6install_qt
%if %qdoc_found
%make -C BUILD DESTDIR=%buildroot VERBOSE=1 install_docs ||:
%endif

%files common
%doc LICENSES/*
%files -n libdqt6-shadertools
%_dqt6_libdir/libQt?ShaderTools.so.*

%files devel
%_bindir/qsb*
%_dqt6_bindir/qsb
%_dqt6_headerdir/Qt*/
%_dqt6_libdir/libQt*.so
%_dqt6_libdatadir/libQt*.so
%_dqt6_libdir/libQt*.prl
%_dqt6_libdatadir/libQt*.prl
%_dqt6_libdir/cmake/Qt*/
#%_dqt6_libdir/pkgconfig/Qt*.pc
%_dqt6_archdatadir/mkspecs/modules/qt_lib_*.pri
%_dqt6_archdatadir/modules/*.json
%_dqt6_archdatadir/metatypes/qt*.json
%_dqt6_libdir/pkgconfig/Qt?*.pc

%files doc
%if %qdoc_found
%_dqt6_docdir/*
%endif
#%_dqt6_examplesdir/*

%changelog
* Mon Jun 08 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.3-alt0.dde.1
- merge with new version

* Tue Apr 07 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.3-alt1
- new version

* Tue Feb 24 2026 Leontiy Volodin <lvol@altlinux.org> 6.10.2-alt0.dde.1
- merge with new version

* Thu Feb 12 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.2-alt1
- new version

* Tue Jan 13 2026 Sergey V Turchin <zerg@altlinux.org> 6.10.1-alt1
- new version

* Fri Nov 21 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.3-alt0.dde.1
- merge with new version

* Thu Nov 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.3-alt1
- new version

* Tue Aug 26 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.2-alt1
- new version

* Thu Jun 19 2025 Leontiy Volodin <lvol@altlinux.org> 6.9.1-alt0.dde.1
- merge with new version

* Tue Jun 03 2025 Sergey V Turchin <zerg@altlinux.org> 6.9.1-alt1
- new version

* Mon Feb 24 2025 Leontiy Volodin <lvol@altlinux.org> 6.8.2-alt0.dde.1
- merge with new version

* Thu Feb 06 2025 Sergey V Turchin <zerg@altlinux.org> 6.8.2-alt1
- new version

* Mon Oct 21 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.2
- fix library detection

* Tue Oct 01 2024 Leontiy Volodin <lvol@altlinux.org> 6.7.2-alt0.dde.1
- fork qt6 for separate deepin packaging (ALT #48138)

* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.7.2-alt1
- new version

* Mon Feb 19 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.2-alt1
- new version

* Thu Feb 01 2024 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt2
- increase docs build verbosity

* Tue Dec 05 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.1-alt1
- new version

* Tue Oct 31 2023 Sergey V Turchin <zerg@altlinux.org> 6.6.0-alt1
- new version

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

