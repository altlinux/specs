Name: ap6611s-bluetooth
Version: 0.1
Release: alt1

Summary: Broadcom AP6611S bluetooth service
License: GPLv2
Group: System/Servers

Url: https://altlinux.space/nenderus/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

Requires: brcm-patchram-plus
Requires: firmware-rockchip

%description
Service for correct work bluetoth on Broadcom AP6611S chip

%prep
%setup

%install
%__mkdir_p %buildroot%_unitdir
%__install -Dp -m0644 %name.service %buildroot%_unitdir/

%post
%post_service %name

%preun
%preun_systemd %name

%files
%doc README.md
%_unitdir/%name.service

%changelog
* Wed Mar 19 2025 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial build for ALT Linux
