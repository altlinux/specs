Name: rg552-hw-control
Version: 0.1
Release: alt5

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
* Mon Jul 01 2024 Anton Midyukov <antohami@altlinux.org> 0.1-alt5
- NMU: rg552-fancontrol, rg552-wifi: do nothing if the device model is not
  Anbernic RG552
- NMU: spec: cleanup commented out lines for udev rules

* Sat Jun 22 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt4
- Minor spec clean

* Sat Jun 15 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt3
- Add preset file

* Tue Jun  4 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Add post section

* Tue May 28 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
