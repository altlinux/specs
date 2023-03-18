%define pg_ver 14

Name:    postgresql%pg_ver-pgaudit
Version: 1.7.0
Release: alt1

Summary: PostgreSQL Audit Extension
License: PostgreSQL
Group:   Other
Url:     https://github.com/pgaudit/pgaudit

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires: libssl-devel libkrb5-devel
BuildRequires: postgresql%pg_ver-server-devel

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
* Fri Mar 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
