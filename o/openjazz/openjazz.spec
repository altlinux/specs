%define optflags_lto %nil

Name: openjazz
Version: 20190106
Release: alt1

Summary: Open source realization of Jazz JackRabbit old-school platformer
License: GPLv2
Group: Games/Arcade

Url: https://github.com/AlisterT/openjazz

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: libSDL-devel ImageMagick-tools

%description
Open source realization of Jazz JackRabbit old-school platformer

Warning! Make sure to place game data files to $HOMEDIR/.openjazz

%prep
%setup -n %name-%version

%build
%make_build

%install
mkdir -p %buildroot%_bindir
install -m 0755 ./OpenJazz %buildroot%_bindir/

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=OpenJazz
Comment=Open source realization of Jazz JackRabbit old-school platformer
Exec=OpenJazz $HOME/.openjazz
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert ./doc/OpenJazz.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files

%_bindir/OpenJazz
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog

* Sat Jul 09 2022 Artyom Bystrov <arbars@altlinux.org> 20190106-alt1
- initial build for ALT Sisyphus
