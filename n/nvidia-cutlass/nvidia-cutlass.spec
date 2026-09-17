%define _unpackaged_files_terminate_build 1

Name:    nvidia-cutlass
Version: 4.4.2
Release: alt2

Summary: CUDA Templates and Python DSLs for High-Performance Linear Algebra
License: BSD-3-Clause
Group:   Development/Other
Url:     https://docs.nvidia.com/cutlass/index.html
Vcs:     https://github.com/NVIDIA/cutlass.git

Source: nvidia-cutlass-%version.tar

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-python3 cmake rpm-build-ninja rpm-macros-cuda-toolkit
%set_gcc_version %cuda_gcc_version
BuildRequires: %cuda_buildreq
BuildRequires: python3-module-setuptools python3-module-wheel
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
export CUDACXX=%_bindir/nvcc

%cmake -GNinja %cuda_cmake_flags \
	-DCUTLASS_ENABLE_HEADERS_ONLY=ON \
	-DCUTLASS_NVCC_ARCHS="%(echo %cuda_archs | tr ' ' ';')" \
	-DCUTLASS_ENABLE_GTEST_UNIT_TESTS=OFF \
	-DCUTLASS_ENABLE_TESTS=OFF \
	-DCUTLASS_ENABLE_CUBLAS=ON \
	-DCUTLASS_ENABLE_CUDNN=ON \
	-DCUTLASS_ENABLE_EXAMPLES=OFF \
	-DCUTLASS_INSTALL_TESTS=OFF
%cmake_build

%install
%cmake_install

%files headers
%doc *.md LICENSE.txt
%_includedir/cutlass
%_includedir/cute
%_cmakedir/NvidiaCutlass

%changelog
* Tue Sep 15 2026 Mikhail Tergoev <fidel@altlinux.org> 4.4.2-alt2
- Use rpm-macros-cuda-toolkit for host compiler and CUDA architectures.

* Fri Jun 26 2026 Nikita Shmatko <nash@altlinux.org> 4.4.2-alt1
- Updated version to 4.4.2.
- Switched from clang-20 to gcc-14 to fix build with glibc 2.43.

* Thu Feb 26 2026 Nikita Shmatko <nash@altlinux.org> 4.3.1-alt1
- New version 4.3.1.
- Minor specfile fixes.

* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 4.2.1-alt1
- Initial build for Sisyphus.
