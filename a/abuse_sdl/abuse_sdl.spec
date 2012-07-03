%define oname abuse
Name: abuse_sdl
Version: 0.7.1
Release: alt2
Packager: Fr. Br. George <george@altlinux.ru>
Summary: The classic Crack-Dot-Com game
License: GPL
Group: Games/Arcade

URL:		http://abuse.zoy.org/
Source0:	http://abuse.zoy.org/raw/Downloads/%oname-%version.tar.gz
#Source1: http://www.labyrinth.net.au/~trandor/files/abuse_datafiles.tar.bz2
Source1: fRaBs210.tar.bz2
Source2: abuse.desktop
Patch0:		abuse_sdl-0.7.0-fixes.patch
Patch1:		abuse_sdl-0.7.0-exit-intro-crash.patch

# Automatically added by buildreq on Sat Apr 11 2009
BuildRequires: ImageMagick-tools gcc-c++ imake libGL-devel libSDL-devel libX11-devel libXext-devel xorg-cf-files

Requires: %name-fRaBs = %version

%description
Abuse-SDL is a port of Abuse, the classic Crack-Dot-Com game, to the
SDL library. It can run at any color depth, in a window or fullscreen,
and it has stereo sound with sound panning.

%package fRaBs
Summary: Free leves set for Abuse
BuildArch: noarch
License: public domain
Group: Games/Arcade
%description fRaBs
fRaBs is just a silly acronym for 'Free Abuse'. It has the network support of the registered version, but also comes equipped with many new single player and deathmatch levels, as well as additional enemies and artwork, all coming from outside, free sources. A list of updates and modifications can be found in the updates section.

%prep
%setup -q -n %oname-%version
%patch0 -p1 -z .fix
%patch1 -p1 -z .intro

%build
%configure
%make_build

convert -size 48x48 abuse.png 48x48.png
convert -size 16x16 abuse.png 16x16.png

%install
%makeinstall

install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

install -D abuse.png %buildroot/%_niconsdir/abuse.png
install -D 48x48.png %buildroot/%_liconsdir/abuse.png
install -D 16x16.png %buildroot/%_miconsdir/abuse.png

install -d %buildroot/{%_gamesdatadir/abuse,%_gamesbindir}
mv %buildroot/%_bindir/abuse %buildroot/%_gamesbindir/abuse.sdl
cat > %buildroot/%_gamesbindir/abuse << EOF
#!/bin/sh
cd %_gamesdatadir/abuse/fRaBs210
exec %_gamesbindir/abuse.sdl -datadir %_gamesdatadir/abuse/fRaBs210 "\$@"
EOF
chmod +x %buildroot/%_gamesbindir/abuse
cd %buildroot/%_gamesdatadir/abuse/
bzcat %SOURCE1 | tar xf -
rm -f fRaBs210/{*.exe,art/*.exe,*.386}
for f in `find . -type f`; do
	dir=`dirname $f`
	base=`basename $f`
	new=$dir/`echo $base | tr [A-Z] [a-z]`
	if [ $new != $f ]; then
		mv $f $new
	fi
done

cd */addon/leon
ln -s lmisc.spe Lmisc.spe

cd sfx
ln -s ambship1.wav Ambship1.wav
ln -s ambship2.wav Ambship2.wav

%files
%doc AUTHORS README TODO
%_gamesbindir/*
%_desktopdir/%name.desktop
%_niconsdir/*.png
%_liconsdir/*.png
%_miconsdir/*.png
%_man6dir/*

%files fRaBs
%_gamesdatadir/abuse

%changelog
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
