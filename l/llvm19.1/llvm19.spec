%define _unpackaged_files_terminate_build 1

%filter_from_requires /python[0-9.]\+(Reporter)/d
%filter_from_requires /python[0-9.]\+(optpmap)/d
%filter_from_requires /python[0-9.]\+(libscanbuild[.].*)/d
# Self-provided by python3(lldb14.0) in a custom path.
%filter_from_requires /python[0-9.]\+(lldb)/d

%global v_major 19
%global v_majmin %v_major.1
%global v_full %v_majmin.1
%global rcsuffix %nil
%global llvm_name llvm%v_majmin
%global clang_name clang%v_majmin
%global clangd_name clangd%v_majmin
%global lld_name lld%v_majmin
%global lldb_name lldb%v_majmin
%global mlir_name mlir%v_majmin
%global polly_name polly%v_majmin
%global clang_sover %v_major
%global clang_cpp_sover %v_major
%global omp_name omp%v_majmin
%global omp_sover %v_majmin
# libomp has own versioning
%global omp_vmajor 5
# According to offload/README.txt
%global libomptarget_arches x86_64 aarch64 ppc64le
%ifarch ppc64le
%global libomp_arch powerpc64le
%else
%global libomp_arch %_arch
%endif
# According libc/src/string/memory_utils/inline_memcpy.h
%global libc_arches x86_64 aarch64

%global llvm_default_name llvm%_llvm_version
%global clang_default_name clang%_llvm_version
%global lld_default_name lld%_llvm_version

%global llvm_prefix %_prefix/lib/llvm-%v_majmin
%global llvm_bindir %llvm_prefix/bin
%global llvm_libdir %llvm_prefix/%_lib
%global llvm_includedir %llvm_prefix/include
%global llvm_libexecdir %llvm_prefix/libexec
%global llvm_datadir %llvm_prefix/share
%global llvm_man1dir %llvm_datadir/man/man1
%global llvm_docdir %llvm_datadir/doc
%global llvm_python3_libdir %llvm_libdir/python3
%global llvm_python3_sitelibdir %llvm_python3_libdir/site-packages

# to make findreq happy with openmp
# as we don't provide libomp.so in _libdir
%add_findreq_skiplist %llvm_libdir/libompd.so
%add_findreq_skiplist %_libdir/libomptarget.so.%omp_sover
%add_findreq_skiplist %_bindir/llvm-omp-device-info-%v_major
%add_findreq_skiplist %_bindir/llvm-omp-kernel-replay-%v_major

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch %ix86 %arm mipsel
%define optflags_debug -g0
#define __nprocs 1
%else
%define optflags_debug -g1
%endif

# LTO-related flags are set by CMake.
# LTO causes LLVM to break badly on %%ix86 see
# https://github.com/llvm/llvm-project/issues/57740
# will enable it conditionally per platform
#%%global optflags_lto %nil

%define hwasan_symbolize_arches x86_64 aarch64
%ifarch riscv64 loongarch64
%def_without lldb
%else
%def_with lldb
%endif

%def_disable tests
# this is not for linking but for building :)
%def_with lld

%ifarch x86_64 ppc64le aarch64
%def_with clang
%def_with mold
%define optflags_lto -flto=thin -ffat-lto-objects
%else
%def_without clang
%def_without mold
%define optflags_lto %nil
%endif

%if_with lldb
%def_with lldb_full
%def_with lldb_python
%def_without lldb_lua
%else
%def_without lldb_full
%def_without lldb_python
%def_without lldb_lua
%endif

%define tarversion %v_full%rcsuffix
%if "%rcsuffix" == ""
%define mversion %v_full
%else
%define mversion %v_full%{?rcsuffix:-%rcsuffix}
%endif

Name: %llvm_name
Version: %v_full
Release: alt0.1
Summary: The LLVM Compiler Infrastructure

Group: Development/C
License: Apache-2.0 with LLVM-exception
Url: http://llvm.org
# Source-URL: https://github.com/llvm/llvm-project/releases/download/llvmorg-%mversion/llvm-project-%tarversion.src.tar.xz
Source: llvm-project-%{v_major}.tar
Patch:  clang-alt-i586-fallback.patch
Patch1: clang-alt-triple.patch
Patch2: 0001-alt-llvm-config-Ignore-wrappers-when-looking-for-current.patch
Patch5: compiler-rt-alt-i586-arch.patch
Patch7: clang-alt-aarch64-dynamic-linker-path.patch
Patch8: clang-tools-extra-alt-gcc-0001-clangd-satisfy-ALT-gcc-s-Werror-return-type.patch
Patch17: llvm-cmake-pass-ffat-lto-objects-if-using-the-GNU-toolcha.patch
Patch18: lld-compact-unwind-encoding.h.patch
Patch19: llvm-alt-cmake-build-with-install-rpath.patch
Patch20: clang-16-alt-rocm-device-libs-path.patch
Patch23: clang-alt-riscv64-dynamic-linker-path.patch
Patch101: clang-ALT-bug-40628-grecord-command-line.patch
Patch102: clang-ALT-bug-47780-Calculate-sha1-build-id-for-produced-executables.patch
Patch103: clang-alt-nvvm-libdevice.patch
Patch104: openmp-alt-soname.patch
# upstream issue 100383
Patch106: llvm-amdgpu-udiv64-opts.patch
Patch107: offload-amdgpu-rocm-path.patch

Patch111: RH-0003-PATCH-clang-Don-t-install-static-libraries.patch
Patch112: RH-0001-Workaround-a-bug-in-ORC-on-ppc64le.patch

Patch200: 0001-RuntimeDyld-RISCV-Minimal-riscv64-support.patch
Patch201: 0002-RuntimeDyld-RISCV-Impleemnd-HI20-and-LO12_I-relocs.patch
Patch202: 0003-RuntimeDyld-RISCV-Add-PCREL_HI20-and-PCREL_LO12_I-re.patch
Patch203: 0004-RuntimeDyld-Minimal-LoongArch64-support.patch

# debian patches for openmp
Patch300: deb-openmp-riscv64.patch

%if_with clang
# https://bugs.altlinux.org/show_bug.cgi?id=34671
%set_verify_elf_method lint=skip
%endif

# ThinLTO requires /proc/cpuinfo to exist; so the same does llvm
BuildPreReq: /proc

# Obtain %%__python3 at prep stage.
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-llvm-common

BuildRequires(pre): cmake >= 3.4.3
BuildRequires: rpm-build >= 4.0.4-alt112 libncursesw-devel
BuildRequires: libstdc++-devel libffi-devel perl-Pod-Parser perl-devel
BuildRequires: zip zlib-devel binutils-devel
BuildRequires: python3-module-myst-parser graphviz
BuildRequires: ninja-build
%if_with lldb
BuildRequires: pkgconfig(liblzma)
BuildRequires: swig-devel
# lldb uses furo sphinx theme
BuildRequires: python3-module-sphinx_basic_ng python3-module-furo
%if_with lldb_full
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(libxml-2.0)
%endif
%if_with lldb_lua
BuildRequires: lua5.3-devel
%endif
%if_with lldb_python
BuildRequires: python3-devel
# python_api doc rely on it
BuildRequires: python3-module-sphinx-automodapi
%endif
%endif #lldb
%if_with clang
BuildRequires: %clang_default_name %llvm_default_name-devel %lld_default_name
%else
BuildRequires: gcc-c++
%endif
%if_with mold
BuildRequires: mold
%endif

%define requires_filesystem Requires: %name-filesystem = %EVR
%requires_filesystem
Requires: llvm >= %_llvm_version

%description
LLVM is a compiler infrastructure designed for compile-time, link-time,
runtime, and idle-time optimization of programs from arbitrary
programming languages. The compiler infrastructure includes mirror sets
of programming tools as well as libraries with equivalent functionality.

%package filesystem
Group: Development/Other
Summary: Owns the installation prefix for LLVM

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description filesystem
This package owns the installation prefix for LLVM. It is designed to be
pulled in by all non-empty LLVM packages.

%package devel
Group: Development/C
Summary: Libraries and header files for LLVM
%requires_filesystem
Requires: llvm-devel >= %_llvm_version
Requires: %name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.

