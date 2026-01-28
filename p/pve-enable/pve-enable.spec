
Name: pve-enable
Version: 0.2
Release: alt1

Summary: Enable and start all PVE services
License: GPL-2.0
Group: Development/Other

ExclusiveArch: x86_64 aarch64 loongarch64

Requires: pve-manager

%description
%summary.

%install
mkdir -p %buildroot

%post
service_list_enable="pve-cluster pveproxy pvedaemon pvestatd pve-firewall \
pvefw-logger pve-guests pve-ha-crm pve-ha-lrm spiceproxy \
lxc lxcfs lxc-net lxc-monitord qmeventd pvescheduler pve-lxc-syscalld ksmtuned networking"
service_list_start="pve-cluster pveproxy pvedaemon pvestatd pve-firewall \
pvefw-logger pve-ha-crm pve-ha-lrm spiceproxy \
lxc lxcfs lxc-net lxc-monitord qmeventd pvescheduler pve-lxc-syscalld ksmtuned networking"

systemctl enable $service_list_enable ||:
systemctl start $service_list_start ||:

%files

%changelog
* Thu Jan 29 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.2-alt1
- enable networking (ifupdown2) and ksmtuned services

* Mon Jul 21 2025 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt2
- NMU: build on loongarch64

* Sat Jun 17 2023 Andrew A. Vasilyev <andy@altlinux.org> 0.1-alt1
- initial release for ALT

