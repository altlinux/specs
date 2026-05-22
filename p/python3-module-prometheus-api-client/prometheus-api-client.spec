%define _unpackaged_files_terminate_build 1
%define pypi_name prometheus-api-client
%define mod_name prometheus_api_client

%def_with check

Name: python3-module-%pypi_name
Version: 0.7.2
Release: alt1

Summary: A Python wrapper for the Prometheus http api and some tools for metrics processing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/prometheus-api-client/
Vcs: https://github.com/4n4nd/prometheus-api-client-python
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
%pyproject_builddeps_build
BuildRequires: rpm-build-pyproject
%if_with check
%add_pyproject_deps_check_filter sphinx
%add_pyproject_deps_check_filter sphinx-rtd-theme
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra all
%pyproject_builddeps_check
%endif

%description
A Python wrapper for the Prometheus http api and some tools for metrics
processing.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipenv Pipfile dev-packages
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vca ./tests \
    --ignore=tests/test_prometheus_connect.py

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/%mod_name/
%python3_sitelibdir_noarch/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir_noarch/tests/

%changelog
* Fri May 22 2026 Andrey Kuzma <kuzmaav@altlinux.org> 0.7.2-alt1
- Initial build for Sisyphus.
