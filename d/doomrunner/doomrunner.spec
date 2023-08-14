%define optflags_lto %nil

Name: doomrunner
Version: 1.8.1
Release: alt1

Summary: Modern preset-oriented graphical launcher of ZDoom and derivatives
License: GPLv2+
Group: Games/Arcade

Url: https://github.com/Youda008/DoomRunner

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: gcc-c++ qt5-base-devel

%description
Doom Runner is yet another launcher of common Doom source ports (like GZDoom, Zandronum, PrBoom, ...)
with graphical user interface. It is written in C++ and Qt, and it is designed around the idea
of presets for various multi-file modifications (Brutal Doom with mutators, Project Brutality with UDV,
Complex Doom Clusterfuck, ...) to allow one-click switching between them and minimize any repetitive work.

First you perform an initial setup, setting up the paths and adding all your Doom engines and IWADs.

%prep
%setup -n %name-%version

%build
%qmake_qt5 "CONFIG+=release"

%make_build

%install

install -Dm0755 DoomRunner %buildroot%_bindir/%name

# install menu icons
for N in 16 24 32 48 64 128;
do
install -D -m 0644 ./Install/XDG/DoomRunner.${N}x${N}.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=DoomRunner
Comment=Modern preset-oriented graphical launcher of ZDoom and derivatives
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -D -m 0644 ./Install/XDG/io.github.Youda008.DoomRunner.appdata.xml %buildroot%_datadir/metainfo/io.github.Youda008.DoomRunner.appdata.xml

%files

%doc README.md LICENSE changelog.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/metainfo/io.github.Youda008.DoomRunner.appdata.xml

%changelog
* Mon Aug 14 2023 Artyom Bystrov <arbars@altlinux.org> 1.8.1-alt1
- Initial build in Sisypus