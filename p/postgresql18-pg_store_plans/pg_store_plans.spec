%define pg_ver 18
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_store_plans
Version: 1.10
Release: alt1
Summary: The pg_store_plans module provides a means for tracking execution plan statistics of all SQL statements executed by a server.
License: PostgreSQL
Group: Databases
Url: https://github.com/ossc-db/pg_store_plans
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
The module must be loaded by adding pg_store_plans to
"shared_preload_libraries" in postgresql.conf, because it requires
additional shared memory. This means that a server restart is required to
add or remove the module. pg_store_plans requires the GUC variable
compute_query_id to be "on" or "auto". If it is set to "no",
pg_store_plans is silently disabled.

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
%doc LICENSE docs

%changelog
* Tue Jun 09 2026 Alexei Takaseev <taf@altlinux.org> 1.10-alt1
- 1.10

* Tue Jun 09 2026 Alexei Takaseev <taf@altlinux.org> 1.8-alt1
- Initial build for ALT Linux
