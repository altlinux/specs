%def_disable clang

Name: deepin-ocr
Version: 1.0.7
Release: alt2

Summary: Base character recognition ability on DDE

License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-ocr

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif
BuildRequires: cmake dqt5-base-devel dqt5-tools-devel
BuildRequires: python3-devel python3-module-opencv
BuildRequires: libopenblas-devel liblapack-devel
BuildRequires: libva-devel libvtk-devel libopencv-devel libdc1394-devel
BuildRequires: libdtkcore-devel libdtkwidget-devel
Requires: %name-models

%description
Deepin OCR provides the base character recognition ability on DDE.

%package models
Summary: Models for %name
Group: Graphics
BuildArch: noarch

%description models
The package provides models for %name.

%prep
%setup
# use system opencv
sed -i 's|../3rdparty/opencv-4.5.4/build/install/include/opencv4|%_includedir/opencv4|' \
  src/CMakeLists.txt
sed -i 's|/build/install/lib/libopencv_world.a|/build/install/%_lib/libopencv_world.a|' \
  src/CMakeLists.txt \
  build3rdparty.sh
sed -i 's|-mcpu=power8|-mcpu=power9 -mvsx|' \
  3rdparty/opencv-4.5.4/cmake/OpenCVCompilerOptimizations.cmake

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CMAKE_PREFIX_PATH=%_dqt5_libdir/cmake:$CMAKE_PREFIX_PATH
export PATH=%_dqt5_bindir:$PATH
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=no \
    -DCMAKE_INSTALL_RPATH=%_dqt5_libdir \
    -DVERSION=%version \
    -DLIB_INSTALL_DIR=%_libdir \
    -DDEFINES+="VERSION=%version" \
%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install
%find_lang --with-qt %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/com.deepin.Ocr.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%dir %_datadir/%name/
%dir %_datadir/%name/translations/
%_datadir/%name/translations/deepin-ocr_es_419.qm

%files models
%dir %_datadir/%name/
%_datadir/%name/model/

%changelog
* Tue Sep 10 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt2
- Built via separate qt5 instead system (ALT #48138).

* Fri Feb 03 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt1
- Initial build for ALT Sisyphus.
