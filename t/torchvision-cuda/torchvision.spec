%define _unpackaged_files_terminate_build 1

# Delete compute_110 from CUDA_ARCH_LIST_CMAKE because of
# nvcc fatal : Unsupported gpu architecture 'compute_110'
%define CUDA_ARCH_LIST "7.5;8.0;8.6;8.7;8.9;9.0;10.0;10.3;12.0;12.1;12.1+PTX"

%def_with check

Name:    torchvision-cuda
Version: 0.27.0
Release: alt1

Summary: Datasets, Transforms and Models specific to Computer Vision
License: BSD-3-Clause
Group:   Development/ML
URL: 	 https://docs.pytorch.org/vision
VCS:     https://github.com/pytorch/vision.git

%set_gcc_version 14

BuildRequires(pre): cmake ninja-build rpm-build-python3 rpm-macros-ml
BuildRequires: gcc%_gcc_version-c++
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libwebp-devel
BuildRequires: nvidia-cuda-devel nvidia-cuda-devel-static
BuildRequires: libcudnn-devel
BuildRequires: libprotobuf-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-torch-cuda
BuildRequires: libtorch-cuda-devel

%if_with check
BuildRequires: python3-module-pytest-mock
%endif

ExclusiveArch: x86_64 aarch64

Source: torchvision-cuda-%version.tar

# Remove python torch dependencies 
%remove_torch_deps

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package        -n  libtorchvision-cuda-devel
Summary:        Datasets, transforms, and models specific to computer vision (C++ library only with GPU support)
Group:          Development/C++
AutoProv:       nolib
Provides:       torchvision
Requires:       libtorch-cuda-devel

%description    -n libtorchvision-cuda-devel
%summary.

%package        -n python3-module-torchvision-cuda
Summary:        Datasets, transforms, and models specific to computer vision (with GPU support)
Group:          Development/ML
AutoProv:       nopython3
Provides:       python-torchvision
Requires:       pytorch
Requires:       python3-module-torch-cuda

%description    -n python3-module-torchvision-cuda
%summary.

%prep
%setup

%build
export CC=gcc
export CXX=g++
%cmake -G Ninja \
       -DWITH_CUDA=ON \
       -DWITH_WEBP=ON \
       -DTORCH_CUDA_ARCH_LIST=%CUDA_ARCH_LIST
%cmake_build 

export FORCE_CUDA=1
export TORCH_CUDA_ARCH_LIST=%CUDA_ARCH_LIST 
%pyproject_build

%install
%cmake_install

%pyproject_install

%check
export PYTHONSAFEPATH=1
export LD_LIBRARY_PATH=%buildroot%_libdir

# Run a stable offline subset covering shared transforms, image I/O
# and compiled operators. CUDA device tests cannot run without a GPU,
%pyproject_run_pytest \
    test/test_functional_tensor.py \
    test/test_transforms.py \
    test/test_transforms_v2.py \
    -k perspective

%ifarch aarch64
# Known aarch64-only float32 mismatch in rotated box IoU
# for the XYXYXYXY input format (upstream # 9499).
%pyproject_run_pytest \
    test/test_image.py \
    test/test_io.py \
    test/test_ops.py \
    -k 'not test_decode_gif' \
    --deselect='test/test_ops.py::TestRotatedBoxIou::test_iou[xyxyxyxy-dtype0-cpu]'
%else
%pyproject_run_pytest \
    test/test_image.py \
    test/test_io.py \
    test/test_ops.py \
    -k 'not test_decode_gif'
%endif


%files          -n libtorchvision-cuda-devel
%_includedir/torchvision
%_libdir/libtorchvision.so
%_datadir/cmake/TorchVision

%files          -n python3-module-torchvision-cuda
%doc *.md LICENSE
%python3_sitelibdir/torchvision
%python3_sitelibdir/%{pyproject_distinfo torchvision}

%changelog
* Wed Sep 02 2026 Nikita Shmatko <nash@altlinux.org> 0.27.0-alt1
- New version 0.27.0.
- Turned on tests.
- Minor specfile fixes.

* Mon Jul 13 2026 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.25.0-alt3
- Switched to GCC 14 as the current cuda toolchain doesn't support GCC 15+.
- Excluded aarch64 build as there is no python3-module-torch-cuda on aarch64.

* Tue Mar 03 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt2
- Switched to rpm-macros-ml.
- Build torchvision-cuda on aarch64.

* Thu Feb 19 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt1
- New version 0.25.0.

* Wed Jan 28 2026 Nikita Shmatko <nash@altlinux.org> 0.24.1-alt1
- Initial build for Sisyphus.
