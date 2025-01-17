%define _unpackaged_files_terminate_build 1
%define pypi_name starlette-testclient
%define mod_name starlette_testclient

%def_with check

Name:    python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary:   A backport of Starlette TestClient using requests
License:   BSD-3-Clause
Group:     Development/Python3
Url:       https://github.com/Kludex/starlette-testclient
Vcs:       https://github.com/Kludex/starlette-testclient.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests
BuildRequires: python3-module-starlette
BuildRequires: python3-module-trio
%endif

Requires: python3-module-starlette
Requires: python3-module-requests

%description
This is a backport of Starlette's TestClient using requests instead of httpx.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -W ignore::pytest.PytestUnraisableExceptionWarning

%files
%doc LICENSE README.*
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 03 2024 Martynenko Evgeniy <enimalojd@altlinux.org> 0.4.0-alt1
  - Initial build for ALT.
