%define pg_ver 15
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-rum
Version: 1.3.15
Release: alt1
Summary: The rum module provides an access method to work with a `RUM` index. It is based on the `GIN` access method's code.
License: PostgreSQL
Group: Databases
Url: https://github.com/postgrespro/rum.git
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
The rum module provides an access method to work with a `RUM` index. It is based
on the `GIN` access method's code.

A `GIN` index allows performing fast full-text search using `tsvector` and
`tsquery` types. But full-text search with a GIN index has several problems:

- Slow ranking. It needs positional information about lexemes to do ranking. A `GIN`
index doesn't store positions of lexemes. So after index scanning, we need an
additional heap scan to retrieve lexeme positions.
- Slow phrase search with a `GIN` index. This problem relates to the previous
problem. It needs positional information to perform phrase search.
- Slow ordering by timestamp. A `GIN` index can't store some related information
in the index with lexemes. So it is necessary to perform an additional heap scan.

`RUM` solves these problems by storing additional information in a posting tree.

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
%doc LICENSE README.md TODO

%changelog
* Thu Mar 12 2026 Alexei Takaseev <taf@altlinux.org> 1.3.15-alt1
- 1.3.15
- Use LLVM if it used in PostgreSQL

* Wed Sep 03 2025 Alexei Takaseev <taf@altlinux.org> 1.3.14-alt1
- Initial build for ALT Linux
