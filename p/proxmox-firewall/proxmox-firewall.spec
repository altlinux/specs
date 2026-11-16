%global _unpackaged_files_terminate_build 1
%define _libexecdir /usr/libexec

Name: proxmox-firewall
Summary: Proxmox VE nftables firewall
Version: 1.2.4
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-firewall.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 loongarch64

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: pkgconfig(openssl)
BuildRequires: /proc

Requires: nftables pve-firewall

%description
This package contains an nftables-based implementation of the Proxmox VE
Firewall.

%package -n proxmox-firewall-data
Summary: Firewall service, protocol, and EtherType name databases
Version: 0.1
Release: alt1
License: GPL-2.0-only
Group: System/Servers
BuildArch: noarch

%description -n proxmox-firewall-data
JSON name databases used by the Proxmox VE firewall.

%prep
%setup

%build
export BUILD_MODE=release
%rust_build --locked

%install
install -pD -m0755 target/release/proxmox-firewall \
    %buildroot%_libexecdir/proxmox/proxmox-firewall
install -pD -m0644 debian/proxmox-firewall.service \
    %buildroot%_unitdir/proxmox-firewall.service
install -pD -m0644 proxmox-firewall-data/data/services.json \
    %buildroot%_datadir/proxmox-firewall/data/services.json
install -pD -m0644 proxmox-firewall-data/data/protocols.json \
    %buildroot%_datadir/proxmox-firewall/data/protocols.json
install -pD -m0644 proxmox-firewall-data/data/ethertypes.json \
    %buildroot%_datadir/proxmox-firewall/data/ethertypes.json

%check
%rust_test --locked

%post
%post_systemd_postponed proxmox-firewall.service

%preun
%preun_systemd proxmox-firewall.service

%files
%doc debian/copyright
%_libexecdir/proxmox/proxmox-firewall
%_unitdir/proxmox-firewall.service

%files -n proxmox-firewall-data
%doc proxmox-firewall-data/debian/copyright
%_datadir/proxmox-firewall/data/*.json

%changelog
* Tue Nov 10 2026 Sergey Konev <darisishe@altlinux.org> 1.2.4-alt1
- 1.2.4
- Package the firewall name databases.

* Wed Aug 19 2026 Sergey Konev <darisishe@altlinux.org> 1.2.3-alt1
- Initial build (Closes: 60106)

