Name: mures
Version: 0.5
Release: alt6.qa2

Summary: Clone of Sega's "Chu Chu Rocket", a multi-player puzzle game

License: GPL
Url: http://mures.sourceforge.net/
Group: Games/Arcade

Source0: http://prdownloads.sourceforge.net/mures/%name-%version.tar
Source1: %name.desktop
Source2: %name.16.xpm
Source3: %name.32.xpm
Source4: %name.48.xpm
Patch0: mures-0.5-alt-DSO.patch

# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: libSDL_image-devel libSDL_net-devel libSDL_ttf-devel
BuildRequires: desktop-file-utils

%description
Mures is a cross-platform clone of Sega's "Chu Chu Rocket" written using
C. To start the game, run "mures -hN -aiM" where N and M are the number of
human and computer players at the local computer. Press enter to start the
game, press P to pause, and Q to quit.
- Player 1: Use the mouse to target, and click and drag in the desired
direction to place an arrow.
- Player 2: Use the arrow keys to target, and the number keypad to place
arrows.
- Player 3: Use A,W,S,D to target and I,J,K,L to place arrows.

%prep
%setup
%patch0 -p2

%build
%configure
%make_build

%install
%makeinstall

mv %buildroot/%_bindir/%name %buildroot/%_bindir/%name.real
cat << EOF > %buildroot/%_bindir/%name
#!/bin/sh
cd %_libdir/%name
%name.real "\$@"
cd -
EOF
chmod +x %buildroot/%_bindir/%name

mkdir -p %buildroot/%_libdir/%name
cp -a src/images src/maps src/sounds src/gui src/textures %buildroot/%_libdir/%name
cp src/*.lua %buildroot/%_libdir/%name
find %buildroot/%_libdir/%name -type f -name Makefile\* -exec rm -f {} \;

install -m0644 %SOURCE1 -D %buildroot/%_desktopdir/%name.desktop

install -m 644 -D %SOURCE2 %buildroot/%_miconsdir/%name.xpm
install -m 644 -D %SOURCE3 %buildroot/%_niconsdir/%name.xpm
install -m 644 -D %SOURCE4 %buildroot/%_liconsdir/%name.xpm
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Game \
	--add-category=ArcadeGame \
	%buildroot%_desktopdir/mures.desktop

%files
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_libdir/%name/
%_desktopdir/*
%_miconsdir/%name.*
%_niconsdir/%name.*
%_liconsdir/%name.*

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt6.qa2
- Fixed build

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.5-alt6.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for mures

* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt6
- fix build, update buildreqs, cleanup spec

* Tue Dec 01 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.5-alt5.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for mures
  * pixmap-in-deprecated-location for mures
  * postclean-05-filetriggers for spec file

* Sat May 31 2008 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt5
- update buildreq
- replace menu file with desktop file

* Tue Jun 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt4.1
- NMU: fix menu group (#4613)

* Wed Aug 20 2003 Rider <rider@altlinux.ru> 0.5-alt4
- buildreq fix (#2141)

* Sat Oct 05 2002 Rider <rider@altlinux.ru> 0.5-alt3
- rebuild

* Sun Mar 10 2002 Rider <rider@altlinux.ru> 0.5-alt2
- rebuild with libSDL_ttf-2.0.so.0

* Fri Jan 18 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5-alt1
- new version

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.4-alt2
- Rebuilt with libSDL_net-1.2.so.0

* Tue Aug 28 2001 Sergey V Turchin <zerg@altlinux.ru> 0.3-alt1
- build for ALT

* Mon Aug 20 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.3-1mdk
- new version
- remove patch0 merged upstream

* Tue Jul 24 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.2-1mdk
- initial spec
