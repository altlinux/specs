%define pg_ver 18-1C
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_variables
Version: 1.2.5
Release: alt1
Summary: The pg_variables module provides functions to work with variables of various types.
License: PostgreSQL
Group: Databases
Url: https://github.com/postgrespro/pg_variables.git
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
The pg_variables module provides functions to work with variables of various
types. Created variables live only in the current user session.

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
* Tue Jun 30 2026 Alexei Takaseev <taf@altlinux.org> 1.2.5-alt1
- Initial build for ALT Linux
