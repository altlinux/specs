%define _unpackaged_files_terminate_build 1

%def_with check

Name: sol2
Version: 20261006
Release: alt1

Summary: C++17 header-only binding library for Lua
License: MIT
Group: Development/C++
URL: https://github.com/maisvendoo/sol2
VCS: https://github.com/maisvendoo/sol2.git

Source0: %name-%version.tar
Patch0: sol2-20261006-use-system-catch2.patch
Patch1: sol2-20261006-fix-system-lua-target.patch
Patch2: sol2-20261006-fix-32bit-alignment-test.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: catch-devel
BuildRequires: liblua5.4-devel
%if_with check
BuildRequires: ctest
%endif

%description
sol2 is a header-only C++ library providing high-level bindings
between C++ and Lua.

It supports Lua 5.1 and newer, including LuaJIT, and provides
bindings for functions, classes, containers, tables, user types,
and other C++ constructs.

%package devel
Summary: Development files for sol2
Group: Development/C++
Requires: liblua5.4-devel

%description devel
Development headers, CMake configuration files and pkg-config
metadata for sol2, a header-only C++ binding library for Lua.

%prep
%setup
%autopatch -p1

%build
%cmake \
    -DSOL2_BUILD_LUA=OFF \
    -DSOL2_LUA_VERSION=5.4 \
    -DSOL2_TESTS=ON \
    -DSOL2_TESTS_SINGLE=OFF \
    -DSOL2_EXAMPLES=OFF \
    -DSOL2_INTEROP_EXAMPLES=OFF \
    -DSOL2_DYNAMIC_LOADING_EXAMPLES=OFF \
    -DSOL2_SINGLE=OFF \
    -DSOL2_DOCS=OFF \
    -DSOL2_ENABLE_INSTALL=ON

%cmake_build

%install
%cmake_install

%check
ctest --test-dir %_cmake__builddir --output-on-failure

%files devel
%doc README.md LICENSE.txt
%_includedir/sol/
%_datadir/cmake/sol2/
%_datadir/pkgconfig/sol2.pc

%changelog
* Tue Oct 06 2026 Timofei Fedotov <sovtouch@altlinux.org> 20261006-alt1
- Initial build for ALT Sisyphus.
