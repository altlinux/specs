%define llvm_ver 15.0
%define soname 1
%define bits 64

# LTO causes segfaults (
%define optflags_lto %nil

Name: rocr-runtime
Version: 5.4.1
Release: alt0.2
License: MIT
Summary: HSA Runtime API and runtime for ROCm
Url: https://github.com/RadeonOpenCompute/ROCR-Runtime
Group: System/Libraries

Source: %name-%version.tar
Patch0: rocr-image-bitcode-path.patch
# https://bugs.gentoo.org/716948
Patch1: rocr-runtime-4.3.0_no-aqlprofiler.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libelf-devel libdrm-devel hsakmt-rocm-devel rocm-device-libs xxd
BuildRequires: clang%{llvm_ver}-devel llvm%{llvm_ver}-devel mlir%{llvm_ver}-tools lld%{llvm_ver}

# only 64-bit
ExclusiveArch: x86_64 aarch64 ppc64le

%description
AMD's implementation of the core HSA Runtime API's.

%package -n libhsa-runtime%{soname}
Summary: HSA Runtime API and runtime for ROCm
Provides: libhsa-runtime%{bits} = %EVR, hsa-rocr = %EVR
Group: System/Libraries

%description -n libhsa-runtime%{soname}
AMD's implementation of the core HSA Runtime API's.

%package -n hsa-rocr-devel
Summary: HSA Runtime API and runtime for ROCm development
Group: Development/C++

%description -n hsa-rocr-devel
HSA Runtime API and runtime for ROCm development headers and library.

%prep
%setup
%patch0 -p1
%patch1 -p0

%build
export ALTWRAP_LLVM_VERSION=%{llvm_ver}
pushd src
%cmake \
	-DBUILD_SHARED_LIBS=ON \
	-DINCLUDE_PATH_COMPATIBILITY=OFF \
	-DCMAKE_INSTALL_LIBDIR=%_lib
%cmake_build

%install
pushd src
%cmake_install

%files -n libhsa-runtime%{soname}
%doc src/LICENSE.md src/README.md
%_libdir/libhsa-runtime%{bits}.so.%{soname}*

%files -n hsa-rocr-devel
%_includedir/hsa
%_libdir/libhsa-runtime%{bits}.so
%_libdir/cmake/hsa-runtime%{bits}

%changelog
* Wed Jan 04 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.2
- Restrict build to 64-bit.

* Mon Jan 02 2023 L.A. Kostis <lakostis@altlinux.ru> 5.4.1-alt0.1
- First build for ALTLinux.
