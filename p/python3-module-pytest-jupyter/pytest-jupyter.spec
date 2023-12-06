%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-jupyter

%def_with check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: A pytest plugin for testing Jupyter libraries and extensions
License: BSD-3-Clause
Group:   Development/Python3
URL: https://pypi.org/project/pytest-jupyter/
VCS: https://github.com/jupyter-server/pytest-jupyter

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-jupyter_core
BuildRequires: python3-module-nbformat
BuildRequires: python3-module-ipykernel
BuildRequires: python3-module-pytest-timeout
%endif

%description
A set of pytest plugins for Jupyter libraries and extensions.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
sed -i '/pytest_jupyter.jupyter_server/d' tests/conftest.py
%pyproject_run_pytest --ignore=tests/test_jupyter_server.py

%files
%doc *.md LICENSE
%python3_sitelibdir/pytest_jupyter
%python3_sitelibdir/pytest_jupyter-%version.dist-info

%changelog
* Wed Dec 06 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

