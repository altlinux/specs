Name:           retroarch-joypad-autoconfig
Version:        1.22.0
Release:        alt1
Summary:        RetroArch Joypad Autoconfig Files
License:        MIT
Group:          Emulators
URL:            https://github.com/libretro/retroarch-joypad-autoconfig

Source:         %{name}-%{version}.tar
Source1:        GAMESIR_Gamesir-X2_Type-C.cfg
Source2:	8BitDo_Ultimate_2C_Wireless.cfg

BuildRequires:  make
BuildArch:      noarch

%description
This package provides joypad autoconfig files for Retroarch. RetroArch is the reference frontend for the libretro API.

Autoconfig files included in this package are used to recognize input devices and automatically setup default mappings between the physical device and Retropad virtual controller.

%prep
%setup -q

%build

%install
#mkdir -p %{buildroot}%{_datadir}/libretro/autoconfig
#cp udev/*.cfg %{buildroot}%{_datadir}/libretro/autoconfig

%makeinstall_std

install -Dm0644 %SOURCE1 %{buildroot}%{_datadir}/libretro/autoconfig/udev/"GAMESIR Gamesir-X2 Type-C.cfg"
install -Dm0644 %SOURCE2 %{buildroot}%{_datadir}/libretro/autoconfig/udev/"8BitDo Ultimate 2C Wireless.cfg"

%files
%doc README.md COPYING retropad_layout.png
%dir %{_datadir}/libretro/autoconfig
%{_datadir}/libretro/autoconfig/*

%changelog
* Mon Feb 02 2026 Artyom Bystrov <arbars@altlinux.org> 1.22.0-alt1
- Update to new version

* Tue Dec 23 2025 Artyom Bystrov <arbars@altlinux.org> 1.17.0-alt3
- Add config for 8BitDo Ultimate 2C Wireless.cfg

* Thu Oct  2 2025 Artyom Bystrov <arbars@altlinux.org> 1.17.0-alt2
- Add configs for handhelds (tnx ROCKNIX)

* Wed Mar 20 2024 Artyom Bystrov <arbars@altlinux.org> 1.17.0-alt1
- Initial commit for Sisyphus