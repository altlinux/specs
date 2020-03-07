Name: ispc
Version: 1.12.0
Release: alt1
Summary: Intel SPMD Program Compiler
License: BSD-3-Clause
Group: Development/C

Source: %name-%version.tar

# Story: https://pharr.org/matt/blog/2018/04/30/ispc-all.html
Vcs: https://github.com/ispc/ispc.git
Url: https://ispc.github.io/

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): python3-module-setuptools
BuildRequires: bison >= 2.4
BuildRequires: cmake >= 3.12
BuildRequires: clang-devel >= 9.0.0
BuildRequires: llvm-devel >= 9.0.0
BuildRequires: llvm-devel-static
BuildRequires: gcc-c++
BuildRequires: flex >= 2.5
BuildRequires: python3-devel
BuildRequires: python3-tools
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
BuildRequires: doxygen

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

%changelog
* Sat Mar 07 2020 Vitaly Chikunov <vt@altlinux.org> 1.12.0-alt1
- Initial import of v1.12.0.
