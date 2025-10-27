Name: retroid-led-control
Version: 0.1
Release: alt2

Summary: Set light of analog sticks fot status of battery on Retroid Pocket 5

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
install -Dm0755 %name %buildroot%_bindir/%name

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_presetdir
install -m 0644 20-%name.preset %buildroot%_presetdir/20-%name.preset


%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_unitdir/%name.service
%_presetdir/20-%name.preset

%changelog
* Mon Oct 27 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Stop service after run script

* Thu Sep  4 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
