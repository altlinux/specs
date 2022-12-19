# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: shadowsocks-rust
Version: 1.15.1
Release: alt1
Summary: A fast tunnel proxy that helps you bypass firewalls
License: MIT
Group: Security/Networking
Url: https://shadowsocks.org/
Vcs: https://github.com/shadowsocks/shadowsocks-rust

Source: %name-%version.tar

BuildRequires: /proc
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:BuildRequires: banner curl python3}}

%description
%summary.

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
cargo build %_smp_mflags --offline --release

%install
cargo install %_smp_mflags --offline --no-track --path .
mkdir -p %buildroot%_unitdir %buildroot%_sysconfdir/%name
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-local.service
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-server.service
install -m0640 .gear/*.json %buildroot%_sysconfdir/%name

%check
.gear/ss-test.sh

%post
%post_service %name-local
%post_service %name-server

%preun
%preun_service %name-local
%preun_service %name-server

%files
%doc README.md LICENSE examples/*
%attr(750,root,wheel) %dir %_sysconfdir/%name
%attr(640,root,wheel) %config(noreplace) %_sysconfdir/%name/*
%_unitdir/*.service
%_bindir/ss*

%changelog
* Mon Dec 19 2022 Vitaly Chikunov <vt@altlinux.org> 1.15.1-alt1
- Update to v1.15.1 (2022-12-17).

* Thu Mar 24 2022 Vitaly Chikunov <vt@altlinux.org> 1.14.2-alt1
- Update to v1.14.2 (2022-03-22).

* Sun Mar 20 2022 Vitaly Chikunov <vt@altlinux.org> 1.14.1-alt2
- Hardened systemd units and configs (latter are made non-world readable).
- Run simple smoke test in %%check.

* Thu Mar 17 2022 Vitaly Chikunov <vt@altlinux.org> 1.14.1-alt1
- First import v1.14.1-5-g62bf462d (2022-03-16).
