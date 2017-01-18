Name: chromium-bsu
Version: 0.9.16.1
Release: alt2
Summary: Fast paced, arcade-style, top-scrolling space shooter
License: Artistic
Group: Games/Arcade
Source: %name-%version.tar.gz
Url: http://chromium-bsu.sourceforge.net

Requires: %name-data = %version

# Automatically added by buildreq on Sun Jul 04 2010
BuildRequires: fontconfig-devel gcc-c++ imake libGL-devel libICE-devel libSDL_image-devel libSDL_mixer-devel libX11-devel libftgl-devel libglpng-devel xorg-cf-files

%description
You are captain of the cargo ship Chromium B.S.U., responsible for
delivering supplies to our troops on the front line. Your ship has
a small fleet of robotic fighters which you control from the relative
safety of the Chromium vessel.

%package data
Summary: Level files for %name
Group: Games/Arcade
Buildarch: noarch

%description data
Level files for %name, %summary

%prep
%setup
# GCC6 fix
sed -i 's/ abs(/ fabs(/g' src/MainSDL_Event.cpp

%build
export FONTCONFIG_CFLAGS="`pkg-config --cflags freetype2`"
%configure

%make_build

%install
%makeinstall
install -D data/png/icon32.png %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
#install -D data/png/icon64.png %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
#install -D data/png/icon64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png

%find_lang %name

%files -f %name.lang
%doc %_defaultdocdir/%name
%_bindir/*
#_pixmapsdir/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*
%_man6dir/*
%dir %_datadir/%name

%files data
%_datadir/%name/*

%changelog
* Wed Jan 18 2017 Fr. Br. George <george@altlinux.ru> 0.9.16.1-alt2
- GCC6 fix

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.9.16.1-alt1
- Autobuild version bump to 0.9.16.1

* Wed Jul 27 2016 Fr. Br. George <george@altlinux.ru> 0.9.16-alt1
- Autobuild version bump to 0.9.16

* Mon Jun 10 2013 Fr. Br. George <george@altlinux.ru> 0.9.15.1-alt1
- Autobuild version bump to 0.9.15.1
- Fix build

* Tue Mar 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.15-alt2.1
- Rebuilt with libftgl2

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 0.9.15-alt2
- Rebuild with libftgl220

* Tue Feb 15 2011 Fr. Br. George <george@altlinux.ru> 0.9.15-alt1
- Autobuild version bump to 0.9.15

* Mon Jul 05 2010 Fr. Br. George <george@altlinux.ru> 0.9.14.1-alt1
- Initial build for ALT
- Yep, I know about 0.9.12-alt6, but found no use of it

