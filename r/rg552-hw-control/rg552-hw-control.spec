Name: rg552-hw-control
Version: 0.1
Release: alt4

Summary: Set of tools for hardware control on Anbernic RG552

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64
BuildRequires(pre): rpm-macros-systemd

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

%description
%summary

%prep
%setup -n %name-%version

%install
for binary in rg552-fancontrol rg552-wifi; do
install -Dm0755 $binary %buildroot%_bindir/$binary
done

for service in rg552-fancontrol.service rg552-wifi.service; do
install -Dm0644 $service %buildroot%_unitdir/$service
done

mkdir -p %buildroot%_presetdir
install -m 0644 20-rg552-hardware.preset %buildroot%_presetdir/


# Enable service automatically if wifi and fan found - work in progress
# cat>%buildroot%_udevrulesdir/90-rg552-hw.rules<<EOF
# SUBSYSTEM=="usb", ACTION=="add", ENV{SYSTEMD_WANTS}="rg552-fancontrol.service", TAG+="systemd"
# SUBSYSTEM=="usb", ACTION=="add", ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="f179", ENV{SYSTEMD_WANTS}="rg552-wifi.service", TAG+="systemd"
# EOF

%post

%post_service rg552-fancontrol.service
%post_service rg552-wifi.service

%preun

%preun_service rg552-fancontrol
%preun_service rg552-wifi

%files
%_bindir/*
%_unitdir/*.service
# %%_udevrulesdir/*.rules
%_presetdir/20-rg552-hardware.preset

%changelog
* Sat Jun 22 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt4
- Minor spec clean

* Sat Jun 15 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt3
- Add preset file

* Tue Jun  4 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Add post section

* Tue May 28 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus