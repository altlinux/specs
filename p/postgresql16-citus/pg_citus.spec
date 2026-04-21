%define pg_ver 16
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-citus
Version: 14.0.1
Release: alt1

Summary: Citus is a PostgreSQL extension that transforms Postgres into a distributed database-so you can achieve high performance at any scale.
License: AGPL-3.0
Group: Databases
Url: https://github.com/citusdata/citus

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: liblz4-devel libzstd-devel libcurl-devel libssl-devel libkrb5-devel libicu-devel
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
With Citus, you extend your PostgreSQL database with new superpowers:

- Distributed tables are sharded across a cluster of PostgreSQL nodes
  to combine their CPU, memory, storage and I/O capacity.
- References tables are replicated to all nodes for joins and foreign
  keys from distributed tables and maximum read performance.
- Distributed query engine routes and parallelizes SELECT, DML, and
  other operations on distributed tables across the cluster.
- Columnar storage compresses data, speeds up scans, and supports fast
  projections, both on regular and distributed tables.
- Query from any node enables you to utilize the full capacity of your
  cluster for distributed queries

You can use these Citus superpowers to make your Postgres database scale-out
ready on a single Citus node. Or you can build a large cluster capable of handling
'high transaction throughputs', especially in 'multi-tenant apps', run
'fast analytical queries', and process large amounts of 'time series' or
'IoT data' for 'real-time analytics'. When your data size and volume grow, you can
easily add more worker nodes to the cluster and rebalance the shards.

%package devel
Summary: Header files for Citus
Group: Databases
BuildArch: noarch

%description devel
Header files for Citus

%prep
%setup
%patch0 -p1

%build
%autoreconf

%configure PG_CONFIG=/usr/bin/pg_server_config

%make_build PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%doc CHANGELOG.md CONTRIBUTING.md DEVCONTAINER.md EXTENSION_COMPATIBILITY.md LICENSE NOTICE README.md SECURITY.md STYLEGUIDE.md
%_libdir/pgsql/*.so
%_libdir/pgsql/citus_decoders
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%files devel
%_includedir/pgsql/server/citus_version.h
%_includedir/pgsql/server/distributed/

%changelog
* Tue Apr 21 2026 Alexei Takaseev <taf@altlinux.org> 14.0.1-alt1
- v14.0.1

* Fri Mar 13 2026 Alexei Takaseev <taf@altlinux.org> 14.0.0-alt2
- Use LLVM if it used in PostgreSQL
- Use %%make_build for speedup compilation

* Wed Feb 18 2026 Alexei Takaseev <taf@altlinux.org> 14.0.0-alt1
- v14.0.0

* Sat Dec 13 2025 Alexei Takaseev <taf@altlinux.org> 13.2.0-alt1
- Initial build for ALT Linux
