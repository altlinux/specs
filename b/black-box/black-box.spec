Name: black-box
License: GPL v2 or later
Group: Games/Puzzles
Summary: Guess where the crystals are hidden, by watching your shots
Version: 1.4.8
Release: alt1
Url: http://www.linux-games.com/black-box/
Source: %name-%version.tar.bz2
Source1: %name.desktop
Patch: black-box-1.4.7.patch
Patch1: black-box-1.4.7-uninitialized.patch
Patch2: black-box-1.4.8-range.patch
# /*G*/ We probably do not need this
Patch3: black-box-1.4.8-strictrange.patch
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Jan 04 2009
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel ImageMagick

%description
There's a black box. You can shoot in and watch, where the shot leaves the box. In the box, crystals are reflecting the shots. You have to guess where the crystals are hidden, by watching your shots.

Authors:
--------
    Karl Bartel <karlb@gmx.net>

%prep
%setup
%patch
#patch1
%patch2
#patch3

%build
#aclocal
#automake -a
#autoconf
%autoreconf
#CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" ./configure --prefix=/usr
%configure
%make
convert -bordercolor transparent -border 7 data/gfx/box.gif 64.png

%install
#make DESTDIR=$RPM_BUILD_ROOT install
%makeinstall
install -D 64.png %buildroot/%_iconsdir/hicolor/64x64/apps/%name.png
install -D %SOURCE1 %buildroot/%_desktopdir/%name.dsektop

%files
%doc AUTHORS COPYING ChangeLog README NEWS
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*
%_iconsdir/hicolor/64x64/apps/%name.png
%_desktopdir/%name.dsektop

%changelog
* Sun Jan 04 2009 Fr. Br. George <george@altlinux.ru> 1.4.8-alt1
- Version up

* Sun Jan 04 2009 Fr. Br. George <george@altlinux.ru> 1.4.7-alt0
- Initial build from OpenSuSE

* Sat May 27 2006 schwab@suse.de
- Don't strip binaries.
- Fix out-of-range array access.
* Fri Feb 24 2006 lmichnovic@suse.cz
- fixed uninitialized variable [#152888]
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Oct 05 2005 lmichnovic@suse.cz
- upgrade to version 1.4.7
* Tue Sep 20 2005 lmichnovic@suse.cz
- fixed gcc warnings
* Thu May 13 2004 ro@suse.de
- get rid of some compiler warnings
* Wed Apr 28 2004 ltinkl@suse.cz
- fix build problems with aliasing and possible buffer overflow
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Thu Jan 23 2003 ro@suse.de
- fixed macro definitions for gcc-3.3
* Fri Feb 01 2002 ro@suse.de
- changed neededforbuild <libpng> to <libpng-devel-packages>
* Fri Nov 23 2001 cihlar@suse.cz
- update to version 1.4.3
* Fri Oct 26 2001 ro@suse.de
- use neededforbuild aliases: SDL_devel-pakages, SDL_mixer-packages
* Thu Aug 16 2001 ro@suse.de
- changed neededforbuild <smpeg> to <smpeg smpeg-devel>
* Wed Aug 08 2001 ro@suse.de
- changed neededforbuild <kdelibs kdelibs-devel> to <kdelibs-artsd>
* Wed Aug 08 2001 ro@suse.de
- changed neededforbuild <sdl> to <SDL>
- changed neededforbuild <sdl-devel> to <SDL-devel>
* Wed Jun 20 2001 cihlar@suse.cz
- added kdelibs and kdelibs-devel to neededforbuild
* Mon Mar 26 2001 ro@suse.de
- changed neededforbuild <sdl> to <sdl sdl-devel>
* Mon Mar 12 2001 cihlar@suse.cz
- fixed neededforbuild
* Fri Mar 09 2001 ro@suse.de
- neededforbuild sdlmixer -> SDL_mixer
* Mon Mar 05 2001 cihlar@suse.cz
- updated to version 1.4
* Wed Feb 21 2001 uli@suse.de
- added alsa, esound, audiofile to neededforbuild (reqd. by new SDL)
* Fri Dec 01 2000 cihlar@suse.cz
- package created
