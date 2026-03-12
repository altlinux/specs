%define _unpackaged_files_terminate_build 1

%define oname cudnn

%define dist_name %{oname}_frontend

Name:    nvidia-cudnn-frontend
Version: 1.15.0
Release: alt2

Summary: cuDNN-frontend provides a c++ wrapper for the cudnn backend API and samples on how to use it
License: MIT
Group:   Development/C++
Url:     https://github.com/NVIDIA/cudnn-frontend

Source: %name-%version.tar

Patch: 0001-added-flag-for-use-system-dlpack.patch 

ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-build-python3 rpm-macros-ml
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: nvidia-cuda-devel
BuildRequires: libcudnn-devel
BuildRequires: dlpack-devel
BuildRequires: pybind11-devel


%description
The cuDNN Frontend is a C++ header-only library providing a modern,
object-oriented interface to the cuDNN backend API.
It simplifies the construction and execution of deep learning operations
by exposing a graph-based abstraction layer over the low-level cuDNN primitives.

%package -n python3-module-%name
%remove_torch_deps
Requires:      pytorch
Summary:       Python bindings for cuDNN frontend API 
Group: 	       Development/Python

%description -n python3-module-%name
Python interface to the cuDNN Frontend library.
Provides access to cuDNN graph and backend APIs from Python,
enabling construction and execution of neural network operations
with fine-grained control over cuDNN execution plans.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

# Move header files into /usr/include
install -d %buildroot%_includedir
find %buildroot%python3_sitelibdir/include -type f -exec sh -c '
  root="$1"
  dst="$2"
  shift 2
  for f; do
    rel="${f#"$root"/}"
    install -Dm0644 "$f" "$dst/$rel"
    rm -f "$f"
  done
' sh %buildroot%python3_sitelibdir/include %buildroot%_includedir {} +

%files
%doc *.md LICENSE.txt
%_includedir/*

%files -n python3-module-%name
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %name}


%changelog
* Thu Mar 05 2026 Nikita Shmatko <nash@altlinux.org> 1.15.0-alt2
- Switched to rpm-macros-ml.
- Minor specfile fixes.

* Thu Feb 05 2026 Nikita Shmatko <nash@altlinux.org> 1.15.0-alt1
- Initial build for Sisyphus.
