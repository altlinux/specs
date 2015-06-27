Name: dolphin-emu
Version: 4.0.2
Release: alt4.git20150715

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://ru.%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

Source: dolphin-%version.tar.gz
Patch0: %name-%version-alt.patch
Patch1: %name-4.0.2-alt-gtk3.patch
Patch2: %name-4.0.2-alt-polarssl.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: libao-devel
BuildRequires: libavformat-devel
BuildRequires: libavresample-devel
BuildRequires: libbluez-devel
BuildRequires: libgomp-devel
BuildRequires: libgtk+3-devel
BuildRequires: liblzo2-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libopenal-devel
BuildRequires: libmbedtls-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsfml-devel
BuildRequires: libsoil-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libwxGTK3.1-devel
BuildRequires: libyui-devel
BuildRequires: libpixman-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libexpat-devel
BuildRequires: libxshmfence-devel
BuildRequires: libpng-devel
BuildRequires: libXinerama-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libepoxy-devel
BuildRequires: libudev-devel
BuildRequires: libevdev-devel

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n dolphin-%version
#patch0 -p1
#patch1 -p2
#patch2 -p2

%build
%add_optflags -fpermissive
%cmake -Wno-dev
%make_build -C BUILD VERBOSE=1

%install
%makeinstall_std -C BUILD
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/%name.xpm

%changelog
* Thu Jul 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt4.git20150715
- New snapshot

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt3.git5fafcb6.1
- Rebuilt with wxGTK3.1 (instead of wxGTK3.0) & gtk+3 (gtk+2)

* Wed Sep 17 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt3.git5fafcb6
- Version from git (commit 5fafcb6)
- Rebuild with new polarssl and GLEW

* Tue Apr 22 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt2
- Rebuild with new polarssl

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Wed Nov 20 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt3
- Rebuild with wxGTK 3.0

* Mon Nov 11 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt2
- Fix build

* Tue Nov 05 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt1
- Initial build for ALT Linux
