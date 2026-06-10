%define _libexecdir %_prefix/libexec

%def_disable clang

Name: dtkgui
Version: 6.7.43
Release: alt1

Summary: Deepin Toolkit, gui module for DDE look and feel

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkgui
VCS: https://github.com/linuxdeepin/dtkgui

Packager: Leontiy Volodin <lvol@altlinux.org>

# Source-url: %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: dtkgui-alt-git.patch

# Common BuildRequires.
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake dtk6-common-devel dtk6-common-configs librsvg-devel treeland-protocols libwayland-egl-devel libwayland-server-devel libfreeimage-devel libraw-devel

%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif

# DTK5 BuildRequires.
# libQt5XkbCommonSupport.a -> dqt5-base-devel-static
BuildRequires(pre): rpm-macros-dqt5
BuildRequires: extra-cmake-modules dqt5-base-devel-static dqt5-svg-devel dqt5-wayland-devel libdtkcore-devel libdqtxdg-devel libdqt5-concurrent libdqt5-waylandclient

# DTK6 BuildRequires.
BuildRequires(pre): rpm-macros-dqt6
BuildRequires: dqt6-base-devel dqt6-wayland-devel libdtk6core-devel libdqt6-waylandclient libdqt6-widgets libdqt6-concurrent vulkan-headers
# waiting Qt6XdgIconLoaderConfig.cmake
# BuildRequires: libdqt6xdg-devel

%description
Deepin Toolkit, gui module for DDE look and feel.

%package -n lib%{name}5
Summary: Library for %name
Group: System/Libraries
Provides: libdtk5-gui = %EVR
Obsoletes: libdtk5-gui < %EVR
Requires: libdqt5-core = %_dqt5_version
Requires: libdqt5-gui = %_dqt5_version
Requires: libdqt5-waylandclient = %_dqt5_version

%description -n lib%{name}5
DtkGui is used for DDE look and feel.
This package contains the shared libraries.

%package -n lib%name-devel
Summary: Development package for %name
Group: Graphical desktop/Other
Provides: dtk5-gui-devel = %EVR
Obsoletes: dtk5-gui-devel < %EVR

%description -n lib%{name}-devel
Header files and libraries for %name.

%package -n dtk6gui
Summary: Deepin Toolkit, gui module for DDE look and feel
Group: Graphical desktop/Other

%description -n dtk6gui
DtkGui is used for DDE look and feel.

%package -n libdtk6gui6
Summary: Library for dtk6gui
Group: System/Libraries
Provides: libdtk6-gui = %EVR
Obsoletes: libdtk6-gui < %EVR
Requires: libdqt6-core = %_dqt6_version
Requires: libdqt6-gui = %_dqt6_version
Requires: libdqt6-waylandclient = %_dqt6_version

%description -n libdtk6gui6
DtkGui is used for DDE look and feel.
This package contains the shared libraries.

%package -n libdtk6gui-devel
Summary: Development package for dtk6gui
Group: Graphical desktop/Other
Provides: dtk6-gui-devel = %EVR
Obsoletes: dtk6-gui-devel < %EVR

%description -n libdtk6gui-devel
Header files and libraries for dtk6gui.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%if_enabled clang
export CC=clang CXX=clang++ LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
%add_optflags -I/usr/lib/gcc/%{_target_alias}/%{get_version libgomp-devel}/include
%endif

echo "Start DTK6 build."
%DQ6build \
  -DDTK5=OFF \
  -DMKSPECS_INSTALL_DIR=%_dqt6_mkspecsdir/modules/ \
  -DPACKAGE_TOOL_INSTALL_DIR=libexec/dtk6/DGui/bin \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_libdir \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DBUILD_DOCS=OFF \
#

echo "Start DTK5 build."
export PATH=%_dqt5_bindir:$PATH
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:%_dqt5_datadir/cmake:$CMAKE_PREFIX_PATH
%cmake -B build5 \
  -GNinja \
  -DDTK5=ON \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DMKSPECS_INSTALL_DIR=%_dqt5_archdatadir/mkspecs/modules/ \
  -DPACKAGE_TOOL_INSTALL_DIR=libexec/dtk5/DGui/bin \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_libdir \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DBUILD_DOCS=OFF \
#
cmake --build build5 -j%__nprocs

%install
%DQ6install
DESTDIR=%buildroot cmake --install build5 --verbose

%files
%doc README.md LICENSE CHANGELOG.md
%dir %_libexecdir/dtk5/
%dir %_libexecdir/dtk5/DGui/
%_libexecdir/dtk5/DGui/bin/

%files -n lib%{name}5
%_libdir/libdtkgui.so.5*

%files -n lib%name-devel
%dir %_includedir/dtk5/
%_includedir/dtk5/DGui/
%_dqt5_archdatadir/mkspecs/modules/qt_lib_dtkgui.pri
%dir %_libdir/cmake/DtkGui/
%_libdir/cmake/DtkGui/DtkGuiConfig.cmake
%_libdir/cmake/DtkGui/DtkGuiConfigVersion.cmake
%_libdir/cmake/DtkGui/DtkGuiTargets*.cmake
%_pkgconfigdir/dtkgui.pc
%_libdir/libdtkgui.so

