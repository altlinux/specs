Name: gzdoom
Version: 4.4.2
Release: alt1

Summary: Enhanced Doom engine
Summary(ru_RU.UTF-8): Продвинутый порт движка Doom
License: GPLv2+
Group: Games/Arcade

Url: http://zdoom.org

Packager: Artyom Bystrov <arbars@altlinux.org>

ExclusiveArch: x86_64

Source: %name-%version.tar
Source1: %name.png

BuildRequires: cmake gcc-c++ rpm-macros-cmake nasm glslang-devel libspirv-tools-devel bzip2
BuildRequires: libSDL2-devel zlib-devel libgme-devel libpng-devel libfluidsynth-devel libjpeg-devel libgomp5-devel libtimidity-devel xz zmusic-devel
BuildRequires: libopenal1-devel libGLU-devel libsndfile-devel libmpg123-devel flac libogg-devel libvorbis-devel ImageMagick-tools

%description
GZDoom is a Doom source port based on ZDoom. It features an OpenGL renderer
and lots of new features, among them:
- 3D floors
- Dynamic lights
- Quake2/Unreal style skyboxes
- True color texture support
- Model support (limited at the moment)

Warning! Make sure to place WAD files to %_datadir/doom/

%description -l ru_RU.UTF-8
GZDoom - порт движка Doom, основанный на ZDoom. Основные особенности - рендер через OpenGL
и огромное количество возможностей в плане модификаций:
- 3D полы
- Динамическое освещение
- Скайбоксы в стиле Quake2/Unreal
- Поддержка текстур true color
- Поддержка моделей (пока ограниченно)

Внимание! Убедитесь, что WAD-файлы лежат в каталоге %_datadir/doom/ или $HOME/.config/gzdoom

%prep
%setup -n %name-%version

%build
%cmake_insource \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
	-DINSTALL_PK3_PATH=%_datadir/doom/

%make_build

%install
%makeinstall_std

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=GZDoom
Comment=Enhanced Doom engine
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %SOURCE1 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%dir /usr/share/icons/hicolor/64x64
%dir /usr/share/icons/hicolor/64x64/apps
%dir /usr/share/icons/hicolor/128x128
%dir /usr/share/icons/hicolor/128x128/apps
%_bindir/%name
%_docdir/%name
%_datadir/doom
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Thu Jul 16 2020 Artyom Bystrov <arbars@altlinux.org> 4.4.2-alt1
- Update version to 4.4.2, now is x86_64-bit only
- zmusic is now a standalone library

* Mon Jan 27 2020 Artyom Bystrov <arbars@altlinux.org> 4.3.3-alt1
- Update version to 4.3.3
- Add patches for correct building for i586, aarch64, ppc64le

* Fri Sep 06 2019 Artyom Bystrov <arbars@altlinux.org> 4.2.0-alt1
- initial build for ALT Sisyphus
