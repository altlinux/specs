%define somajor 4

Name: scnlib
Version: 4.0.1
Release: alt1

Summary: scanf for modern C++
License: Apache-2.0
Group: Development/C++
Url: https://scnlib.dev
Vcs: https://github.com/eliaskosunen/scnlib.git

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libfast_float-devel >= 5.0.0
BuildRequires: ctest libgtest-devel libgmock-devel

%description
scnlib is a modern C++ library for replacing scanf and std::istream.
It provides a fast, type-safe alternative for parsing values from
input, with an interface mirroring that of std::format / {fmt}.

%package -n libscn%somajor
Summary: Shared library of scnlib, a modern C++ scanning library
Group: System/Libraries

%description -n libscn%somajor
scnlib is a modern C++ library for replacing scanf and std::istream.
It provides a fast, type-safe alternative for parsing values from
input, with an interface mirroring that of std::format / {fmt}.

This package contains the shared library libscn.so.%somajor.

%package -n libscn-devel
Summary: Development files for scnlib, a modern C++ scanning library
Group: Development/C++
Requires: libscn%somajor = %EVR
Requires: libfast_float-devel >= 5.0.0

%description -n libscn-devel
scnlib is a modern C++ library for replacing scanf and std::istream.
It provides a fast, type-safe alternative for parsing values from
input, with an interface mirroring that of std::format / {fmt}.

This package contains headers and CMake configuration files needed
for developing applications that use scnlib.

%prep
%setup
%patch0 -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DSCN_INSTALL:BOOL=ON \
	-DSCN_USE_EXTERNAL_FAST_FLOAT:BOOL=ON \
	-DSCN_TESTS:BOOL=ON \
	-DSCN_USE_EXTERNAL_GTEST:BOOL=ON \
	-DSCN_DOCS:BOOL=OFF \
	-DSCN_EXAMPLES:BOOL=OFF \
	-DSCN_BENCHMARKS:BOOL=OFF \
	-DSCN_BENCHMARKS_BUILDTIME:BOOL=OFF \
	-DSCN_BENCHMARKS_BINARYSIZE:BOOL=OFF \
	%nil
%cmake_build

%install
%cmakeinstall_std

%check
%ctest

%files -n libscn%somajor
%doc LICENSE
%_libdir/libscn.so.%{somajor}*

%files -n libscn-devel
%doc README.md CHANGELOG.md
%dir %_includedir/scn
%_includedir/scn/*.h
%_libdir/libscn.so
%dir %_libdir/cmake/scn
%_libdir/cmake/scn/*.cmake

%changelog
* Sun Jul 26 2026 Anton Farygin <rider@altlinux.org> 4.0.1-alt1
- initial build for Sisyphus
