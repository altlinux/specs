%define sover 0
%define git d26c233e
%def_disable static

Name: spirv-cross
Version: 0.55.0
Release: alt0.1.g%{git}
Epoch: 1

Summary: tool to parse and convert SPIR-V to other shader languages
Group: Development/C++
License: Apache-2.0

URL: https://github.com/KhronosGroup/SPIRV-Cross
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar
Patch: %name-alt-cmake-path.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
SPIRV-Cross is a practical tool and library for performing reflection on SPIR-V
and disassembling SPIR-V back to high level languages.

%package -n lib%{name}-devel
Summary: %name devel libraries and headers
Group: Development/C++
Requires: lib%{name}-c-shared%{sover} = %EVR

%description -n lib%{name}-devel
%name development libraries and headers

%package -n lib%{name}-c-shared%{sover}
Summary: %name support libraries
Group: System/Libraries
Provides: lib%{name} = %EVR

%description -n lib%{name}-c-shared%{sover}
%name support libraries

%prep
%setup -n %name-%version
%patch -p1
%ifarch %e2k
sed -i "s/make_msl_version(1, 2)/make_msl_version(1, 2, 0)/" spirv_msl.hpp
%endif

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
%if_disabled static
  -DSPIRV_CROSS_STATIC=OFF \
  -DSPIRV_CROSS_CLI=OFF \
%endif
  -DSPIRV_CROSS_SHARED=ON
%cmake_build
%cmake_install

%files -n lib%{name}-c-shared%{sover}
%_libdir/*.so.*

%files -n lib%{name}-devel
%_includedir/spirv_cross
%_pkgconfigdir/*.pc
%_libdir/*.so
%_datadir/cmake/*

%changelog
* Tue Mar 28 2023 L.A. Kostis <lakostis@altlinux.ru> 1:0.55.0-alt0.1.gd26c233e
- Updated to GIT d26c233e (branch sdk-1.3.243).

* Fri Mar 03 2023 L.A. Kostis <lakostis@altlinux.ru> 1:0.54.0-alt0.2.g4212eef6
- Updated to GIT 4212eef6 (branch sdk-1.3.239).

* Tue Dec 13 2022 L.A. Kostis <lakostis@altlinux.ru> 1:0.52.0-alt0.1.gc77b09b5
- Updated to GIT c77b09b5 (branch sdk-1.3.236).

* Mon Oct 03 2022 L.A. Kostis <lakostis@altlinux.ru> 1:0.49.0-alt0.1
- Updated to sdk-1.3.224.1.
- Bump serial.
- Remove cmake hacks.

* Tue Aug 03 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2021.01.15-alt0.2
- e2k: compiler bug workaround.

* Mon Jun 14 2021 L.A. Kostis <lakostis@altlinux.ru> 2021.01.15-alt0.1
- 2021-01-15.

* Tue Sep 08 2020 L.A. Kostis <lakostis@altlinux.ru> 2020.06.29-alt0.1
- Initial build for Sisyphus.
