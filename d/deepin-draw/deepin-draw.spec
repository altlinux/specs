%define drawboard_ver 0

%def_disable clang

Name: deepin-draw
Version: 7.0.2
Release: alt1

Summary: A lightweight drawing tool for Linux Deepin

License: GPL-3.0+ and (BSD-3-Clause and Apache-2.0)
# deepin-draw-plugins/: BSD-3-Clause and Apache-2.0
# src/qtsingleapplication/: BSD-3-Clause
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-draw

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires(pre): rpm-build-ninja util-linux rpm-macros-dqt5
BuildRequires: cmake libfreeimage-devel libdtkwidget-devel libexif-devel libxcbutil-devel dqt5-base-devel dqt5-svg-devel dqt5-linguist dqt5-multimedia-devel dqt5-x11extras-devel dqt5-tools-devel
# Requires: deepin-session-shell deepin-dqt5integration
Requires: icon-theme-deepin

%description
A lightweight drawing tool for Linux Deepin.

%package -n libdrawboard%drawboard_ver
Summary: Library for %name
Group: System/Libraries

%description -n libdrawboard%drawboard_ver
The package provides library for %name.

%package -n libdrawboard-devel
Summary: Development files for libdrawboard%drawboard_ver
Group: Development/C++

%description -n libdrawboard-devel
The package provides development files for libdrawboard%drawboard_ver library.

%prep
%setup

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%if_enabled clang
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%else
export CC=gcc
export CXX=g++
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
  -DVERSION=%version \
  -DLIB_INSTALL_DIR=%_libdir \
  #
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang %name

%ifnarch armh i586
mkdir -p %buildroot%_libdir
mv -f %buildroot/usr/lib/libdrawboard* %buildroot%_libdir
%endif

%files -f %name.lang
%doc README.md LICENSE.txt
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_datadir/dbus-1/services/com.deepin.Draw.service
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/draw/

%files -n libdrawboard%drawboard_ver
%_libdir/libdrawboard.so.%{drawboard_ver}*

%files -n libdrawboard-devel
%_libdir/libdrawboard.so
%dir %_includedir/drawBoard/
%_includedir/drawBoard/*.h

%changelog
* Tue Sep 10 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.2-alt1
- New version 7.0.2.

* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 7.0.1-alt1
- New version 7.0.1.
- Cleanup spec.
- Packed new subpackages.
- Built via separate qt5 instead system (ALT #48138).

* Fri Oct 20 2023 Ivan A. Melnikov <iv@altlinux.org> 5.10.6-alt1.1
- NMU: remove (pre) from conditional BR's, they don't
  work like that and are not needed (fixes build on loongarch64).

* Wed Feb 09 2022 Leontiy Volodin <lvol@altlinux.org> 5.10.6-alt1
- New version (5.10.6).

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.7-alt1
- New version (5.9.7).

* Mon Jun 07 2021 Leontiy Volodin <lvol@altlinux.org> 5.9.4-alt1
- New version (5.9.4).
- Built with gcc-c++ and cmake instead clang and qmake.

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.20-alt1
- New version (5.8.0.20) with rpmgs script.

* Thu Jul 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.8.0.19-alt1
- Initial build for ALT Sisyphus (thanks fedora and archlinux for this spec).
