Name: love
Version: 0.8.0
Release: alt1
Summary: Legendary Orthogonal Virtual Environment
Group: Games/Other
License: zlib
Source: %name-%version-linux-src.tar.gz
Source1: debian.tar
Url: http://love2d.org/

BuildPreReq: rpm-build-xdg

# Automatically added by buildreq on Fri Sep 02 2011
# optimized out: libGL-devel libGLU-devel libogg-devel libstdc++-devel libX11-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel-static libdevil-devel libfreetype-devel liblua5-devel libmng-devel libmodplug-devel libmpg123-devel libopenal-devel libphysfs-devel libSDL-devel libtiff-devel libvorbis-devel

%description
As you probably know by now, LO:VE is a framework for making 2D games in
the Lua programming language. LO:VE is totally free, and can be used in
anything from friendly open-source hobby projects, to evil,
closed-source commercial ones.

%prep
%setup -n love-%version-linux-src
tar xf %SOURCE1

%build
%configure
%make_build

%install
%makeinstall
install -D debian/love.svg %buildroot%_iconsdir/hicolor/scalable/apps/love.svg
install -D debian/application-x-love-game.svg %buildroot%_iconsdir/hicolor/scalable/mimetypes/application-x-love-game.svg
install -D debian/love.desktop %buildroot%_desktopdir/love.desktop
install -D debian/love.xml %buildroot%_xdgmimedir/packages/love.xml

%files
%doc readme.md
%_bindir/*
%_iconsdir/hicolor/scalable/*/*
%_desktopdir/*
%_xdgmimedir/packages/*

%changelog
* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Autobuild version bump to 0.8.0
- Fix build

* Fri Sep 02 2011 Fr. Br. George <george@altlinux.ru> 0.7.2-alt1
- Initial build from scratch

