%define pre	pre6a

Name: airstrike
Version: 1.0
Release: alt1.%pre

Summary: Incredibly addictive 2D dogfight game
License: GPL
Group: Games/Arcade

Url: http://icculus.org/airstrike/
Source0: %name-%pre-src.tar.gz
Source11: %name-16x16.png
Source12: %name-32x32.png
Source13: %name-48x48.png
Patch0: airstrike-pre6a-config.patch
Patch1: airstrike-pre6a-optflags.patch
Patch3: airstrike-pre6a-fix-build.patch
Patch4: airstrike-pre6a-fix-link-flags.patch

BuildRequires: libSDL-devel libSDL_mixer-devel libSDL_image-devel

%description
Airstrike is a 0-2 players 2d dogfight game in the tradition of the
Intellivision and Amiga games 'Biplanes' and 'BIP'. It features a robust
physics engine and several other extensions of the original games,
such as povray made graphics and incredible gameplay.

%prep
%setup -n %name-%pre-src
%patch0 -p1 -b .config
%patch1 -p1 -b .optflags
%patch3 -p0 -b .build
%patch4 -p1 -b .link

%build
%make OPTFLAGS="%optflags" airstrike-sound

%install
install -pDm755 airstrike %buildroot%_gamesbindir/airstrike.bin

# Launch script
cat <<EOF > %buildroot%_gamesbindir/airstrike
#!/bin/sh
if [ ! -e \$HOME/.airstrikerc ]; then
	cp %_gamesdatadir/%name/airstrikerc \$HOME/.airstrikerc
fi
cd %_gamesdatadir/%name
airstrike.bin \$@
EOF
chmod 755 %buildroot%_gamesbindir/airstrike

install -pDm644 airstrikerc %buildroot%_gamesdatadir/%name/airstrikerc
cp -a data  %buildroot%_gamesdatadir/%name

install -pDm644 doc/airstrike.6 %buildroot%_man6dir/airstrike.6

# Menu items
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=AirStrike
Comment=%summary
Exec=%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -pDm644 %SOURCE11 %buildroot%_miconsdir/%name.png
install -pDm644 %SOURCE12 %buildroot%_iconsdir/%name.png
install -pDm644 %SOURCE13 %buildroot%_liconsdir/%name.png

%files
%doc ChangeLog README doc
%_gamesbindir/*
%_gamesdatadir/%name/
%_man6dir/airstrike.6*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_iconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed Mar 13 2013 Michael Shigorin <mike@altlinux.org> 1.0-alt1.pre6a
- built for Sisyphus (requested by Constantavr)
  + based on mageia package
  + spec cleanup

* Fri Jan 11 2013 umeabot <umeabot> 1.0-1.pre6a.9.mga3
+ Revision: 345356
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sat Dec 15 2012 pterjan <pterjan> 1.0-1.pre6a.8.mga3
+ Revision: 331103
- Fix build
  + dams <dams>
    - add a patch from Nicolas L?\195?\169cureuil to fix includes

* Tue Mar 22 2011 dmorgan <dmorgan> 1.0-1.pre6a.7.mga1
+ Revision: 75541
- Remove mdv macros
- imported package airstrike

