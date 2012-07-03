Name: cairo-dock
Version: 3.0.2
Release: alt1
Summary: A light and eye-candy dock to launch your programs easily
License: GPLv3+
Group: Graphical desktop/Other
Url: https://launchpad.net/cairo-dock-core

Source: http://launchpad.net/cairo-dock-core/3.0/%version/+download/%name-%version.tar
#.gz

# Automatically added by buildreq on Thu Apr 12 2012 (-bi)
# optimized out: GraphicsMagick GraphicsMagick-common cmake-modules elfutils fontconfig fontconfig-devel glib2-devel libGL-devel libX11-devel libXext-devel libXfixes-devel libXi-devel libXrender-devel libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-devel libdbus-glib libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-server pkg-config python-base xorg-compositeproto-devel xorg-fixesproto-devel xorg-inputproto-devel xorg-renderproto-devel xorg-xextproto-devel xorg-xproto-devel
BuildRequires: GConf apt cmake desktop-file-utils gcc-c++ libGLU-devel libXcomposite-devel libXinerama-devel libXtst-devel libcurl-devel libdbus-glib-devel libgtk+3-devel librsvg-devel libxml2-devel wget

# removing GraphicsMagick-ImageMagick-compat and adding
#FIXME: BuildRequires: /usr/bin/convert
BuildRequires: ImageMagick-tools

%description
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%package devel
Summary: Development files for cairo-dock
Group: Development/Other
Requires: %name = %version-%release

%description devel
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the include files and library for cairo-dock functions.

%prep
%setup -n %name-%version

%build
%cmake
%make_build -C BUILD

%install
%make_install DESTDIR=%buildroot install -C BUILD

%find_lang %name

mkdir -p %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
convert data/cairo-dock.svg -resize 48x48 %buildroot%_liconsdir/%name.png
convert data/cairo-dock.svg -resize 16x16 %buildroot%_miconsdir/%name.png
convert data/cairo-dock.svg -resize 32x32 %buildroot%_niconsdir/%name.png
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--add-category="GNOME;GTK;Utility;X-Desktop" \
	%buildroot%_desktopdir/cairo-dock.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--add-category="GNOME;GTK;Utility;X-Desktop" \
	%buildroot%_desktopdir/cairo-dock-cairo.desktop

%files -f %name.lang
%_bindir/*
%_libdir/*.so.*
%_man1dir/*.1.*
%_datadir/%name
%_desktopdir/*.desktop
%_pixmapsdir/*.svg
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Jun 28 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.0.2-alt1
- new version
- cairo-dock-alt-glib2-2.32.0.patch removed

* Thu Apr 12 2012 Ildar Mulyukov <ildar@altlinux.ru> 3.0-alt0.0rc1.1
- new version
- switch to gtk+3

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt2.1.qa2
- Fixed build with new glib2

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.3.0-alt2.1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for cairo-dock

* Thu May 05 2011 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt2.1
- 2.3.0~2

* Tue Oct 19 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt4.1
- update buildreq

* Wed Oct 06 2010 Alexey Shabalin <shaba@altlinux.ru> 2.2.0-alt4
- 2.2.0-4

* Sun Apr 11 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt8
- 2.1.3-8

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt7
- 2.1.3-7

* Sat Mar 06 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt6
- 2.1.3-6

* Fri Feb 05 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.3-alt1
- 2.1.3-1
- add Additional Categories to desktop file; remove key "Encoding"

* Fri Jan 15 2010 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt4
- 2.1.2-4

* Sat Oct 31 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt2
- 2.1.1-2

* Sun Oct 25 2009 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- initial build, mandriva spec based
