Name: cataclysm-dda
Version: 0.F.3
Release: alt1

Summary: Turn-based survival game set in a post-apocalyptic world
License: CC-BY-SA-3.0 and GPLv2+ and OFL-1.1 and BSL-1.0 and Zlib and MIT and BSD-3-Clause
Group: Games/Adventure

URL: https://cataclysmdda.org/
Vcs: https://github.com/CleverRaven/Cataclysm-DDA.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libncursesw-devel
BuildRequires: libSDL2-devel libSDL2_image-devel libSDL2_mixer-devel libSDL2_ttf-devel libfreetype-devel

%define _unpackaged_files_terminate_build 1

%if %{expand:%%{!?_without_check:%%{!?_disable_check:1}}0}
%define runtests 1
%else
%define runtests 0
%endif

%define common_flags PREFIX=%_prefix USE_XDG_DIR=1 RELEASE=1 ASTYLE=0 LINTJSON=0 LOCALIZE=1 LANGUAGES=all DEBUG_SYMBOLS=1 PCH=0

%description
Cataclysm: Dark Days Ahead is a turn-based survival game set in a
post-apocalyptic world. Struggle to survive in a harsh, persistent, procedurally
generated world. Scavenge the remnants of a dead civilization for food,
equipment, or, if you are lucky, a vehicle with a full tank of gas to get you
the hell out of Dodge. Fight to defeat or escape from a wide variety of powerful
monstrosities, from zombies to giant insects to killer robots and things far
stranger and deadlier, and against the others like yourself, that want what you
have...

%package ncurses
Summary: Turn-based survival game set in a post-apocalyptic world (curses interface)
Group: Games/Adventure
Requires: %name-data = %EVR
 
%description ncurses
Cataclysm: Dark Days Ahead is a turn-based survival game set in a
post-apocalyptic world. Struggle to survive in a harsh, persistent, procedurally
generated world. Scavenge the remnants of a dead civilization for food,
equipment, or, if you are lucky, a vehicle with a full tank of gas to get you
the hell out of Dodge. Fight to defeat or escape from a wide variety of powerful
monstrosities, from zombies to giant insects to killer robots and things far
stranger and deadlier, and against the others like yourself, that want what you
have...

This package contains the text-only ncurses-based interface.

%package data
Summary: Data files for %name-ncurses
Group: Games/Adventure
BuildArch: noarch
Requires: %name-ncurses = %EVR
 
%description data
Data files for %name-ncurses.

%package sdl
Summary: Turn-based survival game set in a post-apocalyptic world (with gfx and sound)
Group: Games/Adventure
 
Requires: %name-sdl-data = %EVR
 
%description sdl
Cataclysm: Dark Days Ahead is a turn-based survival game set in a
post-apocalyptic world. Struggle to survive in a harsh, persistent, procedurally
generated world. Scavenge the remnants of a dead civilization for food,
equipment, or, if you are lucky, a vehicle with a full tank of gas to get you
the hell out of Dodge. Fight to defeat or escape from a wide variety of powerful
monstrosities, from zombies to giant insects to killer robots and things far
stranger and deadlier, and against the others like yourself, that want what you
have...

This package contains version with gfx and sound.

%package sdl-data
Summary: Data files for %name-sdl
Group: Games/Adventure
BuildArch: noarch
Requires: %name-sdl = %EVR
Requires: %name-data = %EVR
 
%description sdl-data
Data files for %name-sdl.

%prep
%setup
%patch -p1

%build
export CXXFLAGS="%optflags"
# ncurses version
# Don't build tests, they will be built with SDL version
%make_build %common_flags RUNTESTS=0

# version with gfx and sound
%make_build %common_flags SOUND=1 TILES=1 RUNTESTS=%runtests

%install
# ncurses version
%makeinstall_std %common_flags

# version with gfx and sound
%makeinstall_std %common_flags SOUND=1 TILES=1

%find_lang %name

%check
LC_ALL=C.UTF-8 make PCH=0 check

%files ncurses
%_bindir/cataclysm
 
%files -f %name.lang data
%doc %_datadir/%name/*.txt
%dir %_datadir/%name/
%_datadir/%name/cataicon.ico
%_datadir/%name/core/
%_datadir/%name/credits/
%_datadir/%name/font/
%_datadir/%name/fontdata.json
%_datadir/%name/help/
%_datadir/%name/json/
%_datadir/%name/mods/
%_datadir/%name/motd/
%_datadir/%name/names/
%_datadir/%name/raw/
%_datadir/%name/title/
 
%files sdl
%_bindir/cataclysm-tiles
 
%files sdl-data
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/*/*.svg
%_datadir/%name/gfx/
%_datadir/%name/sound/
%_datadir/metainfo/*.xml

%changelog
* Wed Dec 15 2021 Mikhail Efremov <sem@altlinux.org> 0.F.3-alt1
- Updated to 0.F-3 Frank-3.

* Mon Nov 15 2021 Mikhail Efremov <sem@altlinux.org> 0.F.2-alt1
- Don't use git commit as version.
- Disabled broken tests.
- Fixed build with glibc >= 2.33.9000.
- Initial build.
