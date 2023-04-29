%define pypi_name sphinx-click

%def_with check

Name:    python3-module-%pypi_name
Version: 4.4.0
Release: alt1

Summary: A Sphinx plugin to automatically document click-based applications
License: MIT
Group:   Development/Python3
URL:     https://github.com/click-contrib/sphinx-click

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr

%if_with check
BuildRequires: python3-module-sphinx-tests
BuildRequires: python3-module-click
BuildRequires: python3-module-pytest-cov
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
export PBR_VERSION="%version"
%pyproject_build

%install
export PBR_VERSION="%version"
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.rst
%python3_sitelibdir/sphinx_click
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 4.4.0-alt1
- Initial build for Sisyphus.
