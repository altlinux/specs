%define _unpackaged_files_terminate_build 1

Name: turn-rs
Version: 4.1.5
Release: alt1

Summary: A pure rust implemented turn server
License: MIT
Group: Networking/Other
Url: https://mycrl.github.io/turn-rs
Vcs: https://github.com/mycrl/turn-rs

Source: %name-%version.tar
Source1: vendor.tar
Source2: turn-server-sysusers.conf
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-systemd
BuildRequires: protobuf-compiler
BuildRequires: libprotobuf-devel

%systemd_requires
Requires(pre): systemd

%description
A pure Rust implementation of a forwarding server leverages Rust's memory and
concurrency safety to process 40 million channel data forwarding messages and
600,000 allocation requests per second within a single thread (excluding
network stack overhead). Forwarding latency remains below 35 microseconds
(equivalent to a complete local network send/receive delay between points A and
B). This project prioritizes core functionality, requiring minimal
configuration for use and offering near-out-of-the-box usability.

%prep
%setup -a1
%autopatch -p1
ln -s %_includedir/google sdk/google

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
install -Dm 755 target/release/turn-server %buildroot%_bindir/turn-server
install -Dm 0644 turn-server.service %buildroot%_unitdir/turn-server.service
install -Dm 0644 turn-server.toml \
  %buildroot%_sysconfdir/turn-server/config.toml
install -Dm 0644 %SOURCE2 %buildroot%_sysusersdir/turn-server.conf

%check
%rust_test --test stun

%pre
%sysusers_create_package turn-server %SOURCE2

%post
%systemd_post turn-server.service

%preun
%systemd_preun turn-server.service

%postun
%systemd_postun_with_restart turn-server.service

%files
%_bindir/turn-server
%_unitdir/turn-server.service
%config(noreplace) %_sysconfdir/turn-server/config.toml
%_sysusersdir/turn-server.conf

%changelog
* Thu Aug 27 2026 Pavel Petrykin <silverducks@altlinux.org> 4.1.5-alt1
- Initial build for Alt Linux.
