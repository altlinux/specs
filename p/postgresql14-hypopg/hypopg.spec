%define pg_ver 14
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-hypopg
Version: 1.4.3
Release: alt1
Summary: HypoPG is a PostgreSQL extension adding support for hypothetical indexes.
License: PostgreSQL
Group: Databases
Url: https://github.com/HypoPG/hypopg
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
A hypothetical -- or virtual -- index is an index that doesn't really exist, and
thus doesn't cost CPU, disk or any resource to create.  They're useful to know
if specific indexes can increase performance for problematic queries, since
you can know if PostgreSQL will use these indexes or not without having to
spend resources to create them.

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
%doc CHANGELOG.md CONTRIBUTORS.md LICENSE README.md TODO.md docs

%changelog
* Tue Jun 23 2026 Alexei Takaseev <taf@altlinux.org> 1.4.3-alt1
- Initial build for ALT Linux
