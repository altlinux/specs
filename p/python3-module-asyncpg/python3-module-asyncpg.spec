%define _unpackaged_files_terminate_build 1
%define pypi_name asyncpg

%def_without check

Name: python3-module-%pypi_name
Version: 0.26.0
Release: alt1

Summary: A fast PostgreSQL Database Client Library for Python/asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/asyncpg

Source0: %name-%version.tar
Source1: submodules.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: python3(cython)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(flake8)
%endif

%description
asyncpg is a database interface library designed specifically for PostgreSQL
and Python/asyncio. asyncpg is an efficient, clean implementation of PostgreSQL
server binary protocol for use with Python's asyncio framework.

asyncpg requires Python 3.6 or later and is supported for PostgreSQL
versions 9.5 to 14. Older PostgreSQL versions or other databases implementing
the PostgreSQL protocol may work, but are not being actively tested.

%prep
%setup -a1

%build
%pyproject_build

%install
%pyproject_install

%check
# tests require running postgresql, so they are disables
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.rst LICENSE AUTHORS
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sun Aug 07 2022 Anton Zhukharev <ancieg@altlinux.org> 0.26.0-alt1
- initial build for Sisyphus

