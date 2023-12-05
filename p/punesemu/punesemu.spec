Name: punesemu
Version: 0.110
Release: alt1

Summary: Qt-based NES emulator and NSF/NSFe Music Player
License: GPLv2
Group: Emulators

Url: https://github.com/punesemu/puNES
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake gcc-c++
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: qt5-svg-devel
BuildRequires: libalsa-devel libudev0
BuildRequires: libX11-devel libXrandr-devel libXext-devel
BuildRequires: p7zip
BuildRequires: libavcodec-devel libavformat-devel
BuildRequires: libavutil-devel libswresample-devel
BuildRequires: libswscale-devel
BuildRequires: libGLU-devel

ExcludeArch: armh aarch64


%description
Qt-based Nintendo Entertaiment System emulator and NSF/NSFe Music Player 
(Linux, FreeBSD, OpenBSD and Windows)

%prep
%setup


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
* Mon Dec 04 2023 Alexey Shemyakin <alexeys@altlinux.org> 0.110-alt1
- Inital build for ALT.

