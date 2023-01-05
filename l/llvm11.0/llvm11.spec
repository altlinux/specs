%define _unpackaged_files_terminate_build 1

# Those are self-provided.
%filter_from_requires /python[0-9.]\+(Reporter)/d
%filter_from_requires /python[0-9.]\+(optpmap)/d
%filter_from_requires /python[0-9.]\+(optrecord)/d

%global v_major 11
%global v_majmin %v_major.0
%global v_full %v_majmin.1
%global rcsuffix %nil
%global llvm_name llvm%v_majmin
%global clang_name clang%v_majmin
%global clangd_name clangd%v_majmin
%global lld_name lld%v_majmin
%global lldb_name lldb%v_majmin

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

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%ifarch %ix86 %arm
%define optflags_debug -g0
#define __nprocs 1
%else
%define optflags_debug -g1
%endif

# LTO-related flags are set by CMake.
%global optflags_lto %nil

%define hwasan_symbolize_arches x86_64 aarch64
%define lldb_arches x86_64 %arm

%def_disable tests
%ifarch x86_64 aarch64
%def_without clang
%else
%def_without clang
%endif

%define tarversion %v_full%rcsuffix

Name: %llvm_name
Version: %v_full
Release: alt6
Summary: The LLVM Compiler Infrastructure

Group: Development/C
License: Apache-2.0 with LLVM-exception
Url: http://llvm.org
Source0: https://github.com/llvm/llvm-project/releases/download/llvmorg-%tarversion/llvm-%tarversion.src.tar.xz
Source1: https://github.com/llvm/llvm-project/releases/download/llvmorg-%tarversion/clang-%tarversion.src.tar.xz
Source2: https://github.com/llvm/llvm-project/releases/download/llvmorg-%tarversion/clang-tools-extra-%tarversion.src.tar.xz
Source3: https://github.com/llvm/llvm-project/releases/download/llvmorg-%tarversion/lld-%tarversion.src.tar.xz
Source4: https://github.com/llvm/llvm-project/releases/download/llvmorg-%tarversion/compiler-rt-%tarversion.src.tar.xz
Source5: https://github.com/llvm/llvm-project/releases/download/llvmorg-%tarversion/lldb-%tarversion.src.tar.xz
Patch:  clang-alt-i586-fallback.patch
Patch1: clang-11-alt-triple.patch
Patch2: 0001-alt-llvm-config-Ignore-wrappers-when-looking-for-current.patch
Patch3: llvm-alt-fix-linking.patch
Patch4: llvm-alt-triple.patch
Patch5: compiler-rt-9-alt-i586-arch.patch
Patch6: RH-0001-CMake-Split-static-library-exports-into-their-own-ex.patch
Patch7: clang-alt-aarch64-dynamic-linker-path.patch
Patch8: clang-tools-extra-alt-gcc-0001-clangd-satisfy-ALT-gcc-s-Werror-return-type.patch
Patch9: lld-11-alt-mipsel-permit-textrels-by-default.patch
Patch10: llvm-10-alt-python3.patch
Patch14: llvm-10-alt-riscv64-config-guess.patch
Patch15: llvm-cmake-resolve-symlinks-in-LLVMConfig.cmake.patch
Patch16: clang-cmake-resolve-symlinks-in-ClangConfig.cmake.patch
Patch17: llvm-cmake-pass-ffat-lto-objects-if-using-the-GNU-toolcha.patch
Patch20: compiler-rt-D102059-libsanitizer-Remove-cyclades-inclusion-in-sanitizer.patch
Patch21: llvm-utils-maint-missing-numeric_limits-decl.patch

%if_with clang
# https://bugs.altlinux.org/show_bug.cgi?id=34671
%set_verify_elf_method lint=skip
%endif

# ThinLTO requires /proc/cpuinfo to exist; so the same does llvm
BuildPreReq: /proc

