%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-cloud-cli
%define module_name fastapi_cloud_cli
%def_with check

Name: python3-module-%pypi_name
Version: 0.27.1
Release: alt1

Summary: Deploy and manage FastAPI Cloud apps from the command line
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-cloud-cli/
Vcs: https://github.com/fastapilabs/fastapi-cloud-cli
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

# Sisyphus has no python3-module-uvicorn+standard subpackage yet, so
# uvicorn[standard] is required as the plain uvicorn.
%pyproject_configure_with_runtime_filter 'uvicorn$'
Requires: python3-module-uvicorn

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
%pyproject_configure_with_check_filter 'uvicorn$'
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest-timeout
BuildRequires: git
%endif
%pyproject_configure_pypi_package

%description
%summary.

%pyproject_configure_pypi_subpackage standard

%prep
%setup
%autopatch -p1
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
# tests/utils.py SnapshotCliRunner pins COLUMNS=80 for every invocation,
# so the default temp root (/usr/src/tmp/pytest-of-builder/...) is too long:
# Rich wraps the printed file name mid-word and
# test_create_token_human_output_does_not_print_token_value fails.
# Keep the temp root short so the paths fit into 80 columns.
%pyproject_run_pytest --session-timeout=600 --basetemp=/tmp/pytest

%files
%doc README.md LICENSE
%python3_sitelibdir/%module_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Nov 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.27.1-alt1
- Updated to 0.27.1.

* Fri Sep 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.26.0-alt1
- Updated to 0.26.0.

* Thu Sep 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.24.0-alt1
- Initial build for ALT Sisyphus.
