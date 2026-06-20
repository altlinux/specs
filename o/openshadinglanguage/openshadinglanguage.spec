%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 1.15

# https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/issues/1810
%define optflags_lto %nil

# the required range is 11.0...20.1
%define llvm_ver 21.1

%ifarch x86_64 aarch64
%def_with optix
%filter_from_requires /libcudart\.so\.12/d
%else
%def_without optix
%endif

Name: openshadinglanguage
Version: 1.15.5.0
Release: alt2

Summary: Advanced shading language for production GI renderers
License: BSD-3-Clause
Group: Development/Other

URL: https://github.com/AcademySoftwareFoundation/OpenShadingLanguage

ExcludeArch: %ix86

Source: %name-%version.tar
Source2: %name.watch

Patch0: osl-alt-optix-inc.patch
Patch1: osl-alt-oiio-plugin-path.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): libopenimageio-devel
BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: llvm%{llvm_ver}-devel clang%{llvm_ver}-devel
BuildRequires: boost-complete
BuildRequires: openexr-devel
BuildRequires: flex bison
BuildRequires: libpugixml-devel
BuildRequires: python3 pybind11-devel libnumpy-py3-devel
BuildRequires: qt6-base-devel
BuildRequires: zlib-devel
BuildRequires: partio-devel
BuildRequires: librobin-map-devel
%if_with optix
BuildRequires: optix-devel
# CUDA 12.x nvcc cannot parse libstdc++-15 headers (new __is_pointer,
# __is_volatile, __array_rank builtins). Force g++-14 as nvcc host compiler.
BuildRequires: gcc14-c++
%endif

%define oiio_major_minor_ver %(rpm -q --queryformat='%%{VERSION}' libopenimageio-devel | cut -d . -f 1-2)

%ifarch x86_64
%add_verify_elf_skiplist %_libdir/lib_*_oslexec.so
%endif

%description
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

%package -n lib%name%soname
Summary: Advanced shading language for production GI renderers
Group: System/Libraries

%description -n lib%name%soname
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

%package -n openimageio-plugin-%name
Summary: Open Shading Language input plugin for OpenImageIO
Group: System/Libraries

%description -n openimageio-plugin-%name
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

This is a plugin to access Open Shading Language from OpenImageIO.

%package devel
Summary: Advanced shading language for production GI renderers
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR
Requires: %name-example-shaders-source = %EVR
Requires: %name-common-headers = %EVR
Requires: python3-module-%name = %EVR
Requires: openimageio-plugin-%name = %EVR

%description devel
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

This package contains development files for Open Shading Language.

%package doc
Summary: Documentation for OpenShadingLanguage
Group: Documentation

%description doc
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

This package contains documentation for Open Shading Language.

%package example-shaders-source
Summary: OSL shader examples
Group: Development/Other
Requires: %name-common-headers = %EVR

%description example-shaders-source
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

This package contains some Open Shading Language example shaders.

%package common-headers
Summary: OSL standard library and auxiliary headers
Group: Development/C++

%description common-headers
Open Shading Language (OSL) is a small but rich language
for programmable shading in advanced renderers and other applications,
ideal for describing materials, lights, displacement, and pattern generation.

This package contains the Open Shading Language standard library headers,
as well as some additional headers useful for writing shaders.

%package -n python3-module-%name
Summary: Open Shading Language (OSL) python3 module
Group: Development/Python3

%description -n python3-module-%name
Open Shading Language (OSL) python3 module.

%package optix
Summary: NVIDIA OptiX kernels
Group: Graphics

%description optix
NVIDIA OptiX kernels for OSL. This is currently used to cache ptx generation
for OptiX/GPU rendering.

%prep
%setup
%autopatch -p1

%build
export ALTWRAP_LLVM_VERSION=%llvm_ver
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_STRIP:STRING="" \
	-DCMAKE_CXX_STANDARD=17 \
	-DOSL_SHADER_INSTALL_DIR:PATH=%_datadir/%name/shaders/ \
	-DSTOP_ON_WARNING:BOOL=OFF \
%ifarch x86_64
	-DUSE_SIMD="avx,f16c" \
	-DUSE_BATCHED="b8_AVX" \
%endif
%if_with optix
	-DOSL_USE_OPTIX:BOOL=ON \
	-DOSL_PTX_INSTALL_DIR:PATH=%_datadir/%name/ptx/ \
	-DOSL_EXTRA_NVCC_ARGS="-ccbin=/usr/bin/g++-14" \
%endif
	%nil

%cmake_build -j4

%install
%cmake_install
# remove examples and unused files
rm -f %buildroot%_prefix/build-scripts/serialize-bc.py
rm -f %buildroot%_prefix/cmake/llvm_macros.cmake