# Obtain %%__python3 at prep stage.
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-llvm-common

BuildRequires(pre): cmake >= 3.4.3
BuildRequires: rpm-build >= 4.0.4-alt112 libncursesw-devel
BuildRequires: libstdc++-devel libffi-devel perl-Pod-Parser perl-devel
BuildRequires: python3-module-recommonmark zip zlib-devel binutils-devel ninja-build
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

%description filesystem
This package owns the installation prefix for LLVM. It is designed to be
pulled in by all non-empty LLVM packages.

%package devel
Group: Development/C
Summary: Libraries and header files for LLVM
%requires_filesystem
Requires: llvm-devel >= %_llvm_version
Requires: %name = %EVR

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM infrastructure.

%package devel-static
Summary: Static libraries for LLVM
Group: Development/C
%requires_filesystem
Requires: llvm-devel-static >= %_llvm_version
Requires: %name-devel = %EVR

%description devel-static
This package contains static libraries needed to develop new
native programs that use the LLVM infrastructure.

%package libs
Group: Development/C
Summary: LLVM shared libraries
%requires_filesystem

%description libs
This package contains shared libraries needed to develop new
native programs that use LLVM.

%package doc
Summary: Documentation for LLVM
Group: Documentation
BuildArch: noarch
%requires_filesystem

%description doc
Documentation for the LLVM compiler infrastructure.

%package -n %clang_name
Summary: A C language family frontend for LLVM
Group: Development/C
%requires_filesystem
# clang uses various parts of GNU crt bundled with gcc.
# Should they be packaged separately?
Requires: gcc
Requires: clang >= %_llvm_version

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

%description -n %clang_name-libs
Shared libraries for the clang compiler.

%package -n %clang_name-libs-support
Group: Development/C
Summary: Support for Clang's shared libraries
%requires_filesystem

%description -n %clang_name-libs-support
The Clang's shared libraries implement compilers for C and C++, and thus have
to bundle additional platform support headers and libraries for use within the
compilation product. This package contains the platform support.

%package -n %clang_name-libs-support-shared-runtimes
Group: Development/C
Summary: Shared runtimes for Clang's shared libraries
%requires_filesystem
Requires: %clang_name-libs-support = %EVR

%description -n %clang_name-libs-support-shared-runtimes
This package contains shared runtime libraries for Scudo and sanitizers.

%package -n %clang_name-devel
Summary: Header files for clang
Group: Development/C
%requires_filesystem
Requires: clang-devel >= %_llvm_version
Requires: %clang_name = %EVR

%description -n %clang_name-devel
This package contains header files for the Clang compiler.

%package -n %clang_name-devel-static
Summary: Static libraries for clang
Group: Development/C
%requires_filesystem
Requires: %clang_name-devel = %EVR

%description -n %clang_name-devel-static
This package contains static libraries for the Clang compiler.

%package -n %clang_name-analyzer
Summary: A source code analysis framework
Group: Development/C
BuildArch: noarch
%requires_filesystem
Requires: %clang_name = %EVR

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

%description -n %clang_name-tools
This package contains various code analysis and manipulation tools based on
libclang, including clang-format.

%package -n %clang_name-doc
Summary: Documentation for Clang
Group: Documentation
BuildArch: noarch
%requires_filesystem

%description -n %clang_name-doc
Documentation for the Clang compiler front-end.

%package -n %clangd_name
Summary: A clang-based language server
Group: Development/C
%requires_filesystem
Requires: clangd >= %_llvm_version

%description -n %clangd_name
This package contains clangd, a Clang-based language server for C and C++.

%package -n %lld_name
Summary: LLD - The LLVM Linker
Group: Development/C
%requires_filesystem
Requires: lld >= %_llvm_version

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

%description -n %lld_name-devel
This package contains header files for the LLD linker.

%package -n %lld_name-doc
Summary: Documentation for LLD
Group: Documentation
BuildArch: noarch
%requires_filesystem

