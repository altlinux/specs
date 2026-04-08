Name:    gptokeyb
Version: 0.2.9
Release: alt6.gitb85b098

Summary: Gamepad to Keyboard/mouse/xbox360(gamepad) emulator
License: GPLv2
Group:   Games/Other
Url:     https://github.com/PortsMaster/gptokeyb

Source: %name-%version.tar
Source2: Anbernic-RG-ARC.gptk
Source3: Anbernic-RG-353x.gptk
Source4: Anbernic-RG-552.gptk
Source5: gamepadtokeyboard
Source6: gptokeyb.service
Source7: 20-gptokeyb.preset
Source8: 65-gptokeyb-uinput.rules
Source9: gamecontrollerdb.handhelds.txt

BuildRequires(pre): cmake rpm-build-cmake
BuildRequires: gcc-c++ libSDL2-devel libevdev-devel

%description
gptokeyb provides a kill switch for an application and mapping of gamepad buttons to keys and/or mouse. It also provides an xbox360-compatible controller mode.

%package -n %name-handheld-control
Summary: Service for UI control on handhelds (f.e., Anbernic consoles)
Group: Games/Other
Requires: %name

%description -n %name-handheld-control
Service for UI control on handhelds (f.e., Anbernic consoles)

%prep
%setup

%build
%cmake
%cmake_build

%install
install -Dm0755 ./%_cmake__builddir/gptokeyb %buildroot%_bindir/%name
install -Dm0644 %SOURCE8 %buildroot%_udevrulesdir/65-gptokeyb-uinput.rules

mkdir -p %buildroot%_sysconfdir/%name
cp configs/default.gptk %buildroot%_sysconfdir/%name

cp %SOURCE2 %buildroot%_sysconfdir/%name/
cp %SOURCE3 %buildroot%_sysconfdir/%name/
cp %SOURCE4 %buildroot%_sysconfdir/%name/
install -Dm0755 %SOURCE5 %buildroot%_bindir/

install -Dm0644 %SOURCE6 %buildroot%_unitdir/%name.service

install -Dm0644 %SOURCE7 %buildroot%_presetdir/20-%name.preset

install -Dm0644 %SOURCE9 %buildroot%_datadir/gamecontrollerdb.handhelds.txt

%post -n %name-handheld-control
%post_service %name.service

%preun -n %name-handheld-control
%preun_service %name.service

%files
%doc *.md
%_bindir/%name
%_sysconfdir/%name/default.gptk
%_udevrulesdir/65-gptokeyb-uinput.rules

%files -n %name-handheld-control

%_bindir/gamepadtokeyboard
%dir %_sysconfdir/%name
%_sysconfdir/%name/Anbernic*.gptk
%_unitdir/%name.service
%dir %_presetdir
%_presetdir/20-%name.preset
%_datadir/gamecontrollerdb.handhelds.txt

%changelog
* Wed Apr  8 2026 Artyom Bystrov <arbars@altlinux.org> 0.2.9-alt6.gitb85b098
- Add Anbernic RG DS support

* Fri Mar 27 2026 Artyom Bystrov <arbars@altlinux.org> 0.2.9-alt5.gitb85b098
- Fix name of Anbernic RG353M

* Tue Mar 17 2026 Artyom Bystrov <arbars@altlinux.org> 0.2.9-alt4.gitb85b098
- Fix name of Powkiddy RGB20 Pro

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.9-alt3.gitb85b098
- Fix button mapping

* Thu Aug 28 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.9-alt2.gitb85b098
- Add bunch of devices:
- Retroid Pocket 5;
- Powkiddy RGB20SX;
- Powkiddy x35S;
- Powkiddy X35H.

* Wed Apr  2 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.9-alt1.git2c7a017
- Add new device: Anbernic RG503

* Thu Mar 20 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.8-alt1.git2c7a017
- Add support of Powkiddy RGB30 and RK2023

* Wed Mar  5 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.7-alt1.git2c7a017
- Add support of Powkiddy RGB10Max3

* Tue Feb 18 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.6-alt1.git2c7a017
- Add support of Powkiddy x55
- Minor optimizations in main script

* Sat Jan  4 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.5-alt1.git2c7a017
- Change navigation system for ARC-S and ARC-D (D-Pad is arrows buttons now)
- Add support for full set of symbols in text mode

* Sat Jan  4 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.4-alt1.git2c7a017
- Replace udev rule from anbernic-virtual-controller

* Wed Jan  1 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.3.2-alt1.git2c7a017
- Fix RG35* detection

* Wed Jan  1 2025 Artyom Bystrov <arbars@altlinux.org> 0.2.3.1-alt1.git2c7a017
- Fix ARC-D detection


* Mon Dec 23 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.3-alt1.git2c7a017
- Replace Anbernic stuff into separate package

* Mon Dec 23 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.2-alt1.git2c7a017
- Add service for autorun
- Add configs for Anbernic handhelds

* Thu Dec 19 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt1.git2c7a017
- Initial build