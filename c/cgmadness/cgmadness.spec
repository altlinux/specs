Name:		cgmadness
Version:	1.3
Release:	alt3
Summary:	Marble Madness inspired amrble-and-platforms game
Group:		Games/Puzzles
License:	GPL
Source:		%name-%version-src.tar.bz2
Patch:		cgmadness-1.3-sysgrapple.patch
Patch1:		cgmadness-1.3-unused.patch
URL:		http://www.fluxparticle.com/cgmadness/

# TODO extra levels package

# Automatically added by buildreq on Sun Sep 11 2011
# optimized out: fontconfig libGL-devel libGLU-devel libstdc++-devel
BuildRequires: ImageMagick-tools gcc-c++ libGLUT-devel libglew-devel libgrapple-devel

%description
CG Madness is based on the classic game Marble Madness. It is running on
OpenGL and uses current CG techniques like light maps, bump-mapping and
reflection shader. It also has an editor where you can create your own
levels. If you have done so and you want to share the level, you can
upload it.

%prep
%setup -n %name
rm -rf libgrapple
ln -s %_includedir/grapple libgrapple
%patch -p1
%patch1 -p1

cat > %name.sh <<@@@
#!/bin/sh
test -d "\$HOME/.%name" || {
rm -f "\$HOME/.%name"
mkdir -p "\$HOME/.%name/levels" "\$HOME/.%name/data"
cd "\$HOME/.%name"
ln -s %_gamesdatadir/%name/*.* .
ln -s %_gamesdatadir/%name/data/* data/
ln -s %_gamesdatadir/%name/levels/* levels/
}
cd "\$HOME/.%name"
exec %name.bin
@@@

cat > %name.desktop <<@@@
[Desktop Entry]
Name=CG Madness
GenericName=Marble and platforms game
Comment=%summary
Icon=%name
Exec=%name
Terminal=false
StartupNotify=false
Categories=Game;ArcadeGame;
@@@

%build
%make_build

convert data/logo.tga -crop 120x128 128.png
mv 128-0.png 128.png
for N in 16 32 48 64; do
  convert 128.png -resize ${N}x${N} $N.png
done

%install
# TODO patch "tar" section of Makefile for installation
install -D cgmadness %buildroot%_gamesbindir/cgmadness.bin
install -m755 cgmadness.sh %buildroot%_gamesbindir/cgmadness
install dedicated_server convert-cgm %buildroot%_gamesbindir/
mkdir -p %buildroot%_gamesdatadir/%name
cp -a data levels *.txt *.vert *.frag %buildroot%_gamesdatadir/%name/
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
for N in 128 16 32 48 64; do
  install -D $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc *.txt
%_gamesbindir/*
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 1.3-alt3
- Fix gcc4.6 build

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.3-alt2
- DSO list completion

* Mon Sep 12 2011 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Initial build from scratch


