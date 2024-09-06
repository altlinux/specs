%def_disable clang
%def_enable cmake

Name: deepin-image-viewer
Version: 5.9.18
Release: alt1

Summary: Image viewer for Deepin

License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-image-viewer

Source: %url/archive/%version/%name-%version.tar.gz
Patch: %name-%version-%release.patch

ExcludeArch: armh

Requires: deepin-qt5integration

%if_enabled clang
BuildRequires(pre): clang-devel
%else
BuildRequires(pre): gcc-c++
%endif
%if_enabled cmake
BuildRequires(pre): cmake rpm-build-ninja
%endif
BuildRequires: dqt5-base-devel
BuildRequires: dqt5-tools-devel
BuildRequires: libraw-devel
BuildRequires: dqt5-tools
BuildRequires: libexif-devel
BuildRequires: libdtkwidget-devel
BuildRequires: libimageviewer-devel
BuildRequires: libgio-qt-devel
BuildRequires: dqt5-svg-devel
BuildRequires: dqt5-x11extras-devel
BuildRequires: libfreeimage-devel

%description
%summary.

%package devel
Summary: Development package for %name
Group: Development/KDE and QT

%description devel
Development libraries for %name.

%prep
%setup
%patch -p1
sed -i 's|qt5/plugins/imageformats|../../dqt5/plugins/imageformats|' \
  qimage-plugins/libraw/CMakeLists.txt

%build
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PKG_CONFIG_PATH=%_dqt5_libdir/pkgconfig:$PKG_CONFIG_PATH
export PATH=%_dqt5_bindir:$PATH
%if_enabled cmake
%if_enabled clang
export CC="clang"
export CXX="clang++"
export AR="llvm-ar"
export NM="llvm-nm"
export READELF="llvm-readelf"
%endif
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DVERSION=%version \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
  -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
#
cmake --build "%_cmake__builddir" -j1
%else
%qmake_dqt5 \
%if_enabled clang
  QMAKE_STRIP= -spec linux-clang \
%endif
  CONFIG+=nostrip \
  PREFIX=%prefix \
  DAPP_VERSION=%version \
  DVERSION=%version \
  LIB_INSTALL_DIR=%_libdir \
  QMAKE_RPATHDIR=%_dqt5_libdir \
#
%make
%endif

%install
%if_enabled cmake
%cmake_install
%else
%makeinstall INSTALL_ROOT=%buildroot
%endif
%find_lang %name

%files -f %name.lang
%doc LICENSE.txt README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name/
%dir %_datadir/deepin-manual/
%dir %_datadir/deepin-manual/manual-assets/
%dir %_datadir/deepin-manual/manual-assets/application/
%dir %_datadir/deepin-manual/manual-assets/application/%name/
%_datadir/deepin-manual/manual-assets/application/%name/image-viewer/
%_iconsdir/hicolor/scalable/apps/%name.svg
%_dqt5_plugindir/imageformats/libxraw.so.*
%_datadir/dbus-1/services/com.deepin.ImageViewer.service

%files devel
%_dqt5_plugindir/imageformats/libxraw.so

%changelog
* Wed May 29 2024 Leontiy Volodin <lvol@altlinux.org> 5.9.18-alt1
- New version 5.9.18.
- Built via separate qt5 instead system (ALT #48138).

* Tue Jan 09 2024 Leontiy Volodin <lvol@altlinux.org> 5.9.9-alt3
- Fixed build with APIv23.

* Wed Sep 06 2023 Leontiy Volodin <lvol@altlinux.org> 5.9.9-alt2
- Fixed build with libraw 0.21 (ALT #47425).

* Tue Jan 17 2023 Leontiy Volodin <lvol@altlinux.org> 5.9.9-alt1
- New version (5.9.9).

* Thu Jul 21 2022 Leontiy Volodin <lvol@altlinux.org> 5.9.2-alt1
- New version (5.9.2).

* Thu May 12 2022 Leontiy Volodin <lvol@altlinux.org> 5.8.13-alt1
- New version (5.8.13).
- Not complied for armh architecture.

* Thu Aug 19 2021 Leontiy Volodin <lvol@altlinux.org> 5.8.2-alt1
- New version (5.8.2).

* Wed Jul 14 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.11-alt1
- New version (5.7.11).

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.8-alt1
- New version (5.7.8) with rpmgs script.

* Thu Apr 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.7.4-alt1
- New version (5.7.4) with rpmgs script.

* Mon Mar 15 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt2.gitb4da182
- Updated from commit b4da182b92425880e208c127d5712aef840200a4.
- Built with cmake and ninja instead qmake and make.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.6.3.73-alt1
- New version (5.6.3.73) with rpmgs script.

* Fri Dec 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.6.3.69-alt1
- Initial build for ALT Sisyphus.

