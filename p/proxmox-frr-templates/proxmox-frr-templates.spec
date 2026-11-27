%global _unpackaged_files_terminate_build 1

Name: proxmox-frr-templates
Version: 0.1.3
Release: alt1
Summary: Jinja2 templates for FRR configuration rendering in Proxmox VE
License: AGPL-3.0+
Group: System/Configuration/Other
URL: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/proxmox-ve-rs.git

Source: %name-%version.tar

BuildArch: noarch

%description
Jinja2 templates used by proxmox-frr (Rust library) to render FRR
(Free Range Routing) configuration files in Proxmox VE SDN.

%prep
%setup

%install
install -d %buildroot%_datadir/proxmox-frr/templates
install -pm 0644 templates/* %buildroot%_datadir/proxmox-frr/templates/

%files
%_datadir/proxmox-frr/templates/

%changelog
* Fri Nov 27 2026 Sergey Konev <darisishe@altlinux.org> 0.1.3-alt1
- 0.1.3.
- Update VRF-aware routing templates embedded by proxmox-frr.

* Sun Jun 08 2026 Sergey Konev <darisishe@altlinux.org> 0.1.2-alt1
- Initial build
