%define pg_ver 17
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-pg_cron
Version: 1.6.7
Release: alt2

Summary: The pg_cron is a simple cron-based job scheduler for PostgreSQL
License: PostgreSQL
Group: Databases
Url: https://github.com/citusdata/pg_cron

Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
pg_cron is a simple cron-based job scheduler for PostgreSQL (10 or higher)
that runs inside the database as an extension. It uses the same syntax as
regular cron, but it allows you to schedule PostgreSQL commands directly from
the database.

%prep
%setup
%patch0 -p1

%build
%make_build PG_CONFIG=/usr/bin/pg_server_config

%install
%makeinstall_std

%files
%doc LICENSE README.md pg_cron.conf
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Mon Mar 16 2026 Alexei Takaseev <taf@altlinux.org> 1.6.7-alt2
- Use LLVM if it used in PostgreSQL

* Tue Sep 09 2025 Alexei Takaseev <taf@altlinux.org> 1.6.7-alt1
- 1.6.7
- Enable JIT on LoongArch

* Tue Mar 04 2025 Alexei Takaseev <taf@altlinux.org> 1.6.5-alt1
- Initial build for ALT Linux
