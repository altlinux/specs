%define _unpackaged_files_terminate_build 1

%define pypi_name pytest-sourceorder
%define mname pytest_sourceorder
%def_with check

Name: python3-module-%mname
Version: 0.6.0
Release: alt2
Summary: A pytest plugin for ensuring tests within a class are run in source order
License: GPL-3.0-only
Group: Development/Python3
Url: https://pypi.org/project/pytest-sourceorder
Vcs: https://pagure.io/python-pytest-sourceorder
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# PyPI name
%py3_provides %pypi_name
Provides: python3-module-%pypi_name = %EVR
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%endif

%description
Allows tests within a specially marked class to be run in source order,
instead of the "almost alphabetical" order Pytest normally uses.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%check
%pyproject_run_pytest -vra

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%python3_sitelibdir/%mname.py
%python3_sitelibdir/__pycache__/%mname.*.py*

%changelog
* Fri Jan 26 2024 Stanislav Levin <slev@altlinux.org> 0.6.0-alt2
- Fixed FTBFS (Python 3.12).

* Fri Dec 03 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- 0.5.1 -> 0.6.0.

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 0.5.1-alt2
- Stopped Python2 package build.

* Mon Jul 23 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1
- 0.4 -> 0.5.1
- Build package for Python3

* Tue Dec 29 2015 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Initial build.

