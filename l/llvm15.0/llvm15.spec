%define _unpackaged_files_terminate_build 1

%filter_from_requires /python[0-9.]\+(Reporter)/d
%filter_from_requires /python[0-9.]\+(optpmap)/d
%filter_from_requires /python[0-9.]\+(libscanbuild[.].*)/d
# Self-provided by python3(lldb14.0) in a custom path.
%filter_from_requires /python[0-9.]\+(lldb)/d

%global v_major 15
%global v_majmin %v_major.0
%global v_full %v_majmin.6
%global rcsuffix %nil
%global llvm_name llvm%v_majmin
%global clang_name clang%v_majmin
%global clangd_name clangd%v_majmin
%global lld_name lld%v_majmin
%global lldb_name lldb%v_majmin
%global mlir_name mlir%v_majmin
%global polly_name polly%v_majmin

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
%global optflags_lto %nil

%define hwasan_symbolize_arches x86_64 aarch64
%ifarch riscv64
%def_without lldb
%else
%def_with lldb
%endif

%def_disable tests
%ifarch x86_64 aarch64
%def_with clang
%else
%def_without clang
%endif
%if_with lldb
%def_with lldb_contrib
%def_with lldb_python
%else
%def_without lldb_contrib
%def_without lldb_python
%endif

%define tarversion %v_full%rcsuffix
%if "%rcsuffix" == ""
%define mversion %v_full
%else
%define mversion %v_full%{?rcsuffix:-%rcsuffix}
%endif

Name: %llvm_name
Version: %v_full
Release: alt1.1
Summary: The LLVM Compiler Infrastructure

Group: Development/C
License: Apache-2.0 with LLVM-exception
Url: http://llvm.org
# Source-URL: https://github.com/llvm/llvm-project/releases/download/llvmorg-%mversion/llvm-project-%tarversion.src.tar.xz
Source: llvm-project.tar
Patch:  clang-alt-i586-fallback.patch
Patch1: clang-alt-triple.patch
Patch2: 0001-alt-llvm-config-Ignore-wrappers-when-looking-for-current.patch
Patch3: llvm-alt-fix-linking.patch
Patch4: llvm-alt-triple.patch
Patch5: compiler-rt-alt-i586-arch.patch
Patch6: clang-12-alt-mips-use-fpxx-by-default.patch
Patch7: clang-alt-aarch64-dynamic-linker-path.patch
Patch8: clang-tools-extra-alt-gcc-0001-clangd-satisfy-ALT-gcc-s-Werror-return-type.patch
Patch10: llvm-10-alt-python3.patch
# TODO: upstream this
# Patch11: hwasan_symbolize-python3.patch
Patch12: llvm-12-alt-mips-pcrel-personality.patch
Patch13: llvm-12-debian-mips-force-nomadd4.patch
Patch14: llvm-10-alt-riscv64-config-guess.patch
Patch17: llvm-cmake-pass-ffat-lto-objects-if-using-the-GNU-toolcha.patch
Patch18: lld-compact-unwind-encoding.h.patch
# ROCm needs this
Patch19: llvm-D132140.patch
Patch101: clang-ALT-bug-40628-grecord-command-line.patch

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
BuildRequires: python3-module-recommonmark zip zlib-devel binutils-devel ninja-build
%if_with lldb_contrib
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(ncursesw)
BuildRequires: pkgconfig(libxml-2.0)
#BuildRequires: pkgconfig(lua)
BuildRequires: swig-devel
BuildRequires: python3-module-sphinx-automodapi
%if_with lldb_python
BuildRequires: python3-devel
%endif
%endif
%if_with clang
BuildRequires: %clang_default_name %llvm_default_name-devel %lld_default_name
%else
BuildRequires: gcc-c++
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

%package -n %clang_name-libs
Group: Development/C
Summary: clang shared libraries
%requires_filesystem
Requires: %clang_name-libs-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs
Shared libraries for the clang compiler.

%package -n %clang_name-libs-support
Group: Development/C
Summary: Support for Clang's shared libraries
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs-support
The Clang's shared libraries implement compilers for C and C++, and thus have
to bundle additional platform support headers and libraries for use within the
compilation product. This package contains the platform support.

