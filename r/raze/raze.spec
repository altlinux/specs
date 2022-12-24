Name: raze
Version: 1.6.1
Release: alt1

Summary: Raze is a fork of Build engine games backed by GZDoom tech
License: GPLv2+
Group: Games/Arcade

Url: https://github.com/coelckers/Raze

Packager: Artyom Bystrov <arbars@altlinux.org>

ExclusiveArch: x86_64 %e2k

Source: %name-%version.tar
Patch: 0001-Fix-file-paths.patch

BuildRequires: cmake gcc-c++ rpm-macros-cmake glslang-devel libspirv-tools-devel bzip2 libvpx-devel
BuildRequires: libSDL2-devel zlib-devel libgme-devel libpng-devel libfluidsynth-devel libjpeg-devel libgomp-devel libtimidity-devel xz zmusic-devel libzmusiclite
BuildRequires: libopenal1-devel libGLU-devel libsndfile-devel libmpg123-devel flac libogg-devel libvorbis-devel ImageMagick-tools

%description
Raze is a fork of Build engine games backed by GZDoom
tech and combines Duke Nukem 3D, Blood, Redneck Rampage,
Shadow Warrior and Exhumed/Powerslave in a single package.
It is also capable of playing Nam and WW2 GI.

%prep
%setup -n %name-%version

#%%patch0 -p1

%build
%cmake_insource \
   -D CMAKE_BUILD_TYPE=RelWithDebInfo \
   -D CMAKE_CXX_FLAGS="${CXXFLAGS} -ffile-prefix-map=\"$PWD\"=. -DSHARE_DIR=\\\"%_datadir/raze\\\"" \
   -D DYN_GTK=OFF \
   -D DYN_OPENAL=OFF \
   -DINSTALL_PK3_PATH=%_datadir/%name/
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_datadir/%name/soundfonts
install -D -m 0644 soundfonts/%name.sf2 %buildroot%_datadir/%name/soundfonts

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Raze
Comment=Raze is a fork of Build engine games backed by GZDoom tech
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert source/platform/posix/game.xpm -scale ${N}x${N} $N.xpm;
install -D -m 0644 $N.xpm %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.xpm
done

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.xpm
%_datadir/%name/soundfonts/%name.sf2
%_datadir/%name/%name.pk3

%changelog
* Sat Dec 24 2022 Artyom Bystrov <arbars@altlinux.org> 1.6.1-alt1
- Update to new version

* Thu Sep 14 2022 Artyom Bystrov <arbars@altlinux.org> 1.5.0-alt1
- Update to new version

* Mon May 31 2021 Artyom Bystrov <arbars@altlinux.org> 1.1.2-alt1
- add e2k arch support by fixing libgomp-devel in deps list (thanks to @mike :))

* Thu Apr 29 2021 Artyom Bystrov <arbars@altlinux.org> 1.0.1-alt2
- Add patch for fixing data paths (thanks to Arch Linux Team)

* Wed Apr 14 2021 Artyom Bystrov <arbars@altlinux.org> 1.0.1-alt1
- initial build for ALT Sisyphus
