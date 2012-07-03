
%define rname uqm
%define what remix-pack2
Name: %rname-%what
Version: 1.0
Release: alt4

Group: Sound
Summary: The Ur-Quan Masters Official Remix Add-On. Pack II
Url: http://sc2.sourceforge.net
License: May be copied freely as part of %rname

Buildarch: noarch
Requires: %rname-bin
#Obsoletes: %rname-3domusic

Source0: %rname-%what.zip

%description
The official Ur-Quan Masters remix add-on,
written by the PRECURSORS and members of SC2 fan community

Pack II: Neutral Aliens, Don't Shoot

Tracks:
 1. Through the Angles of Space (4'00)
 2. Welcome to Falayalaralfali (3'39)
 3. We Come In Peace! (2'58)
 4. Floating Gas Bags (2'35)
 5. Across the Galaxy (4'12)
 6. Around the Rainbow Worlds (2'02)
 7. Property of the Crimson Corporation (4'45)
 8. Safe Haven (3'53)
 9. Planet Red Alert (5'31)
 10. Turning Purple (2'49)
 11. Didn't You Mean To Ask About Flowers? (4'03)

Release Date: 10th November 2003
Credits:
 Track 1 composed by Kevin Pavlivec and remixed by Jouni Airaksinen.
 Track 2 composed by Dan Nicholson and remixed by Espen Gaetzschmann. Mixed and mastered at Midtown Music by Pal Jorgen Gaetzschmann and Conor Patrick Johannessen.
 Tracks 3, 4 composed by Dan Nicholson and remixed by Espen Gaetzschmann & Tore Aune Fjellstad .
 Track 5 composed and remixed by Riku Nuottajaervi.
 Tracks 6 and 9 composed by Jouni Airaksinen.
 Track 7 composed by Dan Nicholson and remixed by Jouni Airaksinen.
 Track 8 composed by Eric Berge and remixed by Jouni Airaksinen.
 Track 10 composed by Eric Berge and remixed by Riku Nuottajaervi.
 Track 11 composed by Dan Nicholson and remixed by Riku Nuottajaervi.
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
- depends on uqm-bin rather than uqm

* Thu Nov 20 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt2
- fix description

* Tue Nov 18 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- initial spec
