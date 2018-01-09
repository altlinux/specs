Name: snes9x
Version: 1.55
Release: alt1%ubt

Summary: Super Nintendo Entertainment System emulator
License: Distributable
Group: Emulators

Url: http://www.snes9x.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: https://github.com/snes9xgit/%name/archive/%version/%name-%version.tar.gz

BuildRequires(pre): rpm-build-ubt

BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: libSDL-devel
BuildRequires: libSM-devel
BuildRequires: libXrandr-devel
BuildRequires: libXv-devel
BuildRequires: libalsa-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libminizip-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libxml2-devel

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
./autogen.sh
%configure --with-netplay
%make_build
popd

%install
# Install CLI version
%__install -Dp -m 0755 unix/%name %buildroot%_bindir/%name

# Install GTK version
pushd gtk
%makeinstall_std
%find_lang %name-gtk
popd

%files cli
%doc docs/*.txt unix/docs/readme_unix.html
%_bindir/%name

%files gtk -f gtk/%name-gtk.lang
%doc docs/*.txt gtk/doc/lgpl.txt gtk/doc/LICENSE gtk/doc/README
%_bindir/%name-gtk
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_iconsdir/hicolor/24x24/apps/%name.png
%_niconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Jan 09 2018 Nazarov Denis <nenderus@altlinux.org> 1.55-alt1%ubt
- Version 1.55

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.53-alt0.M70P.1
- Build for branch p7

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.53-alt0.M70T.1
- Build for branch t7

* Sun Oct 06 2013 Nazarov Denis <nenderus@altlinux.org> 1.53-alt1
- Initial build for ALT Linux