%files
%_bindir/*

%files -n lib%name%soname
%doc LICENSE.md THIRD-PARTY.md
%doc CHANGES.md CODE_OF_CONDUCT.md CONTRIBUTING.md GOVERNANCE.md README.md
%_libdir/lib*.so.%{soname}
%_libdir/lib*.so.%{soname}.*

%files -n openimageio-plugin-%name
%_libdir/OpenImageIO-%{oiio_major_minor_ver}/osl.imageio.so

%if_with optix
%files optix
%_datadir/%name/ptx
%endif

%files devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/*
%_pkgconfigdir/*

%files doc
%doc %_defaultdocdir/OSL/

%files example-shaders-source
%_datadir/%name/shaders/*.osl
%_datadir/%name/shaders/*.oso

%files common-headers
%dir %_datadir/%name
%dir %_datadir/%name/shaders
%_datadir/%name/shaders/*.h

%files -n python3-module-%name
%python3_sitelibdir/oslquery

%changelog
* Sat Jun 20 2026 Michael Shigorin <mike@altlinux.org> 1.15.5.0-alt2
- E2K: no need for an older llvm version

* Sat Jun 06 2026 Anton Farygin <rider@altlinux.org> 1.15.5.0-alt1
- 1.15.4.0 -> 1.15.5.0

* Mon May 25 2026 Anton Farygin <rider@altlinux.org> 1.15.4.0-alt1
- 1.14.10.0 -> 1.15.4.0

* Tue Apr 14 2026 L.A. Kostis <lakostis@altlinux.ru> 1.14.10.0-alt0.1
- 1.14.10.0.
- oiio plugin: use OIIO cmake variable for plugin path.

* Thu Feb 19 2026 L.A. Kostis <lakostis@altlinux.ru> 1.14.8.0-alt0.1
- 1.14.8.0.
- compile w/ llvm21.1.

* Tue Nov 25 2025 L.A. Kostis <lakostis@altlinux.ru> 1.14.7.0-alt0.2
- aarch64: build with optix.

* Wed Aug 06 2025 L.A. Kostis <lakostis@altlinux.ru> 1.14.7.0-alt0.1
- 1.14.7.0.
- x86_64: build with optix (fixed by upstream).

* Mon Jul 21 2025 L.A. Kostis <lakostis@altlinux.ru> 1.14.6.0-alt0.2
- x86_64: disable cuda/optix (can't compile reliably).

* Sun Jul 20 2025 L.A. Kostis <lakostis@altlinux.ru> 1.14.6.0-alt0.1
- 1.14.6.0.
- compile w/ llvm20.1.
- build/optix: limit nprocs to 16.

* Sun Jul 20 2025 L.A. Kostis <lakostis@altlinux.ru> 1.14.5.1-alt0.2
- x86_64: build with optix support.

* Mon May 19 2025 L.A. Kostis <lakostis@altlinux.ru> 1.14.5.1-alt0.1
- 1.14.5.1.
- compile w/ llvm19.1.
- qt5->qt6.
- BR: added librobin-map-devel.

* Fri Jan 17 2025 L.A. Kostis <lakostis@altlinux.ru> 1.13.12.0-alt0.1
- 1.13.12.0.

* Mon Jul 08 2024 L.A. Kostis <lakostis@altlinux.ru> 1.13.10.0-alt0.1
- 1.13.10.0.
- compile with llvm18.
- remove lld hacks.
- x86_64: exclude batched lib from verify-elf checks.

* Thu Apr 18 2024 L.A. Kostis <lakostis@altlinux.ru> 1.13.8.0-alt0.1
- 1.13.8.0.

* Sun Mar 31 2024 Michael Shigorin <mike@altlinux.org> 1.13.7.0-alt0.2.1
- E2K: llvm13.0 so far.

* Fri Mar 22 2024 L.A. Kostis <lakostis@altlinux.ru> 1.13.7.0-alt0.2
- batched: disable AVX2 (as not every hardware supports it).

* Tue Mar 12 2024 L.A. Kostis <lakostis@altlinux.ru> 1.13.7.0-alt0.1
- 1.13.7.0.
- Fix build with lld (allow undefined version in lld).
- x86_64: enable SIMD batched targets.
- x86_64: disable CUDA (due OptiX requires).

* Tue Feb 13 2024 L.A. Kostis <lakostis@altlinux.ru> 1.13.6.1-alt0.1
- 1.13.6.1.

* Fri Dec 08 2023 L.A. Kostis <lakostis@altlinux.ru> 1.12.14.0-alt0.2
- Build with CUDA support.

* Tue Nov 07 2023 L.A. Kostis <lakostis@altlinux.ru> 1.12.14.0-alt0.1
- Updated to upstream version 1.12.14.0.

* Wed Oct 25 2023 L.A. Kostis <lakostis@altlinux.ru> 1.12.13.0-alt0.2
- fix FTBFS: build w/ llvm15.0.

* Thu Jul 13 2023 L.A. Kostis <lakostis@altlinux.ru> 1.12.13.0-alt0.1
- Updated to upstream version 1.12.13.0.

* Sun Jun 18 2023 L.A. Kostis <lakostis@altlinux.ru> 1.12.12.0-alt0.1
- Updated to upstream version v1.12.12.0.
- Disable LTO (causes problems with build).

* Sun Jun 18 2023 L.A. Kostis <lakostis@altlinux.ru> 1.12.8.0-alt2.1
- Use lld for linking with llvm libs built with clang.

* Mon Mar 20 2023 Alexander Burmatov <thatman@altlinux.org> 1.12.8.0-alt2
- Fix build requires.

* Wed Jan 18 2023 Alexander Burmatov <thatman@altlinux.org> 1.12.8.0-alt1
- Updated to upstream version 1.12.8.0.

* Mon Jan 17 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.17.0-alt1
- Updated to upstream version 1.11.17.0.

* Thu Dec 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.16.0-alt1
- Updated to upstream version 1.11.16.0.

* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.15.0-alt1
- Updated to upstream version 1.11.15.0.

* Fri Jul 23 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.14.2-alt1
- Updated to upstream version 1.11.14.2.

* Fri Jun 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.14.1-alt1
- Initial build for ALT.
