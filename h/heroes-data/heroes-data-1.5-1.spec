Name:           heroes-data
Version:        1.5
Release:        alt0.1

Summary:        Heroes data.
License:      GPL
Group:          Games/Arcade
URL:            http://heroes.sourceforge.net/
Source:         http://download.sourceforge.net/heroes/%name-%version.tar.bz2
BuildArch:      noarch

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but includes
many graphical improvements and new game features.  In it, you must
maneuver a small vehicle around a world and collect powerups while avoiding
obstacles, your opponents' trails, and even your own trail. Several modes
of play are available, including "get-all-the-bonuses", deathmatch, and
"squish-the-pedestrians".

%prep
%setup -q -n %name-%version

%build
./configure --datadir=%_gamesdatadir

%install
%make_install DESTDIR=%buildroot install

%files
%doc ANNOUNCE AUTHORS COPYING ChangeLog INSTALL NEWS README THANKS
%_gamesdatadir/heroes/levels/niv*.lvl
%_gamesdatadir/heroes/levels/level.lst
%_gamesdatadir/heroes/pics/*.pcx
%_gamesdatadir/heroes/tilesets/level*.pie
%_gamesdatadir/heroes/tilesets/level*.glz
%_gamesdatadir/heroes/tilesets/level*.pcx


%changelog
* Sun Mar 16 2003 Alex Murygin <murygin@altlinux.ru> 1.5-alt0.1
- First build for Sisyphus.

