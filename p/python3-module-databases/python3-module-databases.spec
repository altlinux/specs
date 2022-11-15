%define _unpackaged_files_terminate_build 1
%define pypi_name databases

# tests require running DBMSs
%def_without check

Name: python3-module-%pypi_name
Version: 0.6.2
Release: alt1

Summary: Async database support for Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/databases

Source0: %name-%version.tar
Patch0: databases-0.6.2-alt-fix_breaking_changes_in_sqlalchemy_cursor.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
%endif

BuildArch: noarch

%description
Databases gives you simple asyncio support for a range of databases.

It allows you to make queries using the powerful SQLAlchemy Core expression
language, and provides support for PostgreSQL, MySQL, and SQLite.

Databases is suitable for integrating against any async Web framework,
such as Starlette, Sanic, Responder, Quart, aiohttp, Tornado, or FastAPI.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md LICENSE.md CHANGELOG.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Nov 15 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.2-alt1
- 0.6.1 -> 0.6.2

* Sun Aug 14 2022 Anton Zhukharev <ancieg@altlinux.org> 0.6.1-alt1
- initial build for Sisyphus

