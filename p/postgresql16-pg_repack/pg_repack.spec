%define pg_ver 16
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_repack
Version: 1.5.3
Release: alt2

Summary: pg_repack is a PostgreSQL extension which lets you remove bloat from tables and indexes
License: BSD
Group: Databases
Url: https://github.com/reorg/pg_repack

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libecpg6-%pg_ver-devel-static postgresql%pg_ver-server-devel
BuildRequires: libzstd-devel liblz4-devel libssl-devel zlib-devel
BuildRequires: libreadline-devel setproctitle-devel libnuma-devel

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
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Wed Mar 18 2026 Alexei Takaseev <taf@altlinux.org> 1.5.3-alt2
- Use LLVM if it used in PostgreSQL

* Mon Oct 27 2025 Alexei Takaseev <taf@altlinux.org> 1.5.3-alt1
- 1.5.3

* Fri Oct 17 2025 Alexei Takaseev <taf@altlinux.org> 1.5.2-alt2
- Add BR libnuma-devel
- Enable JIT on LoongArch

* Tue Jan 14 2025 Alexei Takaseev <taf@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Sep 29 2024 Alexei Takaseev <taf@altlinux.org> 1.5.1-alt2
- Fix BuildReq

* Mon Sep 23 2024 Alexei Takaseev <taf@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Apr 17 2024 Alexei Takaseev <taf@altlinux.org> 1.5.0-alt2
- Support PG version 12 and newer

* Sun Mar 17 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.5.0-alt1.1
- NMU: fixed FTBFS on LoongArch

* Fri Mar 15 2024 Alexei Takaseev <taf@altlinux.org> 1.5.0-alt1
- Initial build for ALT Linux
