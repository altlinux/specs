%define pg_ver 15
%def_with jit

Name:    postgresql%pg_ver-orafce
Version: 4.14.3
Release: alt1

Summary: The "orafce" project implements in Postgres some of the functions from the Oracle database that are missing
License: 0BSD
Group:   Databases
URL:     http://github.com/orafce/orafce

Requires(pre): postgresql%pg_ver-server

BuildRequires: clang-devel
BuildRequires: llvm-devel
BuildRequires: libicu-devel
BuildRequires: postgresql%pg_ver-server-devel
BuildRequires: openssl-devel
BuildRequires: libkrb5-devel
BuildRequires: bison
BuildRequires: flex

Source: %name-%version.tar

%description
Functions and operators that emulate a subset of functions and packages from the Oracle RDBMS.

This module contains some useful functions that can help with porting Oracle application to PostgreSQL or that can be generally useful.

Built-in Oracle date functions have been tested against Oracle 10 for conformance. Date ranges from 1960 to 2070 work correctly. Dates before 1100-03-01 cannot be verified due to a bug in Oracle.

All functions are fully compatibles with Oracle and respect all known format strings. Detailed descriptions can be found on the internet. Use keywords like : oracle round trunc date iyyy.

%prep
%setup

%build
%make_build USE_PGXS=1 PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%doc INSTALL.orafce README.asciidoc
%_libdir/pgsql/*.so
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*
%_docdir/postgresql/extension/*


%changelog
* Thu Mar 20 2025 Alexei Takaseev <taf@altlinux.org> 4.14.3-alt1
- 4.14.3
- Enable LLVM for loongarch64

* Fri Feb 21 2025 Alexei Takaseev <taf@altlinux.org> 4.14.2-alt1
- 4.14.2

* Fri Jun 21 2024 Danilkin Danila <danild@altlinux.org> 4.10.3-alt1
- Automatically updated to 4.10.3.

* Sat Apr 13 2024 Danilkin Danila <danild@altlinux.org> 4.9.2-alt1
- Initial build for Sisyphus
