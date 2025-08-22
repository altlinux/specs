Name:     ares
Version:  145
Release:  alt1

Summary:  ares is a cross-platform, open source, multi-system emulator, focusing on accuracy and preservation.
License:  ISC
Group:    Emulators
Url:      https://github.com/ares-emulator/ares

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake libgtk+3-devel libSDL-devel libudev-devel libopenal-devel libXv-devel libpulseaudio-devel libGL-devel libXrandr-devel libalsa-devel libvulkan-devel ImageMagick-tools

ExclusiveArch: x86_64 aarch64

%description
ares is a multi-system emulator that began development
on October 14th, 2004. It is a descendent of higan and bsnes,
and focuses on accuracy and preservation.

%prep
%setup

%build
%cmake -DARES_SKIP_DEPS=ON
%cmake_build

%install
%cmake_install 

cp -dr --no-preserve=ownership ./mia/Database/ %buildroot%_datadir/%name/

%files
%_bindir/%name
%_bindir/sourcery
%dir %_datadir/%name/Database/
%_datadir/%name/Database/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%doc LICENSE

%changelog
* Fri Aug 22 2025 Artyom Bystrov <arbars@altlinux.org> 145-alt1
- update to new version

* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 140-alt1
- update to new version

* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 139-alt1
- update to new version

* Wed Feb 28 2024 Artyom Bystrov <arbars@altlinux.org> 136-alt1
- update to new version

* Thu Aug 31 2023 Artyom Bystrov <arbars@altlinux.org> 133-alt1
- update to new version

* Sun Jun 25 2023 Artyom Bystrov <arbars@altlinux.org> 132-alt2
- Total rework of repo - upstream not changing tag

* Thu Mar 09 2023 Artyom Bystrov <arbars@altlinux.org> 132-alt1
- new version 132

* Wed Feb 22 2023 Artyom Bystrov <arbars@altlinux.org> 131-alt1
- new version 131

* Tue Dec 20 2022 Artyom Bystrov <arbars@altlinux.org> 130.1-alt1
- Initial build for Sisyphus
