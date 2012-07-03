Name: pcsx-df
Version: 1.816
Release: alt2
Summary: Sony PlayStation emulator -- binary
License: GPL2
Group: Emulators
Url: http://packages.debian.org/pcsx-df
Conflicts: pcsx

#FIXME build for x86_64
ExclusiveArch: i586

Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://ftp.de.debian.org/debian/pool/main/p/pcsx-df/%{name}_%version.orig.tar
#.gz
Source1: README.Debian
Patch1: %name-alt-build.patch

# Automatically added by buildreq on Mon Sep 13 2010
BuildRequires: bzlib-devel gcc-c++ libXext-devel libXv-devel libalsa-devel libglade-devel nasm zlib-devel

%description
PCSX-df is an advanced PlayStation (PSX) emulator, which uses a plugin
architecture to provide full support for all components of the PSX. It has
full emulation support for gamepads, videos, sound, memory cards, and other
important PSX components, and is able to play many games without problems.

This package provides the main PCSX-df binary, library, and support files.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure
make

%install
%makeinstall_std
cp -a %SOURCE1 .

%find_lang %name
#hard to fix
%add_verify_elf_skiplist %_libdir/libpcsxcore.so.0.0.0

%files -f %name.lang
%doc AUTHORS COPYING ChangeLog NEWS README*
%_bindir/*
%_libdir/lib*so.*
%_libdir/games/psemu
%_desktopdir/*desktop
%_man1dir/*
%_pixmapsdir/*
%_datadir/pcsx
%_datadir/psemu

%changelog
* Tue Apr 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.816-alt2
- fix build

* Mon Sep 13 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.816-alt1
- initial build for ALT Linux Sisyphus
