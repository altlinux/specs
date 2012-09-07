Name: CGenius
Version: 0.4.0.Beta3
Release: alt1

Summary: CGenius is the clone of Commander Keen
License: GPL
Group: Games/Arcade
Url: http://clonekeenplus.sourceforge.net

Packager: Ildar Mulyukov <ildar@altlinux.ru>

# GIT commit aba08e33488c91a4234668eff408f88cb7705c8c
Source: %name-%version.tar
Source1: %name.desktop

# Automatically added by buildreq on Fri Sep 07 2012
# optimized out: cmake-modules libGL-devel libGLU-devel libogg-devel libstdc++-devel pkg-config
BuildRequires: cmake gcc-c++ libSDL-devel libvorbis-devel

%description
Commander Genius is an open-source clone of Commander Keen which allows you to
play the games, and a majority of the mods made for it.  All of the original
data files are required to do so, however, we conveniently include Episode 1
and 4 for your enjoyment.

So far Commander Keen 1-4 are supported. Keen 1-3 have full support. Keen 4
has partial support, it's entire gameplay is there, but some things are
missing, but are being added

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
%_datadir/CommanderGenius
%_iconsdir/hicolor/512x512/apps/CGLogo.png
# Do not pack games
#%%exclude %_datadir/CommanderGenius/games/*/*

%changelog
* Fri Sep 07 2012 Ildar Mulyukov <ildar@altlinux.ru> 0.4.0.Beta3-alt1
- initial build for ALT Linux Sisyphus
