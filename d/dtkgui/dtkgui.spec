%define _libexecdir %_prefix/libexec

%def_disable clang

Name: dtkgui
Version: 5.6.20
Release: alt1

Summary: Deepin Toolkit, gui module for DDE look and feel

License: LGPL-3.0
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dtkgui

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Wed Oct 18 2023
# optimized out: cmake-modules gcc-c++ glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 libX11-devel libcairo-devel libdouble-conversion3 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglvnd-devel libgpg-error libgsettings-qt liblcms2-devel libp11-kit libqt5-core libqt5-dbus libqt5-gui libqt5-network libqt5-svg libqt5-widgets libqt5-xml libsasl2-3 libssl-devel libstdc++-devel pkg-config python3 python3-base qt5-base-devel qt5-svg-devel sh5 xorg-proto-devel
BuildRequires: cmake dtk6-common-devel libdtkcore-devel libfreeimage-devel libgomp-devel libqtxdg-devel libraw-devel librsvg-devel
# BuildRequires: libpcre2-devel libffi-devel libmount-devel libblkid-devel libselinux-devel libjpeg-devel libtiff-devel bzlib-devel libbrotli-devel libexpat-devel libpixman-devel
# BuildRequires: libXdmcp-devel
%if_enabled clang
BuildRequires: clang-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif

%description
Deepin Toolkit, gui module for DDE look and feel.

%package -n lib%{name}5
Summary: Library for %name
Group: System/Libraries
Provides: libdtk5-gui = %EVR
Obsoletes: libdtk5-gui < %EVR

%description -n lib%{name}5
DtkGui is used for DDE look and feel.
This package contains the shared libraries.

%package -n lib%{name}-devel
Summary: Development package for %name
Group: Graphical desktop/Other
Provides: dtk5-gui-devel = %EVR
Obsoletes: dtk5-gui-devel < %EVR

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
export PATH=%_qt5_bindir:$PATH
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DMKSPECS_INSTALL_DIR=%_qt5_archdatadir/mkspecs/modules/ \
  -DPACKAGE_TOOL_INSTALL_DIR=libexec/dtk5/DGui/bin \
  -DCMAKE_INSTALL_LIBDIR=%_lib \
  -DLIB_INSTALL_DIR=%_libdir \
  -DLIBRARY_INSTALL_DIR=%_lib \
  -DDTK_VERSION=%version \
  -DVERSION=%version \
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
%dir %_libexecdir/dtk5/
%dir %_libexecdir/dtk5/DGui/
%_libexecdir/dtk5/DGui/bin/

%files -n lib%{name}5
%_libdir/libdtkgui.so.5*

%files -n lib%{name}-devel
%dir %_includedir/dtk5/
%_includedir/dtk5/DGui/
%_qt5_archdatadir/mkspecs/modules/qt_lib_dtkgui.pri
%dir %_libdir/cmake/DtkGui/
%_libdir/cmake/DtkGui/DtkGuiConfig.cmake
%_libdir/cmake/DtkGui/DtkGuiConfigVersion.cmake
%_libdir/cmake/DtkGui/DtkGuiTargets*.cmake
%_pkgconfigdir/dtkgui.pc
%_libdir/libdtkgui.so

%changelog
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
