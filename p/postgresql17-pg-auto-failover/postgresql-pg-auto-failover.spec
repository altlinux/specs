%define _unpackaged_files_terminate_build 1
%define pg_ver 17
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg-auto-failover
Version: 2.2
Release: alt3

Summary: Postgres %pg_ver extension and service for automated failover and high-availability
License: PostgreSQL
Group: Databases
Url: https://github.com/hapostgres/pg_auto_failover

Source: pg_auto_failover-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: postgresql%pg_ver-devel
BuildRequires: libncurses-devel
BuildRequires: libselinux-devel
BuildRequires: libzstd-devel
BuildRequires: liblz4-devel
BuildRequires: libxml2-devel
BuildRequires: libpam0-devel
BuildRequires: libssl-devel
BuildRequires: libkrb5-devel
BuildRequires: zlib-devel
BuildRequires: libxslt-devel
BuildRequires: setproctitle-devel
BuildRequires: libreadline-devel
BuildRequires: libselinux-devel
BuildRequires: libecpg6-%pg_ver-devel-static
BuildRequires: libnuma-devel

Requires: postgresql%pg_ver-server
Provides: pg-auto-failover

%description
pg_auto_failover is an extension and service for PostgreSQL that monitors and
manages automated failover for a Postgres cluster. It is optimized for
simplicity and correctness and supports Postgres 10 and newer.

pg_auto_failover supports several Postgres architectures and implements a safe
automated failover for your Postgres service. It is possible to get started
with only two data nodes which will be given the roles of primary and secondary
by the monitor.

%prep
%setup -n pg_auto_failover-%version
%patch0 -p1

%build
%make_build

%install
%makeinstall_std

%files
%doc *.md
%_bindir/pg_autoctl
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension

%changelog
* Mon Mar 16 2026 Alexei Takaseev <taf@altlinux.org> 2.2-alt3
- Use LLVM if it used in PostgreSQL

* Thu Jan 15 2026 Alexei Takaseev <taf@altlinux.org> 2.2-alt2
- Add support PostgreSQL 18
- Add BR libnuma-devel

* Fri Apr 04 2025 Alexei Takaseev <taf@altlinux.org> 2.2-alt1
- 2.2

* Sat Feb 15 2025 Alexei Takaseev <taf@altlinux.org> 2.1-alt2
- Add support PostgreSQL 17

* Sun Sep 29 2024 Alexei Takaseev <taf@altlinux.org> 2.1-alt1.1
- Fix BuildReq

* Thu Mar 14 2024 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- Initial build for Sisyphus.
