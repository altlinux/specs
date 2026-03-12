%define _unpackaged_files_terminate_build 1

%define pypi_name vision

%define rname torch%pypi_name

# Delete compute_110 from CUDA_ARCH_LIST_CMAKE because of
# nvcc fatal : Unsupported gpu architecture 'compute_110'
%define CUDA_ARCH_LIST "7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.3;12.0;12.1;12.1+PTX"
%define CUDA_ARCH_LIST_CMAKE "75;80;86;87;89;90;100;103;120;121;121-virtual"

%def_without check

Name:    %rname-cuda
Version: 0.25.0
Release: alt2

Summary: Datasets, Transforms and Models specific to Computer Vision
License: BSD-3-Clause
Group:   Development/ML
URL: 	 https://docs.pytorch.org/vision
VCS:     https://github.com/pytorch/vision.git

BuildRequires(pre): cmake ninja-build rpm-build-python3 rpm-macros-ml
BuildRequires: gcc-c++
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: nvidia-cuda-devel nvidia-cuda-devel-static
BuildRequires: libcudnn-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-torch-cuda-devel

ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar

# Remove python torch dependencies 
%remove_torch_deps

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package        -n  lib%rname-cuda-devel
Summary:        Datasets, transforms, and models specific to computer vision (C++ library only with GPU support)
Group:          Development/C++
AutoProv: 	nolib
Provides: 	lib%rname-cuda = %EVR
Provides: 	torchvision
Requires: 	pytorch
Requires: 	python3-module-torch-cuda

%description    -n lib%rname-cuda-devel
%summary.

%package        -n python3-module-%rname-cuda
Summary:        Datasets, transforms, and models specific to computer vision (with GPU support)
Group:          Development/ML
AutoProv: 	nopython3
Provides:	python-torchvision
Requires: 	pytorch
Requires: 	python3-module-torch-cuda

%description    -n python3-module-%rname-cuda
%summary.

%prep
%setup

%build
%cmake -G Ninja \
       -DTorch_DIR=%_torchdir \
       -DWITH_CUDA=ON \
       -DUSE_CUDNN=ON \
       -DTORCHVISION_USE_FFMPEG=ON \
       -DTORCHVISION_USE_WEBP=ON \
       -DTORCH_CUDA_ARCH_LIST=%CUDA_ARCH_LIST \
       -DCUDA_ARCH_LIST=%CUDA_ARCH_LIST \
       -DCMAKE_CUDA_ARCHITECTURES=%CUDA_ARCH_LIST_CMAKE
%cmake_build 

export FORCE_CUDA=1
export TORCH_CUDA_ARCH_LIST=%CUDA_ARCH_LIST 
%pyproject_build

%install
%cmake_install

%pyproject_install

%files 		-n lib%rname-cuda-devel
%_includedir/%rname
%_libdir/lib%rname.so
%_datadir/cmake

%files 		-n python3-module-%rname-cuda
%doc *.md LICENSE
%python3_sitelibdir/%rname
%python3_sitelibdir/%{pyproject_distinfo %rname}

%changelog
* Tue Mar 03 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt2
- Switched to rpm-macros-ml.
- Build torchvision-cuda on aarch64.

* Thu Feb 19 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt1
- New version 0.25.0.

* Wed Jan 28 2026 Nikita Shmatko <nash@altlinux.org> 0.24.1-alt1
- Initial build for Sisyphus.
