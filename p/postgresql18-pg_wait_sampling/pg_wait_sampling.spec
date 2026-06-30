%define pg_ver 18
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_wait_sampling
Version: 1.1.9
Release: alt1
Summary: pg_wait_sampling - sampling based statistics of wait events
License: PostgreSQL
Group: Databases
Url: https://github.com/postgrespro/pg_wait_sampling
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
pg_wait_sampling - sampling based statistics of wait events

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
* Tue Jun 30 2026 Alexei Takaseev <taf@altlinux.org> 1.1.9-alt1
- Initial build for ALT Linux
