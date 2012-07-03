Summary: The port of Descent for Linux
Name: d1x-rebirth
Version: 0.57.3
Release: alt1
License: GPL
Group: Games/Arcade
Url: http://www.dxx-rebirth.com
Source: %{name}_v%version-src.tar.gz
Source1: %name.png
Source2: http://www.dxx-rebirth.com/download/dxx/res/d1xrdata.zip
Packager: Fr. Br. George <george@altlinux.ru>
Obsoletes: d1x-common

# Automatically added by buildreq on Mon Nov 10 2008
BuildRequires: dos2unix gcc-c++ libGL-devel libSDL-devel libSDL_mixer-devel libphysfs-devel scons

%description
This is the port of Descent, the famous 3D game for PC.

D1X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need some datafiles installed in
%_gamesdatadir/descent

%package sdl
Group: Games/Arcade
Summary: Descent 1 for Linux, SDL version
Requires: d1x-rebirth = %version
Conflicts: d1x-rebirth-gl
Obsoletes: d1x-sdl-full d1x-sdl-shareware

%description sdl
This is the port of Descent 1, the famous 3D game for PC.

D1X is based on source code that was released the 14 December 1999
by Parallax Software Corporation.

To use this package you'll need some datafiles installed in
/usr/share/games/descent.

This version uses SDL for Audio, Input/Output and graphics
rendering.

You may use SHAREWARE version of descent with d1x-rebirth-shareware-sdl
You can get it from here:
http://download.descent-network.com/shareware1/descent1/playable/d1shar14.exe
and unrar like this:
unrar x -cl d1shar14.exe /usr/share/games/descent-shareware

%package gl
Group: Games/Arcade
Summary: Descent 1 for Linux, OpenGL version
Requires: d1x-rebirth = %version
Conflicts: d1x-rebirth-sdl
Obsoletes: d1x-gl-full d1x-gl-shareware

%description gl
This is the port of Descent 1, the famous 3D game for PC.

d1X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need some datafiles installed in
/usr/share/games/descent.  See dxx-readme.txt.

This version uses SDL for Audio and Input/Output and OpenGL for
graphics rendering.

You may use SHAREWARE version of descent with d1x-rebirth-shareware-gl
You can get it from here:
http://download.descent-network.com/shareware1/descent1/playable/d1shar14.exe
and unrar like this:
unrar x -cl d1shar14.exe /usr/share/games/descent-shareware

%prep
%setup -n %{name}_v%version-src
dos2unix     d1x.ini *.txt
chmod 644 d1x.ini *.txt

%build
# d1x-shareware-sdl
scons -j%__nprocs \
	sharepath=%_gamesdatadir/descent \
	sdl_only=1 \
	shareware=1 \
	sdlmixer=1 \
	no_asm=1
mv d1x-rebirth d1x-rebirth-shareware-sdl

# d1x-sdl
scons -j%__nprocs \
	sharepath=%_gamesdatadir/descent \
	sdl_only=1 \
	sdlmixer=1 \
	no_asm=1
mv d1x-rebirth d1x-rebirth-sdl

# d1x-shareware-gl
scons -c
scons -j%__nprocs \
	sharepath=%_gamesdatadir/descent-shareware \
	sdlmixer=1 \
	shareware=1 \
	PREFIX=%buildroot%prefix
mv d1x-rebirth d1x-rebirth-shareware-gl

# d1x-gl
scons -c
scons -j%__nprocs \
	sharepath=%_gamesdatadir/descent \
	sdlmixer=1 \
	PREFIX=%buildroot%prefix
mv d1x-rebirth d1x-rebirth-gl

%install
# binaries
install -dm 755 %buildroot%_gamesbindir/
install -m 755 d1x-rebirth-gl %buildroot%_gamesbindir/
install -m 755 d1x-rebirth-shareware-gl %buildroot%_gamesbindir/
install -m 755 d1x-rebirth-sdl %buildroot%_gamesbindir/
install -m 755 d1x-rebirth-shareware-sdl %buildroot%_gamesbindir/

install -dm 755 %buildroot%_gamesdatadir/descent
install -dm 755 %buildroot%_gamesdatadir/descent-shareware

# directory for original descent data
install -dm 755 %buildroot%_gamesdatadir/descent/missions

# icon
install -dm 755 %buildroot%_datadir/pixmaps
install -m 644 %SOURCE1 %buildroot%_datadir/pixmaps

# menu
install -dm 755 %buildroot%_desktopdir
cat > %name-sdl.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=d1x (SDL version)
Comment=The port of Descent 1 for Linux
Exec=%_gamesbindir/d1x-rebirth-sdl
Icon=%name
Categories=Game;ActionGame;
EOF

cat > %name-gl.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=d1x (OpenGL version)
Comment=The port of Descent 1 for Linux
Exec=%_gamesbindir/d1x-rebirth-gl
Icon=%name
Categories=Game;ActionGame;
EOF

sed 's/rebirth/rebirth-shareware/g' %name-gl.desktop > %name-shareware-gl.desktop
sed 's/rebirth/rebirth-shareware/g' %name-sdl.desktop > %name-shareware-sdl.desktop

install -m 644 %name-sdl.desktop %buildroot%_desktopdir
install -m 644 %name-gl.desktop %buildroot%_desktopdir
install -m 644 %name-shareware-gl.desktop %buildroot%_desktopdir
install -m 644 %name-shareware-sdl.desktop %buildroot%_desktopdir
install %SOURCE2 %buildroot%_gamesdatadir/descent/

%files
%doc *.txt *.plist *.ini
%dir %_gamesdatadir/descent
%_gamesdatadir/descent/*
%dir %_gamesdatadir/descent-shareware
%dir %_gamesdatadir/descent/missions
%_datadir/pixmaps/%name.png

%files sdl
%doc COPYING*
%_gamesbindir/d1x-rebirth-sdl
%_gamesbindir/d1x-rebirth-shareware-sdl
%_desktopdir/%name-shareware-sdl.desktop
%_desktopdir/%name-sdl.desktop

%files gl
%doc COPYING*
%_gamesbindir/d1x-rebirth-gl
%_gamesbindir/d1x-rebirth-shareware-gl
%_desktopdir/%name-shareware-gl.desktop
%_desktopdir/%name-gl.desktop

%changelog
* Fri Jun 08 2012 Fr. Br. George <george@altlinux.ru> 0.57.3-alt1
- Autobuild version bump to 0.57.3

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 0.57.2-alt1
- Autobuild version bump to 0.57.2

* Tue Jul 19 2011 Fr. Br. George <george@altlinux.ru> 0.57.1-alt1
- Autobuild version bump to 0.57.1

* Tue Jun 28 2011 Fr. Br. George <george@altlinux.ru> 0.57-alt1
- Autobuild version bump to 0.57

* Fri Oct 01 2010 Fr. Br. George <george@altlinux.ru> 0.56-alt1
- Autobuild version bump to 0.56

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.55.1-alt1
- Version up

* Mon Nov 03 2008 Fr. Br. George <george@altlinux.ru> 0.54-alt1
- Initial build

