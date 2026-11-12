%define _unpackaged_files_terminate_build 1
%define pypi_name logfire
# The wrapper distribution ships no code and has no tests of its own;
# the SDK test suite runs in python3-module-logfire-sdk.
%def_without check

Name: python3-module-%pypi_name
Version: 5.4.0
Release: alt1

Summary: Pydantic Logfire Python SDK and command-line interface
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logfire/
Vcs: https://github.com/pydantic/logfire
BuildArch: noarch

Source0: %name-%version.tar
Patch: %name-%version-alt.patch

# Upstream pins logfire-sdk to the same release, the metadata-generated
# dependency carries no version.
Requires: python3-module-logfire-sdk = %version

BuildRequires(pre): rpm-macros-pyproject >= 0.3.0
BuildRequires: rpm-build-pyproject
# No test source to discover: the wrapper has no tests of its own.
%pyproject_configure_without_autodiscovery
%pyproject_configure_pypi_package

%description
Logfire is an observability tool built on OpenTelemetry. Since 5.4.0
this distribution is a thin wrapper: it owns the logfire CLI launcher
and pulls in the SDK from the python3-module-logfire-sdk package.

# Each extra subpackage below requires the matching logfire-sdk one.
# Not packaged, their deps are missing from ALT: agent-sandboxes
# (pydantic-monty-client), datasets (pydantic-evals), dspy and litellm
# (openinference instrumentations).
%pyproject_configure_pypi_subpackage gateway
%pyproject_configure_pypi_subpackage system-metrics
%pyproject_configure_pypi_subpackage asgi
%pyproject_configure_pypi_subpackage wsgi
%pyproject_configure_pypi_subpackage aiohttp
%pyproject_configure_pypi_subpackage aiohttp-client
%pyproject_configure_pypi_subpackage aiohttp-server
%pyproject_configure_pypi_subpackage celery
%pyproject_configure_pypi_subpackage django
%pyproject_configure_pypi_subpackage fastapi
%pyproject_configure_pypi_subpackage flask
%pyproject_configure_pypi_subpackage httpx
%pyproject_configure_pypi_subpackage starlette
%pyproject_configure_pypi_subpackage litestar
%pyproject_configure_pypi_subpackage sqlalchemy
%pyproject_configure_pypi_subpackage asyncpg
%pyproject_configure_pypi_subpackage psycopg
%pyproject_configure_pypi_subpackage psycopg2
%pyproject_configure_pypi_subpackage pymongo
%pyproject_configure_pypi_subpackage redis
%pyproject_configure_pypi_subpackage requests
%pyproject_configure_pypi_subpackage mysql
%pyproject_configure_pypi_subpackage sqlite3
%pyproject_configure_pypi_subpackage urllib
%pyproject_configure_pypi_subpackage aws-lambda
%pyproject_configure_pypi_subpackage google-genai
%pyproject_configure_pypi_subpackage variables

%prep
%setup
%autopatch -p1
cd logfire
%pyproject_setup_deps
cd -

%build
cd logfire
%pyproject_build
cd -

%install
cd logfire
%pyproject_install
cd -

%files
%doc logfire/README.md logfire/LICENSE
%_bindir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 12 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.4.0-alt1
- Updated to 5.4.0.
- Repackaged as a thin wrapper with a CLI launcher whereas the SDK
  implementation was moved to new python3-module-logfire-sdk.

* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 5.1.1-alt1
- Initial build for ALT Sisyphus.
