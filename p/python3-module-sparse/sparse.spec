%define pypi_name sparse

%ifnarch %ix86 aarch64
%def_with check
%else
%def_without check
%endif

Name:    python3-module-%pypi_name
Version: 0.15.4
Release: alt1

Summary: Sparse multi-dimensional arrays for the PyData ecosystem

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/sparse
VCS:     https://github.com/pydata/sparse

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numba
BuildRequires: python3-module-scipy
BuildRequires: python3-module-dask
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
This module implements sparse multidimensional arrays on top of NumPy and
Scipy.sparse. It generalizes the scipy.sparse.coo_matrix layout, but
extends beyond just rows and columns to an arbitrary number of
dimensions.

The original motivation is for machine learning algorithms, but it is
intended for somewhat general use.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 12 2024 Grigory Ustinov <grenka@altlinux.org> 0.15.4-alt1
- Initial build for Sisyphus.
