%define pypi_name jupyter-builder

%def_with check

Name:    python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: Build tools for JupyterLab (and remixes)
License: BSD-3-Clause
Group:   Development/Python3
Url:     https://pypi.org/project/jupyter-builder
Vcs:     https://github.com/jupyterlab/jupyter-builder

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-nodejs-version
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-copier
BuildRequires: python3-module-jupyter_core
BuildRequires: git-core
%endif

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v --ignore=tests/test_tpl.py

%files
%doc README.*
%_bindir/%pypi_name
%_bindir/jlpm
%python3_sitelibdir/jupyter_builder
%python3_sitelibdir/jupyter_builder-%version.dist-info

%changelog
* Thu Jul 30 2026 Anton Vyatkin <toni@altlinux.org> 1.2.0-alt1
- New version 1.2.0.

* Thu Jul 23 2026 Anton Vyatkin <toni@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus.
