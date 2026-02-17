%define _unpackaged_files_terminate_build 1

Name:    dlpack
Version: 1.2
Release: alt1

Summary: Common in-memory tensor structure 
License: Apache-2.0
Group:   Development/C
Url:     https://dmlc.github.io/dlpack/latest/
Vcs:     https://github.com/dmlc/dlpack

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++

%description
DLPack is an open in-memory tensor structure for sharing tensors
among frameworks. DLPack enables
  - Easier sharing of operators between deep learning frameworks.
  - Easier wrapping of vendor level operator implementations,
  allowing collaboration when introducing new devices/ops.
  - Quick swapping of backend implementations, like different version of BLAS
  - For final users, this could bring more operators, and possibility
  of mixing usage between frameworks.
We do not intend to implement Tensor and Ops, but instead use this
as common bridge to reuse tensor and ops across frameworks.

%package devel
Summary: Common in-memory tensor structure
Group: Development/C
Provides: %name = %EVR

%description devel
DLPack is an open in-memory tensor structure for sharing tensors
among frameworks. DLPack enables
  - Easier sharing of operators between deep learning frameworks.
  - Easier wrapping of vendor level operator implementations,
  allowing collaboration when introducing new devices/ops.
  - Quick swapping of backend implementations, like different version of BLAS
  - For final users, this could bring more operators, and possibility
  of mixing usage between frameworks.
We do not intend to implement Tensor and Ops, but instead use this
as common bridge to reuse tensor and ops across frameworks.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE *.md
%_includedir/%name/*.h
%_cmakedir/%name/*.cmake

%changelog
* Wed Nov 26 2025 Nikita Shmatko <nash@altlinux.org> 1.2-alt1
- Initial build for Sisyphus.
