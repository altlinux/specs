Name: altemu-mount
Version: 0.2
Release: alt1

Summary: mount storage with roms

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64 x86_64
BuildRequires(pre): rpm-macros-systemd

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

%description
%summary

%prep
%setup

%install
install -Dm0755 %name %buildroot%_bindir/%name

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_presetdir
install -m 0644 75-%name.preset %buildroot%_presetdir/75-%name.preset

mkdir -p %buildroot%_datadir/altemu
install -m 0644 dir-list %buildroot%_datadir/altemu/

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_datadir/altemu/dir-list
%_unitdir/%name.service
%_presetdir/75-%name.preset

%changelog
* Thu Nov 13 2025 Artyom Bystrov <arbars@altlinux.org> 0.2-alt1
- Add overlayfs support
- Fix issue with unmountig NTFS partition

* Wed Oct 29 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt2
- Fix access rights for user

* Tue Oct 28 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
