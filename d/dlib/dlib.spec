%define repo dlib
%define soname 19

Name: dlib
Version: 19.24
Release: alt1
Summary: C++ toolkit containing machine learning algorithms and tools
License: BSL-1.0
Group: Engineering
Url: http://dlib.net

Source: https://github.com/davisking/%repo/archive/%version/%repo-%version.tar.gz
Patch: 0001-Fix-build-on-ppc64mips64-2689.patch
# Built from VCS.
# git merge -s ours tag --allow-unrelated-histories

BuildRequires: gcc-c++ cmake rpm-build-python3 python3-module-setuptools python3-module-wheel
BuildRequires: liblapack-devel libX11-devel libpng-devel zlib-devel libjpeg-devel libwebp-devel pybind11-devel python3-module-pybind11

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
%patch -p1

%build
%cmake \
  -DLIB_IN_PROJECT_BUILD=false \
  -DLIB_USE_CUDA=false \
  -DBUILD_SHARED_LIBS=true \
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
* Thu Dec 08 2022 Leontiy Volodin <lvol@altlinux.org> 19.24-alt1
- Initial build for ALT Sisyphus.
- Built as require for howdy.
