%define majver 3.1

Name: volk
Version: %majver.2
Release: alt1

Summary: Vector-Optimized Library of Kernels
License: LGPL-3.0-or-later
Group: Development/C++

Url: http://libvolk.org/
Source0: %name-%version.tar
Source1: cpu_features.tar
Patch2000: %name-e2k.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: liborc-devel orc
BuildRequires: boost-filesystem-devel
#BuildRequires: git-core

# python subpackage
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-mako

%define descr \
VOLK:\
- is the Vector-Optimized Library of Kernels;\
- is a free library, currently offered under the LGPL-3.0 license;\
- provides an abstraction of optimized math routines targetting\
  several SIMD processors.

%description
%descr

%package -n lib%name
Group: Development/C++
Summary: Vector-Optimized Library of Kernels

%description -n lib%name
%descr

This package contains the shared library for %name.

%package -n lib%name-devel
Summary: Vector-Optimized Library of Kernels
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
%descr

This package contains the headers to build software against %name.

%package -n python3-module-%name
Summary: The Python 3 bindings for VOLK
Group: Development/Python3
Requires: lib%name = %EVR

%description -n python3-module-%name
%descr

This package contains Python 3 module for VOLK.

%prep
%setup -a 1
%ifarch %e2k
sed -i "/incompatible-pointer-types/d" CMakeLists.txt
%patch2000 -p1
%add_optflags -mno-sse4.2
%endif

%build
# workaround, the code is not yet compatible with the strict-aliasing
%add_optflags -fno-strict-aliasing
%cmake \
	-DGR_PYTHON_DIR=%python3_sitelibdir \
	-DPYTHON_EXECUTABLE=%__python3

%cmake_build

%install
%cmake_install

# Not needed
rm -f %buildroot%_bindir/list_cpu_features
rm -f %buildroot%_libdir/libcpu_features.a
rm -fr %buildroot%_libdir/cmake/CpuFeatures

%files
%_bindir/*
%doc COPYING README.md

%files -n lib%name
%_libdir/lib%name.so.%majver
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_libdir/cmake/%name

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Sun Aug 11 2024 Anton Midyukov <antohami@altlinux.org> 3.1.2-alt1
- new version 3.1.2

* Fri Jul 21 2023 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt3
- %%add_optflags -fno-strict-aliasing

* Mon Apr 10 2023 Michael Shigorin <mike@altlinux.org> 3.0.0-alt2
- E2K: fix build (ilyakurdyukov@)
- spec cleanup

* Fri Feb 24 2023 Anton Midyukov <antohami@altlinux.org> 3.0.0-alt1
- new version 3.0.0
- Update License (GPLv3 -> LGPLv3+)

* Mon Jun 27 2022 Anton Midyukov <antohami@altlinux.org> 2.5.1-alt1
- new version 2.5.1

* Mon Jun 28 2021 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Wed May 05 2021 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- new version 2.4.1

* Thu May 21 2020 Anton Midyukov <antohami@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Fri Nov 22 2019 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt1.1
- NMU: rebuilt with boost-1.67.0

* Sun Apr 22 2018 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- new version 1.4

* Fri Aug 11 2017 Anton Midyukov <antohami@altlinux.org> 1.3-alt1
- New version 1.3

* Tue Mar 25 2016 Dmitry Derjavin <dd@altlinux.org> 1.2.1-alt1
- Initial ALT Linux build.
