Name: snes9x
Version: 1.60
Release: alt3

Summary: Super Nintendo Entertainment System emulator
License: Distributable
Group: Emulators

Url: http://www.snes9x.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/%{name}git/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: %name-alt-gcc11.patch

BuildRequires: gcc-c++
BuildRequires: libSDL2-devel
BuildRequires: libSM-devel
BuildRequires: libXrandr-devel
BuildRequires: libXv-devel
BuildRequires: libepoxy-devel
BuildRequires: libgtk+3-devel
BuildRequires: libminizip-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libwayland-egl-devel
BuildRequires: meson

%description
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES) emulator.
It basically allows you to play most games designed for the SNES and Super Famicom
Nintendo game systems on your Mac, Linux, Windows and so on. The games include some
real gems that were only ever released in Japan.

%package cli
Summary: Super Nintendo Entertainment System emulator - CLI version
Group: Emulators

%description cli
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES) emulator.
It basically allows you to play most games designed for the SNES and Super Famicom
Nintendo game systems on your Mac, Linux, Windows and so on. The games include some
real gems that were only ever released in Japan.

%package gtk
Summary: Super Nintendo Entertainment System emulator - GTK version
Group: Emulators

%description gtk
Snes9x is a portable, freeware Super Nintendo Entertainment System (SNES) emulator.
It basically allows you to play most games designed for the SNES and Super Famicom
Nintendo game systems on your Mac, Linux, Windows and so on. The games include some
real gems that were only ever released in Japan.

This package contains a graphical user interface using GTK+.

%prep
%setup
%patch0 -p1

%build
# Build CLI version
pushd unix
./configure \
	--prefix=%_bindir \
	--enable-netplay
%make_build
popd

#build GTK version
pushd gtk
%meson
%meson_build
popd

%install
# Install CLI version
%__install -Dp -m 0755 unix/%name %buildroot%_bindir/%name

# Install GTK version
pushd gtk
%meson_install
%find_lang %name-gtk
popd

%files cli
%doc docs/*.txt unix/docs/readme_unix.html
%_bindir/%name

%files gtk -f gtk/%name-gtk.lang
%doc docs/*.txt gtk/AUTHORS
%_bindir/%name-gtk
%_datadir/%name/cheats.bml
%_desktopdir/%name-gtk.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%dir %_iconsdir/hicolor/24x24
%dir %_iconsdir/hicolor/24x24/apps
%_iconsdir/hicolor/24x24/apps/%name.png
%dir %_iconsdir/hicolor/64x64
%dir %_iconsdir/hicolor/64x64/apps
%_iconsdir/hicolor/64x64/apps/%name.png
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%_iconsdir/hicolor/128x128/apps/%name.png
%dir %_iconsdir/hicolor/256x256
%dir %_iconsdir/hicolor/256x256/apps
%_iconsdir/hicolor/256x256/apps/%name.png

%changelog
* Sun Sep 26 2021 Nazarov Denis <nenderus@altlinux.org> 1.60-alt3
- Add patch to fix compilation error in gcc11

* Fri May 03 2019 Nazarov Denis <nenderus@altlinux.org> 1.60-alt2
- Fix post-install unowned files

* Wed May 01 2019 Nazarov Denis <nenderus@altlinux.org> 1.60-alt1
- Version 1.60

* Tue Apr 30 2019 Nazarov Denis <nenderus@altlinux.org> 1.55-alt2
- Remove %ubt macro

* Tue Jan 09 2018 Nazarov Denis <nenderus@altlinux.org> 1.55-alt1%ubt
- Version 1.55

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.53-alt0.M70P.1
- Build for branch p7

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.53-alt0.M70T.1
- Build for branch t7

* Sun Oct 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.53-alt1
- Initial build for ALT Linux
