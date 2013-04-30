Name: p6014
Version: 0.2.1
Release: alt1

Group: Games/Adventure
Summary: Mod sequel to Star Control II: The Ur-Quan Masters
Url: http://code.google.com/p/project6014/
License: GPL

Buildarch: noarch

Provides: %name-mini = %version-%release, %name-small = %version-%release
Requires: %name-bin  = %version

%description
Project 6014 - A fan-made sequel to The Ur-Quan Masters

It is the year 2165.
Four years ago you travelled the galaxy, assembling the scattered forces of the old Alliance of Free Stars, striving to free the human race from Ur-Quan enslavement.
You succeeded.
The Ur-Quan fled, leaving their Hierarchy forces in disarray. The Chmmr have emerged as the new leaders of known space and have asserted their authority.
Slave worlds have been freed. And a new era of peace has emerged.
For their service to the Ur-Quan defense, Hierarchy battle thralls have been punished.
The New Alliance of Free Stars is rebuilding decimated homeworlds, and continues to drive out the scattered Ur-Quan from known space.
After many years of travelling the galaxy fighting the Ur-Quan, a peaceful life on Unzervalt with Talana beckons. You have devoted your years to the study of Precursor technology, not willing to be involved in diplomacy, politics or military operations.
But your new life must wait.
Alliance command at Procyon has received a distress signal from a Shofixti scout deep in unknown space. The urgent, garbled message refers to an enormous machine that destroyed several scout vessels upon contact. Then... only static.
The Chmmr have asked YOU to lead an expedition to travel to the distress site far from Earth to track down the Shofixti and neutralize this artifact.
As you punch through the fabric of truespace, you wonder: Are you ready for this?

This is virtual package and contains only dependencies
to standard installation of this game.

%package maxi
Group: Games/Adventure
Summary: The Ur-Quan Masters (port of the classic space game StarControl 2).
Provides: %name-big = %version-%release

Requires: %name-bin = %version
Requires: %name-voice
Requires: %name-3domusic
Requires: %name-hires2x
Requires: %name-hires4x
Requires: %name-voice
#
%description maxi
Project 6014 - A fan-made sequel to The Ur-Quan Masters

It is the year 2165.
Four years ago you travelled the galaxy, assembling the scattered forces of the old Alliance of Free Stars, striving to free the human race from Ur-Quan enslavement.
You succeeded.
The Ur-Quan fled, leaving their Hierarchy forces in disarray. The Chmmr have emerged as the new leaders of known space and have asserted their authority.
Slave worlds have been freed. And a new era of peace has emerged.
For their service to the Ur-Quan defense, Hierarchy battle thralls have been punished.
The New Alliance of Free Stars is rebuilding decimated homeworlds, and continues to drive out the scattered Ur-Quan from known space.
After many years of travelling the galaxy fighting the Ur-Quan, a peaceful life on Unzervalt with Talana beckons. You have devoted your years to the study of Precursor technology, not willing to be involved in diplomacy, politics or military operations.
But your new life must wait.
Alliance command at Procyon has received a distress signal from a Shofixti scout deep in unknown space. The urgent, garbled message refers to an enormous machine that destroyed several scout vessels upon contact. Then... only static.
The Chmmr have asked YOU to lead an expedition to travel to the distress site far from Earth to track down the Shofixti and neutralize this artifact.
As you punch through the fabric of truespace, you wonder: Are you ready for this?

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
%files maxi

%changelog
* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- initial spec
