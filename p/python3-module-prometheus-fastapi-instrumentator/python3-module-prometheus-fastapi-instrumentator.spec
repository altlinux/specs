%define _unpackaged_files_terminate_build 1
%define pypi_name prometheus-fastapi-instrumentator
%define mod_name prometheus_fastapi_instrumentator

%def_with check

Name: python3-module-%pypi_name
Version: 8.0.2
Release: alt1

Summary: Instrument your FastAPI with Prometheus metrics
License: ISC
Group: Development/Python3
Url: https://pypi.org/project/prometheus-fastapi-instrumentator/
Vcs: https://github.com/trallnag/prometheus-fastapi-instrumentator

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

# manually manage runtime dependencies with metadata
AutoReq: yes, nopython3
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter devtools
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-httpx
%endif

%description
A configurable and modular Prometheus Instrumentator for your FastAPI.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Remove 'devtools' requirement
sed -i 's/^from devtools import debug$/debug = print/' tests/conftest.py
sed -i '/HELP process_cpu_seconds_total/d' tests/test_instrumentation.py
%pyproject_run_pytest -vra

%files
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jun 24 2026 Anton Zhukharev <ancieg@altlinux.org> 8.0.2-alt1
- Updated to 8.0.2.

* Mon Jun 08 2026 Anton Zhukharev <ancieg@altlinux.org> 8.0.0-alt1
- Packaged for ALT Sisyphus.
