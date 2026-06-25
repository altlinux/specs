%define _unpackaged_files_terminate_build 1

Name: below
Version: 0.11.0
Release: alt1

Summary: A time traveling resource monitor for modern Linux systems
License: Apache-2.0
Group: Monitoring
Url: https://github.com/facebookincubator/below
VCS: https://github.com/facebookincubator/below

ExcludeArch: %ix86

# Source-url: https://github.com/facebookincubator/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: clang
BuildRequires: libelf-devel
BuildRequires: rust-cargo
BuildRequires: zlib-devel

%description
%name is an interactive tool to view and record historical system data.
It has support for:
  * information regarding hardware resource utilization
  * viewing the cgroup hierarchy
  * cgroup and process information
  * pressure stall information (PSI)
  * `record` mode to record system data
  * `replay` mode to replay historical system data
  * `live` mode to view live system data
  * `dump` subcommand to report script-friendly information (eg JSON, CSV,
  OpenMetrics, etc.)
  * `snapshot` subcommand to create a replayable snapshot file of
  historical system data

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build

%install
%rust_install

install -Dpm 644 ./etc/%name.service %buildroot%_unitdir/%name.service
install -Dpm 644 ./etc/logrotate.conf %buildroot%_logrotatedir/%name.conf
install -Dpm 644 ./below/%name.1 %buildroot%_man1dir/%name.1

%post
%post_systemd %name

%preun
%preun_systemd %name

%postun
%systemd_postun_with_restart %name

%files
%doc README.md
%_bindir/%name
%_unitdir/%name.service
%_man1dir/%name.1*
%config(noreplace) %_logrotatedir/%name.conf

%changelog
* Thu Jun 25 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.11.0-alt1
- initial build for ALT Linux
