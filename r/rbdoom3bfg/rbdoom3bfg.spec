Name: rbdoom3bfg
Version: 1.2.0
Release: alt1

Summary: Doom 3: BFG Edition with soft shadows, cleaned up source, Linux and 64 bit Support
License: GPLv3
Group: Games/Arcade

Url: https://github.com/RobertBeckebans/RBDOOM-3-BFG
Source: %name-%version.tar
Source2: %name.png
Packager: Artyom Bystrov <arbars@altlinux.org>

ExclusiveArch: %ix86 x86_64 %e2k

BuildRequires: cmake gcc-c++ rpm-macros-cmake libjpeg-devel libSDL2-devel ffmpeg libopenal-devel libGLU-devel

Summary(ru_RU.UTF-8): Doom 3: BFG Edition с мягкими тенями, приведёнными в порядок исходниками, поддержкой Linux и 64-битной архитектуры

%description
Doom 3: BFG Edition game engine with soft shadows, cleaned up source, Linux
and 64 bit support.

WARNING! Playing Doom 3: BFG Edition still requires a legitimate copy of
the game. You can purchase a copy from Steam or your favorite retailer.

Place "base" folder from the Doom 3 installation to:
%_gamesdatadir/%name/
or
$HOME/.rbdoom3bfg/

%description -l ru_RU.UTF-8
RBDoom3-BFG - порт движка игры Doom 3: BFG Edition с мягкими тенями, приведёнными
в порядок исходниками, поддержкой Linux и 64-битной архитектуры.

ВНИМАНИЕ! Для игры необходимо наличие файлов с данными игры,
которые можно добыть, например, из копии в Steam.

Положите каталог "base" по следующуему пути:
%_gamesdatadir/%name/
или
$HOME/.rbdoom3bfg/

%prep
%setup
%__subst 's,-march=native,-mcpu=native,' \
	neo/CMakeLists.txt neo/libs/rapidjson/CMakeLists.txt
%__subst 's,-m64,,' neo/libs/zlib/configure

%build
%cmake_insource \
	-DCMAKE_BUILD_TYPE=Release \
	-DONATIVE=ON \
	-DSDL2=ON \
%ifnarch %ix86 x86_64
	-DUSE_INTRINSICS=OFF \
%ifnarch %e2k
	-DCPU_OPTIMIZATION= \
%endif
%endif
	./neo

%make_build

%install
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=rbdoom3bfg
Comment=Doom 3 BFG Edition port for Linux
Comment[ru]=Порт Doom 3 BFG Edition для Linux
Exec=rbdoom3bfg
Icon=rbdoom3bfg
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

mkdir -p %buildroot%_gamesbindir/
mkdir -p %buildroot%_gamesdatadir/%name
install -m 0755 ./RBDoom3BFG %buildroot%_gamesbindir/%name
mkdir -p %buildroot/%_iconsdir
install -Dpm0644 %SOURCE2 %buildroot/%_iconsdir/%name.png

%files
%doc COPYING.txt README.txt
%_gamesbindir/%name
%_gamesdatadir/%name
%_desktopdir/%name.desktop
%_iconsdir/%name.png

%changelog
* Sun Jan 19 2020 Artyom Bystrov <arbars@altlinux.org> 1.2.0-alt1
- Update version to 1.2.0

* Thu Oct 24 2019 Michael Shigorin <mike@altlinux.org> 1.1.0-alt1.1
- E2K: fixed build (disable SIMD)
- minor spec/gear cleanup

* Wed Sep 25 2019 Artyom Bystrov <arbars@altlinux.org> 1.1.0-alt1
- initial build for ALT Sisyphus
