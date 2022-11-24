%define pg_ver 12
%define prog_name repmgr
%def_with jit

Name: postgresql%pg_ver-%prog_name
Version: 5.3.3
Release: alt2
Summary: Replication Manager for PostgreSQL Clusters
Group: Databases
License: GPL-3.0
Url: http://www.repmgr.org/
Vcs: https://github.com/EnterpriseDB/repmgr.git
Source0: %name-%version.tar
Source1: repmgr.init
Source2: repmgr.sudoers
Source3: repmgr.service
Source4: repmgr.tmpfiles
Source5: repmgr.sysconfig

Patch: %name-%version.patch

Requires: postgresql-common
Requires: postgresql%pg_ver-server

Provides: %prog_name = %EVR
Obsoletes: %prog_name < %EVR

BuildRequires: flex
BuildRequires: libssl-devel
BuildRequires: libecpg-devel-static libpq5-devel-static postgresql%pg_ver-server-devel
# for build doc
BuildRequires: docbook-dtds docbook-style-xsl
BuildRequires: /usr/bin/xmllint /usr/bin/xsltproc

%description
Repmgr is an open-source tool suite for managing replication and failover in a
cluster of PostgreSQL servers. It enhances PostgreSQL's built-in hot-standby
capabilities with tools to set up standby servers, monitor replication, and
perform administrative tasks such as failover or manual switchover operations.

%package doc
Summary:  Documentation for the Replication Manager for PostgreSQL Clusters
Group: Documentation
BuildArch: noarch

%description doc
The package contains documentation for the Replication Manager for PostgreSQL Clusters.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure PG_CONFIG=%_bindir/pg_server_config
USE_PGXS=1 %make_build
%make doc
%make doc-repmgr.html

%install
USE_PGXS=1 %makeinstall_std

mkdir -p %buildroot/{%_initdir,%_unitdir,%_tmpfilesdir,%_sysconfdir/{sysconfig,sudoers.d,%prog_name},%_logdir/%prog_name}
install -p -m755 %SOURCE1 %buildroot%_initdir/%prog_name
install -p -m644 %SOURCE2 %buildroot%_sysconfdir/sudoers.d/%prog_name
install -p -m644 %SOURCE3 %buildroot%_unitdir/%prog_name.service
install -p -m644 %SOURCE4 %buildroot%_tmpfilesdir/%prog_name.conf
install -p -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%prog_name
install -p -m644 repmgr.conf.sample %buildroot%_sysconfdir/%prog_name/%prog_name.conf

%post
%post_service %name
echo "Execute the following psql command inside any database that you want to update:"
echo "ALTER EXTENSION repmgr UPDATE;                                                 "

%preun
%preun_service %name

%files
%doc README.md LICENSE
%_bindir/repmgr
%_bindir/repmgrd
%config(noreplace) %_sysconfdir/sysconfig/%prog_name
%config(noreplace) %_sysconfdir/sudoers.d/%prog_name
%dir %attr(750,root,postgres) %_sysconfdir/%prog_name
%config(noreplace) %attr(640,root,postgres) %_sysconfdir/%prog_name/%prog_name.conf
%_initdir/%prog_name
%_unitdir/%prog_name.service
%_tmpfilesdir/%prog_name.conf
%attr(1775,root,postgres) %dir %_logdir/%prog_name
%_libdir/pgsql/*.so
%if %pg_ver >= 11
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%endif
%_datadir/pgsql/extension/*

%files doc
%doc doc/html

%changelog
* Tue Nov 22 2022 Alexei Takaseev <taf@altlinux.org> 5.3.3-alt2
- Join repmgr and postgresqlXY-repmgr subpackages to one
  postgresqlXY-repmgr

* Sat Nov 12 2022 Alexey Shabalin <shaba@altlinux.org> 5.3.3-alt1
- 5.3.3

* Thu Feb 10 2022 Alexey Shabalin <shaba@altlinux.org> 5.3.0-alt1
- 5.3.0

* Wed Feb 24 2021 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt2
- Execute service as postgres system user.

* Wed Feb 10 2021 Alexey Shabalin <shaba@altlinux.org> 5.2.1-alt1
- Initial build.
