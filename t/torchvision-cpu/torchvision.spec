%define _unpackaged_files_terminate_build 1

%define pypi_name vision

%define rname torch%pypi_name

# Delete compute_110 from CUDA_ARCH_LIST_CMAKE because of
# nvcc fatal : Unsupported gpu architecture 'compute_110'
%define CUDA_ARCH_LIST "7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.3;12.0;12.1;12.1+PTX"
%define CUDA_ARCH_LIST_CMAKE "75;80;86;87;89;90;100;103;120;121;121-virtual"

%def_without check

Name:    %rname-cpu
Version: 0.25.0
Release: alt2

Summary: Datasets, Transforms and Models specific to Computer Vision (CPU only)
License: BSD-3-Clause
Group:   Development/ML
URL: 	 https://docs.pytorch.org/vision/
VCS:     https://github.com/pytorch/vision.git

BuildRequires(pre): cmake ninja-build rpm-build-python3 rpm-macros-ml
BuildRequires: gcc-c++
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-torch-cpu-devel

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

# Remove python torch dependencies 
%remove_torch_deps

# Remove python torch debuginfo dependencies
%remove_torch_debug_deps

Conflicts: 	%rname-cpu

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package        -n  lib%rname-cpu-devel
Summary:        Datasets, transforms, and models specific to computer vision (C++ library only with CPU support)
Group:          Development/C++
AutoProv: 	nolib
Provides: 	lib%rname-cpu = %EVR
Provides: 	torchvision
Requires: 	pytorch
Conflicts: 	lib%rname-cuda-devel
Conflicts: 	lib%rname-cuda

%description    -n lib%rname-cpu-devel
%summary.

%package        -n python3-module-%rname-cpu
Summary:        Datasets, transforms, and models specific to computer vision (only with CPU support)
Group:          Development/ML
Requires: 	pytorch
AutoProv: 	nopython3
Provides: 	python-torchvision
Conflicts: 	python3-module-%rname-cuda

%description    -n python3-module-%rname-cpu
%summary.

%prep
%setup

%build
%cmake -G Ninja \
       -DTorch_DIR=%_torchdir \
       -DWITH_CUDA=OFF \
       -DTORCHVISION_USE_FFMPEG=ON \
       -DTORCHVISION_USE_WEBP=ON \
       -DTORCH_CUDA_ARCH_LIST=%CUDA_ARCH_LIST \
       -DCUDA_ARCH_LIST=%CUDA_ARCH_LIST \
       -DCMAKE_CUDA_ARCHITECTURES=%CUDA_ARCH_LIST_CMAKE
%cmake_build 

export FORCE_CUDA=0
export TORCH_CUDA_ARCH_LIST=%CUDA_ARCH_LIST 
%pyproject_build

%install
%cmake_install

%pyproject_install

%files 		-n lib%rname-cpu-devel
%_includedir/%rname
%_libdir/lib%rname.so
%_datadir/cmake

%files 		-n python3-module-%rname-cpu
%doc *.md LICENSE
%python3_sitelibdir/%rname
%python3_sitelibdir/%{pyproject_distinfo %rname}

%changelog
* Wed Feb 25 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt2
- Switched to rpm-macros-ml.

* Thu Feb 19 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt1
- New version 0.25.0.

* Fri Feb 13 2026 Nikita Shmatko <nash@altlinux.org> 0.24.1-alt1
- Initial build for Sisyphus.