%package gold
Summary: gold linker plugin for LLVM
Group: Development/Tools
%requires_filesystem
# requires: libLLVM
Requires: %name-libs

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description gold
This package contains the gold plugin for LLVM objects.

%package polly
Summary: Framework for High-Level Loop and Data-Locality Optimizations
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description polly
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

This package contains the Polly plugin.

%package libs
Group: Development/C
Summary: LLVM shared libraries
%requires_filesystem
# We pull in the gold plugin for e. g. Clang's -flto=thin to work
# out of the box with gold.
Requires: %name-gold
Requires: %name-polly

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description libs
This package contains shared libraries needed to develop new
native programs that use LLVM.

%package doc
Summary: Documentation for LLVM
Group: Documentation
BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description doc
Documentation for the LLVM compiler infrastructure.

%package tools
Summary: Various minor tools bundled with LLVM
Group: Development/C
BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description tools
This package contains various tools maintained as part of LLVM, including
opt-viewer.

%package -n %clang_name
Summary: A C language family frontend for LLVM
Group: Development/C
%requires_filesystem
# clang uses various parts of GNU crt bundled with gcc.
# Should they be packaged separately?
Requires: gcc
Requires: clang >= %_llvm_version
Requires: %clang_name-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name
clang: noun
    1. A loud, resonant, metallic sound.
    2. The strident call of a crane or goose.
    3. C-language family front-end toolkit.

The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

%package -n libclang%clang_sover
Group: Development/C
Summary: clang shared library
%requires_filesystem
Requires: %clang_name-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n libclang%clang_sover
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

This package contains the clang shared library.

%package -n libclang-cpp%clang_cpp_sover
Group: Development/C
Summary: clang-cpp shared libraries
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n libclang-cpp%clang_cpp_sover
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

This package contains the clang-cpp shared library.

%package -n %clang_name-libs
Group: Development/C
Summary: clang shared libraries
%requires_filesystem
# This is a compat package.
Requires: libclang%clang_sover = %EVR
Requires: libclang-cpp%clang_cpp_sover = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

This package contains shared libraries for the clang compiler.

%package -n %clang_name-support
Group: Development/C
Summary: Support for Clang's shared libraries
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-support
The Clang's shared libraries implement compilers for C and C++, and thus have
to bundle additional platform support headers and libraries for use within the
compilation product. This package contains the platform support.

%package -n %clang_name-support-shared-runtimes
Group: Development/C
Summary: Shared runtimes for Clang's shared libraries
%requires_filesystem
Requires: %clang_name-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-support-shared-runtimes
This package contains shared runtime libraries for Scudo and sanitizers.

%package -n %clang_name-devel
Summary: Header files for clang
Group: Development/C
%requires_filesystem
Requires: clang-devel >= %_llvm_version
Requires: %clang_name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-devel
This package contains header files for the Clang compiler.

%package -n %clang_name-analyzer
Summary: A source code analysis framework
Group: Development/C
BuildArch: noarch
%requires_filesystem
Requires: %clang_name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package -n %clang_name-tools
Summary: Various clang-based tools
Group: Development/C
%requires_filesystem
Requires: %clang_name = %EVR
Requires: clang-tools >= %_llvm_version

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-tools
This package contains various code analysis and manipulation tools based on
libclang, including clang-format.

%package -n %clang_name-doc
Summary: Documentation for Clang
Group: Documentation
# graphviz on %%ix86 produce png with zero size so make it arch again until
# the issue will be fixed
#BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-doc
Documentation for the Clang compiler front-end.

%package -n %clangd_name
Summary: A clang-based language server
Group: Development/C
%requires_filesystem
Requires: clangd >= %_llvm_version
Requires: %clang_name-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clangd_name
This package contains clangd, a Clang-based language server for C and C++.

%package -n %lld_name
Summary: LLD - The LLVM Linker
Group: Development/C
%requires_filesystem
Requires: lld >= %_llvm_version
# /proc needed for normal operation
Requires: /proc

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lld_name
LLD is a linker from the LLVM project. That is a drop-in replacement for system
linkers and runs much faster than them. It also provides features that are
useful for toolchain developers.

%package -n %lld_name-devel
Summary: Header files for LLD
Group: Development/C
%requires_filesystem
Requires: lld-devel >= %_llvm_version
Requires: %lld_name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lld_name-devel
This package contains header files for the LLD linker.

%package -n %lld_name-doc
Summary: Documentation for LLD
Group: Documentation
BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lld_name-doc
Documentation for the LLD linker.

%if_with lldb
%package -n %lldb_name
Summary: A next-level high-performance debugger
Group: Development/Debuggers
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lldb_name
LLDB is a next generation, high-performance debugger. It is built as a set of
reusable components which highly leverage existing libraries in the larger LLVM
project, such as the Clang expression parser and the LLVM disassembler.

%package -n lib%lldb_name
Summary: Shared library for LLDB
Group: Development/Debuggers
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%lldb_name
This package contains the LLDB runtime library.

%package -n lib%lldb_name-devel
Summary: Development files for liblldb
Group: Development/Debuggers
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%lldb_name-devel
This package contains header files to build extensions over lldb, as well as
development symlinks for liblldb.

%package -n python3-module-%lldb_name
Summary: Python 3 scripting support for LLDB
Group: Development/Debuggers
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n python3-module-%lldb_name
This package contains the Python 3 interfaces to LLDB.

%package -n %lldb_name-doc
Summary: Documentation for LLDB
Group: Documentation
BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %lldb_name-doc
Documentation for the LLDB debugger.
%endif

%package -n lib%mlir_name
Summary: Multi-Level Intermediate Representation library
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%mlir_name
MLIR is a novel approach to building reusable and extensible compiler
infrastructure.  MLIR aims to address software fragmentation, improve
compilation for heterogeneous hardware, significantly reduce the cost of
building domain specific compilers, and aid in connecting existing compilers
together.

%package -n lib%mlir_name-devel
Summary: Libraries and header files for MLIR
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%mlir_name-devel
MLIR is a novel approach to building reusable and extensible compiler
infrastructure.  MLIR aims to address software fragmentation, improve
compilation for heterogeneous hardware, significantly reduce the cost of
building domain specific compilers, and aid in connecting existing compilers
together.

This package contains headers and other development files for lib%mlir_name.

%package -n %mlir_name-tools
Summary: Various mlir-based tools
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %mlir_name-tools
MLIR is a novel approach to building reusable and extensible compiler
infrastructure.  MLIR aims to address software fragmentation, improve
compilation for heterogeneous hardware, significantly reduce the cost of
building domain specific compilers, and aid in connecting existing compilers
together.

This package contains some bundled tools.

%package -n lib%polly_name-devel
Summary: Development files for Polly
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%polly_name-devel
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

This package contains header files for the Polly optimizer.

%package -n lib%polly_name-doc
Summary: Documentation for Polly
Group: Development/C
BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%polly_name-doc
Polly is a high-level loop and data-locality optimizer and optimization
infrastructure for LLVM. It uses an abstract mathematical representation based
on integer polyhedron to analyze and optimize the memory access pattern of a
program.

This package contains documentation for the Polly optimizer.

%package -n lib%omp_name
Summary: LLVM/OpenMP Host Runtime (libomp)
Group: System/Libraries
# libomp soname remains the same
Conflicts: lib%omp_name < %EVR
Conflicts: lib%omp_name > %EVR
%requires_filesystem

%description -n lib%omp_name
OpenMP runtime for clang.

%package -n lib%omp_name-devel
Summary: OpenMP header files
Group: Development/C
Requires: %clang_name-support = %EVR
%requires_filesystem

%description -n lib%omp_name-devel
OpenMP header files

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%package -n lib%omp_name-doc
Summary: Documentation for OpenMP
Group: Development/C
BuildArch: noarch
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%omp_name-doc
This package contains documentation for the OpenMP.

%package cmake-common-modules
Summary: LLVM common cmake modules
Group: Development/C
BuildArch: noarch
Requires: cmake-modules
%requires_filesystem

%description cmake-common-modules
These are CMake modules to be shared between LLVM projects strictly at build
time.

These modules are used by llvm runtimes built outside of llvm tree.

%prep
# %setup -n llvm-%tarversion.src -a1 -a2 -a3 -a4 -a5 -a6
# for pkg in clang lld lldb; do
   # mv $pkg-%tarversion.src tools/$pkg
