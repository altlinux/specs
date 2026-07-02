%define pg_ver 16
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name:    postgresql%pg_ver-pgauditlogtofile
Version: 1.8.5
Release: alt1

Summary: pgAuditlogtofile addon to redirect audit entries to an independent file
License: PostgreSQL
Group:   Databases
Url:     https://github.com/fmbiete/pgauditlogtofile
Source: %name-%version.tar
Patch0: Add-event_id.patch
Patch1: fix-compress-libs.patch

BuildRequires: postgresql%pg_ver-server-devel libssl-devel libkrb5-devel libuuid-devel
BuildRequires: liblz4-devel libzstd-devel zlib-devel

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
#%%patch0 -p1
%patch1 -p1

%ifarch %e2k
# error: unrecognized command line option
sed -i 's/-fanalyzer//' Makefile
%endif

%build
%make_build USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config top_builddir=%_libdir/pgsql/pgxs

%install
%makeinstall_std USE_PGXS=1 PG_CONFIG=%_bindir/pg_server_config top_builddir=%_libdir/pgsql/pgxs

%post
echo "Execute the following psql command inside any database that you want to update:"
echo "ALTER EXTENSION pgauditlogtofile UPDATE;                                       "

%files
%doc README.md LICENSE
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Thu Jul 02 2026 Alexei Takaseev <taf@altlinux.org> 1.8.5-alt1
- 1.8.5

* Mon Jun 08 2026 Alexei Takaseev <taf@altlinux.org> 1.8.4-alt1
- 1.8.4

* Thu Mar 26 2026 Alexei Takaseev <taf@altlinux.org> 1.8.2-alt1
- 1.8.2

* Mon Mar 23 2026 Alexei Takaseev <taf@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 16 2026 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt2
- Use LLVM if it used in PostgreSQL

* Wed Mar 04 2026 Alexei Takaseev <taf@altlinux.org> 1.8.0-alt1
- 1.8.0

* Wed Feb 18 2026 Alexei Takaseev <taf@altlinux.org> 1.7.7-alt1
- 1.7.7

* Sun Nov 02 2025 Alexei Takaseev <taf@altlinux.org> 1.7.6-alt1
- 1.7.6

* Wed Oct 22 2025 Alexei Takaseev <taf@altlinux.org> 1.7.5-alt1
- 1.7.5

* Thu Sep 11 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.7.2-alt2
- e2k build fix

* Mon Aug 25 2025 Alexei Takaseev <taf@altlinux.org> 1.7.2-alt1
- 1.7.2

* Wed Jul 30 2025 Alexei Takaseev <taf@altlinux.org> 1.7.1-alt1
- 1.7.1

* Wed Jan 15 2025 Alexei Takaseev <taf@altlinux.org> 1.6.4-alt1
- 1.6.4

* Wed Sep 04 2024 Alexei Takaseev <taf@altlinux.org> 1.6.2-alt1
- 1.6.2

* Tue Aug 20 2024 Alexei Takaseev <taf@altlinux.org> 1.6.1-alt1
- Initial build for Sisyphus.
