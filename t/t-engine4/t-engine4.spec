%define beta beta28
Name:		t-engine4
Version:	1.0.0
Release:	alt1%beta
Group:		Games/Adventure
Summary:	A roguelike game engine operating in Lua
Source:		%name-src-%version%beta.tar.bz2
LIcense:	GPLv3

Requires:	%name-data
# Automatically added by buildreq on Sat Jun 11 2011
# optimized out: libGL-devel libGLU-devel libSDL-devel libX11-devel xorg-xproto-devel
BuildRequires: libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel premake

%description
T-Engine4: Flexible roguelike game engine

T-Engine4 (TE4 for short) is a roguelike game engine operating in Lua and available for all major platforms (known to work on Windows, OSX, Linux and various BSD).
What does it do?

T-Engine4 provides many building blocks for your own roguelike game:

    Cross-platform support. A T-Engine4 game is completly made in Lua, as such your game will run automatically on all platforms supported by the engine.
    Fast rendering through the use of OpenGL (but you do not have to worry about it, it is well integrated)
    Support for both "old school" ASCII display or graphical tiles
    Generic save/load code, your objects are automatically saveable without anything to do at all in most cases
    Object Oriented design with lots of flexibility, thanks to Lua
    Map handling
    Generic "Entities" concept that can become terrain features, objects, player(s), NPCs, ...
    Keyboard and Mouse easy support
    Various basic entities class interfaces to make your actors have life, stats, talents, ... with the possibility to define your own
    Generic "Zone" design, that can contain and define levels. A zone can be made into a dungeon, a forest, a wilderness map, a town, ...
    Handle either (or both!) persistent and non-persistent levels
    Malleable data structure design
    Extendable "dialog windows" system
    Many utility classes (chats, stores, default interfaces, character generator, ...)
    Keybind system that allows to user to assign keys to abstract actions and then lets a game bind to those actions
    Integrated download center: If you reference your game on te4.org then existing T-Engine4 users will be able to see the game in their list inside T-Engine
    Particles engine for some neat graphical effects
    Sound and music support
    Many other things, just check it out!

%package data
Summary:	Data files for %name, %summary
BuildArch:	noarch
Group:		Games/Adventure
%description data
Data files for %name, %summary

%package examples
Summary:	Example games for %name, %summary
BuildArch:	noarch
Group:		Games/Adventure
Requires:	%name
%description examples
Example games for %name, %summary

%package tome
Summary:	Tales of Maj'Eyal tactical role-playing roguelike and action game
BuildArch:	noarch
Group:          Games/Adventure
Requires:	%name
%description tome
Tales of Maj'Eyal (ToME) is an open-source, single-player, tactical
role-playing roguelike and action game set in the world of Eyal.

This is the Age of Ascendancy, after over ten thousand years of strife,
pain and chaos the known world is at last at relative peace. The
Spellblaze last effects are now tamed, the land slowly heals itself and
the civilisations rebuild themselves after the Age of Pyre.

It has been one hundred and twenty two years since the Allied Kingdoms
have been established under the rule of Toknor and his wife Mirvenia.
Together they ruled the kingdoms with fairness and brought prosperity to
both halflings and humans. The King died of old age fourteen years ago,
and his son, Tolak, is now king.

The elven kingdoms are quiet. The Shaloren elves in their home of Elvala
are trying to make the world forget about their role in the Spellblaze
and are living happy lives under the leadership of Aranion Gayaeil. The
Thaloren elves keep to their ancient tradition of living in the woods,
ruled as always by Nessilla Tantaelen the wise.

The dwarves of the Iron Throne have started a careful trade relationship
with the Allied Kingdoms for nearly one hundred years, yet not much is
known about them, not even their leader.

While the people of Maj'Eyal know that the mages helped put an end to
the terrors of the Spellblaze, they also did not forget that it was
magic that started those events. As such mages are still shunned from
society, if not downright hunted down. Still, this is a golden age,
civilizations are healing the wounds of thousands of years of conflict,
even the humans and the halflings have made lasting peace.

You are an adventurer, looking for old powers, treasure and glory. You
boldly go in lost and forgotten places, untamed forests and sealed
ruins. What will you find in this age of supposed peace?

%prep
%setup -n %name-src-%version%beta

%build
premake4 gmake
%make_build

cat > %name <<@@@
#!/bin/sh
cd %_gamesdatadir/%name
%_gamesbindir/t-engine
@@@

# TODO desktop/icons

%install
install -Ds t-engine %buildroot%_gamesbindir/t-engine
install -m755 %name %buildroot%_gamesbindir/%name
mkdir -p %buildroot%_gamesdatadir/%name
cp -a bootstrap game %buildroot%_gamesdatadir/%name/

%files
%_gamesbindir/*

%files data
%_gamesdatadir/%name/bootstrap
%_gamesdatadir/%name/game/[^m]*
%dir %_gamesdatadir/%name/game/modules

%files tome
%_gamesdatadir/%name/game/modules/tome

%files examples
%_gamesdatadir/%name/game/modules/example*

%changelog
* Sat Jun 11 2011 Fr. Br. George <george@altlinux.ru> 1.0.0-alt1beta28
- Initial build from scratch

