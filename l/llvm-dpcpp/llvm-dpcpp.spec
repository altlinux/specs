%define _unpackaged_files_terminate_build 1

%filter_from_requires /python[0-9.]\+(Reporter)/d
%filter_from_requires /python[0-9.]\+(optpmap)/d
%filter_from_requires /python[0-9.]\+(libscanbuild[.].*)/d

%global proj dpcpp
# dpc llvm uses llvm21 as codebase
%global v_major 21
%global v_majmin %v_major.0
%global sycl_major 8
%global llvm_name llvm-%proj
%global clang_name clang-%proj
%global lld_name lld-%proj
%global sycl_name %proj-sycl
%global clang_sover %v_major
%global clang_cpp_sover %v_major
%global libclc_name libclc-%proj
%global libclang_name libclang-%proj
%global libclang_cpp_name libclang-cpp-%proj

%global llvm_default_name llvm%_llvm_version
%global clang_default_name clang%_llvm_version
%global lld_default_name lld%_llvm_version

%global llvm_prefix %prefix/lib/llvm-%proj
%global llvm_bindir %llvm_prefix/bin
%global llvm_libdir %llvm_prefix/%_lib
%global llvm_includedir %llvm_prefix/include
%global llvm_datadir %llvm_prefix/share
%global llvm_man1dir %llvm_datadir/man/man1
%global llvm_docdir %llvm_datadir/doc

# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%define optflags_debug -g1

%global optflags_lto -flto=thin -ffat-lto-objects

%def_with clang
%def_with mold
%def_without cuda
%def_without hip
# libclc used by cuda/hip
%def_without clc
# jit used by cuda/hip
%def_without jit
%def_disable tests

%define tarversion v6.3.0
%define mversion %version

Name: %llvm_name
Version: 6.3.0
Release: alt0.2
Epoch: 1
Summary: oneAPI DPC++ compiler Infrastructure
Group: Development/C
License: Apache-2.0 with LLVM-exception
# Source-URL: https://github.com/intel/llvm/archive/refs/tags/%tarversion.tar.gz
Url: https://github.com/intel/llvm.git
Source0: llvm-project-%version.tar
# vc-intrinsics https://github.com/intel/vc-intrinsics
# 60cea7590bd022d95f5cf336ee765033bd114d69
# vc-i is highly coupled with llvm so we can't use system one.
Source1: vc-intrinsics.tar
# compute-runtime headers (25.05.32567.17)
Source2: compute-runtime.tar

# ALTLinux patches
Patch1: clang-alt-triple.patch
Patch2: 0001-alt-llvm-config-Ignore-wrappers-when-looking-for-current.patch
Patch6: clang-ALT-bug-40628-grecord-command-line.patch
Patch7: clang-tools-extra-alt-gcc-0001-clangd-satisfy-ALT-gcc-s-Werror-return-type.patch
Patch10: llvm-cmake-pass-ffat-lto-objects-if-using-the-GNU-toolcha.patch
Patch11: lld-compact-unwind-encoding.h.patch
Patch13: clang-16-alt-rocm-device-libs-path.patch
Patch14: clang-alt-nvvm-libdevice.patch
Patch17: clang-ALT-bug-47780-Calculate-sha1-build-id-for-produced-executables.patch

# ALTLinux/DPC++ specific patches
Patch100: dpc-opencl-alt-use-system-cl-libs.patch
Patch101: xptifw-alt-use-system-phm.patch
Patch102: sycl-alt-do-not-hardcode-cl-lib.patch
Patch104: sycl-alt-remove-cl-headers.patch
Patch106: clang-sycl-fix-arl-ocloc-name.patch
Patch110: llvm-fix-dylib-deps.patch
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
BuildRequires: zip zlib-devel binutils-devel ninja-build libzstd-devel-static

# DPCPP specific requires
BuildRequires: gdb libhwloc-devel libbacktrace-devel emhash-devel
BuildRequires: ocl-icd-devel libtbb-devel spirv-tools libspirv-tools-devel
BuildRequires: libvulkan-devel spirv-headers >= 1.5.5-alt17 glslang glslc libze-devel
BuildRequires: libumf-devel >= 1.0.0 parallel-hashmap-devel
%if_with clang
BuildRequires: %clang_default_name %llvm_default_name-devel
%else
BuildRequires: gcc-c++
%endif