%package -n %clang_name-libs-support-shared-runtimes
Group: Development/C
Summary: Shared runtimes for Clang's shared libraries
%requires_filesystem
Requires: %clang_name-libs-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-libs-support-shared-runtimes
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

%package -n %clang_name-devel-static
Summary: Static libraries for clang
Group: Development/C
%requires_filesystem
Requires: %clang_name-devel = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %clang_name-devel-static
This package contains static libraries for the Clang compiler.

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
BuildArch: noarch
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
MLIR is a novel approach to building reusable and extensible compiler infrastructure.
MLIR aims to address software fragmentation, improve compilation for
heterogeneous hardware, significantly reduce the cost of building domain
specific compilers, and aid in connecting existing compilers together.

%package -n lib%mlir_name-devel
Summary: Libraries and header files for MLIR
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n lib%mlir_name-devel
MLIR is a novel approach to building reusable and extensible compiler infrastructure.
MLIR aims to address software fragmentation, improve compilation for
heterogeneous hardware, significantly reduce the cost of building domain
specific compilers, and aid in connecting existing compilers together.

This package contains headers and other development files for lib%mlir_name.

%package -n %mlir_name-tools
Summary: Various mlir-based tools
Group: Development/C
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %mlir_name-tools
MLIR is a novel approach to building reusable and extensible compiler infrastructure.
MLIR aims to address software fragmentation, improve compilation for
heterogeneous hardware, significantly reduce the cost of building domain
specific compilers, and aid in connecting existing compilers together.

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

%prep
# %setup -n llvm-%tarversion.src -a1 -a2 -a3 -a4 -a5 -a6
# for pkg in clang lld lldb; do
   # mv $pkg-%tarversion.src tools/$pkg
# done
# mv clang-tools-extra-%tarversion.src tools/clang/tools/extra
# for pkg in compiler-rt; do
   # mv $pkg-%tarversion.src projects/$pkg
# done
%setup -n llvm-project
%patch -p1 -b .alt-i586-fallback
%patch1 -p1 -b .alt-triple
%patch2 -p1
sed -i 's)"%%llvm_bindir")"%llvm_bindir")' llvm/lib/Support/Unix/Path.inc
%patch3 -p1 -b .alt-fix-linking
%patch4 -p1 -b .alt-triple
%patch5 -p1 -b .alt-i586-arch
%patch6 -p1
%patch7 -p1 -b .alt-aarch64-dynamic-linker
%patch8 -p1
%patch10 -p1
#patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
#patch15 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1

%patch101 -p1

# LLVM 12 and onward deprecate Python 2:
# https://releases.llvm.org/12.0.0/docs/ReleaseNotes.html
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%build
PROJECTS="clang;clang-tools-extra;compiler-rt;lld;mlir;polly"
%if_with lldb
PROJECTS="$PROJECTS;lldb"
%endif
export NPROCS="%__nprocs"
if [ "$NPROCS" -gt 64 ]; then
	export NPROCS=64
fi
%define _cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=OFF
%define builddir %_cmake__builddir
%cmake -G Ninja -S llvm \
	-DPACKAGE_VENDOR="%vendor" \
%if_with clang
	-DLLVM_PARALLEL_LINK_JOBS=1 \
%else
	-DLLVM_PARALLEL_LINK_JOBS=4 \
%endif
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%llvm_prefix \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DLLVM_ENABLE_PROJECTS="$PROJECTS" \
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
	\
	%if_with clang
	-DLLVM_ENABLE_LTO=Thin \
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
	-DCMAKE_RANLIB:PATH=%_bindir/llvm-ranlib \
	-DCMAKE_AR:PATH=%_bindir/llvm-ar \
	-DCMAKE_NM:PATH=%_bindir/llvm-nm \
	-DLLVM_ENABLE_LLD:BOOL=ON \
	%else
	%ifarch mipsel
	-DLLVM_ENABLE_LTO=Off \
	%else
	-DLLVM_ENABLE_LTO=Off \
	%endif
	%ifnarch riscv64
	-DLLVM_USE_LINKER=gold \
	%endif
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	%endif
	\
	-DLLVM_LIBDIR_SUFFIX="%_libsuff" \
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
	\
	-DMLIR_INSTALL_AGGREGATE_OBJECTS=OFF \
	\
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
ninja -vvv -j $NPROCS -C %builddir

