Name: bomberclone
Version: 0.11.8
Release: alt2.qa1

Summary: BomberClone is a Puzzle game clone of bomberman
License: GPL
Url: http://bomberclone.sourceforge.net/homepage/
Group: Games/Arcade

Packager: Igor Zubkov <icesik@altlinux.org>

Source0: %name-%version.tar.bz2
Source2: %name.xpm

Patch0: bomberclone-0.11.7-alt-path.patch

Requires: %name-data = %version

# Automatically added by buildreq on Mon Dec 17 2007
BuildRequires: imake libICE-devel libSDL-devel libSDL_image-devel libSDL_mixer-devel libX11-devel xorg-cf-files

%description
Clone of bomberman. The goal of the game is to be the last one,
who is alive. You can drop bombs which will explode after a certain
time and destroy everything in horizontal and vertical direction.
So you can remove stones or kill other players. But take care.
Don't kill yourself otherwise the game will be over for you.
During the game you will find differnent powerups to raise your skills.
If you are running faster than your opponent and you have many bombs,
you can catch him within lots of bombs and he has no chance to escape.
Your will get points for every player you have killed. If you win the game,
you can earn additional points depending on how many players played the game.

%package data
Summary: Data files for BomberClone
Group: Games/Arcade
BuildArch: noarch
Conflicts: %name < 0.11.8-alt2

%description data
Clone of bomberman. The goal of the game is to be the last one,
who is alive. You can drop bombs which will explode after a certain
time and destroy everything in horizontal and vertical direction.
So you can remove stones or kill other players. But take care.
Don't kill yourself otherwise the game will be over for you.
During the game you will find differnent powerups to raise your skills.
If you are running faster than your opponent and you have many bombs,
you can catch him within lots of bombs and he has no chance to escape.
Your will get points for every player you have killed. If you win the game,
you can earn additional points depending on how many players played the game.

This is package contains data files for BomberClone.

%prep
%setup -q
%patch0 -p1
%configure --prefix=%buildroot%prefix --disable-debug

%build
%make_build

%install
mkdir -p %buildroot%_gamesdatadir/%name
%makeinstall
install -pD -m644 %SOURCE2 %buildroot%_datadir/pixmaps/%name.xpm

rm -rf %buildroot%_datadir/doc/bomberclone/

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=BomberClone
GenericName=Bomber Clone
Comment=%{summary}
Icon=%{name}
Exec=%name
Terminal=false
Categories=Game;ArcadeGame;
EOF

%files
%doc AUTHORS ChangeLog README TODO
%_bindir/*
%_desktopdir/*

%files data
%_datadir/pixmaps/*
%_gamesdatadir/%name

%changelog
* Mon Mar 28 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.8-alt2.qa1
- NMU: converted debian menu to freedesktop

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 0.11.8-alt2
- apply patch from repocop
- move data files to subpackage and pack it as noarch

* Mon Dec 17 2007 Igor Zubkov <icesik@altlinux.org> 0.11.8-alt1
- 0.11.7 -> 0.11.8
- buildreq

* Sat May 05 2007 Igor Zubkov <icesik@altlinux.org> 0.11.7-alt1
- 0.11.6.2 -> 0.11.7
- security fixes for:
  + CVE-2006-0460
  + CVE-2006-4005
  + CVE-2006-4006
- update Url
- buildreq
- build without debug

* Thu Apr 21 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.11.6.2-alt1
- 0.11.6.2

* Sat Apr 02 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.11.6-alt1
- 0.11.6

* Sat Jan 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.11.5-alt1
- 0.11.5

* Tue Dec 21 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.4-alt1
- 0.11.4

* Tue Jul 13 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.3-alt2
- new menu group Amusement/Arcade

* Fri Jun 18 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.3-alt1
- 0.11.3

* Mon Feb 9 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.2-alt1
- 0.11.2

* Tue Feb 3 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.1-alt1
- 0.11.1
- added deathmatch mode
- added kick bombs special
- fixed major networking and packet handling problem

* Sat Jan 10 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.0-alt2
- rebuild

* Wed Jan 7 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Mon Sep 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.10.1-alt1
- 0.10.1

* Tue Jul 29 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Fri Jun 13 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Sun May 18 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.9.8-alt1
- First version of RPM package.
