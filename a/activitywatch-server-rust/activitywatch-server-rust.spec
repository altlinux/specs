%global _unpackaged_files_terminate_build 1

Name: activitywatch-server-rust
Version: 0.13.1
Release: alt1
Summary: A reimplementation of aw-server in Rust
License: MPL-2.0
Group: System/Servers
Url: https://activitywatch.net
VCS: https://github.com/ActivityWatch/aw-server-rust

Source: %name-%version.tar
Source1: vendor.tar
Source2: activitywatch-server.sysconfig
Source3: activitywatch-server.service
Source4: activitywatch-sync.service

# no webui for i586
ExcludeArch: i586

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: libssl-devel
BuildRequires: perl-IPC-Cmd

Provides: activitywatch-server = %EVR
Requires: activitywatch-webui

%description
High-performance implementation of the ActivityWatch server, written in Rust.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
debug = true
strip = false
EOF

%build
%rust_build

%install
%rust_install aw-server
%rust_install aw-sync
mkdir -p %buildroot%_unitdir \
         %buildroot%_sysconfdir/sysconfig \
         %buildroot%_sharedstatedir/activitywatch-server
install -m 0644 %SOURCE2 %buildroot%_sysconfdir/sysconfig/activitywatch-server
install -m 0644 %SOURCE3 %buildroot%_unitdir/activitywatch-server.service
install -m 0644 %SOURCE4 %buildroot%_unitdir/activitywatch-sync.service

%pre
%_sbindir/groupadd -r -f aw
%_sbindir/useradd -r -g aw -s /bin/bash -d %_sharedstatedir/activitywatch-server aw 2>/dev/null ||:

%post
%post_service activitywatch-server
%post_service activitywatch-sync

%preun
%preun_service activitywatch-server
%preun_service activitywatch-sync

%files
%_bindir/aw-server
%_bindir/aw-sync
%_unitdir/activitywatch-server.service
%_unitdir/activitywatch-sync.service
%config(noreplace) %_sysconfdir/sysconfig/activitywatch-server
%dir %attr(750, aw, aw) %_sharedstatedir/activitywatch-server
%doc LICENSE

%changelog
* Wed Jun 18 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.13.1-alt1
- Initial build for ALT.
