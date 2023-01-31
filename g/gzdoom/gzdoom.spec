%define optflags_lto %nil

Name: gzdoom
Version: 4.10.0
Release: alt1

Summary: Enhanced Doom engine
Summary(ru_RU.UTF-8): Продвинутый порт движка Doom
License: GPLv2+
Group: Games/Arcade

Url: http://zdoom.org

ExclusiveArch: x86_64 %e2k

Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: %name.png

Patch: fix-soundfont-paths.patch

BuildRequires: cmake gcc-c++ rpm-macros-cmake nasm glslang-devel libspirv-tools-devel bzip2
BuildRequires: libSDL2-devel zlib-devel libgme-devel libpng-devel libfluidsynth-devel libjpeg-devel libtimidity-devel xz zmusic-devel
BuildRequires: libopenal1-devel libGLU-devel libsndfile-devel libmpg123-devel flac libogg-devel libvorbis-devel ImageMagick-tools libvpx-devel
Requires: fluidsynth fluid-soundfont-gs
Conflicts: lzdoom

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

%patch0 -p1

%build
%cmake_insource \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
	-DCMAKE_EXE_LINKER_FLAGS="" -DCMAKE_MODULE_LINKER_FLAGS="" \
	-DINSTALL_PK3_PATH=%_datadir/doom/

%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/%name/soundfonts/

install -D -m 0644 fm_banks/* -t %buildroot%_datadir/%name/fm_banks
install -D -m 0644 soundfont/%name.sf2 %buildroot%_datadir/%name/soundfonts/

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
#icons

#fm_banks
%_datadir/%name/fm_banks/

%doc docs/{console,rh-log,skins}.*

%_bindir/%name
%_docdir/%name/
%_datadir/doom
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_datadir/%name/soundfonts/%name.sf2

%changelog
* Tue Jan 31 2023 Artyom Bystrov <arbars@altlinux.org> 4.10.0-alt1
- Update to new version

* Mon Nov 28 2022 Artyom Bystrov <arbars@altlinux.org> 4.9.0-alt1
- Update to new version

* Sat Jul 09 2022 Artyom Bystrov <arbars@altlinux.org> 4.8.2-alt2
- Add "e2k" to ExclusiveArch

* Sat Jul 09 2022 Artyom Bystrov <arbars@altlinux.org> 4.8.2-alt1
- Update to new version

* Thu Dec 09 2021 Artyom Bystrov <arbars@altlinux.org> 4.7.1-alt1
- Update to new version

* Fri Nov 12 2021 Artyom Bystrov <arbars@altlinux.org> 4.7.0-alt2.1
- Add conflict with lzdoom

* Sat Oct 16 2021 Artyom Bystrov <arbars@altlinux.org> 4.7.0-alt2
- fixed paths for soundfont in patch

* Sat Oct 16 2021 Artyom Bystrov <arbars@altlinux.org> 4.7.0-alt1
- Update version to 4.7.0
- Widescreen graphics for Strife
- new GLES backend for better performance on OpenGL 3.3 and early 4.x hardware.
- MBF21 support (still in beta and not fully tested yet, bug reports are welcome)
- DEHEXTRA working properly now
- various enhancements and fixes for ZScript.

* Fri Aug 27 2021 Artyom Bystrov <arbars@altlinux.org> 4.6.1-alt3
- disable link-time optimization;
- delete "Packager" tag

* Tue Aug 10 2021 Artyom Bystrov <arbars@altlinux.org> 4.6.1-alt1
- Update version to 4.6.1
- Add patch for fixing paths for soundfont (thx to jan@ FROM aur)
- Add fluid-soundfont in Requires list

* Sat May 29 2021 Artyom Bystrov <arbars@altlinux.org> 4.6.0-alt1
- Widescreen graphics for Heretic and Hexen
- Sprite shadows like in the Build engine. Both in software and hardware renderer.
- 16 bit channel PNG files can be read
- DEHEXTRA working properly now
- various enhancements and fixes for ZScript.

* Sun Apr 04 2021 Artyom Bystrov <arbars@altlinux.org> 4.5.0-alt1
- Update version to 4.5.0

* Thu Jul 16 2020 Artyom Bystrov <arbars@altlinux.org> 4.4.2-alt1
- Update version to 4.4.2, now is x86_64-bit only
- zmusic is now a standalone library

* Mon Jan 27 2020 Artyom Bystrov <arbars@altlinux.org> 4.3.3-alt1
- Update version to 4.3.3
- Add patches for correct building for i586, aarch64, ppc64le

* Fri Sep 06 2019 Artyom Bystrov <arbars@altlinux.org> 4.2.0-alt1
- initial build for ALT Sisyphus
