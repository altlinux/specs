%define oname arrex

Name: python3-module-arrex
Version: 0.5.2
Release: alt1

Summary: Python module allowing to create efficient dynamic arrays of user-defined types

Url: https://github.com/jimy-byerley/arrex
License: LGPL-3.0 AND GPL-3.0
Group: Development/Python3

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

%filter_from_requires /python3(glm)/d

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

Requires: python3(PyGLM)

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
* Thu Jul 25 2024 Ivan Mazhukin <vanomj@altlinux.org> 0.5.2-alt1
- Initial build for ALT Sisyphus

