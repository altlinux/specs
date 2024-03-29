Name: punesemu
Version: 0.110
Release: alt3

Summary: Qt-based NES emulator and NSF/NSFe Music Player
License: GPLv2
Group: Emulators

Url: https://github.com/punesemu/puNES
Source: %name-%version.tar
Patch1: punesemu-va_list-fix.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake gcc-c++
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: qt5-svg-devel
BuildRequires: libalsa-devel libudev-devel
BuildRequires: libX11-devel libXrandr-devel libXext-devel
BuildRequires: p7zip
BuildRequires: libavcodec-devel libavformat-devel
BuildRequires: libavutil-devel libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libGLU-devel

ExcludeArch: armh


%description
Qt-based Nintendo Entertaiment System emulator and NSF/NSFe Music Player 
(Linux, FreeBSD, OpenBSD and Windows)

%prep
%setup
%patch1 -p1


%build
%cmake 
%cmake_build

%install
%cmakeinstall_std
rm -rf %buildroot/usr/share/doc/puNES/

%files
%doc AUTHORS ChangeLog INSTALL NEWS README.md
%_bindir/*
%_desktopdir/io.github.punesemu.puNES.desktop
%_iconsdir/hicolor/16x16/apps/io.github.punesemu.puNES.png
%_iconsdir/hicolor/22x22/
%_iconsdir/hicolor/24x24/
%_iconsdir/hicolor/32x32/apps/io.github.punesemu.puNES.png
%_iconsdir/hicolor/48x48/apps/io.github.punesemu.puNES.png
%_iconsdir/hicolor/64x64/
%_iconsdir/hicolor/256x256/
%_iconsdir/hicolor/512x512/
%_datadir/metainfo/

%changelog
* Thu Dec 07 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.110-alt3
- NMU: cleaned up build requirements for real (libudev-devel should be
  used, not libudev0). Fixes FTBFS on LoongArch.

* Wed Dec 06 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.110-alt2
- NMU: fixed FTBFS on aarch64 (va_list is NOT a pointer there).
  While at it cleaned up build requirements (libudev-devel should be
  used, not libudev0). Fixes FTBFS on LoongArch.

* Mon Dec 04 2023 Alexey Shemyakin <alexeys@altlinux.org> 0.110-alt1
- Inital build for ALT.

