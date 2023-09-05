Name: russian-doom
Version: 6.2.1
Release: alt1

Summary: Russian Doom, Freedoom, Heretic and Hexen translation project
Summary(ru_RU.UTF-8): Проект перевода Doom, Freedoom, Heretic и Hexen на русский язык
License: GPLv2+
Group: Games/Arcade

Url: https://github.com/JNechaevsky/russian-doom

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: %name.png

Patch0: russian-doom4.6.1-switch-to-python3.patch

BuildRequires(Pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake libstdc++-devel libSDL2-devel libSDL2_net-devel libSDL2_mixer-devel python3-module-Pillow ImageMagick-tools

Conflicts: chocolate-doom chocolate-heretic chocolate-hexen

%description
Russian Doom, Freedoom, Heretic and Hexen translation project

%package -n russian-heretic
Summary: Russian Doom, Freedoom, Heretic and Hexen (Heretic binaries)
Group: Games/Arcade

Requires: russian-doom = %version
%description -n russian-heretic
Russian Doom, Freedoom, Heretic and Hexen translation project

These are the Heretic binaries.

See https://jnechaevsky.github.io/rusdoom for more information.

%package -n russian-hexen
Summary: Russian Doom, Freedoom, Heretic and Hexen (Hexen binaries)
Group: Games/Arcade
Requires: russian-doom = %version

%description -n russian-hexen
Russian Doom, Freedoom, Heretic and Hexen translation project

These are the Hexen binaries.

See https://jnechaevsky.github.io/rusdoom for more information.

%prep
%setup
#patch0 -p1

%build
%cmake \
    -D CMAKE_BUILD_TYPE="Release" \
    -D CMAKE_INSTALL_PREFIX="/usr" \
    -D COMPILE_DOOM="ON" \
    -D COMPILE_HERETIC="ON" \
    -D COMPILE_HEXEN="ON" \
    -D COMPILE_STRIFE="ON" \
    -D BUILD_VERSION_OVERWRITE="%version" \
    -D NO_GIT_HASH="ON"
%cmake_build


%install
%cmake_install

rm -f %buildroot%_desktopdir/screensavers/org.russian_doom.Doom_Screensaver.desktop

# These suck, we don't like them
rm -f %buildroot%_desktopdir/%name.desktop
rm -f %buildroot%_desktopdir/org.russian_doom.Doom.desktop
rm -f %buildroot%_desktopdir/org.russian_doom.Heretic.desktop
rm -f %buildroot%_desktopdir/org.russian_doom.Hexen.desktop
rm -f %buildroot%_desktopdir/org.russian_doom.Setup.desktop
rm -f %buildroot%_desktopdir/org.russian_doom.Strife.desktop

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Russian Doom
Comment=Conservative Doom source port
Exec=%name
Type=Application
Terminal=false
Icon=%name
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/russian-heretic.desktop << EOF
[Desktop Entry]
Name=russian Heretic
Comment=Conservative Heretic source port
Exec=Russian-heretic
Type=Application
Terminal=false
Icon=russian-doom
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/russian-hexen.desktop << EOF
[Desktop Entry]
Name=Russian Hexen
Comment=Conservative Hexen source port
Exec=russian-hexen
Type=Application
Terminal=false
Icon=russian-doom
Categories=Game;ArcadeGame;
EOF

mkdir -p %buildroot%_datadir/%name/appdata/
cat > %buildroot%_datadir/%name/appdata/%name.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2023 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://github.com/russian-doom/russian-doom/issues/406
SentUpstream: 2023-09-05
-->
<application>
  <id type="desktop">russian-doom.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A clone of the popular DOS game DOOM</summary>
  <description>
    <p>
      Russian Doom, Freedoom, Heretic and Hexen translation project.
    </p>
  </description>
  <url type="homepage">http://russian-doom.org/</url>
  <screenshots>
    <screenshot type="default">http://www.russian-doom.org/wiki/images/a/a7/russian-doom.png</screenshot>
  </screenshots>
</application>
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %SOURCE1 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc README.md COMPILING.md LICENSE.txt
%_bindir/%name
%_datadir/%name
%_datadir/doc/%name/GPL.txt
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/bash-completion/completions/%name
%_man6dir/%name.6.*
%_man6dir/ru/%name.6.*

%files -n russian-heretic
%_bindir/russian-heretic
%_desktopdir/russian-heretic.desktop
%_datadir/bash-completion/completions/russian-heretic
%_man6dir/russian-heretic.6.*
%_man6dir/ru/russian-heretic.6.*

%files -n russian-hexen
%_bindir/russian-hexen
%_desktopdir/russian-hexen.desktop
%_datadir/bash-completion/completions/russian-hexen
%_man6dir/russian-hexen.6.*
%_man6dir/ru/russian-hexen.6.*

%changelog
* Tue Sep  5 2023 Artyom Bystrov <arbars@altlinux.org> 6.2.1-alt1
- Update to new version

* Sun Feb 21 2021 Artyom Bystrov <arbars@altlinux.org> 4.6.1-alt1
- initial build for ALT Sisyphus
