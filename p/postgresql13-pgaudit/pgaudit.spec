%define pg_ver 13

Name:    postgresql%pg_ver-pgaudit
Version: 1.5.3
Release: alt1
Epoch: 1

Summary: PostgreSQL Audit Extension
License: PostgreSQL
Group:   Databases
Url:     https://github.com/pgaudit/pgaudit
Source: %name-%version.tar

BuildRequires: libssl-devel libkrb5-devel
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
The PostgreSQL Audit Extension (pgAudit) provides detailed session and/or
object audit logging via the standard PostgreSQL logging facility.

The goal of the pgAudit is to provide PostgreSQL users with capability to
produce audit logs often required to comply with government, financial, or ISO
certifications.

An audit is an official inspection of an individual's or organization's
accounts, typically by an independent body. The information gathered by pgAudit
is properly called an audit trail or audit log. The term audit log is used in
this documentation.

%prep
%setup

%build
%make_build USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config top_builddir=%_libdir/pgsql/pgxs

%install
%makeinstall_std USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config top_builddir=%_libdir/pgsql/pgxs

%post
echo "Execute the following psql command inside any database that you want to update:"
echo "ALTER EXTENSION pgaudit UPDATE;                                                "

%files
%doc README.md LICENSE
%_libdir/pgsql/*
%_datadir/pgsql/extension/*

%changelog
* Wed Mar 19 2025 Alexei Takaseev <taf@altlinux.org> 1:1.5.3-alt1
- 1.5.3

* Tue Feb 25 2025 Alexei Takaseev <taf@altlinux.org> 1:1.5.2-alt1
- Build pgaudit 1.5 for Postgresql 13

* Wed Jan 15 2025 Alexei Takaseev <taf@altlinux.org> 17.0-alt1
- 17.0

* Tue Aug 20 2024 Alexei Takaseev <taf@altlinux.org> 16.0-alt1
- 16.0
- Change Group to Databases
- Build for PG 16

* Fri Apr 07 2023 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt2
- Required postgresql%%pg_ver-server.

* Fri Mar 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
