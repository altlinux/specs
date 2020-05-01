# SPDX-License-Identifier: GPL-2.0-only

Name: ispc
Version: 1.13.0
Release: alt2
Summary: Intel Implicit SPMD Program Compiler
License: BSD-3-Clause
Group: Development/C

Source: %name-%version.tar

# Story: https://pharr.org/matt/blog/2018/04/30/ispc-all.html
Vcs: https://github.com/ispc/ispc.git
Url: https://ispc.github.io/

# Tested on 10.0 to be good too.
%define clang_version 10.0

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: clang%clang_version-devel
BuildRequires: llvm%clang_version-devel
BuildRequires: llvm%clang_version-devel-static
BuildRequires: libstdc++-devel
BuildRequires: flex
BuildRequires: python3-devel
BuildRequires: python3-tools
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
BuildRequires: /proc

ExclusiveArch: x86_64

%description
ispc is a compiler for a variant of the C programming language, with
extensions for single program, multiple data programming. Under the SPMD
model, the programmer writes a program that generally appears to be a regular
serial program, though the execution model is actually that a number of
program instances execute in parallel on the hardware.

%prep
%setup

%build
# -DISPC_INCLUDE_TESTS=OFF = we don't have FileCheck
# -DARM_ENABLED=OFF        = we don't have `arm` and `aarch64` llvm components
#   also, see https://pharr.org/matt/blog/2018/04/29/ispc-retrospective.html#the-unwanted-pull-request
# -DISPC_NO_DUMPS=ON       =
#	CMake Warning at cmake/LLVMConfig.cmake:105 (message):
#	  LLVM was built without assertions enabled (-DLLVM_ENABLE_ASSERTIONS=OFF).
#	  This disables dumps, which are required for ISPC to be fully functional.
#
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_EXE_LINKER_FLAGS="%optflags -fPIE" \
	-DLLVM_DIR=$(llvm-config --cmakedir) \
	-DISPC_NO_DUMPS=ON \
	-DARM_ENABLED=OFF \
	-DISPC_INCLUDE_TESTS=OFF \
	-DISPC_INCLUDE_EXAMPLES=OFF \

%cmake_build

%install
%cmake_install DESTDIR=%buildroot install

%files
%doc LICENSE.txt
%_bindir/%name
%_bindir/check_isa

%check
PATH=BUILD/bin:$PATH
# Increase timeout from 10 to 100 or beekeeper will sometimes fail.
sed -i /run_command/s/10/100/ run_tests.py
# Tests are from .travis.yml
check_isa
ispc --support-matrix
./run_tests.py --jobs=$(nproc) --non-interactive
./run_tests.py --jobs=$(nproc) --non-interactive --arch=$(arch)

%changelog
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
