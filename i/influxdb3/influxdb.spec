%define _unpackaged_files_terminate_build 1

# git rev-parse HEAD
%define git_hash 655664fed2eeedcd126b675dc318f28b10c45e8c
# git rev-parse --short HEAD
%define git_hash_short e38298bbdb

Name: influxdb3
Version: 3.4.1
Release: alt1
Url: https://www.influxdata.com
Vcs: https://github.com/influxdata/influxdb.git
ExcludeArch: i586

Summary: InfluxDB Core is a database built to collect, process, transform, and store event and time series data
License: Apache-2.0, MIT
Group: Databases

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: config.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: protobuf-compiler libprotobuf-devel
BuildRequires: python3-dev

%description
%summary.
It is ideal for use cases that require real-time ingest and fast query response
times to build user interfaces, monitoring, and automation solutions.

Common use cases include:

Monitoring sensor data
Server monitoring
Application performance monitoring
Network monitoring
Financial market and trading analytics
Behavioral analytics

InfluxDB is optimized for scenarios where near real-time data monitoring is
essential and queries need to return quickly to support user experiences such
as dashboards and interactive user interfaces.

%prep
%setup
%patch -P 0 -P 1 -p1
%rust_prep

%build
export GIT_HASH=%git_hash
export GIT_HASH_SHORT=%git_hash_short
export CARGO_ENCODED_RUSTFLAGS=-Cdebuginfo=1
%rust_build --config profile.release.lto=\"thin\"

%install
%rust_install

%check
export GIT_HASH=%git_hash
export GIT_HASH_SHORT=%git_hash_short
# skip flags for tests which need internet connection
%rust_test --config profile.release.lto=\"thin\" -- \
--skip test_load_wal_plugin_from_gh \
--skip test_trigger_create_validates_file_present

%files
%_bindir/%name

%changelog
* Thu Aug 28 2025 Artyom Sinyugin <writers@altlinux.org> 3.4.1-alt1
- New release v3.4.1.

* Thu Aug 08 2025 Artyom Sinyugin <writers@altlinux.org> 3.3.0-alt1
- New release v3.3.0.
- Add lto=thin to %%rust_build to prevent 'idle time limit (3600 seconds) exceeded' error in hsh.
- Delete influxdb_process_git_hash_env.patch.

* Thu Jun 26 2025 Artyom Sinyugin <writers@altlinux.org> 3.0.3-alt1
- Initial build.
