%define _unpackaged_files_terminate_build 1

# Recommended versioning scheme for this package:
# 1. If no sources are changed, just increase release.
# 2. If sources are changed, use current date as version in format YYYYMMDD,
#    and increase release for all subsequent versions made on same day.

Name:    auditd-plugin-clickhouse
Version: 20191217
Release: alt1
Summary: Plugin for Auditd daemon for sending data into Clickhouse database
Group:   Monitoring
License: GPLv3+

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: boost-complete
BuildRequires: libclickhouse-cpp-devel
BuildRequires: libaudit-devel

%description
Plugin for Auditd daemon for sending data into Clickhouse database

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%config(noreplace) %_sysconfdir/audisp/auditd-clickhouse-datatypes.json
%config(noreplace) %_sysconfdir/audisp/auditd-clickhouse.conf
%config(noreplace) %_sysconfdir/audisp/plugins.d/auditd-plugin-clickhouse.conf
%_prefix/libexec/auditd-plugin-clickhouse

%changelog
* Tue Dec 17 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 20191217-alt1
- Initial build for ALT
