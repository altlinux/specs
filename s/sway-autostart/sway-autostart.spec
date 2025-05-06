Name:    sway-autostart
Version: 0.2
Release: alt1

Summary: Systemd service for sway autostart
License: GPLv2
Group:   Graphical desktop/Other

BuildArch: noarch

Requires: sway

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
# nothing to build

%install

install -Dm0644 sway-autostart.service %buildroot%_unitdir/%name.service

install -Dm0644 sway-autostart.preset %buildroot%_presetdir/50-%name.preset

%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%dir %_unitdir
%_unitdir/%name.service
%dir %_presetdir
%_presetdir/50-%name.preset

%changelog
* Tue May  6 2025 Artyom Bystrov <arbars@altlinux.org> 0.2-alt1
- Fix flickering of bootsplash (causing too early tries to run sway)

* Thu Apr 17 2025 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial release for Sisyphus