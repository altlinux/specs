Name: rg552-hw-control
Version: 0.1
Release: alt2

Summary: Set of tools for hardware control on Anbernic RG552

License: GPLv2
Group: Games/Arcade
Url: https://github.com/thrimbor/Hurrican/archive/%version.tar.gz
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

%post

%post_service rg552-fancontrol.service
%post_service rg552-wifi.service

%preun

%preun_service rg552-fancontrol
%preun_service rg552-wifi

%files
%_bindir/*
%_unitdir/*.service

%changelog
* Tue Jun  4 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Add post section

* Tue May 28 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus