Name:           retroarch-joypad-autoconfig
Version:        1.17.0
Release:        alt1
Summary:        RetroArch Joypad Autoconfig Files
License:        MIT
Group:          Emulators
URL:            https://github.com/libretro/retroarch-joypad-autoconfig

Source:         %{name}-%{version}.tar
Source1:        GAMESIR_Gamesir-X2_Type-C.cfg

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

install -Dm0644 %SOURCE1 %{buildroot}%{_datadir}/libretro/autoconfig/udev

%files
%doc README.md COPYING
%dir %{_datadir}/libretro/autoconfig
%{_datadir}/libretro/autoconfig/*

%changelog
* Wed Mar 20 2024 Artyom Bystrov <arbars@altlinux.org> 1.17.0-alt1
- Initial commit for Sisyphus