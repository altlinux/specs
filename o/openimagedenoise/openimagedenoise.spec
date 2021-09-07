%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname oidn
%define soname 1

Name: openimagedenoise
Version: 1.4.1
Release: alt1
Summary: Intel Open Image Denoise library
Group: Development/Other
License: Apache-2.0
URL: https://www.openimagedenoise.org/

# Library only available on x86_64
ExclusiveArch: x86_64

# https://github.com/OpenImageDenoise/oidn/releases/download/v%version/oidn-%version.src.tar.gz
Source: %oname-%version.tar

Source2: %name.watch

BuildRequires: cmake gcc-c++
BuildRequires: ispc
BuildRequires: python3
BuildRequires: tbb-devel
BuildRequires: libopenimageio-devel

%description
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.
Intel Open Image Denoise is part of the Intel oneAPI Rendering Toolkit
and is released under the permissive Apache 2.0 license.

%package -n lib%name%soname
Summary: Intel Open Image Denoise library
Group: System/Libraries

%description -n lib%name%soname
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.
Intel Open Image Denoise is part of the Intel oneAPI Rendering Toolkit
and is released under the permissive Apache 2.0 license.

%package devel
Summary: Intel Open Image Denoise library
Group: Development/C++
Requires: %name = %EVR
Requires: lib%name%soname = %EVR

%description devel
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.
Intel Open Image Denoise is part of the Intel oneAPI Rendering Toolkit
and is released under the permissive Apache 2.0 license.

This package contains development files for Intel Open Image Denoise.

%prep
%setup -n %oname-%version

%build
%cmake \
	-DOIDN_STATIC_LIB:BOOL=OFF \
	%nil

%cmake_build

%install
%cmake_install

# Remove duplicated documentation
rm -rf %buildroot%_defaultdocdir/OpenImageDenoise

%files
%_bindir/%{oname}*

%files -n lib%name%soname
%doc LICENSE.txt
%doc CHANGELOG.md README.md readme.pdf
%_libdir/lib*.so.%{soname}
%_libdir/lib*.so.%{soname}.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/*

%changelog
* Mon Sep 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.

* Wed Jun 09 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.0-alt1
- Initial build for ALT.
