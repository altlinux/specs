Name:	 xblast
Version: 2.10.3
Release: alt3
Summary: The X11 bomberman team game
License: GPL
Icon: %{name}_32x32.png
Group: Games/Arcade
# actually there's no xblast-2.10.3.tar.gz, but http://xblast.sourceforge.net/arc/xblast-060308.tgz
# and newest 2.10.4 version is claimed buggy on the game site
Source0: http://heanet.dl.sourceforge.net/sourceforge/xblast/%name-%version.tar.gz
Source1: %{name}_48x48.png
Source2: %{name}_32x32.png
Source3: %{name}_16x16.png
Source4: %name.desktop
Url: http://xblast.sourceforge.net/
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue Dec 18 2007
BuildRequires: imake libICE-devel libX11-devel xorg-cf-files libXt-devel

Requires: %name-data

%description
XBlast is a multi-player arcade game for X11R5/R6. The game can be played
with at least two players and up to four players. It was inspired by
the video/computer game Bomberman(Dynablaster), which was to my
knowledge first programmed for NEC's PC Engine/Turbo Grafx. Other
(commercial) versions of the original game exist for IBM-PC, Atari ST,
Amiga, NES, GameBoy and Super NES.

%prep
%setup -q -n %name

%build
./autogen.sh
%configure --enable-SMPF --enable-sound --enable-admin --bindir=%_gamesbindir --with-otherdatadir=%_gamesdatadir/XBlast-TNT --prefix=/usr
%make_build

%install
%makeinstall game_datadir=%buildroot/%_gamesdatadir/XBlast-TNT bindir=%buildroot/%_gamesbindir
mkdir -p %buildroot/%_mandir/man6
install %name.man %buildroot/%_mandir/man6/%name.6

mkdir -p  %buildroot%_gamesdatadir/XBlast-TNT/image/misc ## XXX

install -D %SOURCE1 %buildroot%_liconsdir/%name.png
install -D %SOURCE2 %buildroot%_iconsdir/%name.png
install -D %SOURCE3 %buildroot%_miconsdir/%name.png
install -D %SOURCE4 %buildroot%_desktopdir/%name.desktop
%find_lang  %name

%files -f %name.lang
%_gamesbindir/xbsndsrv
%_gamesbindir/%name
%_gamesdatadir/XBlast-TNT
%_mandir/man6/%name.*
%_miconsdir/%name.png
%_liconsdir/%name.png
%_iconsdir/%name.png
%_desktopdir/%name.desktop
%_datadir/locale/*/*/%name.*
%doc README INSTALL ChangeLog AUTHORS NEWS

%changelog
* Wed Sep 01 2010 Fr. Br. George <george@altlinux.ru> 2.10.3-alt3
- Repocop warnings fixed

* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 2.10.3-alt2
- Fix repocop warnings
- Desktop file added

* Sat Nov 21 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.10.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * pixmap-in-deprecated-location for xblast
  * postclean-05-filetriggers for spec file

* Tue Dec 18 2007 Fr. Br. George <george@altlinux.ru> 2.10.3-alt1
- Version up
- Gear adapted
- Data and source package split

* Sat Jan 29 2005 Fr. Br. George <george@altlinux.ru> 2.10.0-alt1
- Totally new branch XBlast-TNT, initial ALT build

* Fri Oct 31 2003 Fr. Br. George <george@altlinux.ru> 2.6.1-alt1
- ALT Linux port

