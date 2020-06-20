Name: lzdoom
Version: 3.85
Release: alt1

Summary: Enhanced Doom engine
Summary(ru_RU.UTF-8): Продвинутый порт движка Doom
License: GPLv3
Group: Games/Arcade

Url: http://zdoom.org

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: ico_%name.png

BuildRequires: cmake gcc-c++ rpm-macros-cmake nasm glslang-devel libspirv-tools-devel bzip2
BuildRequires: libSDL2-devel zlib-devel libgme-devel libpng-devel libfluidsynth-devel libjpeg-devel libgomp5-devel libtimidity-devel xz
BuildRequires: libopenal1-devel libGLU-devel libsndfile-devel libmpg123-devel flac libogg-devel libvorbis-devel ImageMagick-tools

%description
LZDoom is a fork of GZDoom 3.3 compiling with MinGW and running
on older non SSE2 cpus while keeping the DDRAW and D3D backends
for compatibility.

Warning! Make sure to place WAD files to %_datadir/doom/

%description -l ru_RU.UTF-8
LZDoom - ответвление от  GZDoom 3.3, собранное с MinGW для запуска
на старых процессорах без поддержки инструкций SSE2 с поддержкой DDRAW
и бэкендами D3D в целях сохранения совместимости.

Внимание! Убедитесь, что WAD-файлы лежат в каталоге %_datadir/doom/ или $HOME/.config/lzdoom

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
Name=LZDoom
Comment=Fork of GZDoom 3.3
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
%dir %_iconsdir/hicolor/64x64
%dir %_iconsdir/hicolor/64x64/apps
%dir %_iconsdir/hicolor/128x128
%dir %_iconsdir/hicolor/128x128/apps
%_bindir/%name
%_docdir/%name
%_datadir/doom
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sat Jun 20 2020 Artyom Bystrov <arbars@altlinux.org> 3.85-alt1
- initial build for ALT Sisyphus
