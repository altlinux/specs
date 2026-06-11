%define _unpackaged_files_terminate_build 1

%define appname sqlit
%define pypi_name %appname-tui
%define mod_name %{appname}_tui
%def_with check

Name: %pypi_name
Version: 1.5.1
Release: alt1

Summary: Connect and query your database from your terminal in seconds
Group: Development/Databases
License: MIT
Url: https://github.com/Maxteabag/sqlit
VCS: https://github.com/Maxteabag/sqlit.git

BuildArch: noarch

# Source-url: https://github.com/Maxteabag/%appname/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-pytest-asyncio
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A user friendly TUI for SQL databases. Written in python. Supports SQL
server, Mysql, PostreSQL, SQLite, Turso and more.

Supports all major databases: SQL Server, PostgreSQL, MySQL, SQLite,
MariaDB, FirebirdSQL, Oracle, DuckDB, CockroachDB, ClickHouse,
Snowflake, Supabase, CloudFlare D1, Turso, Athena, BigQuery, Spanner,
RedShift, IBM Db2, SAP HANA, Teradata, Trino, Presto and Apache Flight
SQL.

%prep
%setup
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_install

%check
%pyproject_run_pytest -v -k "\
not test_pending_query_set_before_connecting"

%files
%doc README.md
%_bindir/%appname
%_bindir/%pypi_name
%python3_sitelibdir_noarch/%appname/
%python3_sitelibdir_noarch/%{pyproject_distinfo %mod_name}

%changelog
* Thu Jun 11 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.5.1-alt1
- new version

* Wed May 27 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.5.0-alt1
- new version

* Tue Apr 21 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.4.0-alt2
- update

* Mon Apr 20 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.4.0-alt1
- new version

* Wed Apr 08 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.3.1.1-alt1
- initial build for ALT Linux
