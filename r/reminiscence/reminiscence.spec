Name: reminiscence
Summary: game Flashback engine (re-implementation)
Version: 0.3.3
Release: alt1
License: GPL3
Group: Games/Arcade
Url: http://cyxdown.free.fr/reminiscence/

Source: http://cyxdown.free.fr/reminiscence/REminiscence-%version.tar
#.bz2
Source1: %name.sh
Source2: %name.desktop
Source3: README.alt

# Automatically added by buildreq on Thu Aug 24 2017 (-bi)
# optimized out: elfutils libstdc++-devel perl python-base
BuildRequires: gcc-c++ libSDL2-devel libmodplug-devel libogg-devel libtremor-devel zlib-devel

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
%doc README* rs.cfg

%changelog
* Thu Aug 24 2017 Ildar Mulyukov <ildar@altlinux.ru> 0.3.3-alt1
- new version

* Sun Oct 30 2011 Ildar Mulyukov <ildar@altlinux.ru> 0.2.1-alt1
- add the launch script and %name.desktop

* Fri Oct 28 2011 Ildar Mulyukov <ildar@altlinux.ru> 0.2.1-alt0
- initial build for ALT Linux Sisyphus

