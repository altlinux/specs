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
Version: 20250309
Release: alt1
Summary: Stable Diffusion and Flux in pure C/C++
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
Source2: kompute-0.tar
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
Inference of Stable Diffusion and Flux in pure C/C++.
  Supports CPU and CUDA.

  Note that on x86 only x86-64-v3 (with AVX2) is supported.

%prep
%setup
tar xf %SOURCE1 -C .
tar xf %SOURCE2 -C ggml/src/ggml-kompute
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
* Tue Mar 18 2025 Vitaly Chikunov <vt@altlinux.org> 20250309-alt1
- First import master-10c6501 (2025-03-09). Experimental.
