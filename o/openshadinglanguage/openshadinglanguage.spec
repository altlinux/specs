%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 1.13

# https://github.com/AcademySoftwareFoundation/OpenShadingLanguage/issues/1810
%define optflags_lto %nil

# the required range is 9.0...18.9
%ifarch %e2k
%define llvm_ver 13.0
%else
%define llvm_ver 18.1
%endif

Name: openshadinglanguage
Version: 1.13.10.0
Release: alt0.1
Summary: Advanced shading language for production GI renderers
Group: Development/Other
License: BSD-3-Clause
URL: https://github.com/AcademySoftwareFoundation/OpenShadingLanguage

# 64 bit only
ExcludeArch: %ix86

# https://github.com/AcademySoftwareFoundation/OpenShadingLanguage.git
Source: %name-%version.tar

Source2: %name.watch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): libopenimageio-devel
BuildRequires: cmake gcc-c++
BuildRequires: llvm%{llvm_ver}-devel clang%{llvm_ver}-devel
BuildRequires: boost-complete
BuildRequires: openexr-devel
BuildRequires: flex bison
BuildRequires: libpugixml-devel
BuildRequires: python3 pybind11-devel libnumpy-py3-devel
BuildRequires: qt5-base-devel
BuildRequires: zlib-devel
BuildRequires: partio-devel

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

%prep
%setup

%build
export ALTWRAP_LLVM_VERSION=%llvm_ver
%if_with cuda
export GCC_VERSION=12
%endif
%cmake \
	-DCMAKE_CXX_STANDARD=17 \
	-DOSL_BUILD_MATERIALX:BOOL=ON \
	-DOSL_SHADER_INSTALL_DIR:PATH=%_datadir/%name/shaders/ \
	-DSTOP_ON_WARNING:BOOL=OFF \
%ifarch x86_64
	-DUSE_SIMD="avx,f16c" \
	-DUSE_BATCHED="b8_AVX" \
%endif
	%nil

%cmake_build

%install
%cmake_install

# Move the OpenImageIO plugin into its default search path
mkdir -p %buildroot%_libdir/OpenImageIO-%{oiio_major_minor_ver}
mv %buildroot%_libdir/osl.imageio.so %buildroot%_libdir/OpenImageIO-%{oiio_major_minor_ver}/

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
%python3_sitelibdir/*.so

%changelog
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
