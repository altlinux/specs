Name:           heroes-sound-tracks
Version:        1.0
Release:        alt0.1

Summary:        Heroes sound tracks.
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
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%_gamesdatadir/heroes/mod/sound.conf
%_gamesdatadir/heroes/mod/*.xm

%changelog
* Sun Mar 16 2003 Alex Murygin <murygin@altlinux.ru> 1.0-alt0.1
- First build for Sisyphus.

