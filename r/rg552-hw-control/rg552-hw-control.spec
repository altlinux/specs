Name: rg552-hw-control
Version: 0.1
Release: alt1

Summary: Set of tools for hardware control on Anbernic RG552

License: GPLv2
Group: Games/Arcade
Url: https://github.com/thrimbor/Hurrican/archive/%version.tar.gz
ExclusiveArch: aarch64

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

%files
%_bindir/*
%_unitdir/*.service

%changelog
* Tue May 28 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus