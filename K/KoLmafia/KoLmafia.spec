Name: KoLmafia
Version: 14.7
Release: alt1.svn9619
Url: http://kolmafia.sf.net
Group: Games/Adventure
License: BSD
Source: http://puzzle.dl.sourceforge.net/sourceforge/kolmafia/%name-%version.tar.gz
Source1: %name.desktop
Source2: %{name}_32.png

Packager: Damir Shayhutdinov <damir@altlinux.ru>
BuildPreReq: ant
BuildRequires(pre): java-devel-default rpm-build-java

Patch0: KoLmafia-11.9-alt-launch-browser.patch
Patch1: KoLmafia-%version-alt-equipment-fixes.patch
Patch2: KoLmafia-%version-alt-pvp-fixes.patch
Patch4: KoLmafia-%version-alt-monsters-info.patch
Patch5: KoLmafia-%version-alt-badmoon-fixes.patch
Patch7: KoLmafia-%version-alt-ui-fixes.patch
Patch8: KoLmafia-%version-alt-llama-gong.patch

Requires: java java-common

Summary: KoL online game client
BuildArch: noarch
%description
KoLmafia is a cross-platform desktop tool, written in Java (J2SE 1.4 compliant), 
which interfaces with the online adventure game, Kingdom of Loathing.
See http://www.kingdomofloathing.com and http://kolmafia.sf.net for details.

%prep
%setup -c
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1

REVISION=`echo "%release" | sed 's@alt.*svn@@'`
sed -i "s@name=\"revision\" value=\"0\"@name=\"revision\" value=\"$REVISION\"@" build.xml

%build
mkdir dist
ant

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_javadir
mkdir -p %buildroot%_desktopdir
mkdir -p %buildroot%_niconsdir

cp dist/%name-%version.jar %buildroot%_javadir/%name-%version.jar
ln -sf %name-%version.jar %buildroot%_javadir/%name.jar
cat > %buildroot%_bindir/%name <<EOF
#!/bin/sh
mkdir -p \$HOME/.KoLmafia
pushd \$HOME/.KoLmafia >/dev/null 2>&1
java "-DBROWSER=\$BROWSER" -jar %_javadir/KoLmafia.jar "\$@"
popd >/dev/null 2>&1
EOF
chmod +x %buildroot%_bindir/%name
cp %SOURCE1 %buildroot%_desktopdir/%name.desktop
cp %SOURCE2 %buildroot%_niconsdir/%name.png

%files
%_bindir/%name
%_javadir/%name.jar
%_javadir/%name-%version.jar
%_desktopdir/%name.desktop
%_niconsdir/%name.png


%changelog
* Mon Jul 11 2011 Damir Shayhutdinov <damir@altlinux.ru> 14.7-alt1.svn9619
- Updated to KoLmafia-14.7 (sv9619)
  + Too many changes to pin point

* Sun Mar 06 2011 Damir Shayhutdinov <damir@altlinux.ru> 14.4-alt1.svn9137
- Updated to KoLmafia-14.4 (svn9137)
  + You can now use chat commands from CLI (like /command1 && /command2)
  + Pandamonium
  + February IOTM support
  + Revamped Cobb's Knob
  + March IOTM support
  + Tons of other bugfixes


* Sat Jan 22 2011 Damir Shayhutdinov <damir@altlinux.ru> 14.3-alt1.svn8923
- Updated to svn8923
  + More CRIMBCO support
  + January IOTM support
  + Traveling Trader  Disco Bandit skill
  + Lots of other fixes

* Thu Dec 23 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.3-alt1.svn8845
- Updated to KoLmafia-14.3 (svn8845)
  + Automated closeting of worthless items if using chewing gum on a string
  + New Typical Tavern support
  + Skeleton invasion
  + Major Rays are now effects, remove counters
  + Pumpkins!
  + New bat hole
  + Robot Reindeer
  + CRIMBCO
  + Elf Alley support
  + Lots of other fixes

* Mon Oct 18 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.2-alt1.svn8690
- Updated to KoLmafia-14.2 (svn8690)
  + Hippo Ballerina (KoL Con fam) support
  + Sewer change (yay!)
  + Quantum Taco
  + FOTY
  + Lots of other fixes

* Tue Sep 14 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.1-alt1.svn8618
- Updated to svn6818
  + New food/drink changes
  + August/September IOTMs
  + Skill purchase changes
  + Pottery items/skills
  + New Friars items
  + Lots of other bugfixes

* Tue Jul 20 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.1-alt1.svn8549
- Updated to KoLmafia-14.1 (svn8549)
  + Add hints to Game Grid Arcade games (enable it in preferences)
  + Vanya's Castle
  + June IOTM
  + Traveling Trader item
  + Trace sugar items counters
  + Magic Commune
  + Lots of other bugfixes

* Sun Jun 06 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.0-alt1.svn8479
- Updated to svn8479
  + Custom Combat Scripts now use KoL combat scripts
  + Traveling Trader items
  + May and June IOTM support
  + Track slimeling's fullness
  + Underworld familiar
  + Uncle P Antiques paintings content
  + Many other fixes

* Sun Apr 18 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.0-alt1.svn8393
- Updated to svn8393
  + Traveling trader item
  + Tweaks in louvre prediction
  + Few bugfixes

* Sun Apr 11 2010 Damir Shayhutdinov <damir@altlinux.ru> 14.0-alt1.svn8373
- Updated to KoLmafia-14.0 (svn8373)
  + Bugged bugbear support
  + Revamped Greater Than Sign
  + French guard turtles are now distiguised in CSS
  + "hatter" command which tells what effects are available for your hats
  + New TT skill
  + Legendary Beat quest items
  + Various other fixes

