
Name: uqm
Version: 0.6.2
Release: alt1

Group: Games/Adventure
Summary: The Ur-Quan Masters (port of the classic space game StarControl 2).
Url: http://sc2.sourceforge.net
License: GPL

Buildarch: noarch

Provides: %name-mini = %version-%release, %name-small = %version-%release
Requires: %name-bin  = %version

%description
The project started in August 2002, when Toys For Bob <http://toysforbob.com/>
released the partially ported sources of Star Control 2 <http://star-control.com>
3DO version to the fan community. Our goal is to port this wonderful game
to current personal computers and operating systems. It is and will remain
100%% free of charge, and anyone can contribute to the project and thus
help make it even better.

This is virtual package and contains only dependencies
to standard installation of this game.


%package big
Group: Games/Adventure
Summary: The Ur-Quan Masters (port of the classic space game StarControl 2).
Requires: %name-bin = %version
Requires: %name-voice = 0.6.0
#
%description big
The project started in August 2002, when Toys For Bob <http://toysforbob.com/>
released the partially ported sources of Star Control 2 <http://star-control.com>
3DO version to the fan community. Our goal is to port this wonderful game
to current personal computers and operating systems. It is and will remain
100%% free of charge, and anyone can contribute to the project and thus
help make it even better.

This is virtual package and contains only dependencies
to maximum installation of this game.


%package maxi
Group: Games/Adventure
Summary: The Ur-Quan Masters (port of the classic space game StarControl 2).
Requires: %name-bin = %version
Requires: %name-remix-pack1
Requires: %name-remix-pack2
Requires: %name-remix-pack3
Requires: %name-voice = 0.6.0
#
%description maxi
The project started in August 2002, when Toys For Bob <http://toysforbob.com/>
released the partially ported sources of Star Control 2 <http://star-control.com>
3DO version to the fan community. Our goal is to port this wonderful game
to current personal computers and operating systems. It is and will remain
100%% free of charge, and anyone can contribute to the project and thus
help make it even better.

This is virtual package and contains only dependencies
to maximum installation of this game.


%package common
Group: Games/Adventure
Summary: The Ur-Quan Masters (port of the classic space game StarControl 2).
#
%description common
This is virtual package and contains only dependencies
to easy uninstall this %name subpackages.


%files common
%files
%files big
%files maxi

%changelog
* Thu Apr 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Mon May 23 2005 Sergey V Turchin <zerg at altlinux dot org> 0.4.0-alt1
- new version

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt3
- add requires to remix-pack3 in maxi
- change requires remix-* to requires voice in big

* Tue Nov 18 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt2
- split
- add voice subpackage
- replace music subpackage by The Ur-Quan Masters Official Remix Add-On
  project <http://www.spacesynth.net/precursors/>

* Thu Sep 25 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- initial spec
