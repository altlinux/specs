%define _unpackaged_files_terminate_build 1
%define soversion 1
%def_with fftw

Name: teem
Version: 1.12.0
Release: alt2.20150414.r6245
Summary: Coordinated collection of libraries, with a stable dependency graph
%if_with fftw
License: LGPL-2.1-or-later with AdditionRef-GPL-linking-fftw3
%else
License: LGPL-2.1-or-later
%endif
Group: Development/C++
Url: https://teem.sourceforge.net/
VCS: https://github.com/Slicer/teem
# Upstream VCS: git://git.code.sf.net/p/teem/teem.git
# Currently the package is based on the slicer fork

ExcludeArch: %arm

# https://github.com/Slicer/teem.git
Source: %name-%version.tar

Patch0: teem-1.12.0-alt-install-paths.patch
Patch1: teem-1.12.0-debian-cmake-4.1-compat.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: bzip2-devel
%if_with fftw
BuildRequires: libfftw3-devel
%endif

%description
Teem is a coordinated collection of libraries, with a stable
dependency graph.

%package -n libteem%soversion
Summary: Coordinated collection of libraries, with a stable dependency graph
Group: System/Libraries
Obsoletes: libteem

%description -n libteem%soversion
Teem is a coordinated collection of libraries, with a stable
dependency graph.

This package contains Teem shared libraries.

%package devel
Summary: Coordinated collection of libraries, with a stable dependency graph
Group: Development/C++
Requires: libteem%soversion = %EVR
Requires: teem = %EVR

%description devel
Teem is a coordinated collection of libraries, with a stable
dependency graph.

This package contains development files for Teem.

%prep
%setup
%autopatch -p1

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
%if_with fftw
	-DTeem_FFTW3:BOOL=ON \
%endif
	-DBUILD_EXPERIMENTAL_LIBS:BOOL=ON \
	-DBUILD_EXPERIMENTAL_APPS:BOOL=ON \
	-DBUILD_HEX:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*

%files -n libteem%soversion
%doc LICENSE.txt
%doc README.txt
%_libdir/libteem.so.%soversion
%_libdir/libteem.so.%version

%files devel
%_includedir/*
%_libdir/libteem.so
%_libdir/cmake/*

%changelog
* Thu Oct 30 2025 Pavel Petrykin <silverducks@altlinux.org> 1.12.0-alt2.20150414.r6245
- Fix FTBFS: compatibility with newer CMake.
- Ensure compliance with Shared Libs Policy.
- Append SPDX AdditionRef to inform users of libfftw3's GPL license (ALT 56444).

* Wed May 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.12.0-alt1.20150414.r6245
- Initial build for ALT.
