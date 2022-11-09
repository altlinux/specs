%define optflags_lto %nil

Name: spirv-llvm-translator
Version: 13.0.0
Release: alt1
Summary: LLVM to SPIRV Translator
Group: Development/Other
License: NCSA

URL: https://github.com/KhronosGroup/SPIRV-LLVM-Translator
Source0: SPIRV-LLVM-Translator-llvm_release_130.zip
Patch0: SPIRV-LLVM-Translator-ver.patch

BuildRequires: cmake gcc-c++ llvm-devel ninja-build spirv-headers unzip

%description
Khronos LLVM to SPIRV Translator. This is a library
to be used by Mesa for OpenCL support. It translate
LLVM IR to Khronos SPIR-V. It also includes a
standalone tool used for building libclc.

%package devel
Summary: Development files for LLVM to SPIRV Translator
Group: Development/Other

%description devel
This package contains libraries and header files for
developing against %name

%package tools
Summary: Standalone llvm to spirv translator tool
Group: Development/Other

%description tools
This package contains the standalone llvm to spirv tool

%prep
%setup -n SPIRV-LLVM-Translator-llvm_release_130
%patch -p0

%build
%cmake -GNinja \
	-DLLVM_BUILD_TOOLS=ON \
	-DCMAKE_BUILD_TYPE=Release \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	-DCMAKE_INSTALL_RPATH:BOOL=";" \
	-DLLVM_EXTERNAL_PROJECTS="SPIRV-Headers" \
	-DLLVM_EXTERNAL_SPIRV_HEADERS_SOURCE_DIR="/usr/include/spirv/"

%cmake_build

%install
%cmake_install

%files
%doc README.md
%_libdir/libLLVMSPIRVLib.so.*

%files tools
%_bindir/llvm-spirv

%files devel
%_includedir/LLVMSPIRVLib
%_libdir/libLLVMSPIRVLib.so
%_pkgconfigdir/LLVMSPIRVLib.pc

%changelog
* Wed Nov 09 2022 Valery Inozemtsev <shrek@altlinux.ru> 13.0.0-alt1
- initial release

