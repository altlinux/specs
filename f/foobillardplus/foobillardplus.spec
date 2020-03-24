Name: foobillardplus
Version: 3.43
Release: alt1
Summary: A free 3D OpenGL billiard game
Group: Games/Arcade
License: GPLv2
Url: http://foobillardplus.sourceforge.net

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.xz
Source1: %name.6
Source2: intro-nomusic.png
Patch0: foobillardplus-3.43-mga-install-dir-in-configure.in.patch
Patch1: foobillardplus-3.43-mga-user-settings-in-XDG_DATA_HOME.patch

BuildRequires: gcc-c++ imake libGL-devel libGLU-devel libXt-devel libpng-devel xorg-cf-files libSDL-devel libSDL_net-devel libSDL_mixer-devel libfreetype-devel
Requires: fonts-ttf-dejavu
Obsoletes: foobillard < 3.0a-14
Provides: foobillard
Source44: import.info

%description
FooBillard++ is an advanced 3D OpenGL billiard game based on the original
foobillard 3.0a sources from Florian Berger. You can play it with one or two
players or against the computer.

The music has been removed because of its restrictive CC BY-NC-ND license.

%prep
%setup -n %name-%version
%patch0 -p1
%patch1 -p1
# Use system browser
%__subst 's/firefox/www-browser/g' data/browser.sh

%build
autoreconf -vfi
export CFLAGS="%optflags -fgnu89-inline"
%configure --enable-debian
%make

%install
# make install instructions are kind of broken
install -D -m755 src/foobillardplus %buildroot%_gamesbindir/%name
install -d %buildroot%_gamesdatadir/%name
cp -a data/ %buildroot%_gamesdatadir/%name/

# Fixed intro image without the removed music credits
cp -f %SOURCE2 %buildroot%_gamesdatadir/%name/data/intro.png

# icon and man page
install -D -m644 foobillardplus.png %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
install -D -m644 %SOURCE1 %buildroot%_man6dir/%name.6

# symlink to DejaVu fonts
ln -s %_datadir/fonts/ttf/dejavu/DejaVuSans.ttf      %buildroot%_gamesdatadir/%name/data/DejaVuSans.ttf
ln -s %_datadir/fonts/ttf/dejavu/DejaVuSans-Bold.ttf %buildroot%_gamesdatadir/%name/data/DejaVuSans-Bold.ttf

# desktop entry
install -d %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Name=FooBillard++
GenericName=3D OpenGL billiard game
GenericName[de]=3D-OpenGL-Billard-Spiel
GenericName[fr]=Jeu de billard en 3D OpenGL
Comment=3D OpenGL billiard game
Comment[de]=3D-OpenGL-Billard-Spiel
Comment[fr]=Jeu de billard en 3D OpenGL
Comment[ru]=Игра в биллиард на базе OpenGL
Exec=%name
Icon=%name
Type=Application
Categories=Game;Simulation;
EOF

%files
%doc AUTHORS COPYING ChangeLog README
%_gamesbindir/%name
%_gamesdatadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/%name.png
%_man6dir/%name.6*

%changelog
* Tue Mar 24 2020 Artyom Bystrov <arbars@altlinux.org> 3.43-alt1
- initial build for ALT Sisyphus

* Tue Jun 07 2016 Igor Vlasenko <viy@altlinux.ru> 3.43-alt1_0.svn1704
- converted for ALT Linux by srpmconvert tools
