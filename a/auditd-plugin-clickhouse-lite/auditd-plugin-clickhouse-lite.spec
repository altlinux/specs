%define _unpackaged_files_terminate_build 1

# To run the database build test the clickhouse-server package
# is needed.
%ifarch x86_64 aarch64
%def_with dbtest
%else
%def_without dbtest
%endif

Name:    auditd-plugin-clickhouse-lite
Version: 0.1.8
Release: alt2
Summary: A lightweight plugin for auditd daemon to send audit data to a Clickhouse database
Group:   Monitoring
License: GPLv3+

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: boost-complete
BuildRequires: libclickhouse-cpp-devel
BuildRequires: libaudit-devel
BuildRequires: bats /proc

%if_with dbtest
BuildRequires: pytest3 python3(clickhouse_test) clickhouse-server
BuildRequires: python3(clickhouse_driver)
%endif

# audit 3.0 has changed the location for configs
Requires: audit >= 3.0-alt1

%description
A lightweight plugin for auditd daemon to send audit data to a Clickhouse
database.

%package -n clickhouse-audit-utils
Summary: Utilities to work with audit data stored in a Clickhouse database
Group:   Monitoring
License: GPLv3+

%description -n clickhouse-audit-utils
Utilities to work with audit data stored in a Clickhouse database.
Currently the package contains only the export script that could be
used to export the database records back to text (log) files.

%prep
%setup

%build
%add_optflags -Werror
%cmake
%cmake_build

%install
%cmake_install

install -D -m0755 clickhouse-audit-export \
		%buildroot/%_bindir/clickhouse-audit-export

%check
CLICKHOUSE_SERVER_CLEANUP=1 BUILD=%_cmake__builddir \
    ./run-tests.sh normal \
                   chunked \
		   bench \
%if_with dbtest
		   db
%endif

%files
%_prefix/libexec/%name
%dir %_datadir/%name
%_datadir/%name/init_db.sql
%config(noreplace) %attr(600,root,root) %_sysconfdir/audit/%name.conf
%config(noreplace) %_sysconfdir/audit/plugins.d/clickhouse-lite.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name-logrotate.conf

%files -n clickhouse-audit-utils
%_bindir/clickhouse-audit-export

%changelog
* Thu Apr 04 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.8-alt2
- Disable database build test on arches where clickhouse-server is
  not available.

* Thu Apr 04 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.8-alt1
- Added test checking "build_test.log" is written and processed.
- Added test checking "test.log" is written to AuditDataRaw table.
- Added tests that run against a real ClickHouse instance with
  the help of python3-module-clickhouse-test.
- Load init_db.sql statement-by-statement, i. e.: allow to place
  a multi-statement SQL script there.

* Fri Sep 22 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.7-alt1
- Added tests to check the fix.
- Fixed various potential loss of data.
- Fix: Don't panic when no data have been read (EOF).
- CRITICAL FIX: Don't assume the input buffer is always full.
- Fix: Always panic if no end marker (newline) found.

* Mon Jul 31 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.6-alt1
- Fixed search for clickhouse-cpp library and use of its headers.
- Added clickhouse-audit-utils package containing the audit record
  export script.
- Fix: Own %%_datadir/%%name.

* Wed May 24 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.5-alt1
- Check that the plugin copes normally with slow and very slow input.
- Fix: Search for newline only in newly received data.

* Tue May 23 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.4-alt1
- Make writer throw errors when running with -e.

* Tue May 23 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.3-alt1
- Log exceptions from the main process.
- Fix the default syslog Ident=.

* Tue May 23 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.2-alt1
- Fixed insert on timeout.
- Fixed building on 32-bit arches.

* Tue May 23 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Fixed Database= parameter in the default config.

* Tue May 23 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus. Partially based on auditd-plugin-clickhouse.
