Name: xonotic
Version: 0.6.0
Release: alt1

Summary: A free multi-player first person shooter
Group: Games/Arcade
License: GPLv2+
Url: http://www.xonotic.org/

Source0: Xonotic.tar.bz2

Requires: %name-data = %version

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Sat Oct 20 2012
BuildRequires: libSDL-devel libXext-devel libXpm-devel libXxf86vm-devel libalsa-devel libjpeg-devel

%description
Xonotic is a free (GPL), fast-paced first-person shooter that works on 
Microsoft Windows, Mac OSX and Linux.

Xonotic is a direct successor of the Nexuiz Project.

It features much better quality graphics and visual effects.

Xonotic places focus on community involvement as its principal driving force
and structures itself to respect that. The aim of Xonotic is to become the 
best possible open-source FPS (first-person-shooter) of its kind.

%prep
%setup -q -n Xonotic

%build
cd source/darkplaces
make clean
%make_build release CPUOPTIMIZATIONS="%optflags" DP_FS_BASEDIR=%_datadir/%name

%install
install -D -m 755 source/darkplaces/darkplaces-sdl %buildroot%_bindir/%name-sdl
install -D -m 755 source/darkplaces/darkplaces-glx %buildroot%_bindir/%name-glx

install -D -m 644 misc/logos/icons_png/%{name}_16.png %buildroot%_iconsdir/hicolor/16x16/apps/%name.png
install -D -m 644 misc/logos/icons_png/%{name}_32.png %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
install -D -m 644 misc/logos/icons_png/%{name}_64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D -m 644 misc/logos/icons_png/%{name}_128.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png

install -D -m 644 misc/logos/%{name}_icon.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

install -d %buildroot%_datadir/applications

cat > %buildroot%_datadir/applications/%name-sdl.desktop << EOF
[Desktop Entry]
Name=Xonotic-SDL
Comment=Multi-player first person shooter (SDL)
Exec=%_bindir/%name-sdl
Icon=%name
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_datadir/applications/%name-glx.desktop << EOF
[Desktop Entry]
Name=Xonotic-GLX
Comment=Multi-player first person shooter (GLX)
Exec=%_bindir/%name-glx
Icon=%name
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;
EOF

%files
%_bindir/%name-sdl
%_bindir/%name-glx
%_datadir/applications/%name-sdl.desktop
%_datadir/applications/%name-glx.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/apps/%name.svg

%changelog
* Sat Oct 20 2012 Igor Zubkov <icesik@altlinux.org> 0.6.0-alt1
- build for Sisyphus

