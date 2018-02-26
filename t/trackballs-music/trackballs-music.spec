Name: trackballs-music
Version: 1.4
Release: alt1
Epoch: 2

Summary: In-game music for Trackballs
Group: Sound
License: GPLv2+ and EFML
BuildArch: noarch
Url: http://trackballs.sourceforge.net/
# http://downloads.sourceforge.net/trackballs/%name-%version.tar.bz2
Source: %name-%version.tar
Requires: trackballs-data

%description
Some great music to listen to while playing Trackballs.

%prep
%setup -n %name

%install
mkdir -p %buildroot%_datadir/trackballs/music
install -pm644 *.ogg %buildroot%_datadir/trackballs/music/

%files
%_datadir/trackballs/music/*
%doc README fml.html

%changelog
* Mon Jun 07 2010 Dmitry V. Levin <ldv@altlinux.org> 2:1.4-alt1
- Updated to 1.4.
- Relocated installed files to standard location.

* Thu Apr 12 2007 Sergey V Turchin <zerg at altlinux dot org> 2:1.2-alt1
- new version

* Wed Jul 30 2003 Sergey V Turchin <zerg at altlinux dot org> 2:1.0-alt1
- fix version

* Mon Jun 02 2003 Sergey V Turchin <zerg at altlinux dot ru> 1:1.2-alt1
- split from trackballs.src.rpm

