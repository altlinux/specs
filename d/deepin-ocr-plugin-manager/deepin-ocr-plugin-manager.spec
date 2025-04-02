%define dopm_ver 1

%def_disable clang

Name: deepin-ocr-plugin-manager
Version: 0.0.2.0019
Release: alt1

Summary: Deepin OCR plugin manager

License: Apache-2.0 and BSL-1.0 and GPL-3.0+
Group: Graphics
Url: https://github.com/linuxdeepin/deepin-ocr-plugin-manager
Vcs: https://github.com/linuxdeepin/deepin-ocr-plugin-manager.git

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-ocr-plugin-manager-0.0.2.0019-alt-fixes-symbols.patch

ExcludeArch: ppc64le

BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake libncnn-devel deepin-libopencv_world-devel
%if_enabled clang
BuildRequires: clang-devel lld-devel
%else
BuildRequires: gcc-c++ libgomp-devel
%endif

%description
%summary.

%package -n lib%name%dopm_ver
Summary: Development package for %name
Group: System/Libraries

%description -n lib%name%dopm_ver
The package provides development files for %name.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C++

%description -n lib%name-devel
The package provides development files for %name.

%package models
Summary: Models for %name
Group: Graphics
# non-identical noarch packages
# FILETRIGGERSCRIPTPROG:1 (none)
#BuildArch: noarch

%description models
The package provides models for %name.

%prep
%setup
%autopatch -p1
# deepin's opencv_mobile does not have .pc file
sed -i 's| opencv_mobile||; s|stdc++fs|stdc++|' \
  src/CMakeLists.txt

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif
export CPLUS_INCLUDE_PATH=%_includedir/deepin/opencv4:%_includedir/opencv4:$CPLUS_INCLUDE_PATH
export LIBS=" -L%_libdir/deepin -lopencv_world":$LIBS
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DLIB_INSTALL_DIR=%_libdir \
  -DVERSION=%version \
  -DDEFINES+="VERSION=%version" \
%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files -n lib%name%dopm_ver
%_libdir/lib%name.so.%{dopm_ver}*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name/
%_includedir/%name/*.h
%_pkgconfigdir/%name.pc

%files models
%dir %_datadir/%name/
%_datadir/%name/model/

%changelog
* Thu Mar 27 2025 Leontiy Volodin <lvol@altlinux.org> 0.0.2.0019-alt1
- Initial build for ALT Sisyphus.
