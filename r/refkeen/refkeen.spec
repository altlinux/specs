Name: refkeen
Version: 0.18.3
Release: alt2

Summary: Ports of Keen Dreams, Catacomb 3-D and the Catacomb Adventure Series
License: GPLv2+
Group: Games/Arcade

Url: https://github.com/NY00123/refkeen

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ rpm-macros-cmake libSDL2-devel libspeexdsp-devel ImageMagick-tools

ExclusiveArch: %ix86 x86_64
%description
Reflection Keen is a project consisting of source ports of the following titles, all being inspired by the Chocolate Doom port:

    Keen Dreams.
    Catacomb 3-D (The Descent) and The Catacomb Adventure Series.
    Wolfenstein 3D, Spear of Destiny and Super 3-D Noah's Ark (DOS version).

%package reflection-catacomb
Summary:        Reflection Keen: Catacomb-3D source port
Group:          Games/Arcade
Requires:       %name = %version

%description reflection-catacomb
Reflection Keen: Catacomb-3D source port

%package reflection-wolf3d
Summary:        Reflection Keen: Wolfenstein 3D, Spear of Destiny and Super 3-D Noah's Ark source port
Group:          Games/Arcade
Requires:       %name = %version

%description reflection-wolf3d
Reflection Keen: Wolfenstein 3D, Spear of Destiny and Super 3-D Noah's Ark source port

%package reflection-kdreams
Summary:        Reflection Keen: Keen Dreams source port
Group:          Games/Arcade
Requires:       %name = %version

%description reflection-kdreams
Reflection Keen: Keen Dreams source port
    
%prep
%setup -n %name-%version

%build
%cmake_insource

%make_build

%install
install -Dm0755 reflection-catacomb %buildroot%_bindir/reflection-catacomb
install -Dm0755 reflection-kdreams %buildroot%_bindir/reflection-kdreams
install -Dm0755 reflection-wolf3d %buildroot%_bindir/reflection-wolf3d


mkdir -p %buildroot%_datadir/%name/reflection-catacomb
mkdir -p %buildroot%_datadir/%name/reflection-kdreams
mkdir -p %buildroot%_datadir/%name/reflection-wolf3d

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/reflection-catacomb.desktop << EOF
[Desktop Entry]
Name=Reflection Catacomb-3D
Comment=Catacomb-3D source port
Exec=/reflection-catacomb -fulllauncher
Icon=/reflection-catacomb
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/reflection-kdreams.desktop << EOF
[Desktop Entry]
Name=Reflection Keen Dreams
Comment=Keen Dreams source port
Exec=/reflection-kdreams -fulllauncher
Icon=/reflection-kdreams 
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

cat > %buildroot%_desktopdir/reflection-wolf3d.desktop << EOF
[Desktop Entry]
Name=Reflection Wolfenstein 3D
Comment=Wolfenstein 3D source port
Exec=/reflection-wolf3d -fulllauncher
Icon=/reflection-wolf3d
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

for N in 16 32 48 64 128;
do
convert rsrc/reflection-cat3d-128x128.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/reflection-catacomb.png
done

for N in 16 32 48 64 128;
do
convert rsrc/reflection-kdreams-128x128.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/reflection-kdreams.png
done

for N in 16 32 48 64 128;
do
convert rsrc/reflection-wolf3d-128x128.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/reflection-wolf3d.png
done

%files
%doc AUTHORS.md README.md

%files reflection-catacomb
%_bindir/reflection-catacomb
%_datadir/%name/reflection-catacomb
%_desktopdir/reflection-catacomb.desktop
%_iconsdir/hicolor/*/apps/reflection-catacomb.png

%files reflection-kdreams
%_bindir/reflection-kdreams
%_datadir/%name/reflection-kdreams
%_desktopdir/reflection-kdreams.desktop
%_iconsdir/hicolor/*/apps/reflection-kdreams.png

%files reflection-wolf3d
%_bindir/reflection-wolf3d
%_datadir/%name/reflection-wolf3d
%_desktopdir/reflection-wolf3d.desktop
%_iconsdir/hicolor/*/apps/reflection-wolf3d.png

%changelog
* Sat Apr 10 2021 Artyom Bystrov <arbars@altlinux.org> 0.18.3-alt2
- Add ExclusiveArch

* Sat Apr 10 2021 Artyom Bystrov <arbars@altlinux.org> 0.18.3-alt1
- initial build for ALT Sisyphus

