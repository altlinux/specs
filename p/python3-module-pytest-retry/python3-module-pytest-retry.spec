%define _unpackaged_files_terminate_build 1
%define pypi_name pytest-retry
%define mod_name pytest_retry

%def_with check

Name: python3-module-%pypi_name
Version: 1.6.3
Release: alt1.gitbb465fff

Summary: A simple plugin for retrying flaky tests in CI environments
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pytest-retry/
Vcs: https://github.com/str0zzapreti/pytest-retry

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_check
%endif

%description
pytest-retry is a plugin for Pytest which adds the ability to retry flaky tests,
thereby improving the consistency of the test suite results.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync check tox tox.ini "testenv:{py39,py310,py311}"
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.* LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Jul 24 2024 Denis Rastyogin <gerben@altlinux.org> 1.6.3-alt1.gitbb465fff
- Initial build for ALT Sisyphus.
