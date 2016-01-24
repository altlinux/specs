Name: pcsxr
Version: 1.9.93
Release: alt2

Summary: A plugin based PlayStation (PSX) emulator with high compatibility
License: GPLv2 / Public Domain
Group: Emulators

Url: http://pcsxr.codeplex.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: %name-%version.tar.bz2

BuildRequires: glibc-devel-static
BuildRequires: intltool >= 0.35.0
BuildRequires: libSDL-devel
BuildRequires: libXtst-devel
BuildRequires: libXv-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libgtk+3-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-zope

%description
PCSX-Reloaded is an advanced PlayStation (PSX) emulator, which uses a plugin
architecture to provide full support for all components of the PSX. It has full
emulation support for game pads, videos, sound, memory cards, and other
important PSX components, and is able to play many games without problems.

%prep
%setup -n %name

%build
%autoreconf
%configure --enable-opengl
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog ChangeLog.df COPYING INSTALL NEWS README
%_bindir/%name
%dir %_libdir/games/psemu
%_libdir/games/psemu/*
%_desktopdir/%name.desktop
%_man1dir/%name.1.*
%dir %_datadir/%name
%_datadir/%name/*.png
%_datadir/%name/%name.ui
%_pixmapsdir/%name-icon.png
%dir %_datadir/psemu
%_datadir/psemu/*.ui

%changelog
* Sun Jan 24 2016 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt2
- Fix man file

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt0.M70T.1
- Build for branch t7

* Wed Oct 09 2013 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt1
- Initial build for ALT Linux

