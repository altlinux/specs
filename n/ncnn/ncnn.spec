%define llvm_ver 15
%define ncnn_ver 1

%def_disable clang

Name: ncnn
Version: 20221128
Release: alt1

Summary: Mobile neural network inference framework

License: BSD-3-Clause
Group: Engineering
Url: https://github.com/Tencent/ncnn

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ninja
%if_enabled clang
#BuildRequires(pre): rpm-macros-llvm-common
BuildRequires: clang%llvm_ver.0-devel
BuildRequires: lld%llvm_ver.0-devel
BuildRequires: llvm%llvm_ver.0-devel
%else
BuildRequires: gcc-c++
%endif
BuildRequires: cmake
BuildRequires: libgomp-devel python3-devel protobuf-compiler glslang-devel libprotobuf-devel libvulkan-devel

%description
High-performance neural network inference framework
optimized for the mobile platform.

%package tools
Summary: %summary
Group: Engineering

%description tools
High-performance neural network inference framework
optimized for the mobile platform.

The package provides tools for %name.

%package -n libncnn%ncnn_ver
Summary: Development package for %name
Group: System/Libraries

%description -n libncnn%ncnn_ver
The package provides development files for %name.

%package -n libncnn-devel
Summary: Development package for %name
Group: Development/C++

%description -n libncnn-devel
The package provides development files for %name.

%prep
%setup

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang-%llvm_ver
export CXX=clang++-%llvm_ver
export LDFLAGS="-fuse-ld=lld-%llvm_ver $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE='RelWithDebInfo' \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DNCNN_SHARED_LIB=ON \
  -DNCNN_ENABLE_LTO=ON \
  -DNCNN_VULKAN=ON \
  -DNCNN_SYSTEM_GLSLANG=ON \
  -DNCNN_BUILD_EXAMPLES=OFF \
  -DGLSLANG_TARGET_DIR=%_libdir/cmake \
%nil
cmake --build "%_cmake__builddir" -j%__nprocs

%install
%cmake_install

%files tools
%_bindir/*

%files -n libncnn%ncnn_ver
%_libdir/libncnn.so.%{ncnn_ver}*

%files -n libncnn-devel
%dir %_includedir/ncnn/
%_includedir/ncnn/*.h
%dir %_libdir/cmake/ncnn/
%_libdir/cmake/ncnn/*.cmake
%_libdir/libncnn.so
%_pkgconfigdir/ncnn.pc

%changelog
* Fri Feb 03 2023 Leontiy Volodin <lvol@altlinux.org> 20221128-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the spec).