%description -n %lld_name-doc
Documentation for the LLD linker.

%package -n %lldb_name
Summary: A next-level high-performance debugger
Group: Development/Debuggers
%requires_filesystem

%description -n %lldb_name
LLDB is a next generation, high-performance debugger. It is built as a set of
reusable components which highly leverage existing libraries in the larger LLVM
project, such as the Clang expression parser and the LLVM disassembler.

%package -n lib%lldb_name
Summary: Shared library for LLDB
Group: Development/Debuggers
%requires_filesystem

%description -n lib%lldb_name
This package contains the LLDB runtime library.

%package -n lib%lldb_name-devel
Summary: Development files for liblldb
Group: Development/Debuggers
%requires_filesystem

%description -n lib%lldb_name-devel
This package contains header files to build extensions over lldb, as well as
development symlinks for liblldb.

%package -n %lldb_name-doc
Summary: Documentation for LLDB
Group: Documentation
BuildArch: noarch
%requires_filesystem

%description -n %lldb_name-doc
Documentation for the LLDB debugger.

%prep
%setup -n llvm-%tarversion.src -a1 -a2 -a3 -a4 -a5
for pkg in clang lld lldb; do
   mv $pkg-%tarversion.src tools/$pkg
done
mv clang-tools-extra-%tarversion.src tools/clang/tools/extra
for pkg in compiler-rt; do
   mv $pkg-%tarversion.src projects/$pkg
done
%patch -p1 -b .alt-i586-fallback
%patch1 -p1 -b .alt-triple
%patch2 -p1
sed -i 's)"%%llvm_bindir")"%llvm_bindir")' lib/Support/Unix/Path.inc
%patch3 -p1 -b .alt-fix-linking
%patch4 -p1 -b .alt-triple
%patch5 -p1 -b .alt-i586-arch
%patch6 -p1
%patch7 -p1 -b .alt-aarch64-dynamic-linker
%patch8 -p1
%patch9 -p1 -b .alt-mipsel-permit-textrels-by-default
%patch10 -p1
%patch14 -p1
%patch15 -p2
%patch16 -p1
%patch17 -p1
%patch20 -p1
%patch21 -p1

# Explicitly use python3 in select hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(find * -name opt-viewer.py)
# Explicitly use python2 in hashbangs.
# TODO: LLVM 12 and onward deprecate Python 2:
# https://releases.llvm.org/11.0.0/docs/ReleaseNotes.html
subst '/^#!.*python$/s|python$|python2|' $(grep -Rl '#!.*python$' *)

%build
export NPROCS="%__nprocs"
if [ "$NPROCS" -gt 64 ]; then
	export NPROCS=64
fi
%define _cmake__builddir BUILD
%define _cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=OFF
%cmake -G Ninja \
	-DLLVM_PARALLEL_LINK_JOBS=1 \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%llvm_prefix \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
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
	-DLLVM_ENABLE_LTO=On \
	%ifnarch riscv64
	-DLLVM_USE_LINKER=gold \
	%endif
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic" \
	%endif
	\
	-DLLVM_LIBDIR_SUFFIX="%_libsuff" \
	-DLLVM_BUILD_RUNTIME:BOOL=ON \
	\
	-DLLVM_INCLUDE_TOOLS:BOOL=ON \
	-DLLVM_BUILD_TOOLS:BOOL=ON \
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

sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' BUILD/build.ninja
# Do not install opt-viewer into buildroot.
sed -i '1,$d' BUILD/tools/opt-viewer/cmake_install.cmake
ninja -vvv -j "$NPROCS" -C BUILD

%install
pushd BUILD
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%llvm_prefix ../
sed -i 's|man\ tools/lld/docs/docs-lld-html|man|' build.ninja
sed -i '/^[[:space:]]*include.*tools\/lld\/docs\/cmake_install.cmake.*/d' tools/lld/cmake_install.cmake
popd
# Do not install opt-viewer into buildroot.
sed -i '1,$d' BUILD/tools/opt-viewer/cmake_install.cmake
ninja -C BUILD install

