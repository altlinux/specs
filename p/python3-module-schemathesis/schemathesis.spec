%define _unpackaged_files_terminate_build 1
%define pypi_name schemathesis

%def_with check

Name:    python3-module-%pypi_name
Version: 3.39.9
Release: alt1

Summary:   Property-based testing framework for Open API and GraphQL based apps
License:   MIT
Group:     Development/Python3
Url:       https://schemathesis.readthedocs.io
VCS:       https://github.com/schemathesis/schemathesis.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-backoff
BuildRequires: python3-module-harfile
BuildRequires: python3-module-starlette
BuildRequires: python3-module-starlette-testclient
BuildRequires: python3-module-pytest-subtests
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-httpserver
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-trio
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-syrupy
BuildRequires: curl
BuildRequires: python3-module-aiohttp
BuildRequires: python3-module-aiohttp-tests
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-flask
BuildRequires: python3-module-httpx
BuildRequires: python3-module-tomli
BuildRequires: python3-module-tomli_w
BuildRequires: python3-module-junit-xml
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-hypothesis-jsonschema
BuildRequires: python3-module-hypothesis-graphql
BuildRequires: python3-module-hypothesis-openapi
BuildRequires: python3-module-pyrate-limiter
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-trustme
BuildRequires: python3-module-yarl
BuildRequires: python3-module-click
BuildRequires: python3-module-strawberry-graphql
BuildRequires: python3-module-colorama
BuildRequires: python3-module-pyyaml
BuildRequires: python3-module-requests
BuildRequires: python3-module-werkzeug
BuildRequires: python3-module-jsonschema
#Added because the package jsonschema is built in the repository without optional dependencies.
BuildRequires: python3-module-rfc3339-validator
%endif

Requires: python3-module-backoff
Requires: python3-module-pyrate-limiter
Requires: python3-module-httpx

%description
Schemathesis is an API testing tool that automatically
finds crashes and validates spec compliance.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest test/

%files
%doc LICENSE README.*
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%_bindir/%pypi_name
%_bindir/st

%changelog
* Mon Feb 03 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.9-alt1
  - New version 3.39.9

* Mon Jan 27 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.8-alt1
  - New version 3.39.8

* Fri Jan 17 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.7-alt1
  - New version 3.39.7
  - Fix missing runtime dependencies

* Thu Jan 09 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 3.39.5-alt1
  - Initial build for ALT.
