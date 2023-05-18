%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-instafail
%define mod_name pytest_instafail

%def_with check

Name: python3-module-%pypi_name
Version: 0.5.0
Release: alt1
Summary: pytest plugin to show failures instantly
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/pytest-instafail
Vcs: https://github.com/pytest-dev/pytest-instafail
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
# pexpect
BuildRequires: /dev/pts
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%pypi_name is a plugin for pytest that shows failures and errors instantly
instead of waiting until the end of test session.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra

%files
%doc README.*
%python3_sitelibdir/%mod_name.py
%python3_sitelibdir/__pycache__/%mod_name.*.pyc
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
