%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-jupyter

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.1
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
BuildRequires: python3-module-jupyter_server
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
%pyproject_run_pytest -v

%files
%doc *.md LICENSE
%python3_sitelibdir/pytest_jupyter
%python3_sitelibdir/pytest_jupyter-%version.dist-info

%changelog
* Tue Apr 09 2024 Anton Vyatkin <toni@altlinux.org> 0.10.1-alt1
- New version 0.10.1.

* Wed Mar 13 2024 Anton Vyatkin <toni@altlinux.org> 0.9.1-alt1
- New version 0.9.1.

* Thu Feb 22 2024 Anton Vyatkin <toni@altlinux.org> 0.9.0-alt1
- New version 0.9.0.

* Wed Dec 06 2023 Anton Vyatkin <toni@altlinux.org> 0.8.0-alt1
- New version 0.8.0.

* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

