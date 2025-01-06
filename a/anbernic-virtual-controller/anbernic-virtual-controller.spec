Name: anbernic-virtual-controller
Version: 0.3.1
Release: alt1

Summary: Set of tools to combine several input devices into one virtual controller on Anbernic handhelds

License: GPLv2
Group: System/Configuration/Boot and Init
ExclusiveArch: aarch64
BuildRequires(pre): rpm-macros-systemd

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Requires: evsieve

%description
%summary

%prep
%setup -n %name-%version

%install
install -Dm0755 %name %buildroot%_bindir/%name

install -Dm0644 %name.service %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_presetdir
install -m 0644 20-%name.preset %buildroot%_presetdir/20-%name.preset

mkdir -p %buildroot%_udevrulesdir
install -m 0644 99-%name.rules %buildroot%_udevrulesdir/99-%name.rules

mkdir -p %buildroot%_datadir
install -m 0644 gamecontrollerdb.anbernic.txt %buildroot%_datadir/gamecontrollerdb.anbernic.txt


%post
%post_service %name.service

%preun
%preun_service %name.service

%files
%_bindir/%name
%_unitdir/%name.service
%_udevrulesdir/99-%name.rules
%_presetdir/20-%name.preset
%_datadir/gamecontrollerdb.anbernic.txt

%changelog

* Mon Jan  6 2025 Artyom Bystrov <arbars@altlinux.org> 0.3.1-alt1
- Remove udev rule for uinput (moved to gptokeyb)

* Sat Dec 28 2024 Artyom Bystrov <arbars@altlinux.org> 0.3-alt1
- Added new devices: RG353P and ARC S

* Sun Dec 22 2024 Artyom Bystrov <arbars@altlinux.org> 0.2-alt1
- Add keybinding file for keyboard emulator (needed for gptokeyb)
- Change type of systemd service

* Fri Dec 20 2024 Artyom Bystrov <arbars@altlinux.org> 0.1.2-alt1
- Fix virtual device multiplying :)

* Fri Dec 20 2024 Artyom Bystrov <arbars@altlinux.org> 0.1.1-alt1
- Add udev rule for uinput support 

* Wed Dec 18 2024 Artyom Bystrov <arbars@altlinux.org> 0.1-alt1
- Initial commit for Sisyphus
