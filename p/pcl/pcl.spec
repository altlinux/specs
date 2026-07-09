Name:    pcl
Version: 1.15.1
Release: alt1

Summary: Point Cloud Library (PCL)
License: BSD-3-Clause
Group:   Other
URL:     http://pointclouds.org
VCS:     https://github.com/PointCloudLibrary/pcl

Source: %name-%version.tar
Patch0: eigen3-version-compat.patch
Patch1: system-gtest.patch
Patch2: cuda-io-pkgconfig-no-openni.patch
Patch3: cloud-composer-export-symbols.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++ gcc14-c++
BuildRequires: nvidia-cuda-devel nvidia-cuda-devel-static nvidia-cuda-toolkit
BuildRequires: eigen3-devel libflann-devel libflann-devel-static
BuildRequires: libvtk-devel libgl2ps-devel libhdf5-devel libxml2-devel
BuildRequires: jsoncpp-devel libXext-devel libX11-devel libXrandr-devel
BuildRequires: libGL-devel libXi-devel boost-devel boost-signals-devel
BuildRequires: boost-interprocess-devel boost-asio-devel boost-filesystem-devel
BuildRequires: libusb-devel doxygen graphviz libpng-devel python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme libqhull-devel libGLEW-devel
BuildRequires: libpcap-devel libfreeglut-devel libgtest-devel libcjson-devel
BuildRequires: openni-devel libtheora-devel libogg-devel libnetcdf-devel
BuildRequires: libcgns-devel libharu-devel libproj-devel libsqlite3-devel
BuildRequires: libjpeg-devel libtiff-devel librealsense-devel libfreetype-devel
BuildRequires: libdouble-conversion-devel nlohmann-json-devel libbenchmark-devel

ExclusiveArch: x86_64

%description
The Point Cloud Library (PCL) is a standalone, large scale, open project
for 2D/3D image and point cloud processing.

The PCL framework contains numerous state-of-the art algorithms including
filtering, feature estimation, surface reconstruction, registration, model
fitting and segmentation.

%package devel
Summary: Development files for %name
Group: Development/C++
ExclusiveArch: x86_64
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Point cloud tools and viewers
Group: Other
ExclusiveArch: x86_64
Requires: %name = %EVR

%description tools
This package contains tools for point cloud file processing and viewers
for point cloud files and live Kinect data.

%package doc
Summary: PCL API documentation
Group: Documentation
BuildArch: noarch
ExclusiveArch: x86_64

%description doc
The %name-doc package contains API documentation for the Point Cloud
Library.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Workaround: CUDA 12.9 CCCL _CCCL_PP_SPLICE_WITH_IMPL1 macro
# has only 2 args (SEP, P1) but is called with 3 in some expansion
# paths. GCC 14+ treats variadic macro arg mismatch as hard error.
# We inject a fix via -include into all CUDA compilations.
cat > fix_cccl.h << 'FIXEOF'
#include <cuda/std/__cccl/preprocessor.h>
#undef _CCCL_PP_SPLICE_WITH_IMPL1
#define _CCCL_PP_SPLICE_WITH_IMPL1(SEP, P1, ...) P1
FIXEOF

# Inject -include flag at cmake level (avoids shell quoting issues)
_script1='/^if(CMAKE_CUDA_COMPILER)/a set(CMAKE_CUDA_FLAGS "'
_script2='${CMAKE_CUDA_FLAGS} -include ${CMAKE_SOURCE_DIR}/fix_cccl.h")'
sed -i "${_script1}${_script2}" cmake/pcl_find_cuda.cmake

# sphinxcontrib.doxylink is not available in ALT — remove it from Sphinx configs
sed -i "s/, 'sphinxcontrib.doxylink'//g" \
  doc/tutorials/content/conf.py \
  doc/advanced/content/conf.py
sed -i "/^doxylink =/d" \
  doc/tutorials/content/conf.py \
  doc/advanced/content/conf.py

