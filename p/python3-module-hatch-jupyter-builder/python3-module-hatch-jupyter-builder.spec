%define pypi_name hatch-jupyter-builder

%def_with check

Name:    python3-module-%pypi_name
Version: 0.8.3
Release: alt1.1

Summary: A hatch plugin to help build Jupyter packages
License: BSD-3-Clause
Group:   Development/Python3
URL: https://pypi.org/project/hatch-jupyter-builder/
VCS: https://github.com/jupyterlab/hatch-jupyter-builder

BuildArch: noarch

Source: %pypi_name-%version.tar
Patch: hatch-test-nonisolated.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-build
BuildRequires: python3-module-pip
BuildRequires: python3-module-tomli
%endif

%description
This provides a build hook plugin for Hatch that adds a build step for use
with Jupyter packages.

%prep
%setup -n %pypi_name-%version
%patch -p0
sed -i 's/--color=yes//' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%pyproject_run_pytest

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/hatch_jupyter_builder/
%python3_sitelibdir/%{pyproject_distinfo hatch_jupyter_builder}

%changelog
* Tue Sep 19 2023 Stanislav Levin <slev@altlinux.org> 0.8.3-alt1.1
- NMU: fixed FTBFS (build 1.0).

* Fri Jun 02 2023 Anton Vyatkin <toni@altlinux.org> 0.8.3-alt1
- Initial build for Sisyphus
