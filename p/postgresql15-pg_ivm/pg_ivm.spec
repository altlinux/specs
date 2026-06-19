%define pg_ver 15
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_ivm
Version: 1.14
Release: alt1
Summary: The pg_ivm module provides Incremental View Maintenance (IVM) feature for PostgreSQL.
License: PostgreSQL
Group: Databases
Url: https://github.com/sraoss/pg_ivm
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
Incremental View Maintenance (IVM) is a way to make materialized views
up-to-date in which only incremental changes are computed and applied
on views rather than recomputing the contents from scratch as `REFRESH
MATERIALIZED VIEW` does. IVM can update materialized views more
efficiently than recomp utation when only small parts of the view are
changed.

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
%doc LICENSE README.md

%changelog
* Fri Jun 19 2026 Alexei Takaseev <taf@altlinux.org> 1.14-alt1
- Initial build for ALT Linux
