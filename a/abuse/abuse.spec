Name: abuse
Version: 0.8
Release: alt2
Summary: The classic Crack-Dot-Com game
License: GPL
Group: Games/Arcade

URL:		http://abuse.zoy.org/
Source0:	%name-%version.tar.gz
Source2: abuse.desktop
Patch:	abuse-0.8-anyres.patch
Obsoletes:	abuse_sdl abuse_sdl-fRaBs

# Automatically added by buildreq on Sat May 21 2011
# optimized out: libGL-devel libGLU-devel libSDL-devel libX11-devel libstdc++-devel xorg-xproto-devel
BuildRequires: gcc-c++ imake libSDL_mixer-devel libXext-devel xorg-cf-files

BuildRequires: xorg-xproto-devel

Requires: %name-data

%description
Abuse is a dark 2D side-scrolling platform game developed by Crack dot
Com in 1995. It features beautiful lighting, realistic animation and
nasty alien-like creatures to destroy. It is now maintained by Sam
Hocevar in an attempt to prevent it from vanishing from the Internet.

%package data
Group:	Games/Arcade
Summary:	Data files for %name
Buildarch:	noarch
License:	Redistributable
%description data
Data files for %name

%prep
%setup -q
%patch -p1

cat > %name-data.COPYING.txt <<@@@
All levels and artwork are now part of the Abuse source. It is a merge
of abuse-lib, the original shareware version of the game (released into
the public domain except for the sound effects), abuse-frabs, the result
of a community effort to create free Abuse levels, abuse-data, a full
registered game dataset and abuse-mac, the Mac version developed by
Bungie.

Licensing terms for the data are still unclear but are being sorted out.
Jonathan Clark and Dave Taylor, the original Abuse authors, allowed the
full dataset to be freely redistributed with Abuse-SDL. Same with Bobby
Prince, the sound samples author. However Bobby did not allow
modification of the samples.
@@@

%build
%configure
%make_build CXXFLAGS+="-DANYRES"
rm src/sdlport/setup.o
mv src/abuse src/abuse.anyres
%make_build

%install
%makeinstall
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -D doc/abuse.png %buildroot%_niconsdir/abuse.png
install src/abuse.anyres %buildroot%_bindir/

%files
%doc AUTHORS README TODO NEWS
%_bindir/*
%dir %_gamesdatadir/abuse
%_desktopdir/%name.desktop
%_niconsdir/*.png
%_man6dir/*

%files data
%doc %name-data.COPYING.txt
%_gamesdatadir/abuse/*

%changelog
* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 0.8-alt2
- Arbitrary gamefield resolution patch

* Sat May 21 2011 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Upstream packaging policy changed
- Version up

* Tue Jan 19 2010 Fr. Br. George <george@altlinux.ru> 0.7.1-alt2
- Fix icon names

* Sat Apr 11 2009 Fr. Br. George <george@altlinux.ru> 0.7.1-alt1
- Version up
- MDK patches include
- Upstream switch
- Datafiles split

* Sat Mar 10 2007 Michael Shigorin <mike@altlinux.org> 0.7.0-alt4
- added ImageMagick to buildrequires by hand
  (hm, got lost somehow with buildreq)

* Sun Feb 11 2007 Michael Shigorin <mike@altlinux.org> 0.7.0-alt3
- adopted an orphan
- built with gcc4.1
- updated buildrequires
- replaced debian menu file with freedesktop (from Ubuntu)
- added missing manpage

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 0.7.0-alt2
- fix BuildRequires

* Tue Dec 17 2002 Sergey V Turchin <zerg@altlinux.ru> 0.7.0-alt1
- new version
- build with gcc2.96

* Wed Oct 23 2002 Sergey V Turchin <zerg@altlinux.ru> 0.6.1-alt2
- rebuild with gcc3.2

* Fri Feb 08 2002 Sergey V Turchin <zerg@altlinux.ru> 0.6.1-alt1
- new version

* Mon Jan 21 2002 Sergey V Turchin <zerg@altlinux.ru> 0.6.0-alt1
- new version

* Tue Sep 04 2001 Sergey V Turchin <zerg@altlinux.ru> 0.5.0-alt1
- new version

* Thu May  3 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4.8-2mdk
- corrected badly lowercased files

* Tue May  1 2001 Frederic Lepied <flepied@mandrakesoft.com> 0.4.8-1mdk
- first version
