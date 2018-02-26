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
Version: 0.61
Release: alt1

Summary: Free online multiplayer competitive FPS based on the Qfusion engine.
License: GPLv2
Group: Games/Arcade
Url: http://warsow.net

Source: warsow-%version.tar

Requires: warsow-data = %version

BuildRequires: libopenal-devel libGL-devel zlib-devel libcurl-devel libX11-devel libXxf86vm-devel
BuildRequires: xorg-xf86dgaproto-devel libXinerama-devel libjpeg-devel libvorbis-devel
BuildRequires: libSDL-devel libXext-devel libXxf86dga-devel gcc-c++

%description
Warsow is a completely free fast-paced first-person shooter (FPS) for
Windows, Linux and Mac OS X set in a futuristic cartoon-like world where
rocketlauncher-wielding pigs and lasergun-carrying cyberpunks roam
the streets.

%prep
%setup -q

%build
%make_build -C source

sed -i 's,DATA_DIR=,DATA_DIR=%_libdir/games/warsow/,' source/release/{warsow,wsw_server,wswtv_server}

for i in warsow wsw_server wswtv_server; do
cat << __EOF__ >> $i.launcher
#!/bin/sh

%_libdir/games/warsow/$i \$*
exit \$?
__EOF__
done

%install

# install launchers
mkdir -p %buildroot%_bindir

install -D -m 0755 warsow.launcher %buildroot%_bindir/warsow
install -D -m 0755 wsw_server.launcher %buildroot%_bindir/wsw-server
install -D -m 0755 wswtv_server.launcher %buildroot%_bindir/wswtv-server

# install binaries
mkdir -p %buildroot%_libdir/games/warsow/
for i in warsow warsow.%_barch wsw_server wsw_server.%_barch wswtv_server wswtv_server.%_barch; do
	install -pm755 source/release/$i %buildroot%_libdir/games/warsow
done

# install libraries
cp -a source/release/libs/ %buildroot%_libdir/games/warsow

# install icon
#install -D -m 0644 source/win32/warsow.ico %buildroot%_datadir/pixmaps/warsow.ico
install -D -m 644 warsow48.png %buildroot%_liconsdir/warsow.png
install -D -m 644 Warsow.png %buildroot%_iconsdir/hicolor/256x256/apps/warsow.png

# install desktop file
install -D -m 0644 warsow.desktop %buildroot%_desktopdir/warsow.desktop

ln -sf %_datadir/games/warsow/basewsw %buildroot%_libdir/games/warsow/basewsw

%files
%doc docs/
%_libdir/games/warsow
%_bindir/*
%_desktopdir/warsow.desktop
%_iconsdir/hicolor/*/apps/warsow.png


%changelog
* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- new version

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2
- fixed build; fixed desktop file

* Thu Sep 17 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.5-alt1
- Initial build for ALT Linux.
