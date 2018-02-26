
%define rname uqm
%define what remix-pack3
Name: %rname-%what
Version: 1.0
Release: alt3

Group: Sound
Summary: The Ur-Quan Masters Official Remix Add-On. Pack III
Url: http://sc2.sourceforge.net
License: May be copied freely as part of %rname

Buildarch: noarch
Requires: %rname-bin
#Obsoletes: %rname-3domusic

Source0: %rname-%what.zip

%description
Pack III: The Ur-Quan Hierarchy

Tracks:
1. Ur-Quan - Now and Forever (2:56)
2. Ilwrath - All Evil (2:18)
3. VUX - Ultra-gross! (2:21)
4. Umgah - Genetic Modification (3:52)
5. Mycon - Rebirth (3:31)
6. Thraddash - Culture 19 (2:14)
7. Kohr-Ah - Cleansing Required (2:32)
8. Orbit IV - Cold Tectonics (4:23)
9. Orbit V - Extraterrestrial Lifeforms (3:57)

Release date: June 30th, 2004
Credits:
 Track 1 composed by Erol Otus and remixed by Espen Gaetzschmann & Tore Aune Fjellstad.
 Tracks 2, 7 composed by Dan Nicholson and remixed by Riku Nuottajaervi.
 Track 3 composed by Dan Nicholson and remixed by Espen Gaetzschmann & Tore Aune Fjellstad.
 Track 4 composed by Dan Nicholson and remixed by Jouni Airaksinen.
 Track 5 composed and remixed by Riku Nuottajaervi.
 Track 6 composed by Riku Nuottajaervi and remixed by Espen Gaetzschmann & Tore Aune Fjellstad.
 Track 8 composed by Jouni Airaksinen.
 Track 9 composed by Espen Gaetzschmann.
Cover Design Jouni Airaksinen. Kohr-Ah Picture by Erol Otus.

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
* Sat Sep 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.0-alt3
- install the pack into the content directory, not as an addon
  (erthad@; closes: #17114)

* Mon Oct 15 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 1.0-alt2
- resurrected from orphaned
- depends on uqm-bin rather than uqm

* Mon Jul 19 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec
