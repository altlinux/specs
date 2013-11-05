Name: dolphin-emu
Version: 4.0.1
Release: alt1

Summary: The Gamecube / Wii Emulator
License: GPLv2
Group: Emulators

Url: https://ru.%name.org/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libGLEW-devel >= 1.8
BuildRequires: libSDL2-devel
BuildRequires: libXdamage-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXi-devel >= 1.5.0
BuildRequires: libXmu-devel
BuildRequires: libXrandr-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libalsa-devel
BuildRequires: libao-devel
BuildRequires: libavformat-devel
BuildRequires: libbluez-devel
BuildRequires: libgomp-devel
BuildRequires: libgtk+2-devel
BuildRequires: liblzo2-devel
BuildRequires: libminiupnpc-devel
BuildRequires: libopenal-devel
BuildRequires: libpolarssl-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libsfml-devel
BuildRequires: libsoil-devel
BuildRequires: libswscale-devel
BuildRequires: libusb-devel
BuildRequires: libwxGTK2.9-devel

%description
Dolphin-emu is a emulator for Gamecube, Wii, Triforce that lets
you run Wii/GCN/Tri games on your Windows/Linux/Mac PC system.

%prep
%setup -n %name
%patch0 -p1

%build
%cmake
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/%name
%_pixmapsdir/%name.xpm

%changelog
* Tue Nov 05 2013 Nazarov Denis <nenderus@altlinux.org> 4.0.1-alt1
- Initial build for ALT Linux
