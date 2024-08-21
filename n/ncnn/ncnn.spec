%define ncnn_ver 1

%def_disable clang
%def_without python
# not compatable with glslang 14.2.0
%if "%(rpmquery --qf '%%{VERSION}' glslang-devel)" < "14.2.0"
%def_with glslang
%else
%def_without glslang
%endif
%ifarch loongarch64
%{?optflags_lto:%global optflags_lto %optflags_lto -mlsx -mlasx}
%endif

Name: ncnn
Version: 20240820
Release: alt1

Summary: Mobile neural network inference framework

License: BSD-3-Clause
Group: Engineering
Url: https://github.com/Tencent/ncnn

Source: %url/archive/%version/%name-%version.tar.gz
Source1: vendor.tar

BuildRequires(pre): rpm-build-ninja
# Automatically added by buildreq on Tue Oct 31 2023
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 glslang libgpg-error libp11-kit libsasl2-3 libspirv-tools0 libstdc++-devel python3 python3-base sh5
BuildRequires: cmake glslang-devel libgomp-devel libprotobuf-devel libvulkan-devel protobuf-compiler python3-devel

%if_enabled clang
BuildRequires: clang-devel
BuildRequires: lld-devel
BuildRequires: llvm-devel
%else
BuildRequires: gcc-c++
%endif

%if_with python
BuildRequires: pybind11-devel python3-module-pybind11 python3-module-opencv
%endif

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

%if_with python
%package -n python3-module-%name
Summary: Python3 module for %name
Group: Development/Python3

%description -n python3-module-%name
The package provides python3 module for %name.
%endif

%prep
%setup -a1

%if_without glslang
rmdir glslang
mv -f vendor/glslang . -v
sed -i '/OGLCompiler /d' CMakeLists.txt
%endif

%if_with python
# use system pybind11
sed -i '24a include(pybind11_add_module)' \
  python/CMakeLists.txt
sed -i '/add_subdirectory(pybind11)/d' \
  python/CMakeLists.txt
%else
rmdir python/pybind11
mv -f vendor/python/pybind11 python -v
%endif

%build
%if_enabled clang
%define optflags_lto -flto=thin
export CC=clang
export CXX=clang++
export LDFLAGS="-fuse-ld=lld $LDFLAGS"
%endif

%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE='RelWithDebInfo' \
  -DCMAKE_INSTALL_PREFIX=%_prefix \
  -DNCNN_SHARED_LIB=ON \
  -DNCNN_ENABLE_LTO=ON \
  -DNCNN_VULKAN=ON \
  %if_with python
  -DNCNN_PYTHON=ON \
  -Dpybind11_INCLUDE_DIR=%_includedir/pybind11 \
  %endif
  %if_with glslang
  -DNCNN_SYSTEM_GLSLANG=ON \
  -DNCNN_BUILD_EXAMPLES=OFF \
  -DGLSLANG_TARGET_DIR=%_libdir/cmake \
  %endif
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

%if_with python
%files -n python3-module-%name
%python3_sitelibdir/%name-*.egg-info
%python3_sitelibdir/%name/
%endif

%changelog
* Wed Aug 21 2024 Leontiy Volodin <lvol@altlinux.org> 20240820-alt1
- New version 20240820.

* Mon Jul 01 2024 Leontiy Volodin <lvol@altlinux.org> 20240410-alt1
- New version 20240410.
- Fixed build with glslang 14.2.0.

* Wed Jan 10 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 20240102-alt2
- NMU: fixed FTBFS on LoongArch (ensure SIMD is enabled during LTO).

* Wed Jan 10 2024 Leontiy Volodin <lvol@altlinux.org> 20240102-alt1
- New version 20240102.

* Tue Oct 31 2023 Leontiy Volodin <lvol@altlinux.org> 20231027-alt1
- New version 20231027.

* Thu Aug 17 2023 Leontiy Volodin <lvol@altlinux.org> 20230816-alt1
- New version 20230816.

* Fri Jun 09 2023 Leontiy Volodin <lvol@altlinux.org> 20230517-alt1
- New version 20230517.

* Sat Feb 25 2023 Leontiy Volodin <lvol@altlinux.org> 20230223-alt1
- New version (20230223).

* Fri Feb 03 2023 Leontiy Volodin <lvol@altlinux.org> 20221128-alt1
- Initial build for ALT Sisyphus (thanks archlinux for the spec).
