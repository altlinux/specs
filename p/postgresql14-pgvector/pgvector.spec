%define pg_ver 14
%def_with jit

Name: postgresql%pg_ver-pgvector
Version: 0.8.0
Release: alt1
Summary: Open-source vector similarity search for Postgres
License: PostgreSQL
Group: Databases
Url: https://github.com/pgvector/pgvector.git
Source: %name-%version.tar
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
Store your vectors with the rest of your data. Supports:
- exact and approximate nearest neighbor search
- single-precision, half-precision, binary, and sparse vectors
- L2 distance, inner product, cosine distance, L1 distance, Hamming distance, and Jaccard distance
- any [language](#languages) with a Postgres client

%package devel
Summary: pgvector development header files
Group: Development/Databases
Requires: postgresql%pg_ver-server-devel

%description devel
pgvector development header files


%prep
%setup

%build
%make_build PG_CONFIG=%_bindir/pg_server_config USE_PGXS=1

%install
%makeinstall_std

%files
%_libdir/pgsql/*.so
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*
%doc CHANGELOG.md LICENSE README.md

%files devel
%_includedir/pgsql/server/extension/*

%changelog
* Wed Sep 03 2025 Alexei Takaseev <taf@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux
