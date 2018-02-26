# FIXME (there is generated asm)
%set_verify_elf_method textrel=relaxed

Name: tuxvsclippy
Version: 0.2.5
Release: alt3.1

Summary: Tux vs Clippy originated as an xbox game

Group: Games/Arcade
License: GPL
Url: http://www.stolk.org/xgame/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://bram.creative4vision.nl/xgame/%name-%version.tar
Source1: http://bram.creative4vision.nl/xgame/%name-data.tar
Patch: %name-linking.patch
Patch1: %name-gcc43.patch
Patch2: %name-0.2.5-alt-DSO.patch

ExclusiveArch: %{ix86}

%add_findprov_lib_path %_libdir/%name

# Automatically added by buildreq on Fri Sep 02 2011
# optimized out: libICE-devel libX11-devel libXext-devel libstdc++-devel xorg-xf86dgaproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel imake libSDL-devel libSM-devel libXxf86dga-devel libjpeg-devel libtiff-devel xorg-cf-files zlib-devel

%description
Tux vs Clippy originated as an xbox game.
It was the first ever xbox game to be released without microsoft licensing,
but it required an xbox that had been modified to accept unsigned binaries.

The game requires an x86 GNU/Linux system to run. Because it makes
heavy use of assembly code, it is not portable to other processors.
Also, because of the precompiled sprite system, screen resolution
is not scalable. Under X11 you may see large borders.

%prep
%setup
%patch
%patch1
%patch2 -p2
touch NEWS AUTHORS

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

#install -D -m 0644 %name.png %buildroot%_datadir/icons/%name.png

# data files
tar -x -C %buildroot%prefix -f %SOURCE1
mkdir -p %buildroot%_libdir/%name/
mv %buildroot%_datadir/%name/sprite %buildroot%_libdir/%name/sprite

mkdir -p %buildroot%_desktopdir
cat >%buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Tuxvsclippy
GenericName=
Comment=Tux vs clippy
Icon=%name.png
Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc CREDITS README TODO ChangeLog
%_bindir/*
%_libdir/%name/
%_datadir/%name/
%_desktopdir/*

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt3.1
- Fixed build

* Fri Sep 02 2011 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt3
- cleanup spec, update buildreqs

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt2
- fix build with gcc 4.3

* Sun Jun 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.2.5-alt1
- new version 0.2.5
- replace menu file with desktop
- rewrote linking patch
- update buildreqs

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt3
- fix build

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt2
- fix building, move binary sprites to lib

* Wed Dec 15 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2.4-alt1
- new version
- cleanup spec
- fix dir packaging

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.2.3-alt2.1
- Rebuilt with libtiff.so.4.

* Fri Apr 30 2004 Kachalov Anton <mouse@altlinux.ru> 0.2.3-alt2
- rebuild in hasher

* Fri Mar 28 2003 Kachalov Anton <mouse@altlinux.ru> 0.2.3-alt1
- build for Sisyphus

* Sat Mar 08 2003 avl <avl@altlinux.ru> 0.2.3-alt
- initial RPM
