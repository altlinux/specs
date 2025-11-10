%define pg_ver 13
%def_with jit

Name: postgresql%pg_ver-pg_hint_plan
Version: 1.3.11
Release: alt1

Summary: pg_hint_plan makes it possible to tweak PostgreSQL execution plans using so-called "hints" in SQL comments
License: BSD and PostgreSQL
Group: Databases
Url: https://github.com/ossc-db/pg_hint_plan

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
`pg_hint_plan` makes it possible to tweak PostgreSQL execution plans using
so-called "hints" in SQL comments, like `/*+ SeqScan(a) */`.

PostgreSQL uses a cost-based optimizer, that uses data statistics, not static
rules.  The planner (optimizer) estimates costs of each possible execution
plans for a SQL statement, then executes the plan with the lowest cost.
The planner does its best to select the best execution plan, but it is far
from perfect, since it may not count some data properties, like correlation
between columns.


%prep
%setup
%patch0 -p1

%build
%make_build PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%doc COPYRIGHT COPYRIGHT.postgresql doc/
%_libdir/pgsql/*.so
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Mon Nov 10 2025 Alexei Takaseev <taf@altlinux.org> 1.3.11-alt1
- Initial build for ALT Linux
