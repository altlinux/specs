%define _libexecdir /usr/libexec

Name: drbd-reactor
Version: 1.4.1
Release: alt1.1
Summary: React to DRBD events via plugins.

Group: System/Servers
License: Apache-2.0
URL: https://www.github.com/LINBIT/drbd-reactor
Vcs: https://www.github.com/LINBIT/drbd-reactor.git
Source: %name-%version.tar
ExclusiveArch: x86_64 aarch64 loongarch64 ppc64le

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rust-cargo
BuildRequires: systemd-devel
BuildRequires: /proc

Requires: drbd-utils >= 9.28.0

%description
Daemon monitoring the state of DRBD resources, and executing plugins
acting on state changes.
Plugins can for example monitor resources or promote DRBD resources.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF


%build
%rust_build

%install
%makeinstall_std
install -D -m644 example/ctl.completion.bash %buildroot%_datadir/bash-completion/completions/drbd-reactorctl

%post
%post_systemd_postponed %name.service

%preun
%preun_systemd %name.service

%check
%rust_test

%files
%doc README.md example/drbd-reactor-reload.path example/drbd-reactor-reload.service example/drbd-reactor.toml example/on-no-quorum-io-error.sh
%config(noreplace) %_sysconfdir/drbd-reactor.toml
%_sysconfdir/drbd-reactor.d
%systemd_unitdir/drbd-reactor.service
%systemd_unitdir/ocf.rs@.service
%_sbindir/drbd-reactor
%_sbindir/drbd-reactorctl
%_libexecdir/drbd-reactor/
%_libexecdir/drbd-reactor/ocf-rs-wrapper
%_datadir/bash-completion/completions/drbd-reactorctl
%_man1dir/drbd-reactor.1*
%_man1dir/drbd-reactorctl.1*
%_man5dir/drbd-reactor.toml.5*
%_man5dir/drbd-reactor.umh.5*
%_man5dir/drbd-reactor.promoter.5*
%_man5dir/drbd-reactor.agentx.5*
%_man5dir/drbd-reactor.debugger.5*
%_man5dir/drbd-reactor.prometheus.5*

%changelog
* Wed May 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.4.1-alt1.1
- NMU: build for LoongArch

* Tue May 07 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.4.1-alt1
- v1.4.1

* Fri Dec 01 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.4.0-alt1
- v1.4.0

* Wed Oct 11 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.3.0-alt1
- v1.3.0

* Wed May 31 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.2.0-alt1
- Initial release for ALT.

