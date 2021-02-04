Name: chocolate-doom
Version: 3.0.1
Release: alt2
Group: Games/Arcade
Summary: Historically compatible Doom engine
License: GPLv2+
Url: https://www.chocolate-doom.org/
Packager: arbars-alt <arbars-alt@altlinux.org>

Source: %name-%version.tar.gz

Patch: chocolate-doom-3.0.1-switch-to-python3.patch
BuildRequires: libSDL2-devel libSDL2_net-devel libSDL2_mixer-devel python3-module-Pillow

%description
Chocolate Doom is a game engine that aims to accurately reproduce the experience
of playing vanilla Doom. It is a conservative, historically accurate Doom source
port, which is compatible with the thousands of mods and levels that were made
before the Doom source code was released. Rather than flashy new graphics,
Chocolate Doom's main features are its accurate reproduction of the game as it
was played in the 1990s.

The following games can be played:
-Freedoom
-Doom (including the Ultimate Doom expansion pack)
-Doom II
-Final Doom
-Chex Quest

It is also possible to play these expansion packs and commercial games:
-The Master Levels for Doom II
-Hacx

And also various TCs and WAD files:
http://www.chocolate-doom.org/wiki/index.php/User_guide

%package -n chocolate-common
Summary: Common files used by Chocolate engines
Group: Games/Arcade
Conflicts: %name < 2.1.0

%description -n chocolate-common
Common files used by all Chocolate engines.

%package -n chocolate-heretic
Summary: Historically compatible Heretic engine
Group: Games/Arcade
Requires: chocolate-common = %version
Conflicts: %name < 2.1.0

%description -n chocolate-heretic
Chocolate Heretic is a game engine that aims to accurately reproduce the
experience of playing vanilla Heretic. It is a conservative, historically
accurate Heretic source port. Rather than flashy new graphics, Chocolate
Heretic's main features are its accurate reproduction of the game as it
was played in the 1990s.

Warning! Chocolate Heretic needs to know where to find your IWAD file.
To do this, put the file into %_gamesdatadir/doom.

%package -n chocolate-hexen
Summary: Historically compatible Hexen engine
Group: Games/Arcade
Requires: chocolate-common = %version
Conflicts: chocolate-doom < 2.1.0

%description -n chocolate-hexen
Chocolate Hexen is a game engine that aims to accurately reproduce the
experience of playing vanilla Hexen. It is a conservative, historically
accurate Hexen source port. Rather than flashy new graphics, Chocolate
Hexen's main features are its accurate reproduction of the game as it
was played in the 1990s.

Warning! Chocolate Hexen needs to know where to find your IWAD file.
To do this, put the file into %_gamesdatadir/doom.

%package -n chocolate-strife
Summary: Historically compatible Strife engine
Group: Games/Arcade
Requires: chocolate-common = %version
Conflicts: chocolate-doom < 2.1.0

%description -n chocolate-strife
Chocolate Strife is a game engine that aims to accurately reproduce the
experience of playing vanilla Strife. It is a conservative, historically
accurate Strife source port. Rather than flashy new graphics, Chocolate
Strife's main features are its accurate reproduction of the game as it
was played in the 1990s.

Warning! Chocolate Strife needs to know where to find your IWAD file.
To do this, put the file into %_gamesdatadir/doom.

%prep
%setup
%patch0 -p1

%build
autoreconf -fi
%configure
%make_build

%install
%makeinstall_std

rm -f %buildroot%_desktopdir/screensavers/org.chocolate_doom.Doom_Screensaver.desktop

# These suck, we don't like them
rm -f %buildroot%_desktopdir/%name.desktop
rm -f %buildroot%_desktopdir/org.chocolate_doom.Doom.desktop
rm -f %buildroot%_desktopdir/org.chocolate_doom.Heretic.desktop
rm -f %buildroot%_desktopdir/org.chocolate_doom.Hexen.desktop
rm -f %buildroot%_desktopdir/org.chocolate_doom.Setup.desktop
rm -f %buildroot%_desktopdir/org.chocolate_doom.Strife.desktop

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom
Comment=Conservative Doom source port
Exec=%name
Type=Application
Terminal=false
Icon=%name
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-setup.desktop << EOF
[Desktop Entry]
Name=Chocolate Doom Setup
Comment=Setup tool for Chocolate Doom
Exec=%name-setup
Type=Application
Terminal=false
Icon=chocolate-setup
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-heretic.desktop << EOF
[Desktop Entry]
Name=Chocolate Heretic
Comment=Conservative Heretic source port
Exec=chocolate-heretic
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-heretic-setup.desktop << EOF
[Desktop Entry]
Name=Chocolate Heretic Setup
Comment=Setup tool for Chocolate Heretic
Exec=chocolate-heretic-setup
Type=Application
Terminal=false
Icon=chocolate-setup
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-hexen.desktop << EOF
[Desktop Entry]
Name=Chocolate Hexen
Comment=Conservative Hexen source port
Exec=chocolate-hexen
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-hexen-setup.desktop << EOF
[Desktop Entry]
Name=Chocolate Hexen Setup
Comment=Setup tool for Chocolate Hexen
Exec=chocolate-hexen-setup
Type=Application
Terminal=false
Icon=chocolate-setup
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-strife.desktop << EOF
[Desktop Entry]
Name=Chocolate Strife
Comment=Conservative Strife source port
Exec=chocolate-strife
Type=Application
Terminal=false
Icon=chocolate-doom
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/chocolate-strife-setup.desktop << EOF
[Desktop Entry]
Name=Chocolate Strife Setup
Comment=Setup tool for Chocolate Strife
Exec=chocolate-strife-setup
Type=Application
Terminal=false
Icon=chocolate-setup
Categories=Game;ArcadeGame;
EOF

