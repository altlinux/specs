Name: dolphin-emu
Version: 5.0
Release: alt1.rc.1

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://ru.%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

Source: dolphin-%version-rc.tar.gz
Patch0: %name-%version-rc-alt-git.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libSFML-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXcursor-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: libao-devel
BuildRequires: libavformat-devel
BuildRequires: libbluez-devel
BuildRequires: libevdev-devel
BuildRequires: libgtk+2-devel
BuildRequires: liblzo2-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libopenal-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsoil-devel
BuildRequires: libsoundtouch-devel
BuildRequires: libswscale-devel
BuildRequires: libudev-devel
BuildRequires: libusb-devel

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n dolphin-%version-rc
%patch0 -p1

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
%find_lang %name

%files -f %name.lang
%_bindir/*
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/%name.xpm

%changelog
* Sat Feb 20 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0-alt1.rc.1
- rebuilt against libSoundTouch.so.1

* Mon Aug 03 2015 Nazarov Denis <nenderus@altlinux.org> 5.0-alt1.rc
- Version 5.0 RC

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
