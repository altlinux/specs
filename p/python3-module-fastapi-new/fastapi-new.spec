%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-new
%define module_name fastapi_new

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.7
Release: alt1

Summary: Create a new FastAPI project in one command
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-new/
Vcs: https://github.com/fastapi/fastapi-new
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: clean_coverage_usage.py
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: uv
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup tests
%endif

# Clean up the coverage module usage, as we don't need it.
%SOURCE2 tests/

%build
%pyproject_build

%install
%pyproject_install

%check
export UV_SYSTEM_PYTHON=true
export UV_FROZEN=true
export UV_OFFLINE=true
%pyproject_run_pytest

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Jul 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.7-alt1
- Updated to 0.0.7.

* Tue Apr 07 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.6-alt1
- Updated to 0.0.6.

* Thu Mar 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.5-alt1
- Initial build for ALT Sisyphus.