%install
sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' %builddir/build.ninja
sed -i '/^[[:space:]]*include.*tools\/lld\/docs\/cmake_install.cmake.*/d' %builddir/tools/lld/cmake_install.cmake
DESTDIR=%buildroot ninja -C %builddir install

# Prepare Clang documentation.
rm -rf %builddir/clang-docs
mkdir -p %builddir/clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln clang/$f %builddir/clang-docs/
done
rm -rf tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}

install -m 0755 %builddir/%_lib/LLVMHello.so %buildroot%llvm_libdir/
install -m 0755 %builddir/%_lib/BugpointPasses.so %buildroot%llvm_libdir/
mkdir -p %buildroot%llvm_docdir/lld

%ifarch %ix86
cd %buildroot%llvm_libdir/clang/%v_full/lib/*-*-*-*
ls *-i[3-9]86* | while read f; do ln -s $f $(echo $f | sed 's|i[3-9]86|i386|') ; done
cd -
%endif

# The following files are not used by LLVM builds for Linux.
rm -f %buildroot%llvm_bindir/argdumper
rm -f %buildroot%llvm_datadir/clang/clang-format-bbedit.applescript

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
sed < %_tmppath/libclang-support-shared-runtimes 's/^/%%exclude /' > %_tmppath/dyn-files-libclang-support
echo "Expelling likely redundant Clang shared runtimes:" && cat %_tmppath/dyn-files-libclang-support

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
bin	llvm-mc
bin,man	llvm-mca
bin	llvm-ml
bin	llvm-modextract
bin	llvm-mt
bin,man	llvm-nm
bin,man	llvm-objcopy
bin,man	llvm-objdump
bin	llvm-opt-report
bin,man	llvm-otool
bin,man	llvm-pdbutil
bin,man	llvm-profdata
bin,man	llvm-profgen
bin,man	llvm-ranlib
bin	llvm-rc
bin,man	llvm-readelf
bin,man	llvm-readobj
bin	llvm-reduce
bin,man	llvm-remark-size-diff
bin	llvm-rtdyld
bin,man	llvm-size
bin	llvm-sim
bin	llvm-tapi-diff
bin,man	llvm-tli-checker
bin	llvm-windres
bin	llvm-split
bin,man	llvm-stress
bin,man	llvm-strings
bin,man	llvm-strip
bin,man	llvm-symbolizer
bin,man	llvm-tblgen
bin	llvm-undname
bin	llvm-xray
bin	modularize
bin,man	opt
bin	pp-trace
bin	run-clang-tidy
bin	sancov
bin	sanstats
bin	split-file
bin	verify-uselistorder

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
bin	c-index-test
bin	clang-apply-replacements
bin	clang-change-namespace
bin	clang-check
bin	clang-doc
bin	clang-extdef-mapping
bin	clang-format
bin	clang-include-fixer
bin	clang-linker-wrapper
bin	clang-move
bin	clang-nvlink-wrapper
bin	clang-offload-bundler
bin	clang-offload-packager
bin	clang-offload-wrapper
bin	clang-pseudo
bin	clang-query
bin	clang-refactor
bin	clang-rename
bin	clang-reorder-fields
bin	clang-repl
bin	clang-scan-deps
man	clang-tblgen
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
bin	mlir-pdll-lsp-server
bin	mlir-reduce
bin,man	mlir-tblgen
bin	mlir-translate
bin	tblgen-lsp-server
EOExecutableList

emit_filelist >%_tmppath/dyn-files-lib%polly_name-devel <<EOExecutableList
man	polly
EOExecutableList

# Comment out file validation for CMake targets placed
# in a different package.
sed -i '
/APPEND _IMPORT_CHECK_TARGETS \(mlir-\|MLIR\)/ {s|^|#|}
/APPEND _IMPORT_CHECK_TARGETS \(Polly\)/ {s|^|#|}
/APPEND _IMPORT_CHECK_TARGETS \(llvm-omp-device-info\|omptarget\)/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/llvm/LLVMExports-*.cmake

# Comment out file validation for CMake targets producing executables
# that may be placed in a different package.
sed -i '
/APPEND _IMPORT_CHECK_FILES_FOR_.* .*[/]bin[/].*/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/clang/ClangTargets-*.cmake

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
%dir %llvm_datadir
%dir %llvm_datadir/clang
%dir %llvm_datadir/man
%dir %llvm_man1dir
%dir %llvm_docdir
%dir %llvm_docdir/LLVM
%dir %llvm_python3_libdir
%dir %llvm_python3_sitelibdir

