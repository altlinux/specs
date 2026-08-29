%global _unpackaged_files_terminate_build 1
%def_with check

Name: wlctl
Version: 0.1.10
Release: alt1
Summary: TUI for managing wifi/ethernet/vpn on Linux with NetworkManager
License: GPL-3.0
Group: System/Configuration/Networking
URL: https://crates.io/crates/wlctl
VCS: https://github.com/aashish-thapa/wlctl

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

Requires: speedtest-cli

%description
Features:
- Station and Access Point modes
- WPA Enterprise (802.1X)
- Multiple adapters - pick which one to drive, switch on the fly
- VPN connections - toggle, manage autoconnect, and delete saved VPN / WireGuard profiles
- wlctl doctor - walks rfkill, driver, association, IP, DHCP, gateway, DNS, internet
- QR code sharing, hidden networks, speed test
- Vim keys, every binding configurable

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/%name

%changelog
* Sat Aug 29 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.10-alt1
- Updated to version 0.1.10.

* Fri Jul 10 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.1.9-alt1
- Initial build for ALT.
