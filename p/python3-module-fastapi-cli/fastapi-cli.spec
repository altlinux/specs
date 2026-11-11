%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-cli
%define mod_name fastapi_cli
%def_with check

Name: python3-module-%pypi_name
Version: 0.0.32
Release: alt2

Summary: Run and manage FastAPI apps from the command line with FastAPI CLI
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-cli/
Vcs: https://github.com/fastapi/fastapi-cli
BuildArch: noarch

Source0: %name-%version.tar
Source1: clean_coverage.py

# Sisyphus has no python3-module-uvicorn+standard subpackage yet, so
# uvicorn[standard] is required as the plain uvicorn.
%pyproject_configure_with_runtime_filter 'uvicorn$'
Requires: python3-module-uvicorn

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
%if_with check
%pyproject_configure_with_check_filter 'uvicorn$'
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-fastapi-cloud-cli
BuildRequires: python3-module-httpx2
BuildRequires: python3-module-pytest-timeout
%endif
%pyproject_configure_pypi_package

%description
Run and manage FastAPI apps from the command line with FastAPI CLI.

FastAPI CLI is a command line program fastapi that you can use to serve
your FastAPI app, manage your FastAPI project, and more.

%pyproject_configure_pypi_subpackage standard
%pyproject_configure_pypi_subpackage standard-no-fastapi-cloud-cli
%pyproject_configure_pypi_subpackage new

%prep
%setup
%pyproject_setup_deps

%build
%pyproject_build

%install
%pyproject_install

%check
# Clean of the using coverage module, because we don't needs to it.
%SOURCE1 tests/
%pyproject_run_pytest --session-timeout=600 tests

%files
%doc README.* LICENSE
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 11 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.32-alt2
- Packaged the standard, standard-no-fastapi-cloud-cli and new extras.

* Thu Sep 03 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.32-alt1
- Updated to 0.0.32.

* Tue Feb 24 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.24-alt1
- Updated to 0.0.24.

* Mon Dec 29 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.20-alt1
- Updated to 0.0.20.

* Wed Dec 03 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.16-alt1
- Updated to 0.0.16.

* Tue Sep 23 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.13-alt1
- Updated to 0.0.13.

* Thu Sep 18 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.12-alt1
- Updated to 0.0.12.

* Tue Jul 08 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.8-alt1
- Updated to 0.0.8.

* Fri Dec 27 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.7-alt1
- Updated to 0.0.7.

* Mon Aug 05 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.5-alt1
- Updated to 0.0.5.

* Thu May 30 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.4-alt1
- 0.0.3 -> 0.0.4.

* Sun May 19 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.3-alt1
- Initial build for ALT Sisyphus.

