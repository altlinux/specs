%define pg_ver 15
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pgq
Version: 3.5.1
Release: alt1
Summary: PgQ is PostgreSQL extension that provides generic, high-performance lockless queue with simple API based on SQL functions.
License: PostgreSQL
Group: Databases
Url: https://github.com/pgq/pgq
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server
Requires: postgresql%pg_ver-contrib

%description
PgQ is PostgreSQL extension that provides generic, high-performance lockless
queue with simple API based on SQL functions.

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
%_datadir/pgsql/contrib/*
%_datadir/pgsql/extension/*
%doc LICENSE README.rst docs

%changelog
* Wed Jun 24 2026 Alexei Takaseev <taf@altlinux.org> 3.5.1-alt1
- Initial build for ALT Linux
