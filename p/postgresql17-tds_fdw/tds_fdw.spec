%define pg_ver 17
%define prog_name tds_fdw
%ifarch loongarch64
%def_without jit
%else
%def_with jit
%endif

Summary: TDS Foreign data wrapper
Name: postgresql%pg_ver-%prog_name
Version: 2.0.4
Release: alt1
License: PostgreSQL
Group: Databases
Url: https://github.com/tds-fdw/tds_fdw
Packager: Pavel Vasenkov <pav@altlinux.org>
Source: %prog_name.tar

BuildRequires: libfreetds-devel
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server
Conflicts: postgresql-tds_fdw

%description
This is a PostgreSQL foreign data wrapper that can connect to
databases that use the Tabular Data Stream (TDS) protocol, such
as Sybase databases and Microsoft SQL server.

%prep
%setup -n %prog_name-%version

%build

%make PG_CONFIG=%_bindir/pg_server_config USE_PGXS=1
%make_build

%makeinstall_std

%files
%_defaultdocdir/postgresql/extension/*
%_libdir/pgsql/*.so
%if %pg_ver >= 11
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%endif
%_datadir/pgsql/extension/*

%changelog
* Mon Sep 30 2024 Alexei Takaseev <taf@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue May 14 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.0.3-alt4
- NMU: fixed FTBFS on LoongArch

* Fri Dec 02 2022 Alexei Takaseev <taf@altlinux.org> 2.0.3-alt3
- Add conflits to old postgresql-tds_fdw

* Wed Nov 23 2022 Alexei Takaseev <taf@altlinux.org> 2.0.3-alt2
- Use server depended pg_server_config for build

* Tue Nov 22 2022 Pavel Vasenkov <pav@altlinux.org> 2.0.3-alt1
- New version

* Fri Nov 27 2020 Pavel Vasenkov <pav@altlinux.org> 2.0.2-alt2
- Set package name and descriptions

* Fri Nov 13 2020 Pavel Vasenkov <pav@altlinux.org> 2.0.2-alt1
- Initial build in Sisyphus 
