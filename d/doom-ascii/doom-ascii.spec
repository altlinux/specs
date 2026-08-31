Name: doom-ascii
Version: 0.3.1
Release: alt1

Summary: Text-based DOOM in your terminal!
License: GPLv2+
Group: Games/Arcade

Url: http://zdoom.org
Source0: %name-%version.tar
Packager: Artyom Bystrov <arbars@altlinux.org>

BuildRequires: make gcc-c++

%description
Source-port of doomgeneric. Does not have sound.

You will need a WAD file (game data). If you don't own the game, the shareware version is freely available.

%prep
%setup -n %name-%version

%build

%make_build

%install
mkdir -p %buildroot{%_iconsdir,%_desktopdir,%_datadir/metainfo}

install -D -m 0755 _unix/game/%name %buildroot%_bindir/%name
install -D -m 0644 src/AppDir/io.github.wojciech_graj.doom_ascii.desktop %buildroot%_desktopdir/
install -D -m 0644 src/AppDir/io.github.wojciech_graj.doom_ascii.png %buildroot%_iconsdir/
install -D -m 0644 src/AppDir/usr/share/metainfo/io.github.wojciech_graj.doom_ascii.appdata.xml %buildroot%_datadir/metainfo/

%files

%_bindir/%name
%_desktopdir/io.github.wojciech_graj.doom_ascii.desktop
%_iconsdir/io.github.wojciech_graj.doom_ascii.png
%_datadir/metainfo/io.github.wojciech_graj.doom_ascii.appdata.xml

%changelog
* Mon Aug 31 2026 Artyom Bystrov <arbars@altlinux.org> 0.3.1-alt1
- initial build for ALT Sisyphus
