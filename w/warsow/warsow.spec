%set_verify_elf_method textrel=relaxed

%define _user _warsow
%define _group _warsow
%define _home %_localstatedir/%name

%if %_arch == x86_64
%define _barch x86_64
%else
%define _barch i386
%endif

Name: warsow
Version: 2.1
Release: alt1

Summary: Free online multiplayer competitive FPS based on the Qfusion engine.
License: GPLv2
Group: Games/Arcade
Url: http://warsow.net

Source0: %{name}_21_sdk.tar

Source1: %name.desktop
Source2: %name.png
Source3: %{name}48.png

Patch1: %name-fedora-build.patch
Patch2: %name-fedora-paths.patch

Requires: warsow-data = %version

BuildRequires: gcc-c++ hd2u libSDL2-devel libXext-devel libXinerama-devel libXrandr-devel libXxf86dga-devel libXxf86vm-devel libopenal-devel
BuildRequires: libcurl-devel libfreetype-devel libjpeg-devel libpng-devel libtheora-devel libvorbis-devel
BuildRequires: libGL-devel
BuildRequires: cmake /usr/bin/dos2unix

%description
Warsow is a completely free fast-paced first-person shooter (FPS) for
Windows, Linux and Mac OS X set in a futuristic cartoon-like world where
rocketlauncher-wielding pigs and lasergun-carrying cyberpunks roam
the streets.

%prep
%setup -q -n %{name}_21_sdk
%patch1 -p2
%patch2 -p2

sed -i -e "/fs_basepath =/ s:\.:%_libdir/%name:" source/qcommon/files.c

# Remove bundled libs
pushd libsrcs
rm -rf libcurl libfreetype libjpeg libogg libpng libtheora libvorbis OpenAL-MOB openssl SDL2 zlib
popd

dos2unix docs/license.txt
dos2unix docs/sourcecode_quickstart.txt

%build
mkdir -p source/cmake_build
pushd source/cmake_build

cmake \
	-DQFUSION_GAME=Warsow \
	-DUSE_SDL2=YES \
	-DCMAKE_BUILD_TYPE=Debug \
	..

%make

popd

%install
pushd source/build

# Install executables to bindir
install -Dm 755 warsow.* %buildroot%_bindir/warsow
install -Dm 755 wsw_server.* %buildroot%_bindir/warsow-server
install -Dm 755 wswtv_server.* %buildroot%_bindir/warsow-tv-server

# Install private libraries to a private directory
install -d %buildroot%_libdir/%name/libs
install -m 755 libs/*.so %buildroot%_libdir/%name/libs/

popd

# Install icons and the desktop file
install -D -m 0644 %SOURCE1 %buildroot%_desktopdir/warsow.desktop
install -D -m 644 %SOURCE2 %buildroot%_iconsdir/hicolor/256x256/apps/warsow.png
install -D -m 644 %SOURCE3 %buildroot%_liconsdir/warsow.png

ln -sf %_datadir/warsow/basewsw %buildroot%_libdir/warsow/basewsw

%files
%doc docs/*
%_bindir/*
%dir %_libdir/warsow
%_libdir/warsow/
%_desktopdir/warsow.desktop
%_iconsdir/hicolor/*/apps/warsow.png

%changelog
* Fri Aug 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1-alt1
- Updated to upstream version 2.1.

* Sun Mar 17 2013 Igor Zubkov <icesik@altlinux.org> 1.02-alt1
- 0.61 -> 1.02

* Sat Mar 16 2013 Igor Zubkov <icesik@altlinux.org> 0.61-alt2
- Fix build

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- new version

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2
- fixed build; fixed desktop file

* Thu Sep 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux.
