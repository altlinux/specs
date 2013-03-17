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
Version: 1.02
Release: alt1

Summary: Free online multiplayer competitive FPS based on the Qfusion engine.
License: GPLv2
Group: Games/Arcade
Url: http://warsow.net

Source0: %{name}_%{version}_sdk.tar.gz

Source1: %name.desktop
Source2: %name.png
Source3: %{name}48.png

Requires: warsow-data = %version

# Automatically added by buildreq on Sun Mar 17 2013 (-bi)
# optimized out: elfutils libGL-devel libX11-devel libXrender-devel libogg-devel libstdc++-devel pkg-config python-base xorg-randrproto-devel xorg-renderproto-devel xorg-xf86dgaproto-devel xorg-xf86vidmodeproto-devel xorg-xproto-devel zlib-devel
# WTF??? python-module-distribute python-module-zope
BuildRequires:  gcc-c++ hd2u libSDL-devel libXext-devel libXinerama-devel libXrandr-devel libXxf86dga-devel libXxf86vm-devel libcurl-devel libfreetype-devel libjpeg-devel libopenal-devel libpng-devel libtheora-devel libvorbis-devel makedepend

%description
Warsow is a completely free fast-paced first-person shooter (FPS) for
Windows, Linux and Mac OS X set in a futuristic cartoon-like world where
rocketlauncher-wielding pigs and lasergun-carrying cyberpunks roam
the streets.

%prep
%setup -q -n %{name}_%{version}_sdk

sed -i -e "/fs_basepath =/ s:\.:%_libdir/%name:" source/qcommon/files.c

%build
pushd libsrcs/angelscript/angelSVN/sdk/angelscript/projects/gnuc
  %make_build
popd

pushd source
  make \
    BUILD_CLIENT=YES \
    BUILD_SERVER=YES \
    BUILD_TV_SERVER=YES \
    BUILD_IRC=YES \
    BUILD_SND_OPENAL=YES \
    BUILD_SND_QF=YES \
    BUILD_CIN=YES \
    BUILD_ANGELWRAP=YES \
    DEBUG_BUILD=YES
popd

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_libdir/%name/libs

pushd source/debug
  install -m 755 warsow.* %buildroot/%_bindir/%name
  install -m 755 wsw_server.* %buildroot/%_bindir/%name-server
  install -m 755 wswtv_server.* %buildroot/%_bindir/%name-tv-server
  install -m 755 libs/*.so %buildroot/%_libdir/%name/libs
popd

install -D -m 0644 %SOURCE1 %buildroot%_desktopdir/warsow.desktop

install -D -m 644 %SOURCE2 %buildroot%_iconsdir/hicolor/256x256/apps/warsow.png
install -D -m 644 %SOURCE3 %buildroot%_liconsdir/warsow.png

dos2unix docs/license.txt
dos2unix docs/sourcecode_quickstart.txt

ln -sf %_datadir/warsow/basewsw %buildroot%_libdir/warsow/basewsw

%files
%doc docs/*
%_bindir/*
%dir %_libdir/warsow
%_libdir/warsow/
%_desktopdir/warsow.desktop
%_iconsdir/hicolor/*/apps/warsow.png

%changelog
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
