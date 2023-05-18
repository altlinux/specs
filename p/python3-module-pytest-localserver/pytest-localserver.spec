%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-localserver

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1
Summary: pytest plugin to test server connections locally
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-localserver
VCS: https://github.com/pytest-dev/pytest-localserver.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%pypi_name is a plugin for the pytest testing framework which enables
you to test server connections locally.

%prep
%setup
%autopatch -p1
%pyproject_scm_init
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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst
%python3_sitelibdir/pytest_localserver/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 18 2023 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1
- 0.7.0 -> 0.7.1.

* Fri Sep 30 2022 Stanislav Levin <slev@altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus.
