%define _unpackaged_files_terminate_build 1
%define pypi_name clickhouse-connect
%define mod_name clickhouse_connect

%def_with check

Name: python3-module-%pypi_name
Version: 0.10.0
Release: alt1
Summary: ClickHouse Database Core Driver for Python, Pandas, and Superset
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/clickhouse-connect
Vcs: https://github.com/ClickHouse/clickhouse-connect

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-cython
BuildRequires: python3-devel

%if_with check
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-numpy
BuildRequires: python3-module-pyarrow
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-pandas
BuildRequires: python3-module-urllib3
BuildRequires: python3-module-pytz
BuildRequires: python3-module-lz4
BuildRequires: python3-module-zstandard
BuildRequires: python3-module-certifi
%endif

%description
A high performance core database driver
for connecting ClickHouse to Python, Pandas, and Superset.
ClickHouse Connect currently uses the ClickHouse HTTP interface
for maximum compatibility.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
rm -rf %mod_name
# disable integration tests (need running ClickHouse)
%pyproject_run_pytest -vra --ignore=tests/integration_tests --ignore=tests/unit_tests/test_driver

%files
%doc README.md LICENSE
%python3_sitelibdir/%mod_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jan 27 2026 Alexey Rodygin <alehandro@altlinux.org> 0.10.0-alt1
- Initial build for ALT Linux.
