%define pg_ver 15

Name:    postgresql%pg_ver-pgauditlogtofile
Version: 1.6.1
Release: alt1

Summary: pgAuditlogtofile addon to redirect audit entries to an independent file
License: PostgreSQL
Group:   Databases
Url:     https://github.com/fmbiete/pgauditlogtofile
Source: %name-%version.tar
Patch0: Add-event_id.patch

BuildRequires: postgresql%pg_ver-server-devel libssl-devel libkrb5-devel libuuid-devel

Requires: postgresql%pg_ver-server
Requires: postgresql%pg_ver-pgaudit

%description
pgAudit Log to File is an addon to pgAudit than will redirect audit log
lines to an independent file, instead of using PostgreSQL server logger.

This will allow us to have an audit file that we can easily rotate
without polluting server logs with those messages.

Audit logs in heavily used systems can grow very fast. This extension
allows to automatically rotate the files based in a number of minutes.

%prep
%setup
%patch0 -p1

%build
%make_build USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config top_builddir=%_libdir/pgsql/pgxs

%install
%makeinstall_std USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config top_builddir=%_libdir/pgsql/pgxs

%post
echo "Execute the following psql command inside any database that you want to update:"
echo "ALTER EXTENSION pgauditlogtofile UPDATE;                                       "

%files
%doc README.md LICENSE
%_libdir/pgsql/*
%_datadir/pgsql/extension/*

%changelog
* Tue Aug 20 2024 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
