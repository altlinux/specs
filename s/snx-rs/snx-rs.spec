# TODO : https://github.com/rust-lang/cargo/issues/7058
Name: snx-rs
Version: 5.2.2
Release: alt1

Summary: Open source VPN client for Checkpoint security gateways

License: AGPL-3.0
Group: System/Servers
Url: https://github.com/ancwrd1/snx-rs

# Source-url: https://github.com/ancwrd1/snx-rs/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExcludeArch: %ix86 ppc64le

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
# libdbus-sys
BuildRequires: pkgconfig(dbus-1)
# openssl-sys
BuildRequires: pkgconfig(openssl)
# gobject-sys
BuildRequires: pkgconfig(gobject-2.0)
# gdk4-sys
BuildRequires: pkgconfig(gtk4)
# graphene-sys
BuildRequires: pkgconfig(graphene-gobject-1.0)
# libsqlite3-sys
BuildRequires: pkgconfig(sqlite3)

%description
Open source Linux client for Checkpoint VPN tunnels.

This project contains a Rust source code of the unofficial Linux client for Checkpoint VPN.
Based on the reverse engineered protocol from the vendor application.

%prep
%setup -a 1

mkdir .cargo
cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.isakmp]
git = "https://github.com/ancwrd1/isakmp.git"
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

subst 's|strip = true|strip = false|' Cargo.toml
cat >> Cargo.toml <<EOF
debug = 0
EOF
subst 's|/opt/snx-rs/||' package/{snx-rs.service,snx-rs-gui.desktop}


%build
%rust_build

%install
%rust_install snx-rs
%rust_install snxctl

install -D -m 0644 package/snx-rs.service %buildroot%_unitdir/snx-rs.service

%rust_install snx-rs-gui
install -D -m 0644 package/snx-rs-gui.desktop %buildroot%_desktopdir/snx-rs-gui.desktop

%files
%doc README.md
%_bindir/snx-rs
%_bindir/snxctl
%_bindir/snx-rs-gui
%_desktopdir/snx-rs-gui.desktop
%_unitdir/snx-rs.service

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 5.2.2-alt1
- new version 5.2.2

* Mon Mar 09 2026 Vitaly Lipatov <lav@altlinux.ru> 5.2.1-alt1
- new version 5.2.1
- config file removed by upstream
- GUI switched from GTK3 to GTK4, always build snx-rs-gui

* Mon Sep 15 2025 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt2
- NMU: obviously required libayatana-appindicator3-1 (ALT #55965).

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 3.1.1-alt1
- new version 3.1.1 (with rpmrb script)

* Wed Mar 12 2025 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

* Sun Feb 02 2025 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt1
- new version (2.9.0) with rpmgs script

* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- build snx-rs-gui only if webkit2gtk is present

* Sun Apr 07 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Sisyphus
