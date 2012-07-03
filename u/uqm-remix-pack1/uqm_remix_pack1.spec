
%define rname uqm
%define what remix-pack1
Name: %rname-%what
Version: 1.0
Release: alt4

Group: Sound
Summary: The Ur-Quan Masters Official Remix Add-On. Pack I
Url: http://sc2.sourceforge.net
License: May be copied freely as part of %rname

Buildarch: noarch
Requires: %rname-bin
#Obsoletes: %rname-3domusic

Source0: %rname-%what.zip

%description
The official Ur-Quan Masters remix add-on,
written by the PRECURSORS and members of SC2 fan community

Pack I: Super Melee!

Tracks:
 1. Under A Red Sky (5'51)
 2. Corridor Nine (6'05)
 3. To Mine The Heavens (1'39)
 4. Red Alert! (0'05)
 5. The Battle of the Sa-Matra (3'04)
 6. Outfit the Vindicator (2'21)
 7. Rough Repair (3'40)
 8. Exploration (10'06)

Release Date: 27th October 2003
Credits:
 Track 1 composed by Dan Nicholson and remixed by Espen Gaetzschmann and Tore Aune Fjellstad.
 Track 2 composed and remixed by Riku Nuottajaervi.
 Tracks 3, 4, 5, 6, 8 composed by Dan Nicholson and remixed by Jouni Airaksinen.
 Track 7 composed and remixed by Dan Nicholson.
Cover Design Jouni Airaksinen.

Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.

%prep
%build
%install
install -D -m 644 %SOURCE0 %buildroot%_gamesdatadir/%rname/content/packages/%rname-%what.uqm

cat >>copyright << __EOF__
Copyright :
The content -- voiceovers, dialogue, graphics, and music -- are
copyright (C) 1992, 1993, 2002 Toys for Bob, Inc. or their
respective creators.  The content may be copied freely as part of
a distribution of The Ur-Quan Masters.  All other rights are reserved.
__EOF__

%files
%doc copyright
%_gamesdatadir/%rname/content/packages/*.uqm

%changelog
* Sat Sep 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt4
- install the pack into the content directory, not as an addon
  (erthad@; closes: #17114)

* Mon Oct 15 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 1.0-alt3
- resurrected from orphaned
- depends on uqm-bin rather than uqm-common

* Thu Nov 20 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- fix description

* Tue Nov 18 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec
