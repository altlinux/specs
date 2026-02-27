%define _unpackaged_files_terminate_build 1

%define llvm_version 20.1
%define clang_major_version 20
%define clang_minor_version 1
%define clang_version %{clang_major_version}.%{clang_minor_version}

%define oname cutlass
%define dist_name nvidia_%oname

Name:    nvidia-cutlass
Version: 4.3.1
Release: alt1

Summary: CUDA Templates and Python DSLs for High-Performance Linear Algebra
License: BSD-3-Clause
Group:   Development/Other
Url:     https://docs.nvidia.com/cutlass/index.html
Vcs:     https://github.com/NVIDIA/cutlass.git

Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-python3 cmake rpm-build-ninja
BuildRequires: llvm%llvm_version clang%clang_version
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: nvidia-cuda-devel
BuildRequires: nvidia-cuda-devel-static
BuildRequires: libcudnn-devel

%description
CUTLASS is a collection of abstractions for implementing high-performance
matrix-matrix multiplication (GEMM) and related computations at all levels
and scales within CUDA. It incorporates strategies for hierarchical
decomposition and data movement. CUTLASS decomposes these "moving parts"
into reusable, modular software components and abstractions.

%package headers
Summary: CUDA Templates for Linear Alegbra Subroutines (headers only)
Group: Development/Other

%description headers 
%summary.

%prep
%setup

%build

export CC=/usr/bin/clang-%clang_major_version
export CXX=/usr/bin/clang++-%clang_major_version
export CUDACXX=%_bindir/nvcc

%cmake  -GNinja \
	-DCUTLASS_ENABLE_HEADERS_ONLY=ON \
	-DCMAKE_CUDA_HOST_COMPILER=/usr/bin/clang++-%clang_major_version \
	-DCUTLASS_NVCC_ARCHS="70;72;75;80;86;87;89;90;90a" \
	-DCUTLASS_ENABLE_GTEST_UNIT_TESTS=OFF \
	-DUTLASS_ENABLE_TESTS=OFF \
	-DCUTLASS_ENABLE_CUBLAS=ON \
	-DCUTLASS_ENABLE_CUDNN=ON \
	-DCUTLASS_ENABLE_EXAMPLES=OFF \
	-DCUTLASS_INSTALL_TESTS=OFF
%cmake_build

%install
%cmake_install

%files headers
%doc *.md LICENSE.txt
%_includedir/%oname
%_includedir/cute
%_cmakedir/NvidiaCutlass

%changelog
* Thu Feb 26 2026 Nikita Shmatko <nash@altlinux.org> 4.3.1-alt1
- New version 4.3.1.
- Minor specfile fixes.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 4.2.1-alt1
- Initial build for Sisyphus.