# Prepare Clang documentation.
rm -rf BUILD/clang-docs
mkdir -p BUILD/clang-docs
for f in LICENSE.TXT NOTES.txt README.txt; do
  ln tools/clang/$f BUILD/clang-docs/
done
rm -rf tools/clang/docs/{doxygen*,Makefile*,*.graffle,tools}

install -m 0755 BUILD/%_lib/LLVMHello.so %buildroot%llvm_libdir/
install -m 0755 BUILD/%_lib/BugpointPasses.so %buildroot%llvm_libdir/
mkdir -p %buildroot%llvm_docdir/lld

%ifarch %ix86
cd %buildroot%llvm_libdir/clang/%v_full/lib/linux
ls *-i[3-9]86* | while read f; do ln -s $f $(echo $f | sed 's|i[3-9]86|i386|') ; done
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
		# /usr/lib/llvm-11.0/share/man/manD/utilX.D.xz -> /usr/share/man/manD/utilX-11.D.xz
		# Otherwise, brp-alt(compress) keeps fucking us up.
		# It remakes the symlinks first, then compresses their targets,
		# severing the symlinks.
		/usr/lib/rpm/compress_files "$m"

		mb="$(basename "$m")" # e. g. llvm-ar.1.xz
		new_mb="${mb%%.[1-9]*}-%v_major.$mand_index" # e. g. llvm-ar-11.1.xz

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

# Emit executable list for %name.
# A tool can be accompanied by a man page or not.
awk -F'\t' '
$1 ~ "bin" { print "%llvm_bindir/" $2; print "%_bindir/" $2 "-%v_major"; }
$1 ~ "man" { print "%llvm_man1dir/" $2 ".1*"; print "%_man1dir/" $2 "-%v_major.1*"; }
' >%_tmppath/dyn-files-%name <<EOExecutableList
bin,man	bugpoint
bin,man	diagtool
bin,man	dsymutil
bin,man	llc
bin,man	lli
bin,man	llvm-addr2line
bin,man	llvm-ar
bin,man	llvm-as
bin,man	llvm-bcanalyzer
bin	llvm-cat
bin	llvm-cfi-verify
bin,man	llvm-cov
bin	llvm-c-test
bin	llvm-cvtres
bin	llvm-cxxdump
bin,man	llvm-cxxfilt
bin,man	llvm-cxxmap
bin,man	llvm-diff
bin,man	llvm-dis
bin	llvm-dlltool
bin,man	llvm-dwarfdump
bin	llvm-dwp
bin	llvm-elfabi
bin,man	llvm-exegesis
bin,man	llvm-extract
bin	llvm-gsymutil
bin	llvm-ifs
bin	llvm-install-name-tool
bin	llvm-jitlink
bin,man	llvm-lib
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
bin,man	llvm-pdbutil
bin,man	llvm-profdata
bin,man	llvm-ranlib
bin	llvm-rc
bin,man	llvm-readelf
bin,man	llvm-readobj
bin	llvm-reduce
bin	llvm-rtdyld
bin,man	llvm-size
bin	llvm-split
bin,man	llvm-stress
bin,man	llvm-strings
bin,man	llvm-strip
bin,man	llvm-symbolizer
bin	llvm-tblgen
man	tblgen
bin	llvm-undname
bin	llvm-xray
bin	modularize
bin	obj2yaml
bin,man	opt
bin	pp-trace
bin	sancov
bin	sanstats
bin	verify-uselistorder
bin	yaml2obj

man	FileCheck
man	extraclangtools
man	lit
man	llvm-build
man	llvm-locstats
EOExecutableList

%check
%if_enabled tests
LD_LIBRARY_PATH=%buildroot%llvm_libdir:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH
ninja -C BUILD check-all || :
%endif