%build
export CUDA_PATH=%_prefix

%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DWITH_DOCS=ON \
  -DWITH_CUDA=ON \
  -DWITH_TUTORIALS=ON \
  -DBUILD_apps=ON \
  -DBUILD_global_tests=ON \
  -DBUILD_GPU=ON \
  -DBUILD_CUDA=ON \
  -DBUILD_cuda_io=ON \
  -DBUILD_cuda_apps=OFF \
  -DBUILD_gpu_tracking=ON \
  -DBUILD_examples=ON \
  -DBUILD_benchmarks=ON \
  -DBUILD_simulation=ON \
  -DBUILD_apps_3d_rec_framework=ON \
  -DBUILD_apps_cloud_composer=ON \
  -DBUILD_apps_in_hand_scanner=ON \
  -DBUILD_apps_modeler=ON \
  -DBUILD_apps_point_cloud_editor=ON \
  -DPCL_DISABLE_VISUALIZATION_TESTS=ON \
  -DOPENNI_INCLUDE_DIR:PATH=%_includedir/ni \
  -DPCL_WARNINGS_ARE_ERRORS=OFF \
  -DPCL_PKGCONFIG_SUFFIX:STRING="" \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_CUDA_COMPILER=%_bindir/nvcc \
  -DCMAKE_CUDA_HOST_COMPILER=%_bindir/g++-14 \
  -DCUDAToolkit_ROOT=%_prefix \
  -Wno-dev

%cmake_build

%install
%cmake_install

# Remove libtool archives
find %buildroot -name '*.la' -exec rm -f {} ';'

# Remove static library that triggers ALT's brp-strip-lto
# (only contains LTO GIMPLE bytecode, not packaged anyway)
rm -f %buildroot%_libdir/libpcl_cc_tool_interface.a

# cc_tool plugins have undefined symbols (resolved at dlopen from pcl_cloud_composer)
%add_verify_elf_skiplist %_libdir/libpcl_cc_tool_*.so*

# Just a dummy test
rm -f %buildroot%_bindir/timed_trigger_test

# Remove installed documentation (will use %doc)
rm -rf %buildroot%_datadir/doc

pushd %_cmake__builddir
mv doc/doxygen/html doc/doxygen/api
rm -f doc/doxygen/api/_form*
mv doc/tutorials/html doc/tutorials/tutorials
cp -fr ../doc/tutorials/content/sources doc/tutorials/tutorials
mv doc/advanced/html doc/advanced/advanced
cp -fr ../doc/advanced/content/files/* doc/advanced/advanced
popd

mkdir -p %buildroot%_libdir/cmake/pcl
mv %buildroot%_datadir/%name-*/*.cmake %buildroot%_libdir/cmake/pcl/
mv %buildroot%_datadir/%name-*/Modules %buildroot%_libdir/cmake/pcl/

%check
# Run only headless computational tests (no display or GPU required)
# enable_testing() is called in test/CMakeLists.txt (not top-level),
# so point ctest at the test/ subdirectory where tests are registered.
# CMAKE_SKIP_RPATH=ON disables rpath, so set LD_LIBRARY_PATH to find libs.
export LD_LIBRARY_PATH="%_builddir/%name-%version/%_cmake__builddir%_libdir\
${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

%ctest --test-dir %_cmake__builddir/test --tests-regex "common_|geometry_|a_octree"

%files
%doc LICENSE.txt README.md
%_libdir/*.so.*
%_datadir/%name-*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_libdir/cmake/pcl

%files tools
%_bindir/pcl_*

%files doc
%doc %_cmake__builddir/doc/doxygen/api
%doc %_cmake__builddir/doc/tutorials/tutorials
%doc %_cmake__builddir/doc/advanced/advanced

%changelog
* Wed Jul 08 2026 Sergey Palcheh <minergenon@altlinux.org> 1.15.1-alt1
- initial build for ALT Sisyphus

