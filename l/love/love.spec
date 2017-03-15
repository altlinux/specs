Name: love
Version: 0.10.2
Release: alt1
Summary: Legendary Orthogonal Virtual Environment
Group: Games/Other
License: zlib
Source: %name-%version-linux-src.tar.gz
Source1: debian.tar
Url: http://love2d.org/

BuildPreReq: rpm-build-xdg chrpath

# Automatically added by buildreq on Mon Jul 11 2016
# optimized out: gnu-config libX11-devel libogg-devel libstdc++-devel pkg-config python-base python-modules xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel-static libSDL2-devel libfreetype-devel libluajit-devel libmodplug-devel libmpg123-devel libopenal-devel libphysfs-devel libtheora-devel libvorbis-devel lua5 zlib-devel

%description
As you probably know by now, LO:VE is a framework for making 2D games in
the Lua programming language. LO:VE is totally free, and can be used in
anything from friendly open-source hobby projects, to evil,
closed-source commercial ones.

%prep
%setup -n love-%version-linux-src
tar xf %SOURCE1
##rm platform/unix/m4/*
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' configure

# TODO
# love-version?
# script for copiyng current love into game dir (so love rpm can be upgraded)
# test -d "$1" && cat "$1"/conf.lua || unzip -p "$1" conf.lua | grep version ...
# then use love7 or love8

%build
#autoreconf
%configure
%make_build

%install
%makeinstall
install -D debian/love.svg %buildroot%_iconsdir/hicolor/scalable/apps/love.svg
install -D debian/application-x-love-game.svg %buildroot%_iconsdir/hicolor/scalable/mimetypes/application-x-love-game.svg
install -D debian/love.desktop %buildroot%_desktopdir/love.desktop
install -D debian/love.xml %buildroot%_xdgmimedir/packages/love.xml
chrpath -d  %buildroot%_libdir/lib*.so*

%files
%doc readme.md
%_bindir/*
%_iconsdir/hicolor/scalable/*/*
%_desktopdir/*
%_xdgmimedir/packages/*
%_libdir/lib*
%_man1dir/*
%_pixmapsdir/*

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 0.10.2-alt1
- Autobuild version bump to 0.10.2

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.10.1-alt1
- Autobuild version bump to 0.10.1

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 0.9.2-alt3
- Fix build

* Tue Aug 11 2015 Fr. Br. George <george@altlinux.ru> 0.9.2-alt2
- Re-release with fixes

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 0.9.2-alt1
- Autobuild version bump to 0.9.2

* Thu Apr 10 2014 Fr. Br. George <george@altlinux.ru> 0.9.1-alt1
- Autobuild version bump to 0.9.1

* Mon Feb 24 2014 Fr. Br. George <george@altlinux.ru> 0.9.0-alt1
- Autobuild version bump to 0.9.0
- Fix buildreq (introducing chrpath hack)

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 0.8.0-alt1
- Autobuild version bump to 0.8.0
- Fix build

* Fri Sep 02 2011 Fr. Br. George <george@altlinux.ru> 0.7.2-alt1
- Initial build from scratch

