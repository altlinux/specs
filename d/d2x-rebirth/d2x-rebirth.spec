Summary: The port of Descent 2 for Linux
Name: d2x-rebirth
Version: 0.57.3
Release: alt1
License: GPL
Group: Games/Arcade
Url: http://www.dxx-rebirth.de/
Source: %{name}_v%version-src.tar.gz
Source1: %name.png
Source2: D2XBDE01.zip
Patch: %{name}_v0.55.1-overflow.patch

# Automatically added by buildreq on Mon Nov 03 2008
BuildRequires: dos2unix gcc-c++ libGL-devel libSDL-devel libSDL_mixer-devel libphysfs-devel scons unzip

%description
This is the port of Descent 2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need some datafiles installed in
%_gamesdatadir/descent2 See dxx-readme.txt.

%package sdl
Group: Games/Arcade
Summary: Descent 2 for Linux, SDL version
Requires: d2x-rebirth = %version
Conflicts: d2x-rebirth-gl

%description sdl
This is the port of Descent 2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999
by Parallax Software Corporation.

To use this package you'll need some datafiles installed in
/usr/share/games/descent2. See dxx-readme.txt.

This version uses SDL for Audio, Input/Output and graphics
rendering.

You may use SHAREWARE version of descent with d2x
You can get it from here:
http://download.descent-network.com/shareware1/descent2/playable/d2shar10.exe
and unrar like this:
unrar x -cl d2shar10.exe /usr/share/games/descent2

%package gl
Group: Games/Arcade
Summary: Descent 2 for Linux, OpenGL version
Requires: d2x-rebirth = %version
Conflicts: d2x-rebirth-sdl

%description gl
This is the port of Descent 2, the famous 3D game for PC.

D2X is based on source code that was released the 14 December 1999 by
Parallax Software Corporation.

To use this package you'll need some datafiles installed in
/usr/share/games/descent2.  See dxx-readme.txt.

This version uses SDL for Audio and Input/Output and OpenGL for
graphics rendering.

You may use SHAREWARE version of descent with d2x
You can get it from here:
http://download.descent-network.com/shareware1/descent2/playable/d2shar10.exe
and unrar like this:
unrar x -cl d2shar10.exe /usr/share/games/descent2

%prep
%setup -n %{name}_v%version-src -a2
#patch -p0

dos2unix     d2x.ini *.txt
chmod 644 d2x.ini *.txt
sed -i '/MAX_MULTI_MESSAGE_LEN+4/s/MAX_MULTI_MESSAGE_LEN+4/MAX_MULTI_MESSAGE_LEN+22/' main/multi.h
sed -i '/MAX_MULTI_MESSAGE_LEN+4/s/MAX_MULTI_MESSAGE_LEN+4/MAX_MULTI_MESSAGE_LEN+22/' main/multi.c

%build
# d2x-sdl
scons -j%__nprocs \
	sharepath=%_gamesdatadir/descent2 \
	sdl_only=1 \
	sdlmixer=1 \
	no_asm=1
mv d2x-rebirth d2x-rebirth-sdl

# d2x-gl
scons -c
scons -j%__nprocs \
	sharepath=%_gamesdatadir/descent2 \
	sdlmixer=1 \
	PREFIX=%buildroot%prefix
mv d2x-rebirth d2x-rebirth-gl

%install
# binaries
install -dm 755 %buildroot%_gamesbindir/
install -m 755 d2x-rebirth-gl %buildroot%_gamesbindir/
install -m 755 d2x-rebirth-sdl %buildroot%_gamesbindir/

install -dm 755 %buildroot%_gamesdatadir/descent2
# german translations
install -m 644 D2XBDE01/D2XbDE01/*.txb %buildroot%_gamesdatadir/descent2
install -m 644 D2XBDE01/*.txt %buildroot%_gamesdatadir/descent2
# directory for original descent data
install -dm 755 %buildroot%_gamesdatadir/descent2/missions

# man-pages
install -dm 755 %buildroot%_mandir/man1/
install  -m 644 libmve/*.1 %buildroot%_mandir/man1/

# icon
install -dm 755 %buildroot%_datadir/pixmaps
install -m 644 %SOURCE1 %buildroot%_datadir/pixmaps

# menu
install -dm 755 %buildroot%_desktopdir
cat > %name-sdl.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=D2x (SDL version)
Comment=The port of Descent 2 for Linux
Exec=%_gamesbindir/d2x-rebirth-sdl
Icon=%name
Categories=Game;ActionGame;
EOF
install -m 644 %name-sdl.desktop %buildroot%_desktopdir

cat > %name-gl.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=D2x (OpenGL version)
Comment=The port of Descent 2 for Linux
Exec=%_gamesbindir/d2x-rebirth-gl
Icon=%name
Categories=Game;ActionGame;
EOF
install -m 644 %name-gl.desktop %buildroot%_desktopdir

%files
%doc *.txt *.plist *.ini
%dir %_gamesdatadir/descent2
%_gamesdatadir/descent2/*.txb
%_gamesdatadir/descent2/*.txt
%dir %_gamesdatadir/descent2/missions
%_man1dir/*
%_datadir/pixmaps/%name.png

%files sdl
%doc COPYING*
%_gamesbindir/d2x-rebirth-sdl
%_desktopdir/%name-sdl.desktop

%files gl
%doc COPYING*
%_gamesbindir/d2x-rebirth-gl
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

* Sat Oct 02 2010 Fr. Br. George <george@altlinux.ru> 0.56-alt1
- Autobuild version bump to 0.56

* Sun Dec 13 2009 Fr. Br. George <george@altlinux.ru> 0.55.1-alt2
- Fix build with new gcc overflow check eature

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.55.1-alt1
- Version up

* Sun Jan 04 2009 Fr. Br. George <george@altlinux.ru> 0.55-alt1
- Version up

* Mon Nov 03 2008 Fr. Br. George <george@altlinux.ru> 0.54-alt1
- Initial build from SuSE

* Sun Jun 29 2008 Toni Graffy <toni@links2linux.de> - 0.54-0.pm.1
- update to 0.54
* Mon Dec 03 2007 Toni Graffy <toni@links2linux.de> - 0.53-0.pm.2
- rebuild with new physfs(-devel) 1.1.1
* Thu Oct 25 2007 Toni Graffy <toni@links2linux.de> - 0.53-0.pm.1
- update to 0.53
* Sun May 06 2007 Toni Graffy <toni@links2linux.de> - 0.52-0.pm.1
- update to 0.52
* Fri Feb 16 2007 Toni Graffy <toni@links2linux.de> - 0.51-0.pm.1
- update to 0.51
* Sat Nov 11 2006 Toni Graffy <toni@links2linux.de> - 0.50-0.pm.1
- initial package 0.50
