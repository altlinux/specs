%define pypi_name hatch-jupyter-builder

%def_with check

Name:    python3-module-%pypi_name
Version: 0.9.1
Release: alt3

Summary: A hatch plugin to help build Jupyter packages
License: BSD-3-Clause
Group:   Development/Python3
URL: https://pypi.org/project/hatch-jupyter-builder/
VCS: https://github.com/jupyterlab/hatch-jupyter-builder

BuildArch: noarch

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-build
BuildRequires: python3-module-pip
BuildRequires: python3-module-tomli_w
%endif

%description
This provides a build hook plugin for Hatch that adds a build step for use
with Jupyter packages.

%prep
%setup -n %pypi_name-%version
sed -i 's/, "--color=yes"//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
# Calls pip, requires internet
%pyproject_run_pytest -v -k 'not test_hatch_build' tests/

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/hatch_jupyter_builder/
%python3_sitelibdir/%{pyproject_distinfo hatch_jupyter_builder}

%changelog
* Wed Apr 15 2026 Anton Vyatkin <toni@altlinux.org> 0.9.1-alt3
- Fixed FTBFS.

* Tue Feb 24 2026 Stanislav Levin <slev@altlinux.org> 0.9.1-alt2
- NMU: fixed FTBFS (pytest 9).

* Sat Apr 13 2024 Anton Vyatkin <toni@altlinux.org> 0.9.1-alt1
- New version 0.9.1.

* Tue Sep 19 2023 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1.1
- NMU: fixed FTBFS (build 1.0).

* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
