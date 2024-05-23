%define pg_ver 16-1C
%ifarch loongarch64
# XXX: psql jit uses LLVM, versions <= 15.
# These versions do not support LoongArch targets.
%def_without jit
%else
%def_with jit
%endif

Name: postgresql%pg_ver-pg_repack
Version: 1.5.0
Release: alt2

Summary: pg_repack is a PostgreSQL extension which lets you remove bloat from tables and indexes
License: BSD
Group: Databases
Url: https://github.com/reorg/pg_repack

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libecpg6-devel-static postgresql%pg_ver-server-devel
BuildRequires: libzstd-devel liblz4-devel libssl-devel zlib-devel
BuildRequires: libreadline-devel setproctitle-devel

Requires: postgresql%pg_ver-server

%description
pg_repack_ is a PostgreSQL extension which lets you remove bloat from
tables and indexes, and optionally restore the physical order of clustered
indexes. Unlike CLUSTER_ and `VACUUM FULL`_ it works online, without
holding an exclusive lock on the processed tables during processing.
pg_repack is efficient to boot, with performance comparable to using
CLUSTER directly.

%prep
%setup
%patch0 -p1

%build
%make PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/pgsql/*.so
%if_with jit
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Wed Apr 17 2024 Alexei Takaseev <taf@altlinux.org> 1.5.0-alt2
- Support PG version 12 and newer

* Sun Mar 17 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.5.0-alt1.1
- NMU: fixed FTBFS on LoongArch

* Fri Mar 15 2024 Alexei Takaseev <taf@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux
