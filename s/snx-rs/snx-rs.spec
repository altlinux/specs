# TODO : https://github.com/rust-lang/cargo/issues/7058
Name: snx-rs
Version: 2.0.1
Release: alt2

Summary: Open source VPN client for Checkpoint security gateways

License: AGPL-3.0
Group: System/Servers
Url: https://github.com/ancwrd1/snx-rs

# Source-url: https://github.com/ancwrd1/snx-rs/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExcludeArch: %ix86 ppc64le

BuildRequires(pre): rpm-macros-features
BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
# libdbus-sys
BuildRequires: pkgconfig(dbus-1)
# openssl-sys
BuildRequires: pkgconfig(openssl)
# gobject-sys
BuildRequires: pkgconfig(gobject-2.0)
# gdk-sys
BuildRequires: pkgconfig(gdk-3.0)
%if_feature webkit2gtk 4.1
# webkit2gtk (?)
BuildRequires: pkgconfig(webkit2gtk-4.1)
%endif

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
subst 's|/opt/snx-rs/||' assets/{snx-rs.service,snx-rs-gui.desktop}

%if_notfeature webkit2gtk 4.1
subst 's|, "snx-rs-gui"||' Cargo.toml
%endif

%build
%rust_build

%install
%rust_install snx-rs
%rust_install snxctl

install -D -m 0644 assets/snx-rs.service %buildroot%_unitdir/snx-rs.service
install -D -m 0644 assets/snx-rs.conf  %buildroot%_sysconfdir/snx-rs/snx-rs.conf

%if_feature webkit2gtk 4.1
%rust_install snx-rs-gui
install -D -m 0644 assets/snx-rs-gui.desktop %buildroot%_desktopdir/snx-rs-gui.desktop
%endif

%files
%doc README.md
%_bindir/snx-rs
%_bindir/snxctl
%if_feature webkit2gtk 4.1
%_bindir/snx-rs-gui
%_desktopdir/snx-rs-gui.desktop
%endif
%_unitdir/snx-rs.service
%dir %_sysconfdir/snx-rs/
%_sysconfdir/snx-rs/snx-rs.conf

%changelog
* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- build snx-rs-gui only if webkit2gtk is present

* Sun Apr 07 2024 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- initial build for ALT Sisyphus