# done
# mv clang-tools-extra-%tarversion.src tools/clang/tools/extra
# for pkg in compiler-rt; do
   # mv $pkg-%tarversion.src projects/$pkg
# done
%setup -n llvm-project-%{v_major}
%patch -p1 -b .alt-i586-fallback
%patch1 -p2 -b .clang-alt-triple
%patch2 -p1
sed -i 's)"%%llvm_bindir")"%llvm_bindir")' llvm/lib/Support/Unix/Path.inc
%patch5 -p1 -b .alt-i586-arch
%patch7 -p1 -b .alt-aarch64-dynamic-linker
%patch8 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1 -b .llvm-cmake-build-with-install-rpath
%patch20 -p1 -b .clang-rocm-device-path
%patch23 -p2
%patch101 -p1
%patch102 -p2
%patch103 -p1
%patch104 -p2
%patch106 -p1 -b .llvm-amdgpu-udiv64-opts
%patch107 -p2 -b .offload-rocm-path

# RH patches
%patch111 -p1
%patch112 -p1

#%%patch200 -p2
#%%patch201 -p2
#%%patch202 -p2
#%%patch203 -p2

# debian patches
%patch300 -p1

# LLVM 12 and onward deprecate Python 2:
# https://releases.llvm.org/12.0.0/docs/ReleaseNotes.html
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
PROJECTS="clang;clang-tools-extra;compiler-rt;mlir;polly"
# for openmp offload
# https://github.com/llvm/llvm-project/issues/106399
RUNTIMES="openmp;offload"
%if_with lld
PROJECTS="$PROJECTS;lld"
%endif
%if_with lldb
PROJECTS="$PROJECTS;lldb"
%endif
export NPROCS="%__nprocs"
if [ "$NPROCS" -gt 64 ]; then
	export NPROCS=64
fi
%define builddir %_cmake__builddir
%define _cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=OFF
%add_optflags -Wno-error=return-type
%cmake -G Ninja -S llvm \
	-DPACKAGE_VENDOR="%vendor" \
%ifnarch loongarch64
%if_with clang
	-DLLVM_PARALLEL_LINK_JOBS=1 \
%else
	-DLLVM_PARALLEL_LINK_JOBS=4 \
%endif
%endif
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%llvm_prefix \
	%_cmake_skip_rpath \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DCMAKE_BUILD_RPATH:STRING='' \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_ENABLE_PROJECTS:STRING="$PROJECTS" \
	-DLLVM_ENABLE_RUNTIMES:STRING="$RUNTIMES" \
	-DLLVM_TARGETS_TO_BUILD="all" \
	-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD='AVR' \
	-DLLVM_ENABLE_LIBCXX:BOOL=OFF \
	-DLLVM_ENABLE_ZLIB:BOOL=ON \
	-DLLVM_ENABLE_FFI:BOOL=ON \
	-DLLVM_ENABLE_RTTI:BOOL=ON \
	-DLLVM_OPTIMIZED_TABLEGEN:BOOL=ON \
	-DLLVM_BINUTILS_INCDIR="%_includedir/bfd" \
	\
	-DCLANG_PLUGIN_SUPPORT:BOOL=ON \
	-DCLANG_LINK_CLANG_DYLIB=ON \
	-DCLANG_FORCE_MATCHING_LIBCLANG_SOVERSION:BOOL=ON \
	-DENABLE_LINKER_BUILD_ID:BOOL=ON \
	\
	-DTARGET_loongarch64_CFLAGS:STRING='-mcmodel=medium' \
	\
	%if_with clang
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	%if_with mold
	-DLLVM_USE_LINKER=mold \
	%else
	-DLLVM_USE_LINKER=lld \
	%endif
	%else
	-DLLVM_ENABLE_LTO=Off \
	%ifnarch riscv64 loongarch64
	-DLLVM_USE_LINKER=gold \
	%endif
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	%endif
	\
	-DLLVM_LIBDIR_SUFFIX:STRING="%_libsuff" \
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	\
	-DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \
	-DLIBOMP_INSTALL_ALIASES=OFF \
	-DOPENMP_LIBDIR_SUFFIX:STRING="%_libsuff" \
	-DOPENMP_INSTALL_LIBDIR=%llvm_libdir \
	\
	%ifarch %libc_arches
	-DRUNTIMES_nvptx64-nvidia-cuda_LLVM_ENABLE_RUNTIMES=libc \
	-DRUNTIMES_amdgcn-amd-amdhsa_LLVM_ENABLE_RUNTIMES=libc \
	-DLLVM_RUNTIME_TARGETS="default;amdgcn-amd-amdhsa;nvptx64-nvidia-cuda" \
	%endif
	%if_enabled tests
	-DLLVM_INCLUDE_TESTS:BOOL=ON \
	-DLLVM_BUILD_TESTS:BOOL=ON \
	-DLLDB_INCLUDE_TESTS:BOOL=ON \
	%else
	%if_with clang
	-DLLDB_TEST_COMPILER:PATH=%_bindir/clang \
	%else
	-DLLDB_TEST_COMPILER:PATH=%_bindir/gcc \
	%endif
	%endif
	%ifarch %ix86
	-DLLVM_DEFAULT_TARGET_TRIPLE:STRING="i586-pc-linux-gnu" \
	%endif
	\
	-DLLVM_INCLUDE_EXAMPLES:BOOL=ON \
	-DLLVM_BUILD_EXAMPLES:BOOL=OFF \
	\
	-DLLVM_INCLUDE_UTILS:BOOL=ON \
	-DLLVM_INSTALL_UTILS:BOOL=OFF \
	\
	-DLLVM_INCLUDE_DOCS:BOOL=ON \
	-DLLVM_BUILD_DOCS:BOOL=ON \
	-DLLVM_ENABLE_SPHINX:BOOL=ON \
	-DSPHINX_WARNINGS_AS_ERRORS:BOOL=OFF \
	-DSPHINX_EXECUTABLE=%_bindir/sphinx-build-3 \
	-DLLVM_ENABLE_DOXYGEN:BOOL=OFF \
	-DLLVM_BUILD_LLVM_DYLIB:BOOL=ON \
	-DLLVM_LINK_LLVM_DYLIB:BOOL=ON \
	-DLLVM_INSTALL_TOOLCHAIN_ONLY:BOOL=OFF \
	-DPYTHON_EXECUTABLE=%_bindir/python3

sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' %builddir/build.ninja
export LD_LIBRARY_PATH=$(pwd)/%builddir/%_lib
ninja -vvv -j $NPROCS -C %builddir

%install
%if_with lld
sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' %builddir/build.ninja
sed -i '/^[[:space:]]*include.*tools\/lld\/docs\/cmake_install.cmake.*/d' %builddir/tools/lld/cmake_install.cmake
%endif
DESTDIR=%buildroot ninja -C %builddir install

# Prepare Clang documentation.
rm -rf %builddir/clang-docs
mkdir -p %builddir/clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln clang/$f %builddir/clang-docs/
done
rm -rf tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}
rm -rf %buildroot%llvm_datadir/clang-doc
mkdir -p %buildroot%llvm_docdir/lld

#install -m 0755 %builddir/%_lib/LLVMHello.so %buildroot%llvm_libdir/
install -m 0755 %builddir/%_lib/BugpointPasses.so %buildroot%llvm_libdir/

