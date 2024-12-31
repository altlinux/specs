Name:    gptokeyb
Version: 0.2.3
Release: alt1.git2c7a017

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

BuildRequires(pre): cmake rpm-build-cmake
BuildRequires: gcc-c++ libSDL2-devel libevdev-devel

%description
gptokeyb provides a kill switch for an application and mapping of gamepad buttons to keys and/or mouse. It also provides an xbox360-compatible controller mode.

%package -n %name-handheld-control
Summary: Service for UI control on handhelds (f.e., Anbernic consoles)
Group: Games/Other

%description -n %name-handheld-control
Service for UI control on handhelds (f.e., Anbernic consoles)

%prep
%setup

%build
%cmake
%cmake_build

%install
install -Dm0755 ./%_cmake__builddir/gptokeyb %buildroot%_bindir/%name
mkdir -p %buildroot%_sysconfdir/%name
cp configs/default.gptk %buildroot%_sysconfdir/%name

cp %SOURCE2 %buildroot%_sysconfdir/%name/
cp %SOURCE3 %buildroot%_sysconfdir/%name/
cp %SOURCE4 %buildroot%_sysconfdir/%name/
install -Dm0755 %SOURCE5 %buildroot%_bindir/

install -Dm0644 %SOURCE6 %buildroot%_unitdir/%name.service

install -Dm0644 %SOURCE7 %buildroot%_presetdir/20-%name.preset

%post -n %name-handheld-control
%post_service %name.service

%preun -n %name-handheld-control
%preun_service %name.service

%files
%doc *.md
%_bindir/%name
%_sysconfdir/%name/default.gptk

%files -n %name-handheld-control

%_bindir/gamepadtokeyboard
%dir %_sysconfdir/%name
%_sysconfdir/%name/Anbernic*.gptk
%_unitdir/%name.service
%dir %_presetdir
%_presetdir/20-%name.preset

%changelog
* Mon Dec 23 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.3-alt1.git2c7a017
- Replace Anbernic stuff into separate package


* Mon Dec 23 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.2-alt1.git2c7a017
- Add service for autorun
- Add configs for Anbernic handhelds

* Thu Dec 19 2024 Artyom Bystrov <arbars@altlinux.org> 0.2.1-alt1.git2c7a017
- Initial build