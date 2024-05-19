%define _unpackaged_files_terminate_build 1
%define pypi_name fastapi-cli
%define mod_name fastapi_cli

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.3
Release: alt1

Summary: Run and manage FastAPI apps from the command line with FastAPI CLI
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/fastapi-cli/
Vcs: https://github.com/tiangolo/fastapi-cli

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Source2: clean_coverage.py

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
# Package python3-module-fastapi assumes fastapi-slim provides
%add_pyproject_deps_check_filter fastapi-slim$
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Run and manage FastAPI apps from the command line with FastAPI CLI.

FastAPI CLI is a command line program fastapi that you can use to serve
your FastAPI app, manage your FastAPI project, and more.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync check pip_reqfile requirements-tests.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
# Clean of the using coverage module, because we don't needs to it.
%SOURCE2 tests/
%pyproject_run_pytest tests

%files
%doc README.* LICENSE
%_bindir/fastapi
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun May 19 2024 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.3-alt1
- Initial build for ALT Sisyphus.

