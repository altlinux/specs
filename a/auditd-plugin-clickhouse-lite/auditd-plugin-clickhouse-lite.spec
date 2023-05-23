%define _unpackaged_files_terminate_build 1

Name:    auditd-plugin-clickhouse-lite
Version: 0.1.3
Release: alt1
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

# audit 3.0 has changed the location for configs
Requires: audit >= 3.0-alt1

%description
A lightweight plugin for auditd daemon to send audit data to a Clickhouse
database.

%prep
%setup

%build
%add_optflags -Werror
%cmake
%cmake_build

%install
%cmake_install

%check
# A pre-check for bats:
[ -d /dev/fd ] || exit 1
BUILD=%_cmake__builddir bats test-suite.bats

%files
%_prefix/libexec/%name
%_datadir/%name/init_db.sql
%config(noreplace) %attr(600,root,root) %_sysconfdir/audit/%name.conf
%config(noreplace) %_sysconfdir/audit/plugins.d/clickhouse-lite.conf
%config(noreplace) %_sysconfdir/logrotate.d/%name-logrotate.conf

%changelog
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
