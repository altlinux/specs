# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: shadowsocks-rust
Version: 1.20.3
Release: alt1
Summary: A fast tunnel proxy that helps you bypass firewalls
License: MIT
Group: Security/Networking
Url: https://shadowsocks.org/
Vcs: https://github.com/shadowsocks/shadowsocks-rust

Source: %name-%version.tar

BuildRequires: openssl-devel
BuildRequires: /proc
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:
BuildRequires: banner
BuildRequires: curl
BuildRequires: python3
}}

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
# Adding ""--cfg=rustix_use_libc"" to avoid: "error: could not find native static
# library rustix_outline_x86" https://github.com/bytecodealliance/rustix/issues/574
rustflags = ["-Copt-level=3", "-Cdebuginfo=1", "--cfg=rustix_use_libc"]

[profile.release]
strip = false
EOF
%ifnarch %ix86 x86_64 aarch64
# https://github.com/shadowsocks/shadowsocks-rust/issues/1548
sed -i '/"dns-over-h3",/d' Cargo.toml
sed -i '/"local-online-config",/d' Cargo.toml
%endif

%build
export RUST_BACKTRACE=full
cargo build %_smp_mflags --offline --release \
	--features full

%install
cargo install %_smp_mflags --offline --no-track --path .
mkdir -p %buildroot%_unitdir %buildroot%_sysconfdir/%name
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-local.service
install -m0644 .gear/%name.service %buildroot%_unitdir/%name-server.service
install -m0640 .gear/*.json %buildroot%_sysconfdir/%name

%check
target/release/ssmanager --version | grep -Fx 'shadowsocks %version'
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
* Sun Aug 11 2024 Vitaly Chikunov <vt@altlinux.org> 1.20.3-alt1
- Update to v1.20.3 (2024-07-29).

* Sun Jun 02 2024 Vitaly Chikunov <vt@altlinux.org> 1.19.2-alt1
- Update to v1.19.2 (2024-06-01).

* Fri May 31 2024 Vitaly Chikunov <vt@altlinux.org> 1.19.0-alt1
- Update to v1.19.0 (2024-05-26).
- x86(-64), aarch64: Feature list changed from 'default' to 'full'.

* Fri Apr 26 2024 Vitaly Chikunov <vt@altlinux.org> 1.18.3-alt1
- Update to v1.18.3 (2024-04-21).

* Sun Mar 17 2024 Vitaly Chikunov <vt@altlinux.org> 1.18.2-alt1
- Update to v1.18.2 (2024-03-13).

* Tue Feb 13 2024 Vitaly Chikunov <vt@altlinux.org> 1.18.0-alt1
- Update to v1.18.0 (2024-02-08).

* Mon Dec 18 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.1-alt1
- Update to v1.17.1 (2023-11-26).

* Wed Nov 15 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.0-alt1
- Update to v1.17.0 (2023-10-15).

* Mon Sep 25 2023 Vitaly Chikunov <vt@altlinux.org> 1.16.2-alt1
- Update to v1.16.2 (2023-09-23).

* Mon Sep 04 2023 Vitaly Chikunov <vt@altlinux.org> 1.16.1-alt1
- Update to v1.16.1 (2023-09-01).

* Sun Jul 09 2023 Vitaly Chikunov <vt@altlinux.org> 1.15.4-alt1
- Update to v1.15.4 (2023-07-07).

* Mon Jun 05 2023 Vitaly Chikunov <vt@altlinux.org> 1.15.3-alt2
- Fix debuginfo missing Rust source files.

* Tue Mar 28 2023 Vitaly Chikunov <vt@altlinux.org> 1.15.3-alt1
- Update to v1.15.3 (2023-03-13).

* Sun Dec 25 2022 Vitaly Chikunov <vt@altlinux.org> 1.15.2-alt1
- Update to v1.15.2 (2022-12-24).

* Mon Dec 19 2022 Vitaly Chikunov <vt@altlinux.org> 1.15.1-alt1
- Update to v1.15.1 (2022-12-17).

* Thu Mar 24 2022 Vitaly Chikunov <vt@altlinux.org> 1.14.2-alt1
- Update to v1.14.2 (2022-03-22).

* Sun Mar 20 2022 Vitaly Chikunov <vt@altlinux.org> 1.14.1-alt2
- Hardened systemd units and configs (latter are made non-world readable).
- Run simple smoke test in %%check.

* Thu Mar 17 2022 Vitaly Chikunov <vt@altlinux.org> 1.14.1-alt1
- First import v1.14.1-5-g62bf462d (2022-03-16).