%if_with mold
BuildRequires: mold
%endif

%if_with cuda
BuildRequires: nvidia-cuda-devel libcupti-devel
%endif

%if_with hip
BuildRequires: hip-devel hip-runtime-amd rocm-comgr-devel rocm-device-libs hsa-rocr-devel
%endif

%if_enabled tests
BuildRequires: python3-module-psutil
%endif

%define requires_filesystem Requires: %name-filesystem = %EVR
%requires_filesystem
Requires: llvm >= %_llvm_version

# https://github.com/intel/llvm/blob/sycl/sycl/doc/GetStartedGuide.md
# only x86_64 for now, arm still very experimental
ExclusiveArch: x86_64

%description
The DPC++ is a LLVM-based compiler project that implements compiler and runtime
support for the SYCL* language. The project is hosted in the sycl branch and is
synced with the tip of the LLVM upstream main branch on a regular basis
(revisions delay is usually not more than 1-2 weeks). DPC++ compiler takes
everything from LLVM upstream as is, however some modules of LLVM might be not
included in the default project build configuration. Additional modules can be
enabled by modifying build framework settings.

%package filesystem
Group: Development/Other
Summary: Owns the installation prefix for DPC++ LLVM

%description filesystem
This package owns the installation prefix for LLVM. It is designed to be
pulled in by all non-empty LLVM packages.

%package devel
Group: Development/C++
Summary: Libraries and header files for DPC++ LLVM
%requires_filesystem
Requires: llvm-devel >= %_llvm_version
Requires: %name = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description devel
This package contains library and header files needed to develop new
native programs that use the LLVM DPC++ infrastructure.

%package gold
Summary: gold linker plugin for LLVM (dpcpp flavour)
Group: Development/Tools
%requires_filesystem
# requires: libLLVM
Requires: %name-libs

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description gold
This package contains the gold plugin for LLVM objects.

%package libs
Group: Development/C
Summary: LLVM shared libraries
%requires_filesystem
# We pull in the gold plugin for e. g. Clang's -flto=thin to work
# out of the box with gold.
Requires: %name-gold

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description libs
This package contains shared libraries needed to develop new
native programs that use LLVM.

%package -n libsycl%sycl_major
Group: System/Libraries
Summary: SYCL library
%requires_filesystem
Provides: libsycl = %EVR

%description -n libsycl%sycl_major
SYCL library

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
Requires: %clang_name-support = %EVR
Requires: libsycl-devel = %EVR

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

%package -n %libclang_name%clang_sover
Group: Development/C
Summary: clang shared library
%requires_filesystem
Requires: %clang_name-support = %EVR

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %libclang_name%clang_sover
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

This package contains the clang shared library for %proj.

%package -n %libclang_cpp_name%clang_cpp_sover
Group: Development/C
Summary: clang-cpp shared libraries
%requires_filesystem

# We do not want Python modules to be analyzed by rpm-build-python2.
AutoReq: nopython
AutoProv: nopython

%description -n %libclang_cpp_name%clang_cpp_sover
The goal of the Clang project is to create a new C, C++, Objective C
and Objective C++ front-end for the LLVM compiler. Its tools are built
as libraries and designed to be loosely-coupled and extendable.

This package contains the clang-cpp shared library for %proj.

%package -n %clang_name-libs
Group: Development/C
Summary: clang shared libraries
%requires_filesystem
# This is a compat package.
Requires: %libclang_name%clang_sover = %EVR
Requires: %libclang_cpp_name%clang_cpp_sover = %EVR

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

%package -n libsycl-devel
Group: Development/C++
Summary: SYCL Development library and headers
%requires_filesystem
Requires: libsycl = %EVR
%if_with clc
Requires: %libclc_name-devel = %EVR
%endif

%description -n libsycl-devel
SYCL Development library and headers

%package -n %sycl_name-runtime-libraries
Summary: Runtime libraries for SYCL compiler
Group: Development/C
%requires_filesystem
%if_with clc
Requires: %libclc_name = %EVR
%endif

