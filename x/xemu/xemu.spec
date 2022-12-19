Name:     xemu
Version:  0.7.71
Release:  alt1

Summary:  Original Xbox Emulator for Windows, macOS, and Linux (Active Development)
License:  GPL2 LGPL2
Group:    Other
Url:      https://github.com/mborgerson/xemu

Packager: Artyom Bystrov <arbars@altlinux.org>

Source:   %name-%version.tar

BuildRequires(Pre): rpm-macros-meson rpm-build-ninja rpm-macros-ninja-build 
BuildRequires: gcc-c++ libgtk+3-devel libsamplerate-devel libSDL2-devel glib2-devel libGLU-devel libepoxy-devel libpcap-devel meson libssl-devel libpixman-devel python3-dev python3-module-yaml libxxhash-devel libslirp-devel ninja-build

ExcludeArch: %ix86 armh

%description
Original Xbox Emulator for Windows, macOS, and Linux (Active Development).

Attention! BIOS and Boot firmware are not included!

%prep
%setup

%build

  ./configure \
    --audio-drv-list="sdl" \
    --disable-debug-info \
    --enable-slirp=system \
    --extra-cflags="-DXBOX=1" \
    --target-list=i386-softmmu \
    --with-git-submodules=ignore

  make qemu-system-i386

%install
install -vDm755 build/qemu-system-i386 %buildroot%_bindir/%name
install -vDm644 -t %buildroot%_desktopdir  ui/xemu.desktop
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
* Fri Dec 16 2022 Artyom Bystrov <arbars@altlinux.org> 0.7.71-alt1
- Initial build for Sisyphus
