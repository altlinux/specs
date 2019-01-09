%define _vklib amdvlk
%define _vkdir %_datadir/vulkan/icd.d
# Decrease debuginfo verbosity to reduce memory consumption during final library linking
%define optflags_debug -g1

%ifarch x86_64
%define bits 64
%endif
%ifarch %ix86
%define bits 32
%endif

Name: vulkan-amdgpu
Version: 2019.Q1.1
Release: alt1
License: MIT
Url: https://github.com/GPUOpen-Drivers/AMDVLK
Summary: AMD Open Source Driver For Vulkan
Group: System/X11

ExclusiveArch: %ix86 x86_64

Requires: vulkan-filesystem

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc7-c++ cmake python3-devel curl libstdc++7-devel libxcb-devel
BuildRequires: libX11-devel libxshmfence-devel libXrandr-devel
BuildRequires: wayland-devel libwayland-server-devel libwayland-client-devel libwayland-cursor-devel libwayland-egl-devel

Source0: xgl.tar.xz
Source1: pal.tar.xz
Source2: llpc.tar.xz
Source3: spvgen.tar.xz
Source4: llvm.tar.xz
Source5: amd_icd.json

%description
The AMD Open Source Driver for Vulkan(r) is an open-source Vulkan driver for
Radeon(tm) graphics adapters on Linux(r). It is built on top of AMD's Platform
Abstraction Library (PAL), a shared component that is designed to encapsulate
certain hardware and OS-specific programming details for many of AMD's 3D and
compute drivers. Leveraging PAL can help provide a consistent experience across
platforms, including support for recently released GPUs and compatibility with
AMD developer tools.

%prep
%setup -n xgl -b0 -b1 -b2 -b3 -b4

%build
# build amdvlk.so
pushd %_builddir/xgl
export GCC_VERSION=7 \
%cmake \
	-DCMAKE_AR:PATH=%_bindir/gcc-ar \
	-DCMAKE_NM:PATH=%_bindir/gcc-nm \
	-DCMAKE_RANLIB:PATH=%_bindir/gcc-ranlib \
	-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DBUILD_WAYLAND_SUPPORT=ON
%cmake_build
popd

%install
mkdir -p %buildroot{%_vkdir,%_libdir}

install -p -m644 %_builddir/xgl/BUILD/icd/%_vklib%bits.so %buildroot%_libdir/
install -p -m644 %SOURCE5 %buildroot%_vkdir/amd_icd%{bits}.json
subst 's,@LIBDIR@,%_libdir,' %buildroot%_vkdir/amd_icd%{bits}.json
subst 's,@BITS@,%bits,' %buildroot%_vkdir/amd_icd%{bits}.json

%files
%_libdir/*.so
%_vkdir/*.json

%changelog
* Wed Jan 09 2019 L.A. Kostis <lakostis@altlinux.ru> 2019.Q1.1-alt1
- Initial build for ALTLinux:
  + do not build spvgen for now (only tests rely on it);
  + use gcc7 (gcc8 still unsupported by icd);
- Checkout from github:
  + xgl: master--bca286c1146f9f0662bbb7c10d193e487579e6f0
  + pal: master--f924a4fb84efde321f7754031f8cfa5ab35055d3
  + llpc: master--f36099d4c778327f22b050432f09e17dc815474a
  + spvgen: master--328a0990a958f21eb2c6b1ecb092a43629fe5554
  + llvm: master--0843ddd6f5a03468d42b90715e98e9798f772555