%description -n %sycl_name-runtime-libraries
Runtime libraries for SYCL compiler

%package -n %sycl_name-runtime-hip
Summary: HIP runtimes for SYCL compiler
Group: System/Libraries
%requires_filesystem
%if_with clc
Requires: %libclc_name = %EVR
%endif

%description -n %sycl_name-runtime-hip
HIP Runtimes for SYCL compiler

%package -n %sycl_name-runtime-cuda
Summary: CUDA Runtimes for SYCL compiler
Group: System/Libraries
%requires_filesystem
%if_with clc
Requires: %libclc_name = %EVR
%endif

%description -n %sycl_name-runtime-cuda
Runtime libraries for SYCL compiler

%package -n %libclc_name
Group: Development/C++
Summary: An open source implementation of the OpenCL 1.1 library requirements
%requires_filesystem

%description -n %libclc_name
libclc is an open source, BSD licensed implementation of the library
requirements of the OpenCL C programming language, as specified by the
OpenCL 1.1 Specification.

%package -n %libclc_name-devel
Group: Development/C++
Summary: %libclc_name library and headers
%requires_filesystem
Requires: %libclc_name = %EVR

%description -n %libclc_name-devel
%libclc_name library and headers

%prep
%setup -n llvm-project-%version -a1 -a2
%patch1 -p1 -b .alt-triple
#%%patch2 -p1
sed -i 's)"%%llvm_bindir")"%llvm_bindir")' llvm/lib/Support/Unix/Path.inc
#%%patch3 -p1 -b .alt-fix-linking
%patch6 -p1
%patch7 -p1
%patch10 -p1
%patch11 -p1
%patch13 -p1 -b .clang-rocm-device-path
%patch14 -p1
%patch17 -p2

%patch100 -p1
%patch101 -p2 -b .xptifw-use-system-phm
%patch102 -p1
%patch104 -p1 -b .sycl-alt-remove-cl-headers
%patch106 -p1
%patch110 -p2

# LLVM 12 and onward deprecate Python 2:
# https://releases.llvm.org/12.0.0/docs/ReleaseNotes.html
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)
# stdc++fs is a part of libstdc++ on linux
find unified-runtime -name CMakeLists.txt -exec sed -i -e 's/stdc++fs/stdc++/g' {} \;

%build
export NPROCS="%__nprocs"
if [ "$NPROCS" -gt 64 ]; then
	export NPROCS=64
fi
%define builddir %_cmake__builddir

# try recommended way first
# https://github.com/intel/llvm/blob/sycl/sycl/doc/GetStartedGuide.md#build-dpc-toolchain
%if_with clang
export CC=clang
export CXX=clang++
%endif
%if_with cuda
export CUDA_LIB_PATH=%_libdir/stubs
%endif
export PWD=$(pwd)
%_bindir/python3 ./buildbot/configure.py \
	-o "%_cmake__builddir" \
	--l0-headers %_includedir/level_zero \
	--l0-loader %_libdir/libze_loader.so \
%if_with mold
	--cmake-opt="-DLLVM_USE_LINKER=mold" \
%else
	--cmake-opt="-DLLVM_USE_LINKER=gold" \
%endif
	--no-assertions \
%if_without jit
	--disable-jit \
%endif
%if_with cuda
	--cuda \
	--cmake-opt="-DCUDA_TOOLKIT_ROOT_DIR=%_libdir" \
	--cmake-opt="-DCUDA_CUPTI_INCLUDE_DIR=%_datadir/nvidia-cuda-toolkit/extras/CUPTI/include" \
%endif
%if_with hip
	--hip \
	--cmake-opt="-DUR_HIP_ROCM_DIR=%prefix" \
	--cmake-opt="-DUR_HIP_LIB_DIR=%_libdir" \