%files -n dtk6gui
%doc README.md LICENSE CHANGELOG.md
%dir %_libexecdir/dtk6/
%dir %_libexecdir/dtk6/DGui/
%_libexecdir/dtk6/DGui/bin/

%files -n libdtk6gui6
%_libdir/libdtk6gui.so.6*

%files -n libdtk6gui-devel
%dir %_includedir/dtk6/
%_includedir/dtk6/DGui/
%_dqt6_mkspecsdir/modules/qt_lib_dtkgui.pri
%dir %_libdir/cmake/Dtk6Gui/
%_libdir/cmake/Dtk6Gui/Dtk6GuiConfig.cmake
%_libdir/cmake/Dtk6Gui/Dtk6GuiConfigVersion.cmake
%_libdir/cmake/Dtk6Gui/Dtk6GuiTargets*.cmake
%_pkgconfigdir/dtk6gui.pc
%_libdir/libdtk6gui.so

%changelog
* Tue Jun 09 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.43-alt1
- New version 6.7.43.

* Thu May 14 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.41-alt1
- New version 6.7.41.

* Wed Apr 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.39-alt1
- New version 6.7.39.

* Thu Feb 26 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.33-alt1
- New version 6.7.33.

* Sun Feb 15 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.32-alt2
- Built on separate libqtxdg.

* Thu Jan 22 2026 Leontiy Volodin <lvol@altlinux.org> 6.7.32-alt1
- New version 6.7.32.
- Unified dtk5 and dtk6 modules.

* Wed Dec 10 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.28-alt1
- New version 5.7.28.

* Fri Nov 07 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.26-alt1
- New version 5.7.26.

* Fri Oct 24 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.24-alt1
- New version 5.7.24.

* Wed Oct 15 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.23-alt1
- New version 5.7.23.
- Fixed undefined elfs for libdtkgui.

* Tue Jul 22 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.19-alt1
- New version 5.7.19.

* Thu Feb 13 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.9-alt1
- New version 5.7.9.

* Thu Jan 16 2025 Leontiy Volodin <lvol@altlinux.org> 5.7.8-alt1
- New version 5.7.8.
- Added vcs tag.

* Wed Sep 11 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.34.0.12.8cf0-alt1
- New version 5.6.34-12-g8cf037d.

* Tue May 07 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.28-alt1
- New version 5.6.28.
- Built via separate qt5 instead system (ALT #48138).

* Fri Mar 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.26-alt1
- New version 5.6.26.

* Wed Mar 20 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.25-alt1
- New version 5.6.25.

* Tue Mar 05 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt2
- Requires: libqt5-core and libqt5-gui = %%_qt5_version.

* Tue Jan 16 2024 Leontiy Volodin <lvol@altlinux.org> 5.6.22-alt1
- New version 5.6.22.

* Thu Nov 30 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.20-alt1
- New version 5.6.20.
- Renamed subpackages:
  + libdtk5-gui -> dtkgui.
  + dtk5-gui-devel -> libdtkgui-devel.

* Fri Mar 10 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.8-alt1
- New version.

* Tue Feb 21 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.6-alt1
- New version.

* Mon Feb 13 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.5-alt1
- New version.
- Removed gcc patch.

* Thu Jan 19 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt2
- Fixed broken configs.

* Wed Jan 18 2023 Leontiy Volodin <lvol@altlinux.org> 5.6.4-alt1
- New version.
- Built using gcc again.

* Mon Dec 19 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.3-alt1
- New version.
- Built using clang instead gcc.

* Fri Dec 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.2.2-alt1
- New version.

* Mon Oct 17 2022 Leontiy Volodin <lvol@altlinux.org> 5.6.0.2-alt1
- New version.
- Upstream:
  + use cmake instead qmake.

* Wed Jun 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.24-alt1
- New version.
- Upstream:
  + fix: use detected pkg-config to fix cross build.
  + fix: the problem of failure to start again when repairing
  anomalies withdraws.
  + fix: modify the color value of TextWarning under the dark mode.
  + fix: dcc can't start after calling setSingleInstance again.

* Fri Apr 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.22-alt1
- New version (5.5.22).

* Tue Feb 08 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.21-alt1
- New version (5.5.21).

* Mon Jul 12 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.17.1-alt1
- New version (5.5.17.1).

* Mon Jun 28 2021 Leontiy Volodin <lvol@altlinux.org> 5.5.2-alt1
- New version (5.5.2) with rpmgs script.

* Thu Apr 08 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.13-alt1
- New version (5.4.13) with rpmgs script.

* Tue Mar 09 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.10-alt1
- New version (5.4.10) with rpmgs script.

* Thu Dec 03 2020 Leontiy Volodin <lvol@altlinux.org> 5.4.0-alt1
- New version (5.4.0) with rpmgs script.

* Wed Oct 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.18-alt1
- New version (5.2.2.18) with rpmgs script.

* Mon Oct 05 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.15-alt1
- New version (5.2.2.15) with rpmgs script.

* Wed Jul 29 2020 Leontiy Volodin <lvol@altlinux.org> 5.2.2.1-alt1
- Initial build for ALT Sisyphus.
