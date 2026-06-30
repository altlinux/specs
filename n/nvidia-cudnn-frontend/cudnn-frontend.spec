%define _unpackaged_files_terminate_build 1
# Disable Python bindings: they depend on cuda-python
# and Python CUTLASS DSL, which have NVIDIA-specific licensing terms.
%def_without python

Name:    nvidia-cudnn-frontend
Version: 1.22.1
Release: alt1

Summary: cuDNN-frontend provides a c++ wrapper for the cudnn backend API and samples on how to use it
License: MIT
Group:   Development/C++
URL: 	 https://docs.nvidia.com/deeplearning/cudnn/frontend
VCS:     https://github.com/NVIDIA/cudnn-frontend.git

Source: nvidia-cudnn-frontend-%version.tar

Patch: 0001-added-flag-for-use-system-dlpack.patch 

ExclusiveArch: x86_64 aarch64

%if_with python
BuildRequires(pre): rpm-build-python3 rpm-macros-ml
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: pybind11-devel
%endif
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: nvidia-cuda-devel
BuildRequires: libcudnn-devel
BuildRequires: dlpack-devel

%description
The cuDNN Frontend is a C++ header-only library providing a modern,
object-oriented interface to the cuDNN backend API.
It simplifies the construction and execution of deep learning operations
by exposing a graph-based abstraction layer over the low-level cuDNN primitives.

%package 	-n cudnn-frontend-devel
Summary: 	cuDNN-frontend provides a c++ wrapper for the cudnn backend API and samples on how to use it
Group: 		Development/C++
Obsoletes: 	nvidia-cudnn-frontend < %EVR

%description 	-n cudnn-frontend-devel
The cuDNN Frontend is a C++ header-only library providing a modern,
object-oriented interface to the cuDNN backend API.
It simplifies the construction and execution of deep learning operations
by exposing a graph-based abstraction layer over the low-level cuDNN primitives.

%if_with python
%package 	-n python3-module-cudnn-frontend
%remove_torch_deps
Requires:      	pytorch
Summary:       	Python bindings for cuDNN frontend API 
Group: 	       	Development/Python

%description 	-n python3-module-cudnn-frontend
Python interface to the cuDNN Frontend library.
Provides access to cuDNN graph and backend APIs from Python,
enabling construction and execution of neural network operations
with fine-grained control over cuDNN execution plans.
%endif

%prep
%setup
%autopatch -p1

%build

%cmake   \
	-DCUDNN_FRONTEND_BUILD_TESTS=OFF \
	-DCUDNN_FRONTEND_BUILD_SAMPLES=OFF \
        -DCUDNN_FRONTEND_BUILD_PYTHON_BINDINGS=OFF

%cmake_build

%if_with python
%pyproject_build
%endif

%install

%cmakeinstall_std

%if_with python
%pyproject_install
%endif

%files 		-n cudnn-frontend-devel
%doc *.md LICENSE.txt
%_includedir/*
%_cmakedir/cudnn_frontend

%if_with python
%files 		-n python3-module-cudnn-frontend
%python3_sitelibdir/cudnn-frontend
%python3_sitelibdir/%{pyproject_distinfo %name}
%endif

%changelog
* Tue Jun 30 2026 Nikita Shmatko <nash@altlinux.org> 1.22.1-alt1
- New version 1.22.1.
- Renamed header-only package to cudnn-frontend-devel.
- Added URL.
- Disabled python module.

* Thu Mar 05 2026 Nikita Shmatko <nash@altlinux.org> 1.15.0-alt2
- Switched to rpm-macros-ml.
- Minor specfile fixes.

* Thu Feb 05 2026 Nikita Shmatko <nash@altlinux.org> 1.15.0-alt1
- Initial build for Sisyphus.
