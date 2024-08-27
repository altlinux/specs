Name:     xemu
Version:  0.7.132
Release:  alt1

Summary:  Original Xbox Emulator
# The license is essentially the same as that of the QEMU project.
License:  GPL-2.0-only AND GPL-2.0-or-later AND MIT AND LGPL-2.1-or-later AND MIT
Group:    Emulators
Url:      https://github.com/mborgerson/xemu

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires: gcc-c++ libgtk+3-devel libsamplerate-devel libSDL2-devel glib2-devel libGLU-devel libepoxy-devel libpcap-devel meson libssl-devel libpixman-devel python3-dev python3-module-yaml libxxhash-devel libslirp-devel ninja-build

# Xemu does not support ILP32 systems.
ExcludeArch: %ix86 %arm

%description
Original Xbox Emulator for Windows, macOS, and Linux (Active Development).

Attention! BIOS and Boot firmware are not included!

%prep
%setup

%build
./configure \
	--audio-drv-list="sdl" \
	--disable-debug-info \
	--extra-cflags="-DXBOX=1" \
	--target-list=i386-softmmu \
	--with-git-submodules=ignore

make qemu-system-i386

%install
install -vDm755 build/qemu-system-i386 %buildroot%_bindir/%name
install -vDm644 -t %buildroot%_desktopdir ui/xemu.desktop
for size in 24 32 48 256 512; do
  install -vDm644 "ui/icons/xemu_${size}x${size}.png" "%buildroot%_iconsdir/hicolor/${size}x${size}/apps/%name.png"
done
install -vDm644 -t "%buildroot%_iconsdir/hicolor/scalable/apps" ui/icons/xemu.svg

%files
%_bindir/%name
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/xemu.svg
%_desktopdir/xemu.desktop
%doc README.md LICENSE

%changelog
* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 0.7.132-alt1
- Update to new version

* Thu Mar 14 2024 Artyom Bystrov <arbars@altlinux.org> 0.7.119-alt1
- Update to new version

* Mon Aug 21 2023 Artyom Bystrov <arbars@altlinux.org> 0.7.111-alt1
- Update to new version

* Mon Jul 31 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.7.109-alt2
- NMU:
  + Removed the redundant use of the %%set_autoconf_version macro (this project
  doesn't use autoconf at all!).
  + Fixed the License: tag (GPL2 LGPL2 -> GPL-2.0-only AND GPL-2.0-or-later AND
  MIT AND LGPL-2.1-or-later AND MIT).
  + Fixed the Group: tag (Other -> Emulators).
  + Removed redundant BuildRequires(Pre) requirements (this spec currently
  utilizes exclusively the basic macros provided by the rpm-build).

* Sat Jul 29 2023 Artyom Bystrov <arbars@altlinux.org> 0.7.109-alt1
- Update to new version

* Mon Jun 26 2023 Artyom Bystrov <arbars@altlinux.org> 0.7.96-alt1
- Update to new version

* Fri Dec 16 2022 Artyom Bystrov <arbars@altlinux.org> 0.7.71-alt1
- Initial build for Sisyphus
