%define _unpackaged_files_terminate_build 1
%def_disable check

Name:     binaryen
Version:  123
Release:  alt1
Summary:  Compiler infrastructure and toolchain library for WebAssembly
Group:    Development/C++
License:  Apache-2.0
Vcs:      https://github.com/WebAssembly/binaryen

Source:   %name-%version.tar
Patch100: binaryen-use-system-gtest.patch

BuildRequires(pre): rpm-macros-cmake rpm-macros-python3
BuildRequires: cmake
BuildRequires: gcc-c++

%if_enabled check
BuildRequires: libgtest-devel
BuildRequires: rpm-build-nodejs
BuildRequires: python3(filecheck)
BuildRequires: python3(lit)
%endif

%description
Binaryen is a compiler and toolchain infrastructure library for WebAssembly,
written in C++. It aims to make compiling to WebAssembly easy, fast, and
effective:

* Easy: Binaryen has a simple C API in a single header, and can also be used
  from JavaScript. It accepts input in WebAssembly-like form but also accepts
  a general control flow graph for compilers that prefer that.

* Fast: Binaryen's internal IR uses compact data structures and is designed for
  completely parallel codegen and optimization, using all available CPU cores.
  Binaryen's IR also compiles down to WebAssembly extremely easily and quickly
  because it is essentially a subset of WebAssembly.

* Effective: Binaryen's optimizer has many passes that can improve code very
  significantly (e.g. local coloring to coalesce local variables; dead code
  elimination; precomputing expressions when possible at compile time; etc.).
  These optimizations aim to make Binaryen powerful enough to be used as a
  compiler backend by itself. One specific area of focus is on
  WebAssembly-specific optimizations (that general-purpose compilers might not
  do), which you can think of as wasm minification , similar to minification for
  JavaScript, CSS, etc., all of which are language-specific (an example of such
  an optimization is block return value generation in SimplifyLocals).

%package -n lib%name
Summary: Shared library for %name
Group:   System/Libraries

%description -n lib%name
Shared library for Binaryen (WebAssembly toolchain).

%package -n %name-devel
Summary:   Development files for Binaryen
Group:     Development/C++
Requires:  lib%name = %EVR

%description -n %name-devel
Headers and development files for Binaryen.

%prep
%setup
%patch100 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DBUILD_SHARED_LIB=ON \
    -DBUILD_STATIC_LIB=OFF \
    -DCMAKE_SKIP_RPATH=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DCMAKE_INSTALL_RPATH= \
%if_enabled check
    -DBUILD_TESTS=ON \
%else
    -DBUILD_TESTS=OFF \
%endif
    -DENABLE_WERROR=OFF

%cmake_build

%install
%cmake_install

%check
LD_LIBRARY_PATH=%_cmake_builddir/lib \
./check.py \
    --binaryen-bin %_cmake_builddir/bin \
    --binaryen-lib %_cmake_builddir/lib

%files -n lib%name
%_libdir/lib%name.so

%files -n %name-devel
%_includedir/%name-c.h
%_includedir/wasm-delegations.def

%files
%doc README.md LICENSE
%_bindir/wasm*

%changelog
 * Tue Apr 01 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 123-alt1
 - Initial buid