%files -f %_tmppath/dyn-files-%name
%doc llvm/CREDITS.TXT llvm/LICENSE.TXT llvm/README.txt

%files libs
%llvm_libdir/libLLVM-*.so
%_libdir/libLLVM-*.so
%llvm_libdir/libLTO.so.*
%_libdir/libLTO.so.*
%llvm_libdir/libRemarks.so.*
%_libdir/libRemarks.so.*

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
%llvm_libdir/LLVMHello.so
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

%files -n %clang_name-libs
%llvm_libdir/libclang*.so.*
%_libdir/libclang*.so.*

%files -n %clang_name-libs-support -f %_tmppath/dyn-files-libclang-support
%llvm_libdir/clang
# clang-tools
%ifarch %hwasan_symbolize_arches
%exclude %llvm_libdir/clang/%v_full/bin/hwasan_symbolize
%endif

%files -n %clang_name-libs-support-shared-runtimes -f %_tmppath/libclang-support-shared-runtimes

%files -n %clang_name-devel
%llvm_includedir/clang
%llvm_includedir/clang-c
%llvm_includedir/clang-tidy
%llvm_libdir/libclang*.so
%llvm_libdir/cmake/clang
%llvm_libdir/libclang*.a
%llvm_libdir/libfindAllSymbols.a

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
%llvm_libdir/clang/%v_full/bin/hwasan_symbolize
%endif

%files -n %clangd_name
%llvm_bindir/clangd
%_bindir/clangd-%v_major

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

%if_with lldb
%files -n %lldb_name
%llvm_bindir/lldb
%_bindir/lldb-%v_major
%llvm_man1dir/lldb.1*
%_man1dir/lldb-%v_major.1*
%llvm_bindir/lldb-argdumper
%_bindir/lldb-argdumper-%v_major
%llvm_bindir/lldb-instr
%_bindir/lldb-instr-%v_major
%llvm_bindir/lldb-server
%_bindir/lldb-server-%v_major
%llvm_man1dir/lldb-server.1*
%_man1dir/lldb-server-%v_major.1*
%llvm_bindir/lldb-vscode
%_bindir/lldb-vscode-%v_major

%files -n lib%lldb_name
%llvm_libdir/liblldb*.so.*
%_libdir/liblldb*.so.*

%files -n lib%lldb_name-devel
%llvm_includedir/lldb
%llvm_libdir/liblldb*.so
# %_libdir/liblldb*.so

%files -n python3-module-%lldb_name
%llvm_python3_sitelibdir/lldb
# Hope this file will not be needed anywhere else.
%llvm_python3_sitelibdir/six.py
%endif

%files -n lib%mlir_name
%llvm_libdir/libMLIR.so.*
%_libdir/libMLIR.so.*
%llvm_libdir/libmlir_async_runtime.so.*
%_libdir/libmlir_async_runtime.so.*
%llvm_libdir/libmlir_c_runner_utils.so.*
%_libdir/libmlir_c_runner_utils.so.*
%llvm_libdir/libmlir_runner_utils.so.*
%_libdir/libmlir_runner_utils.so.*

%files -n lib%mlir_name-devel
%llvm_includedir/mlir
%llvm_includedir/mlir-c
%llvm_libdir/libMLIR*.a
%llvm_libdir/libMLIR.so
%llvm_libdir/libmlir_async_runtime.so
%llvm_libdir/libmlir_c_runner_utils.so
%llvm_libdir/libmlir_runner_utils.so
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

%files -n %lld_name-doc
%doc %llvm_docdir/lld

%if_with lldb
%files -n %lldb_name-doc
%doc %llvm_docdir/LLVM/lldb
%endif

%files -n lib%polly_name-doc
%doc %llvm_docdir/LLVM/polly

%changelog
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
