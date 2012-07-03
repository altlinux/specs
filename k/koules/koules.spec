Name: koules
Version: 1.4
Release: alt9

Summary: Action game with multiplayer, network and sound support
License: GPL
Group: Games/Arcade

Url: http://www.ucw.cz/~hubicka/koules/English/koules.html
Source0: ftp://sunsite.unc.edu/pub/Linux/games/arcade/%name/%name%version-src.tar.gz
Source1: koules.desktop
Patch0: koules-i386.patch
Patch1: koules-config.patch
Patch2: koules-asmfix.patch
Patch3: koules-optflags.patch
Patch4: koules-noman.patch
Patch5: koules-1.4-alt-makefile.patch
Patch6: koules-schumacher.patch
Patch7: koules-1.4-alt-tmpfile.patch
Patch8: koules-1.4-alt-no-shm.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Dec 13 2009
BuildRequires: gccmakedep imake libX11-devel libXext-devel xorg-cf-files

Summary(pl):	Gra pod X11 dla wielu graczy
Summary(ru_RU.KOI8-R): интерактивная и юморная игра с сетью и звуком
Summary(uk_UA.KOI8-U): ╕нтерактивна та гумористична гра ╕з мережею та звуком

Icon: koules.xpm

%description
Action game with multiplayer, network and sound support.

%description -l pl
Gra pod SVGAlib i X11 ze wsparciem dla wielu graczy, sieci i d╪wiЙku.

%description -l ru_RU.KOI8-R
Koules ("шарики") - замечательная игрушка, которая при всей своей простоте
подкупает оригинальными находками в области стратегии и пародии.

Она гарантирует вам немалое количество потраченного впустую времени. :-)

%description -l uk_UA.KOI8-U
Koules ("кульки") - файна цяцька, що попри вс╕╓╖ сво╓╖ простоти п╕дкупа╓
ори╜╕нальними знах╕дками у област╕ стратег╕╖ та парод╕╖.

Вона ╜аранту╓ вам чималу к╕льк╕сть згаяного часу. :-)

%prep
%setup -n %name%version
%ifarch %ix86
%patch0 -p1
%else
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6
%patch7 -p1
%patch8 -p1

%build
xmkmf -a
%make_build

%install
install -d %buildroot{%_mandir{,/pl}/man6,%_bindir,%_gamesbindir,%_gamesdatadir/koules,%_niconsdir}

install -pm644 sounds/*.raw %buildroot%_gamesdatadir/%name/
install -pm755 koules.sndsrv.linux %buildroot%_gamesbindir/
install -pm755 xkoules %buildroot%_gamesbindir/
install -pm644 xkoules.6 %buildroot%_man6dir/
install -pm755 koules %buildroot%_gamesbindir/
install -pm755 koules.tcl %buildroot%_gamesbindir/
install -pm644 Icon.xpm %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc ANNOUNCE BUGS Card ChangeLog Koules.FAQ README TODO *.xpm
%_gamesbindir/*
%_gamesdatadir/%name/
%_niconsdir/%name.xpm
%_man6dir/*.6*
%_desktopdir/*

# TODO:
# - figure out why xkoules would bail out on SHM usage
# - consider soundwrapper (right now DOESN'T work for me w/emu10k1)

%changelog
* Sun Dec 13 2009 Michael Shigorin <mike@altlinux.org> 1.4-alt9
- buildreq (repocop)

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 1.4-alt8
- fixed sloppy /tmp usage in wrapper script
- disabled XSHM knob by default in GUI launcher
- fixed desktop categories
- fixed pixmap location
- minor spec cleanup

* Sun Dec 21 2008 Fr. Br. George <george@altlinux.ru> 1.4-alt7.1
- Fix schumacher font usage

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 1.4-alt7
- added Packager:

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1.4-alt6
- applied repocop patch
- removed debian menufile (desktop file present)

* Sat Dec 23 2006 Michael Shigorin <mike@altlinux.org> 1.4-alt5
- changed exec line in desktop file (fixes: #10490);
  thanks Nick S. Grechukh (gns@) for test/report/suggestion

* Wed Dec 20 2006 Michael Shigorin <mike@altlinux.org> 1.4-alt4
- added fd.o menu file (based on PLD variant) (fixes: #10462)

* Sun Dec 10 2006 Michael Shigorin <mike@altlinux.org> 1.4-alt3
- added Url:

* Wed Apr 05 2006 Michael Shigorin <mike@altlinux.org> 1.4-alt2
- fixed build with fhs=normal check (soundserver binary was
  located in sounds dir)
- spec cleanup (removed alpha, svgalib and separate sound package
  already commented-out remnants)

* Sat Dec 10 2005 Michael Shigorin <mike@altlinux.org> 1.4-alt1
- dug out from archives ;-)

* Sat Nov 09 2002 Michael Shigorin <mike@altlinux.ru> 1.4-alt0.1
- built for ALT Linux
- spec adopted from PLD (http://pld.org.pl)
  PLD Team <feedback@pld.org.pl>
  All persons listed below can be reached at <cvs_login>@pld.org.pl
    ankry baggins kloczek qboosh zagrodzki 
- spec cleanup
- removed koules-svgalib package as unsupported; could be reverted in need
- renamed koules-x11 package to koules
- merged koules-sound into main package
- moved sound files from /usr/lib/games/koules to %_gamesdatadir/%name 
  (warning, values are also hardwired in config/patches!)
- added menu entries for xkoules and koules.tcl
  XXX FIXME: they are present in the package BUT somehow disappear in the system!!!
