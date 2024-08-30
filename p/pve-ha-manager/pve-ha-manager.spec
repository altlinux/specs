%global _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed

Name: pve-ha-manager
Summary: Proxmox VE HA Manager
Version: 4.0.5
Release: alt1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-ha-manager.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

# from debian/control
Conflicts: watchdog

Requires: libpve-cluster-perl libpve-notify-perl
Requires: pve-container pve-cluster >= 3.0.17 pve-qemu-server >= 6.0.15
# TODO: pve-container >= 5.0.1 pve-qemu-server >= 8.0.2
BuildRequires(pre): rpm-macros-systemd
BuildRequires: pve-access-control libpve-cluster-perl pve-common pve-doc-generator
BuildRequires: pve-cluster >= 3.0.17
BuildRequires: libpve-rs-perl >= 0.7.3
BuildRequires: libpve-notify-perl
BuildRequires: perl-Glib

%description
%summary.

%package -n pve-ha-simulator
Summary: PVE HA Simulator
Group: System/Servers

%description -n pve-ha-simulator
%summary.
This is a simple GUI to simulate the behavior of a Proxmox VE HA cluster.

%prep
%setup

%build
%make_build -C src

%install
%makeinstall_std -C src
mkdir -p %buildroot{%_unitdir,%_sysconfdir/sysconfig}
install -m0644 debian/*.service %buildroot%_unitdir/
install -m0644 debian/pve-ha-manager.default %buildroot%_sysconfdir/sysconfig/pve-ha-manager

%post
%post_systemd_postponed pve-ha-lrm pve-ha-crm

%preun
%preun_systemd pve-ha-crm pve-ha-lrm

%files
%doc debian/copyright
%config(noreplace) %_sysconfdir/sysconfig/pve-ha-manager
%_datadir/pve-manager/templates
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_unitdir/*
%_sbindir/*
%_man1dir/*
%_man8dir/*
%perl_vendor_privlib/PVE/API2/HA
%perl_vendor_privlib/PVE/CLI/*
%perl_vendor_privlib/PVE/HA
%perl_vendor_privlib/PVE/Service/*

%files -n pve-ha-simulator
%_bindir/pve-ha-simulator
%_datadir/pve-ha-simulator

%changelog
* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.0.5-alt1
- 4.0.5

* Thu Feb 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.0.3-alt1
- 4.0.3

* Thu May 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.1-alt3
- add copyright file

* Thu May 04 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.1-alt2
- add Restart=on-failure

* Wed May 03 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.1-alt1
- 3.6-1
- use %%preun_systemd/%%post_systemd_postponed

* Wed May 03 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.0-alt2
- add explicit require for pve-qemu-server

* Mon Mar 20 2023 Andrew A. Vasilyev <andy@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 3.3.4-alt1
- 3.3-4

* Mon Mar 07 2022 Alexey Shabalin <shaba@altlinux.org> 3.3.3-alt1
- 3.3-3
- build as separate package

