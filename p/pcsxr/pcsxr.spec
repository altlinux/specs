%add_optflags -fcommon

Name: pcsxr
Version: 1.9.95
Release: alt1.2

Summary: A plugin based PlayStation (PSX) emulator with high compatibility
License: GPLv3
Group: Emulators

Url: http://pcsxr.codeplex.com/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExcludeArch: ppc64le

Source: %name-%version.tar.bz2
Patch0: %name-zlib-alt.patch
Patch1: %name-loadconfig.patch
Patch2: %name-helpabout.patch
Patch3: %name-confdlg-updategui.patch
Patch4: %name-dfcdrom-opencdhandle.patch

BuildRequires: glibc-devel-static
BuildRequires: intltool >= 0.35.0
BuildRequires: libSDL-devel
BuildRequires: libXtst-devel
BuildRequires: libXv-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libgtk+3-devel
BuildRequires: python-modules-compiler

%description
PCSX-Reloaded is an advanced PlayStation (PSX) emulator, which uses a plugin
architecture to provide full support for all components of the PSX. It has full
emulation support for game pads, videos, sound, memory cards, and other
important PSX components, and is able to play many games without problems.

%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%add_optflags -Wno-error=implicit-function-declaration -Wno-error=int-conversion
%__mkdir include
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
* Sat Jul 04 2026 Nazarov Denis <nenderus@altlinux.org> 1.9.95-alt1.2
- Fix FTBFS

* Wed Nov 06 2024 Nazarov Denis <nenderus@altlinux.org> 1.9.95-alt1.1
- Fix FTBFS

* Sun Dec 13 2020 Nazarov Denis <nenderus@altlinux.org> 1.9.95-alt1
- Version 1.9.95

* Sat Mar 02 2019 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt3
- Rename uncompress2 to avoid conflict with zlib (ALT #36177)

* Sun Jan 24 2016 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt2
- Fix man file

* Wed Oct 16 2013 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt0.M70T.1
- Build for branch t7

* Wed Oct 09 2013 Nazarov Denis <nenderus@altlinux.org> 1.9.93-alt1
- Initial build for ALT Linux

