Name: doomsday
Version: 2.3.1
Release: alt1
Summary: The Doomsday Engine: DOOM/Hertic/Hexen port with pretty graphics
License: GPLv2+
Group: Games/Arcade
Url: http://dengine.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Patch: doomsday-libs.patch 

BuildRequires: qt5-base-devel-static ImageMagick-tools
BuildRequires: cmake
BuildRequires: gcc-c++ >= 6
BuildRequires: libcurl-devel
BuildRequires: libpng-devel
BuildRequires: libncurses-devel
BuildRequires: zlib-devel
BuildRequires: zziplib-devel
BuildRequires: libqt5-core 
BuildRequires: libqt5-gui
BuildRequires: libqt5-network
BuildRequires: libqt5-opengl
##BuildRequires: Qt5OpenGLExtensions)
BuildRequires: libqt5-widgets
BuildRequires: qt5-x11extras-devel
BuildRequires: libSDL2_mixer-devel
BuildRequires: fluidsynth
BuildRequires: libICE-devel
BuildRequires: libminizip-devel
BuildRequires: libopenal-devel
BuildRequires: libSDL2-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr
BuildRequires: libXxf86vm
# Doomsday uses a modified version of assimp, so no pkgconfig(assimp) here :-(
Provides: jdoom = %version-%release
Provides: jheretic = %version-%release
Provides: jhexen = %version-%release
Provides: bundled(assimp) = 3.3.1
Obsoletes: deng < %version-%release
Provides: deng = %version-%release

ExcludeArch: %ix86 aarch64 armh

%description
The Doomsday Engine is a source port with support for Doom, Heretic,
and Hexen. It does not support BOOM extensions.

%prep
%setup
%patch -p1

%build

%cmake \
%ifarch aarch64 %arm
	-DDENG_OPENGL_API=GLES3 \
%endif
	-DCMAKE_SKIP_RPATH:BOOL=ON
%make_build -C ./%_cmake__builddir

%install
%cmake_install

b="%buildroot"
d="$b/%_libdir/doomsday"
rm -Rf "$b/%_includedir" "$b/%_libdir/cmake" "$b/%_docdir/texc" \
    "$d/cmake" "$d/pkgconfig" "$d"/*.a
mkdir -p "$b/%_pixmapsdir"
ln -s "%_datadir/%name/deng-shell-logo-256.png" "$b/%_pixmapsdir/"
ln -s "%_datadir/%name/deng-logo-256.png" "$b/%_pixmapsdir/"

mkdir -p "$b/%_sysconfdir/doomsday";
cat >"$b/%_sysconfdir/doomsday/paths" <<-EOF
    basedir: %_datadir/doomsday
    libdir: %_libdir/doomsday
    iwaddir: %_datadir/doom
EOF

for N in 16 32 48 64 128;
do
convert doomsday/apps/client/res/linux/deng-logo-256.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done



%files
%doc doomsday/*.txt
%dir %_sysconfdir/doomsday
%config %_sysconfdir/doomsday/paths
%_bindir/*
%_libdir/libdeng*.so*
%_libdir/%name/
%_datadir/%name/
%_desktopdir/*.desktop
%_datadir/metainfo/
%_iconsdir/hicolor/*/apps/%name.png
%_pixmapsdir/*.png

%changelog
* Mon Dec 26 2022 Artyom Bystrov <arbars@altlinux.org> 2.3.1-alt1
- initial build for ALT Sisyphus

