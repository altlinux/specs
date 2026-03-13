%define pg_ver 15
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name:    postgresql%pg_ver-pgaudit
Version: 1.7.1
Release: alt2

Summary: PostgreSQL Audit Extension
License: PostgreSQL
Group:   Other
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
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Fri Mar 13 2026 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt2
- Use LLVM if it used in PostgreSQL

* Wed Mar 19 2025 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Feb 25 2025 Alexei Takaseev <taf@altlinux.org> 1.7.0-alt3
- Build pgaudit 1.7 for Postgresql 15

* Fri Apr 07 2023 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt2
- Required postgresql%%pg_ver-server.

* Fri Mar 17 2023 Andrey Cherepanov <cas@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus.
