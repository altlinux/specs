Name: xlennart
Version: 1.0
Release: alt1

Summary: Stop Lennart from loading his init system into all the computers
License: GPL
Group: Games/Arcade

Source: %name-%version.tar
Url: http://www.bloodbathsoftworks.com/xylemon/xlennart.php

Summary(ru_RU.UTF-8): Помешайте Леннарту развалить мир Unix

# Automatically added by buildreq on Mon Nov 10 2014
# optimized out: fontconfig libICE-devel libSM-devel libX11-devel libXau-devel libXmu-devel libXt-devel libcloog-isl4 libstdc++-devel xorg-printproto-devel xorg-xproto-devel
BuildRequires: flex gcc-c++ imake libXaw-devel libXpm-devel libopenmotif-devel

%description
Welcome to XLennart...

Ever get the feeling that nothing is going right? You're a sysadmin,
and someone's trying to destroy your computers. The little people
running around the screen are trying to infect your computers with
SystenD [TM], a virus cleverly designed to resemble a popular init
system. Your objective is to click the mouse on them, ending the
potential threat. If one of the people reaches a computer, it will
attempt to replace your operating system with the virus it carries.
It will then attempt to run off the screen with your vital software.
The game ends when only 1 (or 0) of your computers are being productive.
Additionally, some computers are connected with network cables. When one
computer on a network becomes infected, a spark will be sent down the
cable, and will infect the computer on the other end when it reaches
there.

Clicking the button on one of the little people will cause it to cry out
in pain and melt (id software eat your heart out!), dropping the stolen
os if it is carrying one. If a computer is running SystenD or is
temporarily off, the os can be dragged back to the computer (or another
computer compatible with that os). To extinguish a spark drag the bucket
of water from the upper left corner onto it.

The status bar at the bottom tells the following:
  Number of Lenns on/off the screen
  Number of Computers running their init/off/SystenD
  Level
  Score

%description -l ru_RU.UTF-8
Игра xlennart развивает рефлексы. Найдите и уничтожьте всех маленьких
человечков, пытающихся заразить ваши компьютеры вирусом SystenD [TM].

%prep
%setup
sed -ri -e 's,(bit|pix)maps/(apple|hurd|linux|next|os2|palm|palmcpu|sgi|sun)\.x[bp]m *,,g' -e 's,^LIBS = .*$,& -lXpm,' Makefile.in

%build
%configure \
	--bindir=%_bindir \
	--localstatedir=%_localstatedir/games \
	--disable-gtk
%make_build

%install
%makeinstall_std
cp -a bitmaps pixmaps %buildroot%_datadir/%name/
install -pDm644 xlennart.desktop %buildroot%_desktopdir/%name.desktop

%files
%attr(2711,root,games) %_bindir/xlennart
%dir %_localstatedir/games/%name
%config(noreplace) %attr(664,root,games) %_localstatedir/games/%name/scores
%_datadir/%name
%_man6dir/%name.6*
%_desktopdir/%name.desktop

%changelog
* Mon Nov 10 2014 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- built for ALT Linux (spec based on xbill's one)