%ifarch %ix86
cd %buildroot%llvm_libdir/clang/%v_major/lib/*-*-*-*
ls *-i[3-9]86* | while read f; do ln -s $f $(echo $f | sed 's|i[3-9]86|i386|') ; done
cd -
%endif

# The following files are not used by LLVM builds for Linux.
rm -f %buildroot%llvm_bindir/argdumper
rm -f %buildroot%llvm_datadir/clang/clang-format-bbedit.applescript

# Remove OpenMP static libraries with equivalent shared libraries
rm -rf %buildroot%llvm_libdir/libarcher_static.a
# FIXME! will pack it later
# those files are needed for libompd (OMP debugger)
rm -rf %buildroot%llvm_datadir/gdb

# Install the clang bash completion.
mkdir -p %buildroot%_datadir/bash-completion/completions
ln -sr %buildroot%llvm_datadir/clang/bash-autocomplete.sh %buildroot%_datadir/bash-completion/completions/clang-%v_major

# Symlink executables to %_bindir.
mkdir -p %buildroot%_bindir
for b in %buildroot%llvm_bindir/*; do
	bb="$(basename "$b")"
	echo "$bb" | grep -q -- '-%v_major$' && continue # if already appended
	ln -srv "$b" "%buildroot%_bindir/$bb-%v_major"
done
# Symlink man pages to the man dirs.
for mand in %buildroot%llvm_datadir/man/man*; do
	mand_index="${mand##*/man}"
	for m in "$mand"/*.[1-9]*; do
		# Let's force compress the man page, then symlink it.
		# /usr/lib/llvm-14.0/share/man/manD/utilX.D.xz -> /usr/share/man/manD/utilX-14.D.xz
		# Otherwise, brp-alt(compress) keeps fucking us up.
		# It remakes the symlinks first, then compresses their targets,
		# severing the symlinks.
		/usr/lib/rpm/compress_files "$m"

		mb="$(basename "$m")" # e. g. llvm-ar.1.xz
		new_mb="${mb%%.[1-9]*}-%v_major.$mand_index" # e. g. llvm-ar-12.1.xz

		mkdir -p "%buildroot%_mandir/man$mand_index"
		ln -srv "$m" "%buildroot%_mandir/man$mand_index/$new_mb"
	done
done

# Symlink sonamed shared libraries in %llvm_prefix/%_libdir to %_libdir.
mkdir -p %buildroot%_libdir
find %buildroot%llvm_libdir/*.so* -type f,l \
	| grep -E '^%buildroot%llvm_libdir/.*(%v_major)' | sort | tee %_tmppath/shared-objects \
	| sed 's)%llvm_libdir)%_libdir)' > %_tmppath/shared-object-links
paste %_tmppath/shared-objects %_tmppath/shared-object-links | while read object link; do
	ln -srv "$object" "$link"
done

# OpenMP needs special handling here
ln -srv %buildroot%llvm_libdir/libomp.so.%omp_vmajor %buildroot%_libdir/libomp.so.%omp_vmajor
ln -srv %buildroot%llvm_libdir/libarcher.so %buildroot%_libdir/libarcher.so
%ifarch %libomptarget_arches
mv %buildroot%llvm_libdir/%libomp_arch-unknown-linux-gnu/* %buildroot%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/
ln -srv %buildroot%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget.so.%v_majmin %buildroot%_libdir/libomptarget.so.%v_majmin
%endif
%ifarch %libc_arches
# FIXME! need to figure out why _SUFFIX is not used here
mv %buildroot%llvm_prefix/lib/{amdgcn-amd-amdhsa,nvptx64-nvidia-cuda} %buildroot%llvm_libdir/clang/%v_major/lib/
mv %buildroot%llvm_prefix/lib/%libomp_arch-unknown-linux-gnu/* %buildroot%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/
mv %buildroot%llvm_prefix/lib/clang/%v_major/include/llvm_libc_wrappers/llvm-libc-decls %buildroot%llvm_libdir/clang/%v_major/include/llvm_libc_wrappers/
rm -rf %buildroot%llvm_prefix/lib/{clang,%libomp_arch-unknown-linux-gnu}
rm -rf %buildroot%llvm_libdir/%libomp_arch-unknown-linux-gnu
%endif

# List all packaged binaries in this source package.
find %buildroot%_bindir/*-%v_major > %_tmppath/PATH-executables

# For paranoic reasons library packaging policy covers peculiar directory paths.
# If there are $A.a and $A.so in %llvm_libdir/clang, they should not end up in the
# same package (but can be co-installed on a system).
# Let's list all the $A.so for which $A.a exists into a separate package.
# We also consider i386-symlinks for iN86.
find %buildroot%llvm_libdir/clang -type f,l -name '*.a' -or -name '*.so' | \
    sed -r -n 's/^(\/.+)\.a$/\1/p; s/^(.+)\.so$/\1/p' | sort | uniq -d > %_tmppath/libclang-support-dupes
sed < %_tmppath/libclang-support-dupes 's)^%buildroot)); s/$/.a/' > %_tmppath/libclang-support-static-runtimes
sed < %_tmppath/libclang-support-dupes 's)^%buildroot)); s/$/.so/' > %_tmppath/libclang-support-shared-runtimes
sed < %_tmppath/libclang-support-shared-runtimes 's/^/%%exclude /' > %_tmppath/dyn-files-clang-support
echo "Expelling likely redundant Clang shared runtimes:" && cat %_tmppath/dyn-files-clang-support

# Emit a stanza list for %%files.
# A tool can be accompanied by a man page or not.
emit_filelist() {
    awk -F'\t' '
$1 ~ "bin" { print "%llvm_bindir/" $2; print "%_bindir/" $2 "-%v_major"; }
$1 ~ "man" { print "%llvm_man1dir/" $2 ".1*"; print "%_man1dir/" $2 "-%v_major.1*"; }
'
}

# Emit executable list for %name.
emit_filelist >%_tmppath/dyn-files-%name <<EOExecutableList
bin,man	bugpoint
bin,man	diagtool
bin,man	dsymutil
bin,man	llc
bin,man	lli
bin,man	llvm-addr2line
bin,man	llvm-ar
bin,man	llvm-as
bin,man	llvm-bcanalyzer
bin	llvm-bitcode-strip
bin	llvm-cat
bin	llvm-cfi-verify
bin,man	llvm-cov
bin	llvm-c-test
bin	llvm-cvtres
bin	llvm-cxxdump
bin,man	llvm-cxxfilt
bin,man	llvm-cxxmap
bin	llvm-debuginfod-find
bin	llvm-debuginfod
bin,man	llvm-diff
bin,man	llvm-dis
bin	llvm-dlltool
bin,man	llvm-dwarfdump
bin,man	llvm-dwarfutil
bin	llvm-dwp
bin,man	llvm-exegesis
bin,man	llvm-extract
bin	llvm-gsymutil
bin	llvm-ifs
bin,man	llvm-install-name-tool
bin	llvm-jitlink
bin,man	llvm-lib
bin,man	llvm-libtool-darwin
bin,man	llvm-link
bin,man	llvm-lipo
bin	llvm-lto
bin	llvm-lto2
bin,man	llvm-mc
bin,man	llvm-mca
bin	llvm-ml
bin	llvm-modextract
bin	llvm-mt
bin,man	llvm-nm
bin,man	llvm-objcopy
bin,man	llvm-objdump
bin,man	llvm-opt-report
bin,man	llvm-otool
bin,man	llvm-pdbutil
bin,man	llvm-profdata
bin,man	llvm-profgen
bin,man	llvm-ranlib
bin	llvm-rc
bin,man	llvm-readelf
bin,man	llvm-readobj
bin,man	llvm-reduce
bin	llvm-readtapi
bin	llvm-rtdyld
bin,man	llvm-size
bin	llvm-sim
bin,man	llvm-tli-checker
bin	llvm-windres
bin	llvm-split
bin,man	llvm-stress
bin,man	llvm-strings
bin,man	llvm-strip
bin,man	llvm-symbolizer
bin,man	llvm-tblgen
bin,man	llvm-debuginfo-analyzer
bin,man	llvm-remarkutil
bin	llvm-undname
bin	llvm-xray
bin	modularize
bin,man	opt
bin	pp-trace
bin	run-clang-tidy
bin	sancov
bin	sanstats
bin	verify-uselistorder
bin	tblgen-to-irdl
bin	reduce-chunk-list

man	FileCheck
man	extraclangtools
man	lit
man	llvm-ifs
man	llvm-locstats
man	lldb-tblgen
man	tblgen
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name <<EOExecutableList
bin,man	clang
bin	clang++
bin	clang-cl
bin	clang-cpp
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name-analyzer <<EOExecutableList
bin	analyze-build
bin	intercept-build
bin,man	scan-build
bin	scan-build-py
bin	scan-view
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name-tools <<EOExecutableList
bin	amdgpu-arch
bin	nvptx-arch
bin	c-index-test
bin	clang-apply-replacements
bin	clang-change-namespace
bin	clang-check
bin	clang-doc
bin	clang-extdef-mapping
bin	clang-format
bin	clang-include-cleaner
bin	clang-include-fixer
bin	clang-installapi
bin	clang-linker-wrapper
bin	clang-move
bin	clang-nvlink-wrapper
bin	clang-offload-bundler
bin	clang-offload-packager
bin	clang-pseudo
bin	clang-query
bin	clang-refactor
bin	clang-rename
bin	clang-reorder-fields
bin	clang-repl
bin	clang-scan-deps
bin,man	clang-tblgen
bin	clang-tidy
bin	find-all-symbols
bin	git-clang-format
bin	hmaptool
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%mlir_name-tools <<EOExecutableList
bin	mlir-cpu-runner
bin	mlir-linalg-ods-yaml-gen
bin	mlir-lsp-server
bin	mlir-opt
bin	mlir-pdll
bin	mlir-pdll-lsp-server
bin	mlir-reduce
bin,man	mlir-tblgen
bin	mlir-transform-opt
bin	mlir-translate
bin	tblgen-lsp-server
bin	mlir-cat
bin	mlir-minimal-opt
bin	mlir-minimal-opt-canonicalize
bin	mlir-query
EOExecutableList

emit_filelist >%_tmppath/dyn-files-lib%polly_name-devel <<EOExecutableList
man	polly
EOExecutableList

emit_filelist >%_tmppath/dyn-files-lib%omp_name-devel <<EOExecutableList
%ifarch %libomptarget_arches
bin	llvm-omp-device-info
bin	llvm-omp-kernel-replay
%endif
EOExecutableList

# Comment out file validation for CMake targets placed
# in a different package.
sed -i '
/APPEND _cmake_import_check_targets \(mlir-\|MLIR\)/ {s|^|#|}
/APPEND _cmake_import_check_targets \(tblgen-lsp-server\)/ {s|^|#|}
/APPEND _cmake_import_check_targets \(Polly\)/ {s|^|#|}
/APPEND _cmake_import_check_targets \(llvm-omp-device-info\|llvm-omp-kernel-replay\|omptarget\)/ {s|^|#|}
/APPEND _cmake_import_check_targets \(omp\)/ {s|^|#|}
/APPEND _cmake_import_check_targets \(LibcTableGenUtil\)/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/llvm/LLVMExports-*.cmake

# Comment out file validation for CMake targets producing executables
# that may be placed in a different package.
sed -i '
/APPEND _cmake_import_check_files_for_.* .*[/]bin[/].*/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/clang/ClangTargets-*.cmake

