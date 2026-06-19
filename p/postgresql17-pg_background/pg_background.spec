%define pg_ver 17
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_background
Version: 2.0.2
Release: alt1
Summary: Run SQL queries in background workers with autonomous transactions
License: PostgreSQL
Group: Databases
Url: https://github.com/vibhorkum/pg_background
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel
BuildRequires: libssl-devel libkrb5-devel

Requires: postgresql%pg_ver-server

%description
pg_background is a PostgreSQL extension that executes SQL commands in background
worker processes. Workers run inside the PostgreSQL server with their own
transactions, enabling asynchronous SQL execution without blocking the client
session, autonomous transactions that commit or roll back independently of the
caller, and an observable worker lifecycle with explicit launch, wait, cancel,
and detach semantics. Includes a v2 cookie-protected API, structured error returns,
worker labels, batch operations, and convenience helpers like pg_background_run_v2()
and pg_background_outcome_v2().

%prep
%setup

%build
%make_build PG_CONFIG=%_bindir/pg_server_config USE_PGXS=1

%install
%makeinstall_std PG_CONFIG=%_bindir/pg_server_config USE_PGXS=1

%files
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*
%doc LICENSE README.md CLAUDE.md docs

%changelog
* Fri Jun 19 2026 Alexei Takaseev <taf@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Jun 11 2026 Alexei Takaseev <taf@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
