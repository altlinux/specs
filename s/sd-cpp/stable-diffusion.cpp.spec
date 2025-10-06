# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%ifarch x86_64
%def_enable cuda
%else
%def_disable cuda
%endif

Name: sd-cpp
Version: 20250925
Release: alt1
Summary: Diffusion model (SD, Flux, Wan) inference in pure C/C++
License: MIT
Group: Sciences/Computer science
Url: https://github.com/leejet/stable-diffusion.cpp
Provides: sd.cpp = %EVR
Provides: stable-diffusion.cpp = %EVR
# No point to support only x86-64-v3 on ix86.
ExcludeArch: %ix86
%if_enabled cuda
%filter_from_requires /(libcudart\.so\.12)/d
%filter_from_requires /debug64(libcuda\.so\.1)/d
Requires: libnvidia-ptxjitcompiler
%endif

Source: %name-%version.tar
Source1: ggml-0.tar
BuildRequires(pre): rpm-build-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
BuildRequires: libstdc++-devel-static
%if_enabled cuda
BuildRequires: gcc12-c++
BuildRequires: nvidia-cuda-devel-static
%endif

%description
Inference of Diffusion models in pure C/C++. Supports CPU and CUDA.

Supported models:
  Image Models: SD1.x, SD2.x, SD-Turbo, SDXL, SDXL-Turbo, SD3/SD3.5,
    Flux-dev/Flux-schnell, Chroma
  Image Edit Models: FLUX.1-Kontext-dev
  Video Models: Wan2.1/Wan2.2
  PhotoMaker support
  Control Net support with SD 1.5
  LoRA support, same as stable-diffusion-webui
  Latent Consistency Models support (LCM/LCM-LoRA)
  Faster and memory efficient latent decoding with TAESD
  Upscale images generated with ESRGAN

Package note: on x86 only x86-64-v3 (with AVX2) is supported.

%prep
%setup
tar xf %SOURCE1 -C .
# We have sd in sd (another rust tool rewrite) and sdcpp in sdcc (C compiler).
# To avoid making a conflict with these tools just rename the sd binary.
sed -i '/set(TARGET/s/sd/sd-cpp/' examples/cli/CMakeLists.txt

%build
%add_optflags %(getconf LFS_CFLAGS)
export NVCC_PREPEND_FLAGS=-ccbin=g++-12
# Even when CUDA is enabled it uses CPU inference for t5xxl (Flux text encoder)
# which can take 15 minutes on 1 core with SSE4.2. We desperately need AVX2.
# Basically, we want to build with `-DGGML_AVX2`, but cannot do it lazy way,
# because upstream build system is broken (perhaps this code path is untested).
# (It detects it's building under RPM (by SOURCE_DATE_EPOCH thx to OpenSUSE)
# and turns off GGML_NATIVE_DEFAULT and then it messes up -march= flags). But,
# thanks our build farm is AVX2 capable, we can just build 'native', yet.
%cmake \
	-DGGML_NATIVE=ON \
%if_enabled cuda
	-DSD_CUDA=ON \
	-DCMAKE_CUDA_ARCHITECTURES='52-virtual;80-virtual' \
%endif
	-DGGML_BUILD_NUMBER=1 \
	-DSD_BUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install
# submodule installing devel files.
rm -rf %buildroot%_includedir %buildroot%_cmakedir
find %buildroot%_prefix -name '*.a' -print -delete

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md docs assets
%_bindir/sd-cpp

%changelog
* Mon Oct 06 2025 Vitaly Chikunov <vt@altlinux.org> 20250925-alt1
- Update to master-309-35843c7 (2025-09-25).

* Thu Sep 11 2025 Vitaly Chikunov <vt@altlinux.org> 20250910-alt1
- Update to master-b017918 (2025-09-10).
- Added Wan2.2 (vid_gen) support.

* Mon Aug 11 2025 Vitaly Chikunov <vt@altlinux.org> 20250803-alt1
- Update to master-5b8996f-1-g5900ef66 (2025-08-03).

* Tue Mar 18 2025 Vitaly Chikunov <vt@altlinux.org> 20250309-alt1
- First import master-10c6501 (2025-03-09). Experimental.
