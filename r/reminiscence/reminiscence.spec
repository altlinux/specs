Name: reminiscence
Summary: game Flashback engine (re-implementation)
Version: 0.2.1
Release: alt1
License: GPL3
Group: Games/Arcade
Url: http://cyxdown.free.fr/reminiscence/
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://cyxdown.free.fr/reminiscence/REminiscence-0.2.1.tar
#.bz2
Source1: %name.sh
Source2: %name.desktop
Source3: README.alt

# Automatically added by buildreq on Fri Oct 28 2011 (-bi)
# optimized out: elfutils libstdc++-devel
BuildRequires: gcc-c++ libSDL-devel zlib-devel

%description
REminiscence is a re-implementation of the engine used in the game Flashback
made by Delphine Software and released in 1992. More informations about the
game can be found at [1], [2] and [3].
You will need the original files of the PC (DOS or CD) or Amiga release.

[1] http://www.mobygames.com/game/flashback-the-quest-for-identity
[2] http://en.wikipedia.org/wiki/Flashback:_The_Quest_for_Identity
[3] http://ramal.free.fr/fb_en.htm

%prep
%setup -n REminiscence-%version
cp -a %SOURCE3 .

%build
make

%install
mkdir -p %buildroot{%_gamesbindir/,%_desktopdir/}
install -p -m 755 %SOURCE1 rs %buildroot%_gamesbindir/
install -p -m 644 %SOURCE2 %buildroot%_desktopdir/

%files
%_gamesbindir/*
%_desktopdir/*.desktop
%doc README*

%changelog
* Sun Oct 30 2011 Ildar Mulyukov <ildar@altlinux.ru> 0.2.1-alt1
- add the launch script and %name.desktop

* Fri Oct 28 2011 Ildar Mulyukov <ildar@altlinux.ru> 0.2.1-alt0
- initial build for ALT Linux Sisyphus

