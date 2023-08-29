%define _unpackaged_files_terminate_build 1
%define pypi_name databases

# tests require running DBMSs
%def_without check

Name: python3-module-%pypi_name
Version: 0.8.0
Release: alt1

Summary: Async database support for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/databases/
Vcs: https://github.com/encode/databases

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Databases gives you simple asyncio support for a range of databases.

It allows you to make queries using the powerful SQLAlchemy Core expression
language, and provides support for PostgreSQL, MySQL, and SQLite.

Databases is suitable for integrating against any async Web framework,
such as Starlette, Sanic, Responder, Quart, aiohttp, Tornado, or FastAPI.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_tox
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.md LICENSE.md CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 29 2023 Anton Zhukharev <ancieg@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Sat May 06 2023 Anton Zhukharev <ancieg@altlinux.org> 0.7.0-alt1
- New version.

* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Sun Aug 14 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.1-alt1
- initial build for Sisyphus

