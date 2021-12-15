%define optflags_lto %nil

Name: lzdoom
Version: 3.88
Release: alt1

Summary: Enhanced Doom engine - version for old systems
Summary(ru_RU.UTF-8): Продвинутый порт движка Doom - версия для слабых систем
License: GPLv3
Group: Games/Arcade

Url: http://zdoom.org

Source: %name-%version.tar
Source1: ico_%name.png

Patch1: 0001-Fix-soundfont-search-path.patch

BuildRequires: cmake gcc-c++ rpm-macros-cmake nasm glslang-devel libspirv-tools-devel bzip2 zmusic-devel
BuildRequires: libSDL2-devel zlib-devel libgme-devel libpng-devel libfluidsynth-devel libjpeg-devel libtimidity-devel xz
BuildRequires: libopenal1-devel libGLU-devel libsndfile-devel libmpg123-devel flac libogg-devel libvorbis-devel ImageMagick-tools
Requires: fluidsynth fluid-soundfont-gs

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

%patch1 -p1

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
* Wed Dec 15 2021 Artyom Bystrov <arbars@altlinux.org> 3.88-alt1
- Update to new version

* Fri Aug 27 2021 Artyom Bystrov <arbars@altlinux.org> 3.87c-alt4
- disable link-time optimization;
- delete "Packager" tag

* Sat Aug 07 2021 Artyom Bystrov <arbars@altlinux.org> 3.87c-alt3
- Add patch for fixing paths for soundfont (thx to jan@ FROM aur)
- Add fluid-soundfont in Requires list

* Sun Apr 04 2021 Artyom Bystrov <arbars@altlinux.org> 3.87c-alt2
- Add patch for fixing bild on x86 arch (taked from ROSA Linux gzdoom repo);
- Add zmusic library in list of deps

* Sun Apr 04 2021 Artyom Bystrov <arbars@altlinux.org> 3.87c-alt1
- Update to 3.87c

* Sat Jun 20 2020 Artyom Bystrov <arbars@altlinux.org> 3.85-alt1
- initial build for ALT Sisyphus
