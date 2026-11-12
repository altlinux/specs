%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-new
%define module_name fastapi_new

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.9
Release: alt1

Summary: Create a new FastAPI project in one command
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-new/
Vcs: https://github.com/fastapi/fastapi-new
BuildArch: noarch

Source0: %name-%version.tar
Source1: clean_coverage_usage.py
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
BuildRequires: uv
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

# Clean up the coverage module usage, as we don't need it.
%SOURCE1 tests/

%build
%pyproject_build

%install
%pyproject_install

%check
export UV_SYSTEM_PYTHON=true
export UV_FROZEN=true
export UV_OFFLINE=true
# These tests install fastapi[standard] into the generated project with uv,
# which needs network access (and Python 3.12 and 3.11 for the first one).
%pyproject_run_pytest --session-timeout=600 \
    --deselect=tests/test_new.py::test_creates_project_with_python_version \
    --deselect=tests/test_new.py::test_runs_project_with_current_python

%files
%doc LICENSE README.md
%_bindir/%pypi_name
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.9-alt1
- Updated to 0.0.9.

* Wed Jul 01 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.7-alt1
- Updated to 0.0.7.

* Tue Apr 07 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.6-alt1
- Updated to 0.0.6.

* Thu Mar 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.5-alt1
- Initial build for ALT Sisyphus.
