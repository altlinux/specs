%define repo dlib
%define soname 19

Name: dlib
Version: 19.24.6
Release: alt1
Summary: C++ toolkit containing machine learning algorithms and tools
License: BSL-1.0
Group: Engineering
Url: http://dlib.net

Source: https://github.com/davisking/%repo/archive/%version/%repo-%version.tar.gz
# Built from VCS.
# git merge -s ours tag --allow-unrelated-histories

# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libX11-devel libfftw3-devel libgif-devel libjpeg-devel libpng-devel libsqlite3-devel openmpi-devel python3-devel
# END SourceDeps(oneline)
BuildRequires: cmake rpm-build-python3 python3-module-setuptools python3-module-wheel
BuildRequires: liblapack-devel libopenblas-devel libavdevice-devel libavfilter-devel libavformat-devel libavcodec-devel libswresample-devel libswscale-devel libavutil-devel libpostproc-devel pybind11-devel python3-module-pybind11

%description
Dlib is a general purpose cross-platform C++ library
designed using contract programming and modern C++ techniques.

%package -n lib%name%soname
Summary: Library for %name
Group: System/Libraries

%description -n lib%name%soname
This package provides library for %name.

%package devel
Summary: Development files for %name
Group: Development/C++

%description devel
This package provides development files for %name.

%ifnarch ppc64le
%package -n python3-module-%name
Summary: Python3-module for %name
Group: Development/Python3

%description -n python3-module-%name
This package provides python module for %name.
%endif

%prep
%setup -n %repo-%version
rm -rf dlib/external
sed -i 's|add_subdirectory(../../dlib/external/pybind11 pybind11_build)|find_package(pybind11 CONFIG)|' \
  tools/python/CMakeLists.txt
# don't apply cmake options for cmake into python's setup.py
sed -i -e '/USE_SSE4_INSTRUCTIONS/s| ON | OFF |; /USE_AVX_INSTRUCTIONS/s| ON | OFF |;' \
  dlib/cmake_utils/set_compiler_specific_options.cmake

%build
%cmake \
  -DLIB_IN_PROJECT_BUILD=false \
  -DLIB_USE_CUDA=false \
  -DBUILD_SHARED_LIBS=true \
  -DBLAS_LIBRARIES=%_libdir/libopenblas.so \
  -DDLIB_JXL_SUPPORT=false \
#   -DUSE_AVX_INSTRUCTIONS=false \
#   -DUSE_SSE4_INSTRUCTIONS=false \
#
%cmake_build
%ifnarch ppc64le
%pyproject_build
%endif

%install
%cmake_install
%ifnarch ppc64le
%pyproject_install
%endif

%files -n lib%name%soname
%doc LICENSE.txt README.md
%_libdir/lib%name.so.%{soname}*

%files devel
%_includedir/%name/
%_libdir/cmake/%name/
%_pkgconfigdir/dlib-1.pc
%_libdir/lib%name.so

%ifnarch ppc64le
%files -n python3-module-dlib
%python3_sitelibdir/*%{repo}*
%endif

%changelog
* Mon Sep 02 2024 Leontiy Volodin <lvol@altlinux.org> 19.24.6-alt1
- New version 19.24.6.

* Thu Apr 04 2024 Leontiy Volodin <lvol@altlinux.org> 19.24.4-alt1
- New version 19.24.4.

* Tue Mar 12 2024 Leontiy Volodin <lvol@altlinux.org> 19.24.3-alt1
- New version 19.24.3.

* Thu Nov 09 2023 Leontiy Volodin <lvol@altlinux.org> 19.24.2-alt3
- Built without SSE4 and AVX (ALT #48280).

* Mon Sep 11 2023 Leontiy Volodin <lvol@altlinux.org> 19.24.2-alt2
- Spec:
  + Updated BuildRequires.
  + Fixed build with new ffmpeg.

* Tue Jul 18 2023 Leontiy Volodin <lvol@altlinux.org> 19.24.2-alt1
- New version 19.24.2.
- Spec:
  + Added BuildRequires.

* Mon Dec 12 2022 Leontiy Volodin <lvol@altlinux.org> 19.24-alt2
- Built with system pybind11 instead built-in.

* Thu Dec 08 2022 Leontiy Volodin <lvol@altlinux.org> 19.24-alt1
- Initial build for ALT Sisyphus.
- Built as require for howdy.
