# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%def_with lld
%if_with lld
%set_verify_elf_method skip
%else
%set_verify_elf_method strict
%endif

Name: ispc
Version: 1.21.0
Release: alt1
Summary: Intel Implicit SPMD Program Compiler
License: BSD-3-Clause
Group: Development/C

%define docdir %_docdir/%name-%version

Source: %name-%version.tar

# Story: https://pharr.org/matt/blog/2018/04/30/ispc-all.html
Vcs: https://github.com/ispc/ispc.git
Url: https://ispc.github.io/

BuildRequires(pre): rpm-macros-cmake
BuildRequires: banner
BuildRequires: cmake
BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: libstdc++-devel
BuildRequires: libstdc++-devel-static
BuildRequires: flex
BuildRequires: python3-devel
BuildRequires: python3-tools
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
BuildRequires: /proc
BuildRequires: tbb-devel
%if_with lld
BuildRequires: lld
%endif

# armh: clang-11: error: unsupported option '--with-fpu=hardfp'
# i586: Even though it builds it's not working until this fixed:
#       https://github.com/ispc/ispc/issues/2105
ExclusiveArch: x86_64 aarch64

%description
ispc is a compiler for a variant of the C programming language, with
extensions for "single program, multiple data" (SPMD) programming. Under the
SPMD model, the programmer writes a program that generally appears to be a
regular serial program, though the execution model is actually that a number
of program instances execute in parallel on the hardware.

ispc compiles a C-based SPMD programming language to run on the SIMD units of
CPUs and the Intel Xeon Phi architecture; it frequently provides a 3x or more
speedup on CPUs with 4-wide vector SSE units and 5x-6x on CPUs with 8-wide AVX
vector units, without any of the difficulty of writing intrinsics code.
Parallelization across multiple cores is also supported by ispc, making it
possible to write programs that achieve performance improvement that scales by
both number of cores and vector unit size.

%package libs-static
Summary: static libraries for %name
Group: Development/C
Requires(pre): %name = %EVR

%description libs-static
Static libraries for %name.

%package checkinstall
Summary: checkinstall for %name
Group: Development/C
Requires(pre): gcc-c++
Requires(pre): %name = %EVR

%description checkinstall
This package will try to build all %name examples.

%prep
%setup
sed -i 's/clangFrontend.*clangLex/clang-cpp/' CMakeLists.txt

%build
%if_with lld
%define optflags_lto -flto=thin
%endif

# -DISPC_INCLUDE_TESTS=OFF = we don't have FileCheck
# -DISPC_NO_DUMPS=ON       =
#	CMake Warning at cmake/LLVMConfig.cmake:105 (message):
#	  LLVM was built without assertions enabled (-DLLVM_ENABLE_ASSERTIONS=OFF).
#	  This disables dumps, which are required for ISPC to be fully functional.
# -DWASM_ENABLED=ON requires emcc.
# -DGENX_ENABLED=ON requires level_zero.

%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_EXE_LINKER_FLAGS="%optflags %{?_with_lld:-fuse-ld=lld -Wl,--build-id=sha1} -fPIE" \
%if_with lld
	-DCMAKE_SHARED_LINKER_FLAGS="$LDFLAGS %{?_with_lld:-fuse-ld=lld -Wl,--build-id=sha1}" \
%endif
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DCMAKE_STRIP:STRING="" \
	-DISPC_NO_DUMPS=ON \
	-DISPC_INCLUDE_TESTS=OFF \
	-DISPC_INCLUDE_EXAMPLES=OFF \

%ifarch %ix86
  # Workaround https://github.com/ispc/ispc/issues/2066
  # /usr/include/gnu/stubs.h:10:11: fatal error: 'gnu/stubs-64.h' file not found
  sed -i s/-m64/-m32/g %_cmake__builddir/CMakeFiles/ispc.dir/build.make
  # There is similar problem on armh with `gnu/stubs-soft.h'.
%endif

%cmake_build

%pre checkinstall
set -ex
mkdir /tmp/BUILD
cd /tmp/BUILD
cmake %docdir/examples/cpu
# Fix: aarch64-alt-linux-g++: error: unrecognized command-line option '-m64'
[ $(arch) = aarch64 ] && find -name flags.make | xargs sed -i 's/-m64//'
make -j$(nproc)
simple/simple

%install
%cmake_install

mkdir -p %buildroot%docdir
cp -a LICENSE.txt README.md SECURITY.md contrib/ docs/*.rst examples/ \
   docs/ReleaseNotes.txt %buildroot%docdir

%files
%_bindir/%name
%_bindir/check_isa
%_includedir/ispcrt
%_libdir/cmake
%_libdir/*.so*
%docdir

%files libs-static
%_libdir/libispcrt_static.a

%files checkinstall

%check
banner check
PATH=%_cmake__builddir/bin:$PATH
# Increase timeout from 10 to 100 or beekeeper will sometimes fail.
sed -i /run_command/s/10/100/ run_tests.py
# Tests are from .travis.yml
check_isa
ispc --support-matrix
%ifarch x86_64
  ./run_tests.py --jobs=$(nproc) --non-interactive
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=x86_64
%endif
%ifarch %ix86
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=x86
%endif
%ifarch aarch64
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=aarch64 --target=neon-i32x8
%endif
%ifarch armh
  ./run_tests.py --jobs=$(nproc) --non-interactive --arch=arm --target=neon-i32x8
%endif

%changelog
* Mon Sep 11 2023 L.A. Kostis <lakostis@altlinux.ru> 1.21.0-alt1
- 1.21.0.

* Wed Jun 21 2023 L.A. Kostis <lakostis@altlinux.ru> 1.20.0-alt1
- Update to 1.20.0 (20230-05-05).
- BR: added tbb-devel
- link with ldd.
- Added headers/cmake and libraries.

* Mon Sep 06 2021 Vitaly Chikunov <vt@altlinux.org> 1.16.1-alt1
- Update to v1.16.1 (2021-07-15).
- spec: Fix build with LTO.
- spec: Do not build for i586.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.15.0-alt3
- NMU: spec: adapt to new cmake macros.

* Fri Apr 23 2021 Vitaly Chikunov <vt@altlinux.org> 1.15.0-alt2
- Use latest Clang/LLVM (11.0).
- Enable x86 and aarch64.

* Mon Dec 21 2020 Vitaly Chikunov <vt@altlinux.org> 1.15.0-alt1
- Update to v1.15.0 (2020-12-18).

* Sun Aug 30 2020 Vitaly Chikunov <vt@altlinux.org> 1.14.1-alt1
- Update to v1.14.1 (2020-08-28).

* Fri Jul 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.14.0-alt1
- Update to v1.14.0 (2020-07-30).

* Wed May 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt4
- spec: Add test to compile all examples in checkinstall.

* Wed May 06 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt3
- Add examples and documentation to the package.

* Fri May 01 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt2
- spec: Improve %%check section.

* Sat Apr 25 2020 Vitaly Chikunov <vt@altlinux.org> 1.13.0-alt1
- Update to v1.13.0.
- Use Clang/LLVM 10.
- spec: Add tests into %%check section.

* Sat Mar 28 2020 Vitaly Chikunov <vt@altlinux.org> 1.12.0-alt2
- Clean up spec to fix compiling.

* Sat Mar 07 2020 Vitaly Chikunov <vt@altlinux.org> 1.12.0-alt1
- Initial import of v1.12.0.