* Sun Mar 14 2010 Damir Shayhutdinov <damir@altlinux.ru> 13.9-alt1.svn8268
- Updated to svn8268
  + More IOTM support (incl. chess autosolver, hat switcher and tweedleporium)
  + New Uncle P's antiques
  + Various other fixes


* Mon Mar 08 2010 Damir Shayhutdinov <damir@altlinux.ru> 13.9-alt1.svn8233
- Updated to svn8233
  + More nemesis quest
  + March IOTM support
  + Fix manual choice from O Cap'm
  + Show Disco Combos in combat - turn it on in Preferences-Relay (say hi to raorn@)
  + Quick switch of familiars from KoL GUI
  + Solve the lava
  + Go to Goal button for Louvre & Fog
  + Other bugfixes

* Thu Feb 18 2010 Damir Shayhutdinov <damir@altlinux.ru> 13.9-alt1.svn8153
- Updated to KoLmafia-13.9
  + Fix choice conditions counted twice
  + KoLmafia now automatically learns new items and writes overrides
  + Travelling trader
  + BRICKOs!!!
  + ballpit CLI command
  + "Use another dance card" option on Rotting Matilda adv
  + pool CLI command (i.e pool mys, mus, mox)
  + Nemesis quest items (not complete)
  + Tons of other bugfixes and minor features

* Sat Jan 23 2010 Damir Shayhutdinov <damir@altlinux.ru> 13.8-alt1.svn7998
- Updated to svn7998
  + Travelling trader item & skill
  + Color monster name based on the element
  + Support for Stinky Cheese counter
  + Various bugfixes

* Sat Jan 02 2010 Damir Shayhutdinov <damir@altlinux.ru> 13.8-alt1.svn7952
- Updated to KoLmafia-13.8 (svn7952)
  + Rest of Crimbo support (including Tree)
  + January IOTM support
  + When you visit the shore, add a 35-turn counter to let you space out shore trips
  + Many other fixes

* Thu Dec 17 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.7-alt1.svn7890
- Updated to svn7890
  + Some support for Crimbo town
  + Deduct crimbux when play 11 or slots
  + Some minor fixes

* Wed Dec 16 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.7-alt1.svn7880
- Updated to KoLmafia 13.7 (svn7880)
  + Many chat fixes
  + December IOTM support
  + Crimbo support
  + Arena params for FOTYs
  + Many other fixes

* Sat Nov 07 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.6-alt1.svn7788
- Updated to svn7788
  + More Skate Park support
  + Familiar support in effect maximizer
  + Familiars of the year
  + Special Badmoon adventures support
  + Mr. Familiars are free pulls
  + When semirare is encountered, add "semirare window begin/end counters"
  + Dolphin whistle support
  + Sea familiars are now marked as such
  + Halloween items support
  + November IOTM support
  + Ajaxify outfit switching and NPC purchases
  + Many other fixes

* Thu Oct 08 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.6-alt1.svn7713
- Updated to KoLmafia-13.6 (svn7713)
  + October IOTM support
  + New Bathroom choice support
  + Skate Park support
  + Tons of other fixes

* Wed Sep 30 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.5-alt1.svn7674
- Updated to svn7674
  + Fix quest item recognition
  + Autosort button in Trophy Arranger
  + Many other bugfixes

* Mon Sep 21 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.5-alt1.svn7642
- Updated to svn7642
  + Show Hero possibility on battlefield
  + User-added counters now can use location (loc=N)
  + More efficient mana burning
  + Many other fixes

* Mon Sep 07 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.5-alt1.svn7608
- Updated to svn7608
  + Sugar tome preliminary shupport
  + Heartbreaker's hotel support
  + Counter for Harold's bell
  + Various other fixes

* Tue Sep 01 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.5-alt1.svn7589
- Updated to svn7589
  + Chrys Rock items
  + Wumpinator fix (inline image)
  + Various other fixes

* Mon Aug 24 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.5-alt1.svn7564
- Updated to KoLmafia-13.5 (svn 7564)
  + MMG support
  + Improved support of He-Builder
  + Added "filter by autosell price" option in Item Manager (type "$ > 100")
  + Support for new Nemesis quest (auto password guessing)
  + 4-d camera
  + Refactor Wumpus Manager (tie it with Wumpinator)
  + Many other fixes

* Thu Aug 06 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.4-alt1.svn7523
- Updated to svn7523
  + IOTM
  + Floaty content
  + Added "whatif" command, which tells what happens if you do a CLI command
  + Tons of Minor bugfixes

* Mon Jul 27 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.4-alt1.svn7489
- Updated to svn7489
  + Added Modifer Maximizer feature (super hot!)
  + Wumpus hunt improvements
  + Many bugfixes

