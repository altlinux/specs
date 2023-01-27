%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define soname 1.12

Name: openshadinglanguage
Version: 1.12.8.0
Release: alt1
Summary: Advanced shading language for production GI renderers
Group: Development/Other
License: BSD-3-Clause
URL: https://github.com/AcademySoftwareFoundation/OpenShadingLanguage

# 64 bit only
ExcludeArch: %ix86 %arm

# https://github.com/AcademySoftwareFoundation/OpenShadingLanguage.git
Source: %name-%version.tar

Source2: %name.watch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): libopenimageio-devel
BuildRequires: cmake gcc-c++
BuildRequires: llvm-devel clang-devel
BuildRequires: boost-complete
BuildRequires: ilmbase-devel openexr-devel
BuildRequires: flex bison
BuildRequires: libpugixml-devel
BuildRequires: python3 pybind11-devel libnumpy-py3-devel
BuildRequires: qt5-base-devel
BuildRequires: zlib-devel
BuildRequires: partio-devel

%define oiio_major_minor_ver %(rpm -q --queryformat='%%{VERSION}' libopenimageio-devel | cut -d . -f 1-2)

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
%cmake \
	-DCMAKE_CXX_STANDARD=17 \
	-DOSL_BUILD_MATERIALX:BOOL=ON \
	-DOSL_SHADER_INSTALL_DIR:PATH=%_datadir/%name/shaders/ \
	-DSTOP_ON_WARNING:BOOL=OFF \
	%nil

%cmake_build

%install
%cmake_install

# Move the OpenImageIO plugin into its default search path
mkdir -p %buildroot%_libdir/OpenImageIO-%{oiio_major_minor_ver}
mv %buildroot%_libdir/osl.imageio.so %buildroot%_libdir/OpenImageIO-%{oiio_major_minor_ver}/

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
