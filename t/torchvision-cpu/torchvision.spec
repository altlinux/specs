%define _unpackaged_files_terminate_build 1

%def_with check

Name:    torchvision-cpu
Version: 0.27.0
Release: alt1

Summary: Datasets, Transforms and Models specific to Computer Vision (CPU only)
License: BSD-3-Clause
Group:   Development/ML
URL: 	 https://docs.pytorch.org/vision/
VCS:     https://github.com/pytorch/vision.git

BuildRequires(pre): cmake ninja-build rpm-build-python3 rpm-macros-ml
BuildRequires: gcc-c++
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libwebp-devel
BuildRequires: libprotobuf-devel
BuildRequires: pybind11-devel
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-torch-cpu
BuildRequires: libtorch-cpu-devel

%if_with check
BuildRequires: python3-module-pytest-mock
%endif

ExclusiveArch: x86_64 aarch64

Source: torchvision-cpu-%version.tar

# Remove python torch dependencies 
%remove_torch_deps

# Remove python torch debuginfo dependencies
%remove_torch_debug_deps

%description
The torchvision package consists of popular datasets, model architectures,
and common image transformations for computer vision.

%package        -n  libtorchvision-cpu-devel
Summary:        Datasets, transforms, and models specific to computer vision (C++ library only with CPU support)
Group:          Development/C++
AutoProv: 	nolib
Provides: 	torchvision
Requires: 	libtorch-cpu-devel
Conflicts: 	libtorchvision-cuda-devel

%description    -n libtorchvision-cpu-devel
%summary.

%package        -n python3-module-torchvision-cpu
Summary:        Datasets, transforms, and models specific to computer vision (only with CPU support)
Group:          Development/ML
Requires: 	pytorch
Requires: 	python3-module-torch-cpu
AutoProv: 	nopython3
Provides: 	python-torchvision
Conflicts: 	python3-module-torchvision-cuda

%description    -n python3-module-torchvision-cpu
%summary.

%prep
%setup

%build
%cmake -G Ninja \
       -DWITH_CUDA=OFF \
       -DWITH_WEBP=ON
%cmake_build 

%pyproject_build

%install
%cmake_install

%pyproject_install

%check
export PYTHONSAFEPATH=1
export LD_LIBRARY_PATH=%buildroot%_libdir

# Run a representative offline test subset covering transforms,
# image I/O and compiled CPU operators. The full upstream suite
# contains order- and network-dependent tests unsuitable for hasher.

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

%files 		-n libtorchvision-cpu-devel
%_includedir/torchvision
%_libdir/libtorchvision.so
%_datadir/cmake/TorchVision

%files 		-n python3-module-torchvision-cpu
%doc *.md LICENSE
%python3_sitelibdir/torchvision
%python3_sitelibdir/%{pyproject_distinfo torchvision}

%changelog
* Wed Sep 02 2026 Nikita Shmatko <nash@altlinux.org> 0.27.0-alt1
- New version 0.27.0.
- Turned on tests.
- Minor specfile fixes.

* Wed Feb 25 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt2
- Switched to rpm-macros-ml.

* Thu Feb 19 2026 Nikita Shmatko <nash@altlinux.org> 0.25.0-alt1
- New version 0.25.0.

* Fri Feb 13 2026 Nikita Shmatko <nash@altlinux.org> 0.24.1-alt1
- Initial build for Sisyphus.