# Shared cmake files for llvm projects
mkdir -p %buildroot%llvm_datadir/cmake
cp -ar cmake/Modules %buildroot%llvm_datadir/cmake/

%check
%if_enabled tests
LD_LIBRARY_PATH=%buildroot%llvm_libdir:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
ninja -C %builddir check-all || :
%endif

# Do not generate dependencies for clang-{format,rename} plugins.
%add_findreq_skiplist %llvm_datadir/clang/*

%files filesystem
%dir %llvm_prefix
%dir %llvm_bindir
%dir %llvm_libdir
%dir %llvm_libdir/cmake
%dir %llvm_includedir
%dir %llvm_libexecdir
%if "%_libsuff" == "64"
%dir %llvm_prefix/lib
%endif
%dir %llvm_datadir
%dir %llvm_datadir/cmake
%dir %llvm_datadir/clang
%dir %llvm_datadir/man
%dir %llvm_man1dir
%dir %llvm_docdir
%dir %llvm_docdir/LLVM
%if_with lldb_python
%dir %llvm_python3_libdir
%dir %llvm_python3_sitelibdir
%endif

%files -f %_tmppath/dyn-files-%name
%doc llvm/CREDITS.TXT llvm/LICENSE.TXT llvm/README.txt

%files libs
%llvm_libdir/libLLVM-%v_major.so
%_libdir/libLLVM-%v_major.so
%llvm_libdir/libLLVM.so.%v_majmin
%_libdir/libLLVM.so.%v_majmin
%llvm_libdir/libLTO.so.%v_majmin
%_libdir/libLTO.so.%v_majmin
%llvm_libdir/libRemarks.so.%v_majmin
%_libdir/libRemarks.so.%v_majmin

%files tools
%llvm_datadir/opt-viewer

%files devel
%llvm_bindir/llvm-config
%_bindir/llvm-config-%v_major
%llvm_man1dir/llvm-config.1.*
%_man1dir/llvm-config-%v_major.1.*
%llvm_includedir/llvm
%llvm_includedir/llvm-c
%llvm_libdir/libLLVM.so
%llvm_libdir/libLTO.so
%llvm_libdir/libRemarks.so
#%%llvm_libdir/LLVMHello.so
%llvm_libdir/BugpointPasses.so
%llvm_libdir/cmake/llvm
%llvm_libdir/libLLVM*.a

%files gold
%llvm_libdir/LLVMgold.so

%files -n %clang_name -f %_tmppath/dyn-files-%clang_name
%doc %builddir/clang-docs/*
%llvm_bindir/clang-%v_major
%llvm_datadir/clang/bash-autocomplete.sh
%_datadir/bash-completion/completions/clang*

%files -n libclang%clang_sover
%llvm_libdir/libclang.so.%{clang_sover}*
%_libdir/libclang.so.%{clang_sover}*

%files -n libclang-cpp%clang_cpp_sover
%llvm_libdir/libclang-cpp*.so.%{clang_cpp_sover}*
%_libdir/libclang-cpp*.so.%{clang_cpp_sover}*

%files -n %clang_name-libs
# This is a compat package.

%files -n %clang_name-support -f %_tmppath/dyn-files-clang-support
%llvm_libdir/clang
# clang-tools
%ifarch %hwasan_symbolize_arches
%exclude %llvm_libdir/clang/%v_major/bin/hwasan_symbolize
%endif
%exclude %llvm_libdir/clang/%v_major/include/omp.h
%ifnarch %arm
%exclude %llvm_libdir/clang/%v_major/include/omp-tools.h
%exclude %llvm_libdir/clang/%v_major/include/ompt.h
%exclude %llvm_libdir/clang/%v_major/include/ompt-multiplex.h
%endif
%ifarch %libc_arches
%exclude %llvm_libdir/clang/%v_major/include/llvm_libc_wrappers/llvm-libc-decls
%exclude %llvm_libdir/clang/%v_major/lib/amdgcn-amd-amdhsa
%exclude %llvm_libdir/clang/%v_major/lib/nvptx64-nvidia-cuda
%exclude %llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libcgpu-*.a
%exclude %llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libmgpu-*.a
%endif
%ifarch %libomptarget_arches
%exclude %llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget.devicertl.a
%exclude %llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget-amdgpu-*.bc
%exclude %llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget-nvptx-*.bc
%exclude %llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget.so*
%endif

%files -n %clang_name-support-shared-runtimes -f %_tmppath/libclang-support-shared-runtimes

%files -n %clang_name-devel
%llvm_includedir/clang
%llvm_includedir/clang-c
%llvm_includedir/clang-tidy
%llvm_libdir/libclang*.so
%llvm_libdir/cmake/clang

%files -n %clang_name-analyzer -f %_tmppath/dyn-files-%clang_name-analyzer
%llvm_libexecdir/c++-analyzer
%llvm_libexecdir/ccc-analyzer
%llvm_datadir/scan-build
%llvm_datadir/scan-view
%llvm_prefix/lib/libear
%llvm_prefix/lib/libscanbuild
%llvm_libexecdir/analyze-*
%llvm_libexecdir/intercept-*

%files -n %clang_name-tools -f %_tmppath/dyn-files-%clang_name-tools
%llvm_datadir/clang
%exclude %llvm_datadir/clang/bash-autocomplete.sh
%ifarch %hwasan_symbolize_arches
%llvm_libdir/clang/%v_major/bin/hwasan_symbolize
%endif

%files -n %clangd_name
%llvm_bindir/clangd
%_bindir/clangd-%v_major

%if_with lld
%files -n %lld_name
%llvm_bindir/lld
%_bindir/lld-%v_major
%llvm_bindir/lld-link
%_bindir/lld-link-%v_major
%llvm_bindir/ld*.lld
%_bindir/ld*.lld-%v_major
%llvm_bindir/wasm-ld
%_bindir/wasm-ld-%v_major

%files -n %lld_name-devel
%dir %llvm_includedir/lld
%llvm_includedir/lld/*
# see Patch18: lld-compact-unwind-encoding.h.patch
%llvm_includedir/mach-o
%llvm_libdir/cmake/lld
%llvm_libdir/liblld*.a
%endif

%if_with lldb
%files -n %lldb_name
%llvm_bindir/lldb
%_bindir/lldb-%v_major
%llvm_bindir/lldb-argdumper
%_bindir/lldb-argdumper-%v_major
%llvm_bindir/lldb-instr
%_bindir/lldb-instr-%v_major
%llvm_bindir/lldb-server
%_bindir/lldb-server-%v_major
%llvm_man1dir/lldb.1*
%_man1dir/lldb-%v_major.1*
%llvm_man1dir/lldb-server.1*
%_man1dir/lldb-server-%v_major.1*
%llvm_bindir/lldb-dap
%_bindir/lldb-dap-%v_major

%files -n lib%lldb_name
%llvm_libdir/liblldb*.so.*
%_libdir/liblldb*.so.*

%files -n lib%lldb_name-devel
%llvm_includedir/lldb
%llvm_libdir/liblldb*.so

%if_with lldb_python
%files -n python3-module-%lldb_name
%llvm_python3_sitelibdir/lldb
%endif # lldb_python
%endif

%files -n lib%mlir_name
%llvm_libdir/libMLIR.so.*
%_libdir/libMLIR.so.*
%llvm_libdir/libmlir_async_runtime.so.*
%_libdir/libmlir_async_runtime.so.*
%llvm_libdir/libmlir_c_runner_utils.so.*
%_libdir/libmlir_c_runner_utils.so.*
%llvm_libdir/libmlir_runner_utils.so.*
%llvm_libdir/libmlir_float16_utils.so.*
%_libdir/libmlir_runner_utils.so.*
%_libdir/libmlir_float16_utils.so.*
%llvm_libdir/libmlir_arm_runner_utils.so.*
%llvm_libdir/libmlir_arm_sme_abi_stubs.so.*
%_libdir/libmlir_arm_runner_utils.so.*
%_libdir/libmlir_arm_sme_abi_stubs.so.*
%llvm_libdir/libMLIRExecutionEngineShared.so.*
%_libdir/libMLIRExecutionEngineShared.so.*

%files -n lib%mlir_name-devel
%llvm_includedir/mlir
%llvm_includedir/mlir-c
%llvm_libdir/libMLIR*.a
%llvm_libdir/libMLIR.so
%llvm_libdir/libMLIRExecutionEngineShared.so
%llvm_libdir/libmlir_async_runtime.so
%llvm_libdir/libmlir_c_runner_utils.so
%llvm_libdir/libmlir_runner_utils.so
%llvm_libdir/libmlir_float16_utils.so
%llvm_libdir/libmlir_arm_runner_utils.so
%llvm_libdir/libmlir_arm_sme_abi_stubs.so
%llvm_libdir/cmake/mlir

%files -n %mlir_name-tools -f %_tmppath/dyn-files-%mlir_name-tools

%files polly
%llvm_libdir/LLVMPolly.so

%files -n lib%polly_name-devel -f %_tmppath/dyn-files-lib%polly_name-devel
%llvm_includedir/polly
%llvm_libdir/cmake/polly
%llvm_libdir/libPolly*.a

%files doc
%doc %llvm_docdir/LLVM/llvm

%files -n %clang_name-doc
%doc %llvm_docdir/LLVM/clang
%doc %llvm_docdir/LLVM/clang-tools

%if_with lld
%files -n %lld_name-doc
%doc %llvm_docdir/lld
%endif

%if_with lldb
%files -n %lldb_name-doc
%doc %llvm_docdir/LLVM/lldb
%endif

%files -n lib%polly_name-doc
%doc %llvm_docdir/LLVM/polly

%files -n lib%omp_name
%llvm_libdir/libomp.so.%omp_vmajor
%_libdir/libomp.so.%omp_vmajor
%ifarch %libomptarget_arches
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget.so.%v_majmin
%_libdir/libomptarget.so.%v_majmin
%endif

%files -n lib%omp_name-devel -f %_tmppath/dyn-files-lib%omp_name-devel
%llvm_libdir/clang/%v_major/include/omp.h
%llvm_libdir/libomp.so
%llvm_libdir/libompd.so
%llvm_libdir/libarcher.so
%llvm_libdir/clang/%v_major/include/omp-tools.h
%llvm_libdir/clang/%v_major/include/ompt.h
%llvm_libdir/clang/%v_major/include/ompt-multiplex.h
%llvm_libdir/cmake/openmp
%_libdir/libarcher.so
%ifarch %libomptarget_arches
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget.devicertl.a
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget-amdgpu-*.bc
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget-nvptx-*.bc
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libomptarget.so
%endif
%ifarch %libc_arches
%llvm_includedir/amdgcn-amd-amdhsa
%llvm_includedir/nvptx64-nvidia-cuda
%llvm_includedir/llvmlibc_rpc_opcodes.h
%llvm_includedir/llvmlibc_rpc_server.h
%llvm_libdir/clang/%v_major/include/llvm_libc_wrappers/llvm-libc-decls
%llvm_libdir/clang/%v_major/lib/amdgcn-amd-amdhsa
%llvm_libdir/clang/%v_major/lib/nvptx64-nvidia-cuda
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libcgpu-*.a
%llvm_libdir/clang/%v_major/lib/%libomp_arch-unknown-linux-gnu/libmgpu-*.a
%llvm_libdir/libLibcTableGenUtil.a
%llvm_libdir/libllvmlibc_rpc_server.a
%endif

%files cmake-common-modules
%dir %llvm_datadir/cmake/Modules
%llvm_datadir/cmake/Modules/*

%changelog
* Wed Oct 02 2024 L.A. Kostis <lakostis@altlinux.ru> 19.1.1-alt0.1
- Update to 19.1.1.
- loongarch64: remove merged patches.
- ppc64le: don't build GPU libc (unsupported arch).
- GPU libc: exclude it from LLVMExports.

* Mon Sep 23 2024 L.A. Kostis <lakostis@altlinux.ru> 19.1.0-alt0.2
- Enable GPU libc for omptarget.
- OpenMP: relocate some libs to satisfy clang requires.

* Wed Sep 18 2024 L.A. Kostis <lakostis@altlinux.ru> 19.1.0-alt0.1
- Update to 19.1.0.
- Re-apply all patches, drop merged ones.
- Don't apply -alt MCJIT riscv64/loongarch64 patches yet.
- llvm/AMDGPU: apply optimisation fix for s/udiv64 (issue 100383).

* Tue Jun 25 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.8-alt0.1
- Update to 18.1.8.
- Pass -ffat-lto-objects for lto=thin.

* Thu May 23 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.6-alt0.1
- Update to 18.1.6.

* Mon May 06 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.5-alt0.1
- Update to 18.1.5.

* Mon Apr 22 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.4-alt0.1
- Update to 18.1.4.

* Thu Apr 18 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 18.1.3-alt0.3
- Fixed FTBFS on LoongArch: do package libomptarget (partially
  supported as of LLVM 18.1).
- Re-enabled MCJIT patches for riscv64 and LoongArch (a subset
  of relocations just enough for llvmpipe to work).

* Wed Apr 17 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.3-alt0.2
- lld: added /proc to requires.

* Sun Apr 14 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.3-alt0.1
- Update to 18.1.3.

* Thu Mar 28 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.2-alt0.2
- Make clang-doc package arch until graphviz issue will be
  resolved on %%ix86.
- lldb/BR: untangle sphinx/python3 deps.
- lldb: lldb_contrib->lldb_full.
- lldb: lldb-vscode->lldb-dap.
- mold: make build knob more visible.
- openmp/libompd: do not link libomp.
- cmake-modules: move to %%llvm_datadir.

* Mon Mar 25 2024 L.A. Kostis <lakostis@altlinux.ru> 18.1.2-alt0.1
- 18.1.2.
- Compile with mold on all supported 64-bit arches.
- Re-apply all patches from llvm17 which still needed.
- Disable lldb_contrib: (too many deps, will fix them later).
- Added patches from RH:
  + clang/unittests: fix ORC bug on ppc64le
  + clang-tools-extra: make test deps on LLVMHello optional
  + clang/cmake: don't install static libraries.
- libomp: added conflicts with previous/next versions.
- libomp: remove loongarch64 exclusion (offically supported now).
- BR: added graphviz (clang docs need dot app).
- cmake-common-modules: added conflicts with previous/next versions.
- .spec: optimize lldb BR.
- Disabled loognarch64/risc-v llvmpipe patches.

* Tue Mar 19 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 17.0.6-alt3
- compiler-rt: build with medium code model on LoongArch. Required for
  chromium and other non-trivial apps, as the default code model is too
  tight (maximal code offset is 128 MB)

* Thu Feb 08 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.6-alt2
- clang: fix wrong -print-runtime-dir on %%ix86.

* Sun Jan 21 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.6-alt1
- 17.0.6.
  BR: build lldb with lzma support.

* Tue Jan 09 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 17.0.3-alt6
- NMU: fixed FTBFS on LoongArch: libomptarget is not supported here (but
  surprisingly it's not completely disabled either).

* Mon Jan 08 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.3-alt5
- Exclude omp from LLVMExports.

* Mon Jan 01 2024 L.A. Kostis <lakostis@altlinux.ru> 17.0.3-alt4
- Build OpenMP target.
- Make separate package for cmake common modules.

* Sun Dec 10 2023 L.A. Kostis <lakostis@altlinux.ru> 17.0.3-alt3
- Applied fixes:
  + clang: fix CUDA libdevice search path.

* Fri Oct 27 2023 Ivan A. Melnikov <iv@altlinux.org> 17.0.3-alt2
- Enchance riscv64 and loongarch64 support:
  + correct dynamic linker path on riscv64;
  + add riscv64-alt-linux to clang-alt-triple.patch;
  + return to building with gcc on loongarch64;
  + implement minimal support of resolving relocations
    for riscv64 and loongarch64 in MCJIT (just enough
    for Mesa's llvmpipe to work);
  + do NOT restrict build concurrency on LoongArch (asheplyakov@)
- Extract %%clang_name-tidy-devel-static package
  to overcome rpmbuild payload size limit.

* Sat Oct 21 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.3-alt1
- 17.0.3.

* Fri Oct 06 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.2-alt3
- Apply new patch for compat with g++-13 -Werror:
  + clang-AST-Use-explicit-type-erasure.patch
- Restore the enforce-DWARF4 patch.

* Wed Oct 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 17.0.2-alt2
- spec: build lld on LoongArch (LoongArch targets are already supported).
- spec: build llvm with clang on LoongArch.

* Tue Oct 03 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.2-alt1
- 17.0.2.
- Add explicit dependency on clangX-support to clang and clangd.

* Tue Oct 03 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.2-alt0.1
- 17.0.2.
- This is an intermediate release to work around broken 17.0.1-alt4.

* Sat Sep 30 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.1-alt4
- Split libclang-cpp.so into its own package. (Closes: 44263)
- Split libclang.so into its own package, making clangX-libs a compat package
  which pulls both shared libraries in.

* Thu Sep 28 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.1-alt3
- clang: Restore the default disposition of -grecord-command-line.
- clang: Pass --build-id=sha1 to linkers by default. (Closes: 47780)
  Both of these changes are applied to clangs we build ALT packages with; if we
  ever decouple clang-for-packages from clang-for-users, upstream behaviour can
  be restored for the latter.

* Mon Sep 25 2023 Arseny Maslennikov <arseny@altlinux.org> 17.0.1-alt2
- Readjusted CMake file validation fixes.

* Tue Sep 19 2023 Nazarov Denis <nenderus@altlinux.org> 17.0.1-alt1
- 17.0.1

* Tue Sep 19 2023 Nazarov Denis <nenderus@altlinux.org> 17.0.0-alt1
- 17.0.0 final

* Fri Sep 15 2023 Nazarov Denis <nenderus@altlinux.org> 17.0.0-alt0.2.rc4
- Fix unowned directory on 64-bit arches
- Build tools package as noarch

* Sat Sep 09 2023 Nazarov Denis <nenderus@altlinux.org> 17.0.0-alt0.1.rc4
- 17.0.0 rc4

* Tue Sep 05 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 16.0.6-alt4
- Support LoongArch architecture (lp64d ABI):
  + clang-alt-triple-loongarch64.patch: added loongarch64-alt-linux triple
  + spec: do not build/package lld on LoongArch (LoongArch targets are
    not supported yet)
  + spec: do not build lldb on LoongArch (not supported yet)
  + spec: build with GCC/binutils on LoongArch (since lld does not support
    LoongArch targets yet)

* Mon Aug 07 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.6-alt3
- Added patches:
  + lld: added python 3.12+ compatibility patch.
  + clang: switch from recommonmark to myst_parser.

* Thu Jun 29 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.6-alt2
- x86_64: link with lld again (as mold needs non-standard ldflags which pollute
  llvm-config output).
- clang: update alt-triple patch (which should fix ROCM path detection in
  AMDGPU driver).

* Wed Jun 21 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.6-alt1
- 16.0.6.
- clang: fix rocm search path patch.
- use versioned sources to fix debuginfo path intersections.

* Tue Jun 20 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.5-alt3
- Sync changes from llvm15.0:
  + clang: extend rocm device libs lookup path.
  + libpolly-doc: Marked as noarch (by arseny@).
  + Dropped tblgen-lsp-server from LLVMExports target check. That program is
    located in a different subproject (by arseny@).

* Sat Jun 10 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.5-alt2
- x86_64: use mold instead of lld.
- aarch64: compile w/ gcc again (still 5hrs to compile w/ clang).
- disable LTO if compiling w/ gcc (as upstream issue 57740).

* Thu Jun 08 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.5-alt1
- 16.0.5.
- cmake: use install rpath instead of build rpath to make
  verify-elf happy.
- clang: use DWARF4 by default (patch from RH).
- spec: try to compile ppc64/aarch64 w/ clang again.

* Tue May 30 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.4-alt0.5
- trying to fix armh build.

* Mon May 29 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.4-alt0.4
- armh: build with clang without LLD/LTO.

* Mon May 29 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.4-alt0.3
- scanbuild: fix noarch install.
- aarch64: use gcc (compilation with clang takes 5hrs!).

* Sun May 28 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.4-alt0.2
- .spec: fix %%ix86 build.

* Fri May 26 2023 L.A. Kostis <lakostis@altlinux.ru> 16.0.4-alt0.1
- 16.0.4.
- Rediffed -alt patches.
- .spec: update for new tools/directories.

* Tue Jan 03 2023 L.A. Kostis <lakostis@altlinux.ru> 15.0.6-alt1.1
- llvm/AMDGPU: Added __builtin_amdgcn_s_sendmsg_rtn (D132140).

* Tue Jan 03 2023 L.A. Kostis <lakostis@altlinux.ru> 15.0.6-alt1
- NMU:
  + Updated to 15.0.6.

* Mon Sep 12 2022 Arseny Maslennikov <arseny@altlinux.org> 15.0.0-alt1
- 15.0.0.

* Tue Jun 28 2022 Arseny Maslennikov <arseny@altlinux.org> 14.0.6-alt1
- 14.0.6.
- Built LLDB without Lua support.

* Mon Apr 25 2022 Arseny Maslennikov <arseny@altlinux.org> 13.0.1-alt3
- Restored doc generation, which was disabled in -alt2.
- Built LLDB with libedit and SWIG support.

* Fri Apr 15 2022 Arseny Maslennikov <arseny@altlinux.org> 13.0.1-alt2
- Dropped certain targets from import checks in CMake configs.
  This will fix bug 39685, or, at least, dramatically reduce its impact.
- Built without gcc-LTO, since it miscompiles the LLVM optimizer.
- Temporarily disabled doc generation to urgently push the fix above.

* Sat Feb 19 2022 Arseny Maslennikov <arseny@altlinux.org> 13.0.1-alt1
- 13.0.1.
- Merge llvm-devel-static with llvm-devel.
- Merge clang-devel-static with clang-devel.
- New LLVM subprojects: mlir, polly.

* Tue Sep 21 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.1-alt3
- Included git-clang-format in clang-tools (closes: bug 40912).
  Split off LLVMgold.so to its own package.
  Added a requirement on llvmN-gold from llvmN-libs.

* Sun Sep 05 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.1-alt2
- Marked the package as built by ALT Linux Team (-DPACKAGE_VENDOR) so it's
  easier to distinguish from custom builds.
- If compiled with gcc, we now pass -ffat-lto-objects to it.
- Enabled -grecord-command-line by default (closes: bug 40628).
  Code generation is unaffected.

* Tue Aug 10 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.1-alt1
- 12.0.0 -> 12.0.1. (Closes: bug 40358)

* Tue May 11 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.0-alt2
- Built with python2 in BTE to appease python2's findprov.

* Fri Apr 16 2021 Arseny Maslennikov <arseny@altlinux.org> 12.0.0-alt1
- 12.0.0.

* Fri Jan 08 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt1
- 11.0.0 -> 11.0.1.
- New LLVM subproject: lldb.

* Fri Dec 11 2020 Arseny Maslennikov <arseny@altlinux.org> 11.0.0-alt2
- Installed to /usr/lib/llvm-11.0 to ensure peaceful co-existence with other
  LLVM versions.
  Numbered shared libraries in %llvm_prefix/%%_lib are symlinked to %%_libdir
  to properly generate library dependencies.
- Moved clang-format and other clang-based tools to clang11.0-tools.
- New LLVM subproject: clang-tools-extra.
  + 2 new packages: clang11.0-tools, clangd11.0
- Enabled all LLVM targets.
- Moved C/C++ compiler support away from clang-libs to clang-libs-support.
- Moved Clang .so runtimes (scudo and sanitizers) with available static variants
  to clang-libs-support-shared-runtimes to comply with sisyphus-check-static.

* Tue Oct 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 11.0.0-alt1
- 11.0.0
- Built with gcc.

* Wed Aug 12 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 10.0.1-alt2
- Applied upstream patch which should fix ppc64le-specific issue.

* Tue Aug 11 2020 Valery Inozemtsev <shrek@altlinux.ru> 10.0.1-alt1
- 10.0.1

* Tue May  5 2020 Nikita Ermakov <arei@altlinux.org> 10.0.0-alt2
- add riscv64 support

* Wed Mar 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 10.0.0-alt1
- 10.0.0

* Fri Mar 20 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.0.1-alt3
- use 'Release' build
- clang: fixed link with option -fsanitize=address (closes: #38250)

* Thu Feb 13 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.0.1-alt2
- build with clang

* Mon Feb 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 9.0.1-alt1
- 9.0.1

* Wed May 22 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 7.0.1-alt4.rel
- Added mipsel-alt-linux and ppc64le-alt-linux triples support.
- lld:
  + mipsel: allowed textrels by default;
  + ppc64le: backported upstream fixes for ThinLTO support and relocation
  checks.

* Mon Jan 21 2019 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt3.rel
- Added patches from stable:
  + llvm-nm: Add --portability as alias for --format=posix.
  + llvm-objdump: Implement -z/--disassemble-zeroes.
  + AMDGPU: test for uniformity of branch instruction, not its
            condition.

* Fri Jan 04 2019 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt2.rel
- Rebuild by clang7.0.

* Fri Dec 21 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt1.rel.1
- Bootstrap w/ gcc.

* Mon Dec 17 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.1-alt1.rel
- Updated to 7.0.1.
- Split static library exports in cmake (patch from RH).
- Build with clang.

* Sat Sep 22 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt1.rel
- First try of 7.0.0.

* Wed Sep 05 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.0.0-alt0.11.rel
- NMU: updated build with clang for aarch64.

* Tue Jun 19 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.10.rel
- llvm-ar: backported support of dashed options (chromium build
  depends on it).

* Tue Jun 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.0.0-alt0.9.rel
- aarch64: rebuilt with clang.

* Tue Jun 12 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 6.0.0-alt0.8.rel
- lld: backported upstream commit implementing --{push,pop}-state support.
- clang: changed default dynamic linker path for aarch64 architecture.
- aarch64: temporarily rebuilt with gcc to fix build from source.
- clang-alt-triple.patch: added mipsel and mips64el triplets.

* Wed Mar 28 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.3.r328699
- Rebased to llvm master SVN r328699.

* Tue Mar 20 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.7.rel
- Reduce debuginfo for x86_64.
- Use 'Release' build on x86_64.
- Fix provides/obsoletes.
- Move clang libs to separate pkg (to ease future migrations).

* Sun Mar 18 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.2.r327779
- Rebased to llvm master SVN r327779.
- Build w/ clang and lld.
- .spec: sync changes with llvm6.0.

* Thu Mar 15 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.6.rel
- Bootstrap with clang, lld and ThinLTO.
- .spec: sync with RH
  + 0001-DebugInfo-Discard-invalid-DBG_VALUE-instructions-in-.patch
  + 0001-Fixup-for-rL326769-RegState-Debug-is-being-truncated.patch
  + RH-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
- .spec: move gold plugin to -devel (tnx to legion@)
- Build changes:
  + Reduce memory consumption on x86:
    + Reduce amount of debuginfo (use -g1)
    + Use Release as build target.
  + Use compiler-rt (instead of libgcc).
  + Use 8 build jobs.

* Mon Mar 12 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.5.rel
- Test build using clang and lld.
- Increase build jobs number to 16 (thanks to lld/thinLTO).

* Sun Mar 11 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.4.rel
- Prepare for LLD/clang build bootstrap.

* Sun Mar 11 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.3.rel
- Added LLD build.

* Sat Mar 10 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.2.rel
- Added flag to build with clang (should reduce memory usage for LTO).
- Reduce build jobs (workaround to reduce memory consumption).

* Fri Mar 09 2018 L.A. Kostis <lakostis@altlinux.ru> 6.0.0-alt0.1.rel
- Updated to 6.0.0 release.
- Build changes:
  + use LTO by default.
  + enabled gold linker.
  + use ninja build.

* Tue Feb 27 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.1.r326101
- Rebased to llvm master SVN r326101.

* Thu Feb 15 2018 L.A. Kostis <lakostis@altlinux.ru> 7.0.0-alt0.1.r325294
- Rebased to llvm master SVN r325294.
- Use host as build target (tnx to glebfm@).

* Sun Feb 04 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.0.1-alt1.3.rel
- Replaced X86 with native in the list of targets.
- Added provides and obsoletes to replace old llvm packages and its
  subpackages.

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 4.0.1-alt1.2.rel
- NMU: changed CMake Modules install path

* Thu Sep 14 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.1-alt1.1.rel
- remove conflicts: llvm from -libs pkg (closes #33879).

* Sun Sep 10 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.0.1-alt1.rel
- Updated 4.0.0 release and build configuration:
  + Enabled AVR experimental target.

* Thu Sep 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt2.rel
- Installed example llvm plugins required by cmake modules.

* Sun Mar 19 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt1.rel
- Define cmake modules dir correctly (closes #33250).

* Mon Mar 13 2017 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.9.rel
- Updated 4.0.0 release.

* Thu Dec 29 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.6.r290127
- Enabled gold plugin.

* Wed Dec 28 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.5.r290127
- Renamed clang to clang4.0 (to coexist with 3.x clang).

* Sun Dec 25 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.4.r290127
- repackage clang-analyzer, now with proper dirs.

* Thu Dec 22 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.3.r290127
- llvm: Fix segfault in libLLVM due missing /proc/cpuinfo.
- .spec: fix libs intersections between llvm and clang.
- .spec: remove unsupported stuff from clang-analyzer.

* Wed Dec 21 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.2.r290127
- Update build configuration:
  + Enabled BPF target.
  + Enabled optimisation.
  + Disabled unconditionally enabled tests.

* Mon Dec 19 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r290127
- Updated LLVM to SVN r290127.
- Enabled clang (SVN r290130).

* Tue Nov 08 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r286177
- Updated to SVN r286177.

* Fri Sep 30 2016 L.A. Kostis <lakostis@altlinux.ru> 4.0.0-alt0.1.r282877
- Updated to SVN r282877.

* Fri Aug 05 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r277804
- Updated to SVN r277804.

* Sat Jun 25 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r273782
- Updated to SVN r273782.

* Wed Jun 15 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r272815
- Updated to SVN r272815.
- Enabled X86 target (for llvmpipe).

* Sun Jun 12 2016 L.A. Kostis <lakostis@altlinux.ru> 3.9.0-alt0.1.r272517
- build as separate lib for Mesa-dev.