mkdir -p %buildroot%_datadir/appdata
cat > %buildroot%_datadir/appdata/%name.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://github.com/chocolate-doom/chocolate-doom/issues/406
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">chocolate-doom.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A clone of the popular DOS game DOOM</summary>
  <description>
    <p>
      Chocolate Doom is an original source port of the popular DOOM game for the PC.
    </p>
    <p>
      It accurately reproduces the playing experience of the original DOOM game
      and is compatible with the numerous mods and levels designed for the original.
    </p>
  </description>
  <url type="homepage">http://chocolate-doom.org/</url>
  <screenshots>
    <screenshot type="default">http://www.chocolate-doom.org/wiki/images/a/a7/Chocolate-doom.png</screenshot>
  </screenshots>
</application>
EOF

%files
%doc ChangeLog COPYING.md NEWS.md NOT-BUGS.md README.md README.Music.md TODO.md
%_bindir/%name
%_bindir/%name-setup
%_datadir/appdata/%name.appdata.xml
%_desktopdir/%name.desktop
%_desktopdir/chocolate-setup.desktop
%_datadir/bash-completion/completions/%name
%_man5dir/%name.cfg.5.*
%_man6dir/%name.6.*

%files -n chocolate-common
%doc ChangeLog COPYING.md NEWS.md NOT-BUGS.md README.md README.Music.md TODO.md
%_bindir/chocolate-server
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/apps/chocolate-setup.png
%_man5dir/default.cfg.5.*
%_man6dir/chocolate-server.6.*

%files -n chocolate-heretic
%doc ChangeLog COPYING.md NEWS.md NOT-BUGS.md README.md README.Music.md TODO.md
%_bindir/chocolate-heretic
%_bindir/chocolate-heretic-setup
%_desktopdir/chocolate-heretic.desktop
%_desktopdir/chocolate-heretic-setup.desktop
%_datadir/bash-completion/completions/chocolate-heretic
#{_defaultdocdir}/chocolate-heretic/
%_man5dir/chocolate-heretic.cfg.5.*
%_man5dir/heretic.cfg.5.*
%_man6dir/chocolate-heretic.6.*
%_man6dir/chocolate-heretic-setup.6.*

%files -n chocolate-hexen
%doc ChangeLog COPYING.md NEWS.md NOT-BUGS.md README.md README.Music.md TODO.md
%_bindir/chocolate-hexen
%_bindir/chocolate-hexen-setup
%_desktopdir/chocolate-hexen.desktop
%_desktopdir/chocolate-hexen-setup.desktop
%_datadir/bash-completion/completions/chocolate-hexen
#{_defaultdocdir}/chocolate-hexen/
%_man5dir/chocolate-hexen.cfg.5.*
%_man5dir/hexen.cfg.5.*
%_man6dir/chocolate-hexen.6.*
%_man6dir/chocolate-hexen-setup.6.*

%files -n chocolate-strife
%doc ChangeLog COPYING.md NEWS.md NOT-BUGS.md README.md README.Music.md TODO.md
%_bindir/chocolate-strife
%_bindir/chocolate-strife-setup
%_desktopdir/chocolate-strife.desktop
%_desktopdir/chocolate-strife-setup.desktop
%_datadir/bash-completion/completions/chocolate-strife
#{_defaultdocdir}/chocolate-strife/
%_man5dir/chocolate-strife.cfg.5.*
%_man5dir/strife.cfg.5.*
%_man6dir/chocolate-strife.6.*
%_man6dir/chocolate-strife-setup.6.*

%changelog
* Thu Feb 04 2021 Artyom Bystrov <arbars@altlinux.org> 3.0.1-alt2
- enable build to number of packages (thanks to ROSA Team!)

* Wed Nov 25 2020 arbars-alt <arbars@altlinux.org> 3.0.1-alt1
- initial build for ALT Sisyphus
