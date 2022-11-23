%define pg_ver 14
%define prog_name tds_fdw
%def_with jit

Summary: TDS Foreign data wrapper
Name: postgresql%pg_ver-%prog_name
Version: 2.0.3
Release: alt2
License: PostgreSQL
Group: Databases
Url: https://github.com/tds-fdw/tds_fdw
Packager: Pavel Vasenkov <pav@altlinux.org>
Source: %prog_name-%version.tar.gz

BuildRequires: libfreetds-devel
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
This is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and Microsoft SQL server.

%package -n postgresql-%name
Summary: PostgreSQL foreign data wrapper extension for PostgreSQL
Group: Databases

%description -n postgresql-%name
This is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and Microsoft SQL server.

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
* Wed Nov 23 2022 Alexei Takaseev <taf@altlinux.org> 2.0.3-alt2
- Use server depended pg_server_config for build

* Tue Nov 22 2022 Pavel Vasenkov <pav@altlinux.org> 2.0.3-alt1
- New version

* Fri Nov 27 2020 Pavel Vasenkov <pav@altlinux.org> 2.0.2-alt2
- Set package name and descriptions

* Fri Nov 13 2020 Pavel Vasenkov <pav@altlinux.org> 2.0.2-alt1
- Initial build in Sisyphus 
