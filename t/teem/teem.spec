%define _unpackaged_files_terminate_build 1

Name: teem
Version: 1.12.0
Release: alt1.20150414.r6245
Summary: Coordinated collection of libraries, with a stable dependency graph
License: LGPL-2.1+
Group: Development/C++
Url: https://github.com/Slicer/teem

ExcludeArch: %arm

# https://github.com/Slicer/teem.git
Source: %name-%version.tar

Patch1: %name-alt-install.patch

BuildRequires: gcc-c++ cmake
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: bzip2-devel
BuildRequires: libfftw3-devel

Requires: lib%name = %EVR

%description
Teem is a coordinated collection of libraries, with a stable
dependency graph.

%package -n lib%name
Summary: Coordinated collection of libraries, with a stable dependency graph
Group: System/Libraries

%description -n lib%name
Teem is a coordinated collection of libraries, with a stable
dependency graph.

This package contains Teem shared libraries.

%package devel
Summary: Coordinated collection of libraries, with a stable dependency graph
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name = %EVR

%description devel
Teem is a coordinated collection of libraries, with a stable
dependency graph.

This package contains development files for Teem.

%prep
%setup
%patch1 -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DTeem_FFTW3:BOOL=ON \
	-DBUILD_EXPERIMENTAL_LIBS:BOOL=ON \
	-DBUILD_EXPERIMENTAL_APPS:BOOL=ON \
	-DBUILD_HEX:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*

%files -n lib%name
%doc LICENSE.txt
%doc README.txt
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

%changelog
* Wed May 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1.20150414.r6245
- Initial build for ALT.
