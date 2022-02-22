%set_verify_elf_method unresolved=relaxed
%add_findprov_lib_path %_libdir/torcs/lib

Name: speed-dreams
Version: 2.2.3
Release: alt1
Summary: Car motorsport simulation
License: GPL-2.0-or-later
Group: Games/Sports
Url: https://www.speed-dreams.net

Source:  %name-src-base.tar.xz
Source1:  %name-src-hq-cars-and-tracks.tar.xz
Source2:  %name-src-more-hq-cars-and-tracks.tar.xz
Source3:  %name-src-wip-cars-and-tracks.tar.xz
Source4:  %name-src-unmaintained.tar.xz

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: fdupes
BuildRequires: libfreeglut-devel
BuildRequires: gcc-c++
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: plib-devel
BuildRequires: libexpat-devel
BuildRequires: libalut-devel
BuildRequires: libglvnd-devel
BuildRequires: libenet-devel
BuildRequires: libogg-devel
BuildRequires: libopenal-devel
BuildRequires: libOpenSceneGraph-devel
BuildRequires: libOpenThreads-devel
BuildRequires: libSDL2-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: libvorbis-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: zlib-devel
BuildRequires: libcurl-devel
BuildRequires: libGL-devel
BuildRequires: libEGL-devel
BuildRequires: chrpath
BuildConflicts: libOpenSceneGraph-devel < 3.2

Requires: %name-data = %version
Requires: libfreeglut plib libalut

ExclusiveArch: %ix86 x86_64

%description
Speed Dreams ia a fork of the racing car simulator Torcs,
with new features:
* new car sets: Super Cars, 36 GP, LS-GT1
* updated TBR1 car set
* a few new tracks
* Simu V3 physics engine

%package data
Summary: Game data for Speed Dreams
Group: Games/Sports
Requires: %name = %version

%description data
Speed Dreams ia a fork of the racing car simulator Torcs,
with some new features.

This subpackage contains the game data, such as textures, sounds,
maps, and so on.

%package devel
Group: Games/Sports
Summary:       The Open Racing Car Simulator development files
Requires:      %name = %version

%description devel

This package contains the development files for the game.

%prep
%setup -n  %name-%version 
%setup -q -T -D -b 1 -n  %name-%version 
%setup -q -T -D -b 2 -n  %name-%version 
%setup -q -T -D -b 3 -n  %name-%version 
%setup -q -T -D -b 4 -n  %name-%version

chmod -x *.txt

find ./ -name "*.xml" -print0 | xargs -0 sed -i "s|\xE9|e|g"

%build
%cmake_insource \
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DBUILD_SHARED_LIBS=OFF
    
%make_build

%install

%makeinstall_std

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Speed Dreams
Comment=Racing car simulator
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;Simulation;
EOF

mkdir -p %buildroot%_iconsdir
install ./data/data/icons/icon.png %buildroot%_iconsdir/%name.png
mkdir -p %buildroot%_datadir/appdata
install packaging/appdata/speed-dreams-2.appdata.xml %buildroot%_datadir/appdata/%name.appdata.xml



mkdir -p %buildroot%_man6dir
install -m644 doc/man/sd2-accc.6 %buildroot%_man6dir/sd2-accc.6
install -m644 doc/man/sd2-nfs2ac.6 %buildroot%_man6dir/sd2-nfs2ac.6
install -m644 doc/man/sd2-nfsperf.6 %buildroot%_man6dir/sd2-nfsperf.6
install -m644 doc/man/sd2-trackgen.6 %buildroot%_man6dir/sd2-trackgen.6
install -m644 doc/man/speed-dreams-2.6 %buildroot%_man6dir/speed-dreams-2.6

find %buildroot%_libdir/games/speed-dreams-2/drivers/../ -name '*.so' | xargs -n 1 chrpath -d
#find %%buildroot%%_libdir/games/speed-dreams-2/lib/ -name '*.so' | xargs -n 1 ln -s %%buildroot%%_libdir/*.so

ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/libephemeris.so  %buildroot%_libdir/libephemeris.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/liblearning.so %buildroot%_libdir/liblearning.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/libnetworking.so %buildroot%_libdir/libnetworking.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/libportability.so %buildroot%_libdir/libportability.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/librobottools.so %buildroot%_libdir/librobottools.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/libtgf.so %buildroot%_libdir/libtgf.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/libtgfclient.so %buildroot%_libdir/libtgfclient.so
ln -sr %buildroot%_libdir/games/speed-dreams-2/lib/libtgfdata.so %buildroot%_libdir/libtgfdata.so


%files
%doc CHANGES.txt COPYING.txt README.txt
%_datadir/applications/%name.desktop
%_gamesbindir/%name-2
%_gamesbindir/sd2-*
%_iconsdir/%name.png
%_datadir/appdata/%name.appdata.xml

%dir %_libdir/games/%name-2
%_libdir/games/%name-2/drivers/
%_libdir/games/%name-2/lib/
%_libdir/games/%name-2/modules/
%_libdir/*.so
%_mandir/man6/sd2-*.6*
%_mandir/man6/%name-2.6*

%files data
%_gamesdatadir/%name-2/

%files devel
%_includedir/%name-2/

%changelog
* Tue Feb 08 2022 Artyom Bystrov <arbars@altlinux.org> 2.2.3-alt1
- initial build for ALT Sisyphus