%endif
	--cmake-opt="-DLLVM_LINK_LLVM_DYLIB=ON" \
	--cmake-opt="-DLLVM_ENABLE_RTTI=ON" \
	--cmake-opt="-DCMAKE_C_FLAGS:STRING='%optflags'" \
	--cmake-opt="-DCMAKE_CXX_FLAGS:STRING='%optflags'" \
	--cmake-opt="-DCMAKE_INSTALL_PREFIX=%llvm_prefix" \
	--cmake-opt="-DINCLUDE_INSTALL_DIR:PATH=%_includedir" \
	--cmake-opt="-DLIB_INSTALL_DIR:PATH=%_libdir" \
	--cmake-opt="-DLIB_DESTINATION=%_lib" \
	--cmake-opt="-DLLVM_LIBDIR_SUFFIX=%_libsuff" \
	--cmake-opt="-DLLVM_VERSION_SUFFIX=%proj" \
	--cmake-opt="-DPACKAGE_VENDOR=%vendor" \
	--cmake-opt="-DPYTHON_EXECUTABLE=%_bindir/python3" \
	--cmake-opt="-DLLVM_BINUTILS_INCDIR=%_includedir/bfd" \
	--cmake-opt="-DFETCHCONTENT_FULLY_DISCONNECTED=ON" \
	--cmake-opt="-DUR_OPENCL_INCLUDE_DIR=%_includedir" \
	--cmake-opt="-DUR_USE_EXTERNAL_UMF=ON" \
	--cmake-opt="-DUR_LEVEL_ZERO_INCLUDE_DIR=%_includedir/level_zero" \
	--cmake-opt="-DL0_COMPUTE_RUNTIME_HEADERS=$PWD/compute-runtime" \
	--cmake-opt="-DOpenCL_INCLUDE_DIR=%_includedir" \
	--cmake-opt="-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR=%_includedir" \
	--cmake-opt="-DSYCL_EMHASH_DIR=%_includedir" \
	--cmake-opt="-DXPTIFW_PHM_DIR=%_includedir" \
	--cmake-opt="-DLLVMGenXIntrinsics_SOURCE_DIR=$PWD/vc-intrinsics" \
	--cmake-opt="-DLLVMGenXIntrinsics_INCLUDE_DIR=$PWD/vc-intrinsics/GenXIntrinsics/include" \
	--cmake-opt="-DLLVM_INCLUDE_UTILS=ON" \
	--cmake-opt="-DLLVM_INSTALL_UTILS=OFF" \
	--cmake-opt="-DNATIVECPU_USE_OCK=OFF" \
	--cmake-opt="-DLLVM_EXPERIMENTAL_TARGETS_TO_BUILD=SPIRV" \
	%nil

%_bindir/python3 ./buildbot/compile.py -j $NPROCS -v -o x86_64-alt-linux -t sycl-toolchain
#export LD_LIBRARY_PATH=$(pwd)/%builddir/%_lib
#ninja -vvv -j $NPROCS -C %builddir

%install
DESTDIR=%buildroot ninja -C %builddir install

# The following files are not used by LLVM builds for Linux.
rm -f %buildroot%llvm_datadir/clang/clang-format-bbedit.applescript

# Install the clang bash completion.
mkdir -p %buildroot%_datadir/bash-completion/completions
ln -sr %buildroot%llvm_datadir/clang/bash-autocomplete.sh %buildroot%_datadir/bash-completion/completions/clang-%proj