* Mon Jul 13 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.4-alt1.svn7459
- Updated to KoLmafia-13.4 (svn7459)
  + Slimeling support
  + Fix gear-tags (closes #20759)
  + Minor bugfixes 

* Fri Jul 10 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3.1-alt1.svn7452
- Updated to svn7452
  + Mer-kin digpick
  + July IOTM support
  + added CLI command "modifies <param>" that lists all the known source of param modification
  + Many bugfixes

* Mon Jun 29 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3.1-alt1.svn7429
- Updated to svn7429
  + July IOTM preliminary support
  + Hobopolis Market spoilers
  + Some minor fixes and ASH improvements

* Thu Jun 18 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3.1-alt1.svn7401
- Updated to svn7401
  + More Wumpus support
  + Slime monster stats
  + Minor bugfixes

* Sun Jun 14 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3.1-alt1.svn7392
- Updated to KoLmafia-13.3.1 (svn7392)
  + Fix usage of items which gives choice or combat advs
  + More slime content
  + Update combat items count from item dropdown list each round in combat
  + Some bugfixes

* Tue Jun 09 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3-alt2.svn7380
- Updated to svn7380
  + Fix multi-use of restoratives
  + Wumpus hunt improvements

* Tue Jun 09 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3-alt2.svn7378
- Updated to svn7378
  + Emergency patch for server-side restorative changes
  + Added Sandworm to list of Basement familiars (replacing Sombrero)
  + Some helps in 6th element quest
  + New options to "burn" CLI command - "burn extra" (like previous),
    "burn *" - burning all mana, "burn <num>" - no more than specified
    amount of MP, "burn -<num>" - burn all but num MP.
  + Mafia now can be more intelligent about burning, during "nuns" CLI
    command or when eating Dr. Lucifer, it will first burn the excess
    mana, then restore.
  + Many other Slime and agua de vida items updates 

* Fri Jun 05 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.3-alt2.svn7362
- Updated to KoLmafia-13.3 (svn7362)
  + Preliminary June IOTM support
  + Added choice spoilers for the Wumpus Hunt.
  + Fix quest items recongnition due to server-side change
  + More Slimy updates
  + Some bugfixes

* Wed Jun 03 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.2-alt2.svn7342
- Fix building 

* Tue Jun 02 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.2-alt1.svn7342
- Updated to svn7342
  + Added "hottub" or "soak" command to visit VIP hot tub
  + Support for infernal Seals
  + Disturbing fanfic update
  + Preliminary support of Slime Tube
  + Many other fixes

* Mon May 25 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.2-alt1.svn7308
- Updated to svn7308
  + Fix solving dwarf code
  + Aria effect cap on +60 ML
  + Kmail can now be sent from the CLI (send to <recipient> || <message>)
  + Many other minor fixes

* Sun May 17 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.2-alt1.svn7273
- Updated to KoLmafia-13.2 (svn7273)
  + Support for the Vacuum Chamber (factory vacuum <n> <item>)
  + Seal Clubber and Turtle Tamer updates support
  + Dwarf code solver
  + Many bugfixes

* Wed May 06 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.1-alt1.svn7235
- Updated to svn7235
  + Added "factory setdigits" and "factory report" CLI commands
  + Fix combat action bar detection
  + New Seal Clubber update
  + Minor fixes

* Sun May 03 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.1-alt1.svn7226
- Updated to svn7226
  + Add "factory check" and "factory report" CLI commands
  + More Deluxe Mr. Klaw items
  + Fix breakfast with Deluxe Mr. Klaw

* Sat May 02 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.1-alt1.svn7221
- Updated to svn7221
  + New dwarven quest support
  + Clan VIP Lounge support
  + New CLI command "factory report CIJFDGB"
  + New Deluxe Mr. Klaw items
  + Many other fixes

* Tue Apr 21 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.1-alt1.svn7190
- Updated to svn7190
  + Change name of super-spikey hair gel
  + Add a preference for stealth login
  + Ronin ends as you free the king
  + Spaded formulas for mutant Raffle familiars
  + Implement 'nonstackable watch' boolean modifier for watches
  + Fix boss warnings
  + Many other fixes

* Sat Apr 11 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.1-alt1.svn7155
- Updated to svn7155
  + Fix hedge puzzle processing
  + Fix rampaging adding machine in Birdform
  + Massive changes with the way how GET/POST request are processed in relay
  + Various other fixes

* Fri Apr 03 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.1-alt1.svn7132
- Updated to KoLmafia-13.1 (svn7132)
  + April IOTM/IOTD
  + More new items
  + Few bugfixes

* Mon Mar 30 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.0-alt1.svn7125
- Updated to svn7125
  + Add switch support for ASH
  + Typical Tavern swill and its byproducts
  + New ranged weapons (with mariachi support)
  + Fix dusty wines auto-identification
  + Many other fixes

* Sun Mar 22 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.0-alt1.svn7092
- Updated to svn7092
  + New items, recipes and familiars
  + When deciding whenever to buy or create an item, consider the price of ingredients recursively
  + Initial support for new pastamancers combat ghosts
  + Many other fixes

* Fri Mar 06 2009 Damir Shayhutdinov <damir@altlinux.ru> 13.0-alt1.svn7045
- Updated to KoLmafia-13.0 (svn7045)
  + Added plurals (fixing buying from mall)
  + Add "quark" CLI command for pasting with quarks
  + Sushi can be created and consumed with "create" command
  + March IOTM
  + Vampire pearl
  + Various other fixes

* Thu Feb 26 2009 Damir Shayhutdinov <damir@altlinux.ru> 12.9-alt1.svn7011
- Updated to svn7011
  + Massive Mall changes
  + Cache mall requests
  + New commands (cheapest and expensive), in addition to special word "it" (cheapest hi mein; eat 3 it)
  + Delete relay/basement.js due to change in basementing interface
  + Fix in hobo gristles bounty
  + Many other fixes

* Sat Feb 21 2009 Damir Shayhutdinov <damir@altlinux.ru> 12.9-alt1.svn6985
- Updated to svn6985
  + New pickpocket items, recipes and such
  + More updates to effects
  + Add automatic sheet/olfaction/extractors usage with conditions
  + Tons of other bugfixes

* Sat Feb 07 2009 Damir Shayhutdinov <damir@altlinux.ru> 12.9-alt1.svn6904
- Updated to KoLmafia-12.9 (svn6904)
  + New CLI command (fold <item>) which folds items like Putty or Origami until it gets the desired item
  + Limit item price with buy command (buy N item @ limit)
  + Sea content (mine and bar)
  + Identify dusty bottles as soon as you get spectacles (without equipping)
  + After ascension, perform complete session refresh
  + February IOTM support
  + Custom outfits can now execute actions when equipped, if you add special strings to name
    + F=<familiar> - change familiar
    + E=<famitem>  - equip fam item
    + M=<mood>     - change mood
    + C=<command>  - CLI command
  + New pickpocket-only items
  + Added more control over "automatic actions in combat", like pickpocketing, entangling or using MP restorers in combat
  + Many other fixes

* Tue Jan 27 2009 Damir Shayhutdinov <damir@altlinux.ru> 12.8-alt1.svn6839
- Updated to svn6839
  + Warn about unpurchased trophies before ascension
  + When item drops during combat, accomodate them and append to final combat page
  + New sea content
  + 10-turn counters after use of PADL phones or windchimes
  + Disable HTTP timeout in valhalla (better ascension logging)
  + Various bugfixes

* Mon Jan 19 2009 Damir Shayhutdinov <damir@altlinux.ru> 12.8-alt1.svn6792
- Updated to svn6792
  + New underwater content: deep sauce, tempuramancy, sea salt pulverization
  + +ML no longer has an effect on combat rate
  + Various other improvements

* Sun Jan 11 2009 Damir Shayhutdinov <damir@altlinux.ru> 12.8-alt1.svn6748
- Updated to KoLmafia-12.8 (svn6748)
  + Sushi rolling fixes
  + Support for summoning Pastamancer's ghost in CCS (summon ghost)
  + January IOTM and its derivatives
  + Rage gland support
  + Detect Black Cat's prevention of skill and item use during combat
  + Keep track of the number of uses of each Birdfrom skill that counts towards getting feathers
  + Mining interface update (better view), like in tavern
  + Manage free pulls
  + Added "gong" CLI command for controlling gong choices
  + Various other fixes

* Sun Dec 28 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.7-alt1.svn6684
- Updated to svn6684
  + Add "grow" link to familiar hatchlings in relay
  + Use "consume some" feature to eat/drink multiple at once
  + In Hidden City, add spoilers for billiard balls
  + Add spoiler for all consumable items in Item Manager (like "5/15 Fishy")
  + Experimental upgrade to Mr. Skills in breakfast - see preferences

* Thu Dec 25 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.7-alt1.svn6661
- Updated to svn6661 Crimbo Edition
  + Maki rolling support
  + The rest of Crimbo items/effect
  + Show counters in relay browser
  + Minor bugfixes
  + Merry Crimbo!

* Fri Dec 19 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.7-alt1.svn6636
- Updated to svn6636
  + Added Crimbo zones for auto-adventuring
  + Recognize item usage from Relay Browser
  + Extended "recent location history" to 5 locations
  + Support for locking fam items via CLI (familiar lock/unlock)
  + Detects "eat some/drink some" in relay browser
  + Sushi can be created from Item Manager now
  + New Crimbo effects, items, monsters etc

* Sun Dec 14 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.7-alt1.svn6621
- Updated to svn6621
  + If the character has spectacles equipped, identify dusty wine if needed
  + Fix auto-adventuring in non-bounty zones
  + Blob-shaped Crimbo Cookie

* Sat Dec 13 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.7-alt1.svn6616
- Updated to KoLmafia-12.7 svn6616
  + Crimbo content
  + Fix various problems due to server-side lag-fighting changes
  + Many other fixes

* Sun Dec 07 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6586
- Updated to svn6586
  + Added properties of depleted grimacite equip
  + Toaster and Feng-shui are no longer campground items
  + Added Pulverize panel to Equipment Manager
  + December IOTM, Sneaky Pete's day items, Advent Calendar items
  + Protection from accidental dance card usage
  + New underwater items, effects and a familiar
  + Add Big Brother to the Coin Masters
  + Various other fixes

* Thu Nov 27 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6538
- Updated to svn6538
  + More underwater content
  + Decorate wheel choice in pyramid
  + Tirevalanche calculator in BB
  + 3 turns counter for dance card
  + Initial support for "Summon Stickers" skill
  + GMoB and ballroom state shown on the second floor of Spookyraven's
  + Various other fixes

* Mon Nov 10 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6488
- Updated to svn6488
  + Add 'gnaw through' choice
  + Add choice spoilers for all llama lama gong choice adventures
  + Underwater content
  + November IOTM support
  + Add Clownosity as a tracked modifier
  + Add moon sign spoilers to the resurrect screen
  + Halloween items
  + Add hatrack spoilers to Gear Changer
  + Add Daily Deeds list
  + Restore "galaktik" CLI command to fully or partially cure HP or MP
  + Give choice spoilers to Orcish Frat House Blueprints

* Sat Oct 18 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6402
- Updated to svn6402
  + Fixed exceptions when mallselling item you don't have in inventory
  + Disambiguate monsters with same name
  + Fix certain frames not closing properly
  + Fix wand of nagamar warning before NS fight
  + In the bird form, plump juicy grubs and delicious moths are now options for HP/MP restore.
  + Various other minor fixes

* Sun Oct 12 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6378
- Updated to svn6378
  + Preliminary support for underwater content
  + Autoequip gatorskin umbrella when lose one in the sewers
  + Track monsters tagged by Olfaction or odor
  + Added drop location spoilers to the Spookyraven wine cellar
  + New annual familiars
  + Consumption helpers like divine champagne flute, now can be "used" before consuming
  + Fix pirate {brochure, pamphlet, tract} buying in the Barrrtlesby's

* Sat Oct 04 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6334
- Updated to svn6334
  + Add meat/item drop bonuses when wearing multiple brimstone
  + Disembodied Hand support
  + Added decorator for Barrel Full of Barrels
  + Various other fixes

* Fri Sep 26 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6316
- Updated to svn6316
  + Fix crafting
  + Fullness/inebrity for Hobo Food Court food & booze
  + New sauceror recipes

* Wed Sep 17 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.6-alt1.svn6298
- Updated to KoLmafia-12.6 (svn6298)
  + More support for llama automation
  + Added "Collect Garbage" fun button right near memory monitor
  + Haiku State of Mind support
  + Support fo tallying hobo parts
  + Long skinny balloons update
  + Spice melange support
  + Various other fixes

* Wed Sep 03 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.5-alt1.svn6275
- Updated to svn6275
  + Configure Hobopolis semirare advs
  + Server 8 doesn't exist anymore
  + New Haiku dungeon
  + September IOTM
  + Fix Goblin King detection
  + Various other fixes

* Thu Aug 14 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.5-alt1.svn6232
- Updated to svn6232
  + Rainbow gravitation support
  + New halloween candies
  + Zapping hobopolis outfits
  + Multi-use bird-form consumables
  + Support for August IOTM
  + Hobo nickel count shows on the marketplace choice adventure
  + Hobopolis choice adventures support

* Thu Jul 17 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.5-alt1.svn6207
- Updated to svn6207
  + New chefstaves
  + Junkyard update
  + Log progress of war in CLI an session log
  + Rainbow's Gravity initial support
  + Many other fixes


* Thu Jul 03 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.5-alt1.svn6184
- Updated to svn6184
  + Hobopolis support
  + July IOTM support
  + Reset counters if people ascend outside KoLmafia
  + Arrrbor day items
  + Many additional fixes

* Sat Jun 21 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.5-alt1.svn6158
- Updated to KoLmafia-12.5 (+patches to svn6158)
  + Fix use class of bird items
  + Auto-create badass belt
  + Still no hobopolis support!
  + Added hobo/ghost feeding links in item manager
  + Fix Haunted Wine Cellar zones
  + Various other fixes

* Mon Jun 09 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6124
- Updated to svn6124
  + Fix item recognition
  + Restore old clover protection
  + Fix basement outfits
  + Fix purchasing of identified bang potions in mall

* Sun Jun 08 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6114
- Updated to svn6115
  + Fix backup outfit
  + Added some more bird skills from IOTM

* Sun Jun 08 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6109
- Updated to svn6109
  + Fix some form handling
  + Fix candy hearts summoning with mana burning
  + Haunted Wine Cellar is now 4 zones.

* Thu Jun 05 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6100
- Updated to svn6100
  + New SSPD day items
  + During mana burning, alternate libram casts between divine & hearts
  + Initial support for June IOTM

* Sun May 18 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6087
- Updated to svn6087
  + More monsters info
  + Initial support for the May IOTM
  + Estimate current fullness/spleen based on failure to consume messages
  + Fix incorrect counters decrementing when pulverizing

* Wed Apr 30 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6075
- Updated to svn6075
  + Metallic foil cat ears: you can has dem!
  + New puppy formula for item drops
  + Ignore skills you can't use in the current ascension

* Tue Apr 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6069
- Updated to svn6069
  + New PM skills & content
  + Fix delicious salad fullness
  + Add zap wand exploding to ascension reminders
  + Fix outfit checkpointing

* Wed Apr 02 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6028
- Updated to svn6028
  + Fixed battlefield counting with action bar
  + Added PRESSIE as possible sombrero replacement for basement
  + Initial support for April IOTM

* Sun Mar 30 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6021
- Updated to svn6021
  + New hilarious items and effects
  + Arrrbor day items
  + Some minor fixes

* Sat Mar 22 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn6011
- Updated to svn6011
  + New Elemental Resistance formala
  + Fix Insult Beer Pong first round matching
  + Fix resistances for elemental powders

* Thu Mar 20 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1.svn5999
- Updated to svn5999
  + First pass on new elemental resistances
  + Crossbow Fever skill
  + Added checks for headless DISPLAY
  + Some minor fixes

* Mon Mar 17 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.4-alt1
- Updated to KoLmafia-12.4
  + Applied style to relay buttons (raorn@)
  + Saint Sneaky Pete Day content
  + Added NotBot buffbot support
  + More combat bar support
  + Other fixes

* Fri Mar 14 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.3-alt1.svn5957
- Updated to svn5957
  + Fix handling of *
  + Generic Summer Holiday
  + More reliable end-of-combat detection with new combat bar
  + Other fixes

* Mon Mar 10 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.3-alt1.svn5922
- Updated to KoLmafia-12.3 (svn5922)
  + Fix bang potion at three gates puzzle
  + Improved DoD ring enchantments
  + Additional hatrack support
  + Other bugfixes

* Thu Mar 06 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5872
- Updated to svn5872
  + Fix recent equipment page update
  + Fuzzy matching enhancements
  + Experimental item aliasing
  + Other minor fixes

* Sun Mar 02 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5854
- Updated to svn5854
  + Experimental Spleen panel
  + Preliminary support for March IOTM
  + Fix shadow fight
  + Other fixes

* Thu Feb 28 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5843
- Updated to svn5843
  + Various fuzzy matching improvements
  + Fix "*" meaning in CLI
  + Auto-switch to attack when using dictionary on an adding machine
  + Increase timeout wait time to 16 seconds
  + Various bugfixes
  + Detect when shore trip will overrun the fortune counter

* Tue Feb 26 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5822
- Updated to svn5822
  + Updated monsters-info patch (Hey Deze monster drops)
  + Restore fuzzy matching
  + Lo meins dewokified
  + Restore relay browser links from bounty items
  + Minor bugfixes

* Sun Feb 24 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5811
- Updated to svn5811
  + Fixed worthless item acquisition
  + Fix cheese counting in relay
  + Fly-By-Knight Heraldy support
  + Minor bugfixes

* Fri Feb 22 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5798
- Updated to svn5798
  + Update monsters-info patch (Pre-war Hippy/Frat monsters)
  + Before you ascend, use up any 31337 scrolls
  + Refactor use/create/navigate/eat link decorations
  + Fix auto attack setting/unsetting
  + Set price ceiling of 20k on automated purchases
  + Some ASH enhancements
  + Fix El Vibrato helmet card insertions
  + Remove fuzzy matching for CLI commands
  + Relay browser clover protection always active

* Mon Feb 18 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.2-alt1.svn5778
- Updated to KoLmafia-12.2 (svn5778)
  + More El Vibrato support (use power spheres)
  + Store Manager now handles items with parenthesis
  + Fix various item renames
  + More aggressive clover protection
  + Never reset user-defined autoattack
  + Other fixes

* Thu Feb 14 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5734
- Updated to svn5734
  + Updated price-limit patch from raorn@
  + Sync monsters-info patch with upstream
  + rename "visit" to "check" in Coin Masters window

* Wed Feb 13 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5733
- Updated to svn5733
  + El Vibrato support
  + Some more monster drops fixes
  + More refactorization
  + Some bugfixes

* Sat Feb 09 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5711
- Updated to svn5711
  + More Friday update items
  + Evil Golden Arches excluded from breakfast
  + Add "ghost" command to feed GGG with food
  + Clean inventory before update
  + More ASH fixes

* Fri Feb 08 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5703
- Updated to svn5703
  + Fix inventory identification
  + Fix type in monsters-info patch
  + More ASH refactorization

* Tue Feb 05 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5685
- Updated to svn5685
  + Fix infinite recurse bug (by refactoring)
  + Automatic pirate insult collection
  + "insults" CLI command to display collected insults
  + Calculate and display odds of winning Insult Beer Pong Match
  + Massive code reorganization continued, now ASH is refactored

* Sun Feb 03 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5667
- Updated to svn5667
  + Updated equipment-fixes patch from raorn@
  + Rename Post-war Frat/Hippy houses to Stone Age ones to avoid confusion
  + Minor bugfixes

* Sat Feb 02 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.1-alt1.svn5660
- Updated to KoLmafia-12.1 (svn5660)
  + More code reorganization -> more regressions to be expected
  + February IOTM
  + Log Daily Dungeon adventures
  + Allow connections to time out
  + New, faster Display Case access
  + KoL now requires confirmation to change housing type
  + Yuletide items and effects
  + Many other fixes

* Sat Jan 19 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.0-alt1.svn5583
- Updated to svn5583
  + Silly divine can was renamed
  + Massive code reorganization, some regressions can be expected
  + "counters" command lists last turn where a semirare was found
  + New halloween candies
  + Auto-select correct stone sphere
  + New (old) bookshelf behaviour
  + new command "raffle <count> [inventory|storage]" for buying raffle tickets

* Tue Jan 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 12.0-alt1.svn5549
- Updated to KoLmafia-12.0
  + More Cyborger patterns
  + Going Postal quest fixes
  + More Coin Masters: now BHH
  + Recognize bookshelf summons in relay
  + Updated adv/stats for some food
  + Recognize zapping
  + Add "Go back to Island" link for "no more ducks" page
  + Collect farmer products/bombs during in-war breakfast
  + Attempt to enable access to Hangk in BadMoon after freeing the king
  + Various other fixes

* Mon Jan 07 2008 Damir Shayhutdinov <damir@altlinux.ru> 11.9-alt1.svn5505
- Updated to svn5505
  + quest-fixes patch has gone upstream
  + Add muscle, mysticality, and moxie as standard ocean destinations
  + Fix Ronin detection in casual runs
  + Crimbo town (unfortunately, it's gone)
  + Enable crimbo toy usage at breakfast
  + Bookshelf support
  + IOTM items
  + Show adventures used in creation queue
  + Log fortune cookie Lucky Numbers to gCLI and session

* Sun Dec 30 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.9-alt1.svn5468
- Updated to svn5468
  + Updated familiar training info
  + "concert <effect>" command to get desired status effect
  + More coin master stuff
  + Fix "worthless item" condition
  + Usual fixes

* Wed Dec 26 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.9-alt1.svn5450
- Updated to svn5450
  + Almost all Crimbo content
  + Crimbo and Cursed outfits
  + Fix relay browser overrides
  + Various fixes

* Wed Dec 19 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.9-alt1.svn5413
- Updated to svn5413
  + More Crimbo content
  + Bulk purchases when running moods
  + Increase timeout to 30 seconds
  + Smarter handling of relay combat actions

* Sun Dec 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.9-alt1.svn5387
- Updated to svn5387
  + More Crimbo content
  + Better cafe support
  + Various other bugfixes

* Tue Dec 11 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.9-alt1.svn5370
- Updated to 11.9 (svn5370)
  + More Pirate content
  + Log unexpected monsters
  + Sidequest marking is optional
  + Count nuns meat
  + Clingfilm recipes

* Wed Dec 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.8-alt1.svn5333
- Updated to svn5333
  + Auto-select best "papaya war" choice (by raorn@)
  + Completely normal Advent treats
  + Crimbo P.R.E.S.S.I.E.
  + Some customized images for big islands sidequests
  + Preliminary Pirate content support

* Sat Dec 01 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.8-alt1.svn5318
- Updated to svn5318
  + Battlefield casualty counters
  + New holiday drinks
  + Highlight molybdenium tools usage
  + Guy Made Of Bees counter and defeat
  + Other minor fixes
  + Zim Merman guitar fix from raorn@

* Thu Nov 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.8-alt1.svn5287
- Updated to svn5287
  + Jolly Roger charm
  + Many bugfixes
  + Blue glowstick
  + New KoL holidays

* Thu Nov 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.8-alt1.svn5254
- Updated to svn5254
  + Limit price of auto-purchased items to 2xminimal mall price
  + Added zap command to menu
  + Automatically filter out unzappable items from zap combo box
  + Add more info to snapshot at startup (printed to debug log)
  + Fix new events detection
  + Many other bugfixes

* Thu Nov 01 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.8-alt1.svn5226
- Updated to svn5226
  + Correct AT/DB skills
  + New wad transmutation recipes
  + New Ultra Rare item (Dallas Dynasty Falcon Crest shield)
  + Basic November IOTM support
  + Spooky Surpize Egg and Tiny Plastics series 2

* Mon Oct 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.8-alt1.svn5220
- Updated to 11.8 release (svn5220)
  + Festival of Jarlsberg holiday and an item
  + JEW hat buff duration change works from inventory

* Tue Oct 23 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.7-alt1.svn5215
- Updated to svn5215
  + Fix Swing's handling of <br> tags for copy/paste
  + Support for bricks of sand
  + Fix some ASH bugs

* Wed Oct 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.7-alt1.svn5209
- Updated to svn5209
  + Fix inebrities
  + Add option for price limit for expensive items (from raorn@)
  + Updated monsters info for Oasis, Pyramid, Wine Racks, Orchard, Dooks, 
    Themtar Hills, Black Forest, Palindome, and Bodyguard Bat (from damir@)

* Tue Oct 16 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.7-alt1.svn5207
- Updated to svn5207
  + Gnomad camp quest support
  + Friars blessing support
  + Fix forum links

* Thu Oct 11 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.7-alt1.svn5202
- Updated to svn5202
  + New Mr. Store familiars, new items and new effects
  + Fixes PvP vs. Devsters or defeated players

* Sat Oct 06 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.7-alt1.svn5201
- Updated to svn5201
  + New Penultimate choice adventure
  + Initial support for October FIOTM
  + Remove MCD boss reminder in BadMoon
  + Fix monster level in basement spoiler
  + Complete BadMoon status effects

* Mon Sep 24 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.7-alt1.svn5191
- Updated to svn5191
  + Lucrecore support
  + More BadMoon support
  + Usual bugfixes

* Wed Sep 12 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.6-alt1.svn5124
- Updated to svn5124
  + Fixed bug with mood editing
  + Demon summoning support (via CLI)
  + Black pudding and drum machine adventures
  + Lowered stat requirement for greater-than sign
  + Bounty hunting outfit
  + Fix goat cheese pizza tracking
  + Abort timeout retries when world peace is declared
  + Gauntlet fixes

* Sun Sep 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.6-alt1.svn5030
- Updated to 11.6 + new features (svn5030)
  + More BadMoon support
  + September IOTM skill support
  + Added BadMoon to ascension page
  + Usual bugfixing

* Wed Aug 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.5-alt1.svn4965
- Updated to svn4965
  + More BadMoon support
  + Telescope support
  + Many bugfixes

* Tue Aug 28 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.5-alt1.svn4929
- Updated to 11.5 + new features (svn4929)
  + Initial Bad Moon support (Store, Styx, some status effects, ash function in_bad_moon()
  + Usual bugfixing

* Thu Aug 23 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.4-alt1.svn4891
- Updated to svn4891
  + Jiggle stationary button
  + Fix session time-in
  + Add "auto" button for choice adventures
  + Allow "jiggle" as a Custom Combat command
  + Relay browser safety spoilers
  + New Haunted Kitchen items
  + Better estimate for Gauntlet Gauntlet

* Mon Aug 20 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.4-alt1.svn4822
- Updated to 11.4 + fixes (svn4822)
  + CLI login fixes and Daily Dungeon fixes gone upstream
  + Item drops from gremlins
  + Around the World miniquest support
  + Usual bugfixing

* Fri Aug 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.3-alt1.svn4763
- Updated to svn4763
  + Some fixes to Daily Dungeon treasure chests handling by raorn@
  + Fixes to allow CLI to run with empty DISPLAY environment variable by raorn@
  + Massive basement impoves and fixes
  + Show "Entangling noodles" button in battle
  + More spleentacular items
  + Usual bugfixing

* Tue Aug 14 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.3-alt1.svn4727
- Updated to svn4727
  + More default actions for moods
  + Fix "item not found" errors
  + Fix mood with skills handling
  + Update fullness/inebrity data for food/booze
  + Basement spoilers
  + Item drop data for Black Forest and Arid, Extra-Dry Desert
  + Other bugfixes

* Fri Aug 10 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.3-alt1.svn4695
- 11.3 version + 2 commits
  + Many bigfixes
  + More filters in item manager
  + Auto-disassembly of barrel clovers
  + Wizard Action Figure
  + Fix CLI mode login

* Thu Aug 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt2.svn4605
- Updated to svn4605
  + Couple of new monsters
  + Couple of new status effects
  + Usual bugfixing
  + Introduce relay ASH scripting

* Mon Jul 30 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt2.svn4541
- Updated to svn4541
  + Fix mood handling during auto adventure
  + Exotic Parrot
  + Add a couple of monsters

* Sun Jul 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt2.svn4522
- Fixed equipment manager patch

* Sun Jul 29 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt1.svn4522
- Updated to svn4522
  + New patch for better equipment manager useability
  + Option to show monster stats/drops in relay browser

* Sat Jul 28 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt1.svn4505
- Updated to svn4505
  + Many bugfixes
  + Rampaging Adding Machine support
  + Patch for hagnk-like equipment manager was obsoleted by upstream
  + Gallery and Spookyraven second floor automatic unlocking
  + Update Health and Mana restorers list
  + Boss reminders for all signs

* Sun Jul 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt1.svn4402
- Updated to svn4402
  + Dusty bottles support
  + Fix leprechaun equipment bug
  + Removed "login" command
  + Blackbird autoassembly
  + Auto-unlock goatlet
  + Added "pvp" command
  + Dvorak's revenge handling
  + Add multiplier to "mood execute"

* Wed Jul 18 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.2-alt1.svn4327
- 11.2 release (updated to r4327)
  + Patch for hagnk-like equipment manager gone upstream
  + Ronin duration fixed in upstream
  + Fix endless loop bug when parsing effects in charpane
  + Better NS13 support

* Sat Jul 14 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4252
- Updated to r4252
  + Update voleyball formula
  + Detect steel organ aquisition
  + Auto-auto-attack feature
  + Usual bugfixing

* Wed Jul 11 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4213
- Updated to r4213
  + Hagnk-like equipment manager (patch from raorn@)
  + Hedge maze solving
  + Pyramid choice adventure
  + Usual bugfixing

* Sun Jul 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4174
- Updated to r4174
  + Fix logout after closing all windows
  + Many other bugfixes

* Sat Jul 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4148
- Updated to r4148
- Added patch for Ronin duration

* Sat Jul 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4146
- Updated to r4146
  + War Hippy camp
  + New Bounty Hunter Hunter support
  + Cupcake status effects (finally!)
  + Bang potion support (finally!!!)
  + July IOTM
  + New KoLMafia rule, kids: We Don't Attack Our Clanmates in PvP

* Mon Jul 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4078
- Updated to r4078
  + even more NS13 support

* Sat Jun 30 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4056
- Updated to r4056
  + More NS13 support

* Wed Jun 27 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1.svn4000
- Updated to r4000
  + NS13 preliminary support

* Sun Jun 24 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.1-alt1
- Updated to 11.1 release

* Wed Jun 20 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3925
- Updated to r3925
  + New Grimacite items and zone
  + Fix crafting tools autosell price

* Thu Jun 14 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3911
- Updated to r3911
  + New shirts
  + New shore items
  + MCD bossed fix
  + Doc Galactic's partial restorers
  + Reworked tab interface
  + Many bugfixes

* Thu Jun 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3862
- Updated to r3862
  + Green Pixie and absinth stuff
  + New holidays
  + Ram battering staff and icy-hot katana now are meatsmithing items
  + Corrected(doubled) antiques drop rate.
  + usual bugfixes

* Wed May 30 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3836
- Updated to r3876
  + New turtleslinger
  + New cookbooks
  + More clover protection
  + usual bugfixes

* Thu May 17 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3796
- Updated to r3796
  + Swamp gas
  + Automated flower hunter
  + many bugfixes

* Wed May 09 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3738
- Updated to r3738
  + Monday update: turtle totem

* Mon May 07 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3734
- Updated to r3734
  + More fixes to login/logout in CLI

* Sat May 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1.svn3724
- Updated to r3724
  + Female constellations
  + Update Palindome monsters
- Obsoleted patch for ALT #11605 

* Wed May 02 2007 Damir Shayhutdinov <damir@altlinux.ru> 11.0-alt1
- 11.0 release

* Sat Apr 28 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.9-alt4.svn3664
- Updated to r3664

* Wed Apr 25 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.9-alt4.svn3642
- Updated to r3642:
  + jewelrymaking changes (24/04)
  + some UI changes and bugfixes - see git or svn changelogs for details

* Mon Apr 23 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.9-alt4.svn3617
- Remove unneeded login after "logout" command (ALT #11605)

* Sun Apr 22 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.9-alt3.svn3617
- Updated to 3617 svn revision, featuring following major changes:
  + new shirts 
  + always logout on exit
  + usual bugfixing


* Wed Apr 11 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.9-alt2
- Added .desktop file and icon.
- Pass command-line parameters to KoLmafia.

* Sun Apr 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.9-alt1
- New version.

* Thu Apr 05 2007 Damir Shayhutdinov <damir@altlinux.ru> 10.8-alt1
- Initial build for ALT Linux.
