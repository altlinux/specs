%define _unpackaged_files_terminate_build 1
%define pypi_name fastuuid

%def_with check

Name:    python3-module-%pypi_name
Version: 0.14.0
Release: alt1

Summary: FastUUID is a library which provides CPython bindings to Rust's UUID library
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/fastuuid/
VCS:     https://github.com/fastuuid/fastuuid

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel 
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-wheel 
BuildRequires: python3-module-maturin
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
%if_with check
BuildRequires: python3-module-pytest python3-module-hypothesis
%endif

Source0: %name-%version.tar
Source1: %name-vendor-%version.tar
Patch0:  %name-%version-alt.patch

%description
FastUUID is a Python library that provides CPython bindings 
to Rust's UUID implementation. 
It offers fast UUID generation and parsing while exposing
an API compatible with Python's standard uuid module.

%prep
%setup -q -a 1
%autopatch -p1
%rust_prep

%build
%pyproject_build

%install
%pyproject_install

%check
HYPOTHESIS_PROFILE=debug \
  %pyproject_run_pytest -q tests/test_uuid.py -k "not benchmark"

%files
%doc README.rst LICENSE
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Mar 31 2026 Matvey Pyanov <sen@altlinux.org> 0.14.0-alt1
- First build for Alt.
