%define oname arrex

Name: python3-module-arrex
Version: 0.5.4
Release: alt1

Summary: Python module allowing to create efficient dynamic arrays of user-defined types

Url: https://github.com/jimy-byerley/arrex
License: LGPL-3.0 AND GPL-3.0
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry
BuildRequires: python3-module-Cython

%description
Arrex is a module that allows to create typed arrays much like numpy.ndarray and array.array,
but resizeable and using any kind of element, not only numbers.
Its dtype system is extremely flexible and makes it ideal to work and share structured data with compiled code.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/*

%changelog
* Thu Sep 11 2025 Grigory Ustinov <grenka@altlinux.org> 0.5.4-alt1
- Build new version for python3.13.

* Mon May 26 2025 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1.1
- NMU: fixed FTBFS (PyGLM 2.8.2-alt1).

* Thu Jul 25 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.5.2-alt1
- Initial build for ALT Sisyphus