# Symlink executables to %_bindir.
mkdir -p %buildroot%_bindir
for b in %buildroot%llvm_bindir/*; do
	bb="$(basename "$b")"
	echo "$bb" | grep -q -- '-%proj$' && continue # if already appended
	ln -srv "$b" "%buildroot%_bindir/$bb-%proj"
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

# Python GDB extension
# See https://sourceware.org/gdb/current/onlinedocs/gdb.html/Python.html
mkdir -p %buildroot%_datadir/gdb/python
mv %buildroot%llvm_libdir/*.py %buildroot%_datadir/gdb/python/

# Symlink sonamed shared libraries in %llvm_prefix/%_libdir to %_libdir.
mkdir -p %buildroot%_libdir
find %buildroot%llvm_libdir/*.so* -type f,l \
	| grep -E '^%buildroot%llvm_libdir/.*(%v_major|libur|libsycl\.|libsycl\-preview|libxptifw)' | sort | tee %_tmppath/shared-objects \
	| sed 's)%llvm_libdir)%_libdir)' > %_tmppath/shared-object-links
paste %_tmppath/shared-objects %_tmppath/shared-object-links | while read object link; do
	ln -srv "$object" "$link"
done

# libsycl-devicelib-host hardcoded in clang
ln -srv %buildroot%llvm_libdir/libsycl-devicelib-host.a %buildroot%_libdir/libsycl-devicelib-host.a
ln -srv %buildroot%llvm_libdir/libsycl-devicelib-host.new.a %buildroot%_libdir/libsycl-devicelib-host.new.a

# List all packaged binaries in this source package.
find %buildroot%_bindir/*-%proj > %_tmppath/PATH-executables

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
$1 ~ "bin" { print "%llvm_bindir/" $2; print "%_bindir/" $2 "-%proj"; }
'
}

# cleanup
rm -rf %buildroot%llvm_includedir/{CL,LLVMSPIRVLib,.clang-format}
rm -rf %buildroot%llvm_libdir/pkgconfig
rm -rf %buildroot%llvm_docdir/{LLVM/examples}

# Emit executable list for %name.
emit_filelist >%_tmppath/dyn-files-%name <<EOExecutableList
bin	append-file
bin	bugpoint
bin	diagtool
bin	dsymutil
bin	file-table-tform
bin	llc
bin	lli
bin	llvm-addr2line
bin	llvm-ar
bin	llvm-as
bin	llvm-bcanalyzer
bin	llvm-bitcode-strip
bin	llvm-cat
bin	llvm-cfi-verify
bin	llvm-cgdata
bin	llvm-cov
bin	llvm-c-test
bin	llvm-ctxprof-util
bin	llvm-cvtres
bin	llvm-cxxdump
bin	llvm-cxxfilt
bin	llvm-cxxmap
bin	llvm-debuginfod-find
bin	llvm-debuginfod
bin	llvm-diff
bin	llvm-dis
bin	llvm-dlltool
bin	llvm-dwarfdump
bin	llvm-dwarfutil
bin	llvm-dwp
bin	llvm-exegesis
bin	llvm-extract
bin	llvm-foreach
bin	llvm-gsymutil
bin	llvm-ifs
bin	llvm-install-name-tool
bin	llvm-jitlink
bin	llvm-lib
bin	llvm-libtool-darwin
bin	llvm-link
bin	llvm-lipo
bin	llvm-lto
bin	llvm-lto2
bin	llvm-mc
bin	llvm-mca
bin	llvm-ml
bin	llvm-ml64
bin	llvm-modextract
bin	llvm-nm
bin	llvm-objcopy
bin	llvm-objdump
bin	llvm-opt-report
bin	llvm-otool
bin	llvm-pdbutil
bin	llvm-profdata
bin	llvm-profgen
bin	llvm-ranlib
bin	llvm-rc
bin	llvm-readelf
bin	llvm-readobj
bin	llvm-reduce
bin 	llvm-readtapi
bin 	llvm-rtdyld
bin	llvm-size
bin 	llvm-sim
bin	llvm-spirv
bin	llvm-tli-checker
bin 	llvm-windres
bin 	llvm-split
bin	llvm-stress
bin	llvm-strings
bin	llvm-strip
bin	llvm-symbolizer
bin	llvm-tblgen
bin	llvm-debuginfo-analyzer
bin	llvm-remarkutil
bin 	llvm-undname
bin 	llvm-xray
bin	opt
bin	opencl-aot
bin	sancov
bin	sanstats
bin	spirv-to-ir-wrapper
bin	verify-uselistorder
bin	reduce-chunk-list
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name <<EOExecutableList
bin	clang
bin	clang-%v_major
bin	clang++
bin	clang-cl
bin	clang-cpp
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name-analyzer <<EOExecutableList
bin	analyze-build
bin	intercept-build
bin,man	scan-build
man	scan-build-%v_major
bin	scan-build-py
bin	scan-view
EOExecutableList

emit_filelist >%_tmppath/dyn-files-%clang_name-tools <<EOExecutableList
bin	amdgpu-arch
bin	nvptx-arch
bin	c-index-test
bin	clang-check
bin	clang-extdef-mapping
bin	clang-format
bin	clang-installapi
bin	clang-linker-wrapper
bin	clang-nvlink-wrapper
bin	clang-offload-bundler
bin	clang-offload-deps
bin	clang-offload-extract
bin	clang-offload-packager
bin	clang-offload-wrapper
bin	clang-refactor
bin	clang-repl
bin	clang-scan-deps
bin	clang-sycl-linker
bin	clang-tblgen
bin	git-clang-format
bin	offload-arch
bin	hmaptool
EOExecutableList

# Emit executable list for SYCL library tools.
emit_filelist >%_tmppath/dyn-files-sycl-tools <<EOExecutableList
bin	sycl-ls
bin	sycl-post-link
bin	sycl-prof
bin	sycl-sanitize
bin	sycl-trace
bin	sycl-module-split
bin	syclbin-dump
EOExecutableList

# Comment out file validation for CMake targets placed
# in a different package.
sed -i '
/APPEND _cmake_import_check_targets \(tblgen-lsp-server\)/ {s|^|#|}
/APPEND _cmake_import_check_targets \(LibcTableGenUtil\)/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/llvm/LLVMExports-*.cmake

# Comment out file validation for CMake targets producing executables
# that may be placed in a different package.
sed -i '
/APPEND _cmake_import_check_files_for_.* .*[/]bin[/].*/ {s|^|#|}
' %buildroot%llvm_libdir/cmake/clang/ClangTargets-*.cmake

# Do not generate dependencies for clang-{format,rename} plugins.
%add_findreq_skiplist %llvm_datadir/clang/*

%check
%if_enabled tests
LD_LIBRARY_PATH=%buildroot%llvm_libdir \
%_bindir/python3 ./buildbot/check.py -o %_cmake__builddir || :
%endif

%files filesystem
%dir %llvm_prefix
%dir %llvm_bindir
%dir %llvm_libdir
%dir %llvm_includedir
%dir %llvm_libexecdir
%dir %llvm_prefix/lib
%dir %llvm_datadir
%dir %llvm_datadir/clang
%dir %llvm_datadir/man
%dir %llvm_man1dir

%files -f %_tmppath/dyn-files-%name
%doc llvm/CREDITS.TXT llvm/LICENSE.TXT llvm/README.txt

%files libs
%llvm_libdir/libLLVM-%v_major%proj.so
%_libdir/libLLVM-%v_major%proj.so
%llvm_libdir/libLLVM.so.%v_majmin%proj
%_libdir/libLLVM.so.%v_majmin%proj
%llvm_libdir/libLTO.so.%v_majmin%proj
%_libdir/libLTO.so.%v_majmin%proj
%llvm_libdir/libRemarks.so.%v_majmin%proj
%_libdir/libRemarks.so.%v_majmin%proj

%files tools
%llvm_datadir/opt-viewer

%files devel
%llvm_bindir/llvm-config
%_bindir/llvm-config-%proj
%llvm_includedir/llvm
%llvm_includedir/llvm-c
%llvm_libdir/libLLVM.so
%llvm_libdir/libLTO.so
%llvm_libdir/libRemarks.so
%llvm_libdir/cmake/llvm
%llvm_libdir/libLLVM*.a

%files gold
%llvm_libdir/LLVMgold.so

%files -n %clang_name -f %_tmppath/dyn-files-%clang_name
%llvm_datadir/clang/bash-autocomplete.sh
%_datadir/bash-completion/completions/clang*

%files -n %libclang_name%clang_sover
%llvm_libdir/libclang.so.%{clang_sover}*
%_libdir/libclang.so.%{clang_sover}*

%files -n %libclang_cpp_name%clang_cpp_sover
%llvm_libdir/libclang-cpp*.so.%{clang_cpp_sover}*
%_libdir/libclang-cpp*.so.%{clang_cpp_sover}*

%files -n %clang_name-libs
# This is a compat package.

%files -n %clang_name-support -f %_tmppath/dyn-files-clang-support
%llvm_libdir/clang

%files -n %clang_name-support-shared-runtimes -f %_tmppath/libclang-support-shared-runtimes
%files -n %clang_name-devel
%llvm_includedir/clang
%llvm_includedir/clang-c
%llvm_includedir/std
%llvm_libdir/libclang*.a
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
%llvm_man1dir/scan-build.1*
%_man1dir/scan-build-%v_major.1*

%files -n %clang_name-tools -f %_tmppath/dyn-files-%clang_name-tools
%llvm_datadir/clang
%exclude %llvm_datadir/clang/bash-autocomplete.sh

# hip uses lld for amdgpu ELF generation
%if_with hip
%files -n %lld_name
%llvm_bindir/lld
%_bindir/lld-%proj
%llvm_bindir/lld-link
%_bindir/lld-link-%proj
%llvm_bindir/ld*.lld
%_bindir/ld*.lld-%proj
%llvm_bindir/wasm-ld
%_bindir/wasm-ld-%proj

%files -n %lld_name-devel
%dir %llvm_includedir/lld
%llvm_includedir/lld/*
# see Patch11: lld-compact-unwind-encoding.h.patch
%llvm_includedir/mach-o
%llvm_libdir/cmake/lld
%llvm_libdir/liblld*.a
%endif

%files -n libsycl%sycl_major
%llvm_libdir/libsycl.so.*
%llvm_libdir/libsycl-preview.so.*
%_libdir/libsycl.so.*
%_libdir/libsycl-preview.so.*

%files -n libsycl-devel -f %_tmppath/dyn-files-sycl-tools
%llvm_libdir/libsycl.so
%llvm_libdir/libsycl-preview.so
%if_with jit
%llvm_libdir/libsycl-jit.so*
%llvm_libdir/libsycl-jit*.a
%endif
%llvm_libdir/libsycl*.bc
%llvm_libdir/libsycl*.spv
%llvm_libdir/libsycl*.o
%llvm_libdir/libsycl-devicelib-host*.a
%llvm_libdir/*_collector.so
%if_with jit
%llvm_libdir/libSYCLKernelJITPasses.a
%llvm_libdir/SYCLKernelJIT.so
%_libdir/libsycl-jit.so*
%endif
%_libdir/libsycl.so
%_libdir/libsycl-preview.so
%_libdir/libsycl-devicelib-host*.a
%llvm_includedir/sycl
%llvm_includedir/syclcompat
%llvm_includedir/syclcompat.hpp
%llvm_includedir/ur_*
%llvm_includedir/xpti
%_datadir/gdb/python/*.py
%llvm_prefix/lib/cmake

%files -n %sycl_name-runtime-libraries
%llvm_libdir/libur_common.a
%llvm_libdir/libxpti.a
%llvm_libdir/libur*.so*
%llvm_libdir/libxptifw.so
%_libdir/libur*.so*
%if_with hip
%exclude %llvm_libdir/libur_adapter_hip*
%exclude %_libdir/libur_adapter_hip*
%endif
%if_with cuda
%exclude %llvm_libdir/libur_adapter_cuda*
%exclude %_libdir/libur_adapter_cuda*
%endif
%_libdir/libxptifw.so

%if_with cuda
%files -n %sycl_name-runtime-cuda
%llvm_libdir/libur_adapter_cuda*
%_libdir/libur_adapter_cuda.so*
%endif

%if_with hip
%files -n %sycl_name-runtime-hip
%llvm_libdir/libur_adapter_hip*
%_libdir/libur_adapter_hip.so*
%endif

%if_with clc
%files -n %libclc_name
%llvm_bindir/libclc-remangler
%_bindir/libclc-remangler-%proj
%llvm_libdir/devicelib-amdgcn-amd-amdhsa.bc
%llvm_libdir/devicelib-nvptx64-nvidia-cuda.bc
%llvm_libdir/clc
%llvm_datadir/clc

%files -n %libclc_name-devel
%llvm_includedir/clc
%llvm_datadir/pkgconfig/libclc.pc
%endif

%changelog
* Wed Mar 25 2026 L.A. Kostis <lakostis@altlinux.ru> 1:6.3.0-alt0.2
- bash-completion: fix filename clash with clang-21.

* Fri Mar 13 2026 L.A. Kostis <lakostis@altlinux.ru> 1:6.3.0-alt0.1
- Initial build of 6.3.0:
  + cleanup merged/obsoleted patches.
  + vc-intrinsics: update to 60cea7590bd022d95f5cf336ee765033bd114d69.
  + BR: bump umf requires.

* Tue Dec 09 2025 L.A. Kostis <lakostis@altlinux.ru> 1:6.2.0-alt0.2
- build: disable assertions (were enabled by default).

* Mon Aug 25 2025 L.A. Kostis <lakostis@altlinux.ru> 1:6.2.0-alt0.1
- Initial build of 6.2.0:
  + llvm-project: update to stable 6.2.0
  + vc-intinsics: update to 4e51b2467104a257c22788e343dafbdde72e28bb
  + compute-runtime: ship special version for dpcpp
  + update/rediffed -alt patches
  + remove unneeded patches/sources
  + llvm-spirv: Fix LLVM_SPIRV_BACKEND_TARGET_PRESENT detection
  + build with system umf, emhash and parallel-hashmap.

* Thu May 01 2025 L.A. Kostis <lakostis@altlinux.ru> 2025.03.25-alt0.1
- New snapshot (2025-WW13):
  + clang: enable RTTI
  + debloat boost modules (patch from blender)
  + use system umf
  + vc-intrinsics: use bundled 0.22.1.
  + BR: requires spirv-headers from vulkan 1.4.309!
  + libclang/libclang-cpp: rename to avoid clash with future
    llvm versions.

* Mon Apr 28 2025 L.A. Kostis <lakostis@altlinux.ru> 1:6.0.1-alt0.1
- Downgrade to stable 6.0.1 (previous version had too many problems).
- Applied patches:
  + sycl: backport zstd support (patch from blender);
  + sycl: decrease boost modules usage (patch from blender);
  + clang/sycl: fix Arc/T130 device name/family.
  + sycl: use system vc-intrisics.
  + sycl: downgrade unified-runtime to 0.10.15.
  + sycl: update unified-memory-framework to 0.11.0.

* Sat Mar 15 2025 L.A. Kostis <lakostis@altlinux.ru> 2024.10.24-alt0.4
- Enable zstd support (for --offload-compress).

* Wed Feb 26 2025 L.A. Kostis <lakostis@altlinux.ru> 2024.10.24-alt0.3
- Disable HIP/CUDA for now (due debuginfo constrains).

* Wed Jan 29 2025 L.A. Kostis <lakostis@altlinux.ru> 2024.10.24-alt0.2
- Enable HIP and CUDA.
- Enable lld for HIP.
- Enable LLVM LLVM_DYLIB.

* Thu Jan 23 2025 L.A. Kostis <lakostis@altlinux.ru> 2024.10.24-alt0.1
- First build for ALTLinux:
  + build based on existing llvm19.x/rocm
  + use bundled packages.
- Bundled packages revisions:
  + parallel-hashmap: update to 8a889d3699b3c09ade435641fb034427f3fd12b6
  + emhash: update to 96dcae6fac2f5f90ce97c9efee61a1d702ddd634
  + boost-throw_exception: update to 7c8ec2114bc1f9ab2a8afbd629b96fbdd5901294
  + boost-static_assert: update to ba72d3340f3dc6e773868107f35902292f84b07e
  + boost-predef: update to 0fdfb49c3a6789e50169a44e88a07cc889001106
  + boost-describe: update to 50719b212349f3d1268285c586331584d3dbfeb5
  + boost-core: update to 083b41c17e34f1fc9b43ab796b40d0d8bece685c
  + boost-container_hash: update to 6d214eb776456bf17fbee20780a034a23438084f
  + boost-config: update to 11385ec21012926e15a612e3bf9f9a71403c1e5b
  + boost-assert: update to 447e0b3a331930f8708ade0e42683d12de9dfbc3
  + boost-unordered: update to 5e6b9291deb55567d41416af1e77c2516dc1250f
  + boost-mp11: update to 863d8b8d2b20f2acd0b5870f23e553df9ce90e6c
  + umf: update to fa006eea503a58e79fa197891f1391c9dcda73e1
  + unified-runtime: update to 3db3a5e2d935630f2ffddd93a72ae0aa9af89acb
  + vc-intrinsics: update to e1e2f81165ae75576a0201f342e7f1ea2ca40273
