%define pg_ver 18-1C
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_qualstats
Version: 2.1.3
Release: alt1
Summary: pg_qualstats is a PostgreSQL extension keeping statistics on predicates.
License: PostgreSQL
Group: Databases
Url: https://github.com/powa-team/pg_qualstats
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
pg_qualstats is a PostgreSQL extension keeping statistics on predicates found
in WHERE statements and JOIN clauses.

This is useful if you want to be able to analyze what are the most-often
executed quals (predicates) on your database. The "powa" project makes use of
this to provide advances index suggestions.

It also allows you to identify correlated columns, by identifying which columns
are most frequently queried together.

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
%doc LICENSE README.md CHANGELOG CONTRIBUTORS.md

%changelog
* Fri Jun 19 2026 Alexei Takaseev <taf@altlinux.org> 2.1.3-alt1
- Initial build for ALT Linux
