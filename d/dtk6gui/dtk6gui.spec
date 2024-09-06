%define _libexecdir %_prefix/libexec

%def_disable clang

Name: dtk6gui
Version: 6.0.19
Release: alt1

Summary: Deepin Toolkit, gui module for DDE look and feel

License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtk6gui

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja rpm-macros-qt6
BuildRequires: cmake dtk6-common-devel qt6-base-devel libdtk6core-devel librsvg-devel libraw-devel libfreeimage-devel
# waiting Qt6XdgIconLoaderConfig.cmake
# BuildRequires: libqt6xdg-devel
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif

%description
Deepin Toolkit, gui module for DDE look and feel.

%package -n lib%{name}6
Summary: Library for %name
Group: System/Libraries
Provides: libdtk6-gui = %EVR
Obsoletes: libdtk6-gui < %EVR
Requires: libqt6-core = %_qt6_version
Requires: libqt6-gui = %_qt6_version

%description -n lib%{name}6
DtkGui is used for DDE look and feel.
This package contains the shared libraries.

%package -n lib%{name}-devel
Summary: Development package for %name
Group: Graphical desktop/Other
Provides: dtk6-gui-devel = %EVR
Obsoletes: dtk6-gui-devel < %EVR

%description -n lib%{name}-devel
Header files and libraries for %name.

%prep
%setup
%patch -p1

%build
%add_optflags -I/usr/lib/gcc/%{_target_alias}/%{get_version libgomp-devel}/include
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
export PATH=%_qt6_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_qt6_archdatadir/mkspecs/modules/ \
  -DPACKAGE_TOOL_INSTALL_DIR=libexec/dtk6/DGui/bin \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_libdir \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DBUILD_DOCS=OFF \
  %if_enabled clang
  -DLLVM_USE_LINKER=lld \
  %endif
#
cmake --build %_cmake__builddir -j%__nprocs

%install
%cmake_install

%files
%doc README.md LICENSE
%dir %_libexecdir/dtk6/
%dir %_libexecdir/dtk6/DGui/
%_libexecdir/dtk6/DGui/bin/

%files -n lib%{name}6
%_libdir/lib%name.so.6*

%files -n lib%{name}-devel
%dir %_includedir/dtk6/
%_includedir/dtk6/DGui/
%_qt6_archdatadir/mkspecs/modules/qt_lib_dtkgui.pri
%dir %_libdir/cmake/Dtk6Gui/
%_libdir/cmake/Dtk6Gui/Dtk6GuiConfig.cmake
%_libdir/cmake/Dtk6Gui/Dtk6GuiConfigVersion.cmake
%_libdir/cmake/Dtk6Gui/Dtk6GuiTargets*.cmake
%_pkgconfigdir/dtk6gui.pc
%_libdir/lib%name.so

%changelog
* Fri Aug 30 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.19-alt1
- New version 6.0.19.

* Fri May 17 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.16-alt1
- New version 6.0.16.

* Mon Apr 22 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.11-alt1
- New version 6.0.11.

* Tue Apr 02 2024 Leontiy Volodin <lvol@altlinux.org> 6.0.9-alt1
- Initial build for ALT Sisyphus.
