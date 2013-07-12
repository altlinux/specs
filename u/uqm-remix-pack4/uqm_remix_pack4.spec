
%define rname uqm
%define what remix-disc4
Name: %rname-remix-pack4
Serial: 1
Version: 0.7.0
Release: alt1

Group: Sound
Summary: The Ur-Quan Masters Official Remix Add-On. Pack III
Url: http://sc2.sourceforge.net
License: May be copied freely as part of %rname

Buildarch: noarch
Requires: %rname-bin >= 0.7.0

Source0: %rname-%what.uqm

%description
Pack IV: The New Alliance of Free Stars

Tracks:
01_-_Main_Menu_-_Control_the_Stars.ogg
02_-_Intro_-_Into_the_Void.ogg
03_-_Chmmr_-_Photosynthesis.ogg
04_-_Shofixti_-_Bonsai!.ogg
05_-_Syreen_-_Close_Encounters_of_the_Seventh_Kind.ogg
06_-_Yehat_-_Years_Late_Mix.ogg
07_-_Pkunk_-_Pkunks_Not_Dead.ogg
08_-_Utwig_-_Mask_of_Ultimate_Embarrassment_and_Shame.ogg
09_-_Zoq-Fot-Pik_-_Frungy_Party.ogg
10_-_Orz_-_Squeezing_the_Juice.ogg
11_-_Utwig_-_The_Ultron.ogg
12_-_Supox_-_Shake_Yer_Rootz.ogg
13_-_Spathi_-_Fwiffos_Starrunner.ogg
14_-_Super_Melee_Menu_-_Fight!.ogg
16_-_Outro_-_Awaking_Dreams.ogg
17_-_Credits_-_So_Long_and_Thanks_for_All_the_Orz.ogg

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
* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.7.0-alt1
- initial spec
- version for uqm >= 0.7.0
