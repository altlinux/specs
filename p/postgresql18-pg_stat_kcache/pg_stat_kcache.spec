%define pg_ver 18
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_stat_kcache
Version: 2.3.2
Release: alt1
Summary: Gathers statistics about real reads and writes done by the filesystem layer.
License: PostgreSQL
Group: Databases
Url: https://github.com/powa-team/pg_stat_kcache
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
It is provided in the form of an extension for PostgreSQL >= 9.4., and requires
pg_stat_statements extension to be installed. PostgreSQL 9.4 or more is
required as previous version of provided pg_stat_statements didn't expose the
queryid field.

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
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.rst

%changelog
* Tue Jun 23 2026 Alexei Takaseev <taf@altlinux.org> 2.3.2-alt1
- Initial build for ALT Linux
