%define _unpackaged_files_terminate_build 1
%define git_hash 655664fed2eeedcd126b675dc318f28b10c45e8c
%define git_hash_short e38298bbdb

Name: influxdb3
Version: 3.11.5
Release: alt1
Summary: Scalable datastore for metrics, events, and real-time analytics
License: Apache-2.0 and MIT
Group: Databases
URL: https://www.influxdata.com
VCS: https://github.com/influxdata/influxdb.git

Source: %name-%version.tar
Source1: vendor.tar
Source2: cargo-vendor-config.toml
Source3: wasm-binaries.tar
Patch: alt-iox-query-udf-offline-wasm-binaries.patch

# upstream ships prebuilt wasm binaries only for these targets
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: python3-dev

%description
InfluxDB 3 Core is a database built to collect, process, transform, and store event
and time series data. It is ideal for use cases that require real-time ingest and
fast query response times to build user interfaces, monitoring, and automation solutions.

Common use cases include:
- Monitoring sensor data
- Server monitoring
- Application performance monitoring
- Network monitoring
- Financial market and trading analytics
- Behavioral analytics

InfluxDB is optimized for scenarios where near real-time data monitoring is
essential and queries need to return quickly to support user experiences such
as dashboards and interactive user interfaces.

%prep
%setup -a1 -a3
%rust_prep
cat %SOURCE2 >> .cargo/config.toml
%patch -p1

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
# test_disable_package_management_preserves_existing_venv assumes versioned venv layout (lib/pythonX.Y), ALT uses lib/python3
# test_size_option_env_vars_mirror_cli_behavior mutates process env and races with parallel Config-parsing tests
%rust_test --config profile.release.lto=\"thin\" -- \
--skip test_load_wal_plugin_from_gh \
--skip test_trigger_create_validates_file_present \
--skip test_disable_package_management_preserves_existing_venv \
--skip test_size_option_env_vars_mirror_cli_behavior

%files
%_bindir/%name

%changelog
* Tue Sep 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 3.11.5-alt1
- Updated to version 3.11.5.

* Thu Aug 28 2025 Artyom Sinyugin <writers@altlinux.org> 3.4.1-alt1
- New release v3.4.1.

* Fri Aug 08 2025 Artyom Sinyugin <writers@altlinux.org> 3.3.0-alt1
- New release v3.3.0.
- Add lto=thin to %%rust_build to prevent 'idle time limit (3600 seconds) exceeded' error in hsh.
- Delete influxdb_process_git_hash_env.patch.

* Thu Jun 26 2025 Artyom Sinyugin <writers@altlinux.org> 3.0.3-alt1
- Initial build.
