Name: CGenius
Version: 1.4.4
Release: alt1.git.19.gf044876

Summary: CGenius is the clone of Commander Keen
License: GPL
Group: Games/Arcade
Url: http://clonekeenplus.sourceforge.net

Packager: Ildar Mulyukov <ildar@altlinux.ru>

# git://github.com/gerstrong/Commander-Genius.git
# GIT commit f0448760a3cf7e6b6f6be621ae3b5e0c34b041a8
Source: %name-%version.tar
Source1: %name.desktop

# Automatically added by buildreq on Fri Aug 02 2013
# optimized out: cmake-modules libGL-devel libGLU-devel libSDL-devel libX11-devel libXau-devel libXrender-devel libogg-devel libstdc++-devel pkg-config xorg-kbproto-devel xorg-xproto-devel
BuildRequires: boost-devel-headers cmake gcc-c++ libSDL_image-devel libXext-devel libXft-devel libvorbis-devel

%description
Commander Genius is an open-source clone of Commander Keen which allows you to
play the games, and a majority of the mods made for it.  All of the original
data files are required to do so, however, we conveniently include Episode 1
and 4 for your enjoyment.

So far Commander Keen 1-6 are fully supported. Keen Dreams is the only game
where we don't have support. Being considered not as popular, we might support
it later.

It is strongly recommended to install the High-Quality Pack (HPQ) for better
()and fresh) user experience.

%prep
%setup

%if "%_lib" == "lib64"
%define cg_buildtype LINUX64
%define cg_tgtdir Linux64
%else
%define cg_buildtype LINUX32
%define cg_tgtdir Linux32
%endif

%build
%cmake \
	-DBUILD_TYPE=%cg_buildtype \

mkdir -p BUILD/build/%cg_tgtdir
%make_build -C BUILD

%install
%makeinstall_std -C BUILD
install -m644 -D CGLogo.png %buildroot%_iconsdir/hicolor/512x512/apps/CGLogo.png
install -m644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%doc BUILD/README* changelog.txt
%_gamesbindir/*
%_desktopdir/%name.desktop
%_gamesdatadir/commandergenius
%_iconsdir/hicolor/512x512/apps/CGLogo.png
# Do not pack games
%exclude %_gamesdatadir/commandergenius/games/*/*

%changelog
* Fri Aug 02 2013 Ildar Mulyukov <ildar@altlinux.ru> 1.4.4-alt1.git.19.gf044876
- new version
- known problems with OpenGL mode, upstream issue #142

* Fri Sep 07 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0.Beta3-alt1
- initial build for ALT Linux Sisyphus
