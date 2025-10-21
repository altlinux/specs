%define pypi_name finch-tensor

%def_without check

Name:    python3-module-%pypi_name
Version: 0.2.14
Release: alt1

Summary: Sparse and Structured Tensor Programming in Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/finch-tensor
VCS:     https://github.com/finch-tensor/finch-tensor-python

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-sparse
BuildRequires: python3-module-scipy
BuildRequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.md
%python3_sitelibdir/finch
%python3_sitelibdir/finch_tensor-%version.dist-info

%changelog
* Tue Oct 21 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.14-alt1
- Automatically updated to 0.2.14.

* Thu Jul 03 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.12-alt1
- Initial build for Sisyphus