# Do not generate dependencies for clang-{format,rename} plugins.
%add_findreq_skiplist %llvm_datadir/clang/*

%files filesystem
%dir %llvm_prefix
%dir %llvm_bindir
%dir %llvm_libdir
%dir %llvm_includedir
%dir %llvm_libexecdir
%dir %llvm_datadir
%dir %llvm_datadir/clang
%dir %llvm_datadir/man
%dir %llvm_man1dir
%dir %llvm_docdir

%files -f %_tmppath/dyn-files-%name
%doc CREDITS.TXT LICENSE.TXT README.txt

%files libs
%llvm_libdir/libLLVM-*.so
%_libdir/libLLVM-*.so
%llvm_libdir/libLTO.so.*
%_libdir/libLTO.so.*
%llvm_libdir/libRemarks.so.*
%_libdir/libRemarks.so.*

%files devel
%llvm_bindir/llvm-config
%_bindir/llvm-config-%v_major
%llvm_man1dir/llvm-config.1.*
%_man1dir/llvm-config-%v_major.1.*
%llvm_includedir/llvm
%llvm_includedir/llvm-c
%llvm_libdir/libLLVM.so
%llvm_libdir/libLTO.so
%llvm_libdir/LLVMgold.so
%llvm_libdir/libRemarks.so
%llvm_libdir/LLVMHello.so
%llvm_libdir/BugpointPasses.so
%dir %llvm_libdir/cmake
%llvm_libdir/cmake/llvm
%exclude %llvm_libdir/cmake/llvm/LLVMStaticExports.cmake

%files devel-static
%llvm_libdir/*.a
%exclude %llvm_libdir/libclang*.a
%dir %llvm_libdir/cmake
%dir %llvm_libdir/cmake/llvm
%llvm_libdir/cmake/llvm/LLVMStaticExports.cmake

%files -n %clang_name
%doc BUILD/clang-docs/*
%llvm_bindir/clang-%v_major
%llvm_bindir/clang
%_bindir/clang-%v_major
%llvm_bindir/clang++
%_bindir/clang++-%v_major
%llvm_bindir/clang-cl
%_bindir/clang-cl-%v_major
%llvm_bindir/clang-cpp
%_bindir/clang-cpp-%v_major
%llvm_man1dir/clang.1*
%_man1dir/clang-%v_major.1*
%exclude %llvm_bindir/clang-check*
%exclude %_bindir/clang-check*
%exclude %llvm_bindir/clang-extdef-mapping*
%exclude %_bindir/clang-extdef-mapping*
%exclude %llvm_bindir/clang-format*
%exclude %_bindir/clang-format*
%exclude %llvm_bindir/git-clang-format*
%exclude %_bindir/git-clang-format*
%exclude %llvm_bindir/clang-offload-*
%exclude %_bindir/clang-offload-*
%exclude %llvm_bindir/clang-refactor*
%exclude %_bindir/clang-refactor*
%exclude %llvm_bindir/clang-rename*
%exclude %_bindir/clang-rename*
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
%dir %llvm_libdir/cmake
%llvm_libdir/cmake/clang

%files -n %clang_name-devel-static
%llvm_libdir/libclang*.a

%files -n %clang_name-analyzer
%llvm_prefix/libexec/*-analyzer
%llvm_bindir/scan-build
%_bindir/scan-build-%v_major
%llvm_bindir/scan-view
%_bindir/scan-view-%v_major
%llvm_datadir/scan-build
%llvm_datadir/scan-view
%llvm_man1dir/scan-build.1*
%_man1dir/scan-build-%v_major.1*

%files -n %clang_name-tools
%llvm_bindir/c-index-test
%_bindir/c-index-test-%v_major
%llvm_bindir/clang-*
%_bindir/clang-*
%exclude %llvm_bindir/clang-%v_major
%exclude %llvm_bindir/clang
%exclude %_bindir/*clang-%v_major
%exclude %llvm_bindir/clang++
%exclude %_bindir/clang++-%v_major
%exclude %llvm_bindir/clang-cl
%exclude %_bindir/clang-cl-%v_major
%exclude %llvm_bindir/clang-cpp
%exclude %_bindir/clang-cpp-%v_major
%llvm_bindir/find-all-symbols
%_bindir/find-all-symbols-%v_major
%llvm_bindir/hmaptool
%_bindir/hmaptool-%v_major
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
%dir %llvm_libdir/cmake
%llvm_libdir/cmake/lld

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
%llvm_bindir/lldb-vscode
%_bindir/lldb-vscode-%v_major

%files -n lib%lldb_name
%llvm_libdir/liblldb*.so.*
%_libdir/liblldb*.so.*

%files -n lib%lldb_name-devel
%llvm_includedir/lldb
%llvm_libdir/liblldb*.so
# %_libdir/liblldb*.so

%files doc
%doc %llvm_docdir/llvm

%files -n %clang_name-doc
%doc %llvm_docdir/clang
%doc %llvm_docdir/clang-tools

%files -n %lld_name-doc
%doc %llvm_docdir/lld

%files -n %lldb_name-doc
%doc %llvm_docdir/lldb

%changelog
* Thu Jan 05 2023 L.A. Kostis <lakostis@altlinux.ru> 11.0.1-alt6
- .spec: fix lldb symlinks.

* Sun Nov 21 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt5
- Stopped packaging opt-viewer-11 since it depends on python2(yaml).
  Users are advised to use more recent opt-viewer.

* Fri Nov 12 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt4
- Fixed FTBFS due to missing std::numeric_limits declaration.

* Tue Aug 10 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt3
- Made opt-viewer use python3. (closes: bug 40691)
- Backported from llvmorg-12.0.1:
  D102059: 884040d "libsanitizer: Remove cyclades inclusion in sanitizer"
  This is needed for the package to be buildable from source with modern
  glibc-kernheaders. (closes: bug 40357)

* Tue Jun 01 2021 Arseny Maslennikov <arseny@altlinux.org> 11.0.1-alt2
- spec: adapted to https://altlinux.org/CMakeMigration2021

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

* Thu Jun 02 2016 Rudolf Kastl <rkastl@redhat.com> 3.9.0-0.1.r
- using a random svn checkout of 3.9
- removed CppBackend
- updated files section

* Thu Mar 10 2016 Dave Airlie <airlied@redhat.com> 3.8.0-1
- llvm 3.8.0 release

* Wed Mar 09 2016 Dan Horák <dan[at][danny.cz> 3.8.0-0.3
- install back memory consumption workaround for s390

* Thu Mar 03 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.2
- llvm 3.8.0 rc3 release

* Fri Feb 19 2016 Dave Airlie <airlied@redhat.com> 3.8.0-0.1
- llvm 3.8.0 rc2 release

* Tue Feb 16 2016 Dan Horák <dan[at][danny.cz> 3.7.1-7
- recognize s390 as SystemZ when configuring build

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-6
- export C++ API for mesa.

* Sat Feb 13 2016 Dave Airlie <airlied@redhat.com> 3.7.1-5
- reintroduce llvm-static, clang needs it currently.

* Fri Feb 12 2016 Dave Airlie <airlied@redhat.com> 3.7.1-4
- jump back to single llvm library, the split libs aren't working very well.

* Fri Feb 05 2016 Dave Airlie <airlied@redhat.com> 3.7.1-3
- add missing obsoletes (#1303497)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.1-1
- new upstream release
- enable gold linker

* Wed Nov 04 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- fix Requires for subpackages on the main package

* Tue Oct 06 2015 Jan Vcelak <jvcelak@fedoraproject.org> 3.7.0-100
- initial version using cmake build system
