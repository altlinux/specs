%define llvm_ver 15

%def_disable clang

Name: deepin-ocr
Version: 1.0.7
Release: alt1

Summary: Base character recognition ability on DDE

License: GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/%name

Source: %url/archive/%version/%name-%version.tar.gz

%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif
BuildRequires: cmake qt5-base-devel qt5-tools-devel
BuildRequires: python3-devel python3-module-opencv
BuildRequires: libopenblas-devel liblapack-devel
BuildRequires: libva-devel libvtk-devel libopencv-devel libdc1394-devel
BuildRequires: dtk5-core-devel dtk5-widget-devel
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
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
export LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
%endif
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
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
* Fri Feb 03 2023 Leontiy Volodin <lvol@altlinux.org> 1.0.7-alt1
- Initial build for ALT Sisyphus.
