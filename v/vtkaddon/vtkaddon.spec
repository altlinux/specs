%define _unpackaged_files_terminate_build 1

Name: vtkaddon
Version: 0
Release: alt1.git.402e7c6
Summary: General-purpose features that may be integrated into VTK library in the future
License: BSD-style
Group: Development/Tools
Url: https://github.com/Slicer/vtkAddon

ExcludeArch: %arm

# https://github.com/Slicer/vtkAddon.git
Source: %name-%version.tar

Patch1: vtkaddon-alt-install.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ cmake
BuildRequires: libvtk-devel

%description
This module contains general-purpose features
that may be integrated into VTK library in the future.

%package -n lib%name
Summary: General-purpose features that may be integrated into VTK library in the future
Group: System/Libraries

%description -n lib%name
This module contains general-purpose features
that may be integrated into VTK library in the future.

This package contains vtkAddon shared libraries.

%package devel
Summary: General-purpose features that may be integrated into VTK library in the future
Group: Development/C++
Requires: lib%name = %EVR
Requires: python3-module-%name = %EVR

%description devel
This module contains general-purpose features
that may be integrated into VTK library in the future.

This package contains development files for vtkAddon.

%package -n python3-module-%name
Summary: General-purpose features that may be integrated into VTK library in the future
Group: Development/Python3
Requires: lib%name = %EVR

%description -n python3-module-%name
This module contains general-purpose features
that may be integrated into VTK library in the future.

This package provides Python bindings to vtkAddon.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DvtkAddon_USE_UTF8:BOOL=ON \
	-DvtkAddon_WRAP_PYTHON:BOOL=ON \
	-DvtkAddon_INSTALL_NO_DEVELOPMENT:BOOL=OFF \
	-DvtkAddon_INSTALL_LIB_DIR:STRING=%_lib \
	-DvtkAddon_INSTALL_CMAKE_DIR:STRING=%_lib/cmake/vtkAddon \
	-DvtkAddon_INSTALL_PYTHON_MODULE_LIB_DIR=%_lib/python3/site-packages \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc LICENSE
%doc README.md
%_libdir/lib*.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_libdir/cmake/*

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Fri May 21 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0-alt1.git.402e7c6
- Initial build for ALT.
