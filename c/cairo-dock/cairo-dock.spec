%def_enable session
Name: cairo-dock
Version: 3.4.1
Release: alt3

Summary: A light and eye-candy dock to launch your programs easily
Summary(ru_RU.UTF-8): Приятный глазу док для простого запуска ваших программ
License: GPLv3+
Group: Graphical desktop/Other
# http://glx-dock.org
Url: https://launchpad.net/cairo-dock-core

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
BuildPreReq: cmake rpm-macros-cmake
# Automatically added by buildreq on Wed Sep 09 2015 (-bi)
# optimized out: at-spi2-atk cmake-modules elfutils fontconfig glib-networking glib2-devel libGL-devel libX11-devel libXfixes-devel libXrender-devel libat-spi2-core libatk-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libdbus-devel libdbus-glib libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libpango-devel libstdc++-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl libwayland-server pkg-config python-base wayland-devel xorg-compositeproto-devel xorg-fixesproto-devel xorg-kbproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: ImageMagick-tools cmake desktop-file-utils gcc-c++ libGConf libGLU-devel libXcomposite-devel libcurl-devel libdbus-glib-devel libgtk+3-devel librsvg-devel libxml2-devel
%if_enabled session
BuildRequires: libpixman-devel libXtst-devel libXrandr-devel libXdmcp-devel libwayland-egl-devel 	libharfbuzz-devel libexpat-devel libdrm-devel libXdamage-devel libXxf86vm-devel libpng-devel libXinerama-devel libXcursor-devel 	libxkbcommon-x11-devel libwayland-cursor-devel libepoxy-devel at-spi2-atk-devel libat-spi2-core-devel
%endif

%description
Cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%description -l ru_RU.UTF-8
Сairo-dock использует cairo для рендеринга приятной графики и Glitz для
задействования аппаратного ускорения. Это полностью настраиваемая и
многофункциональная панель задач. Вы можете легко включить апплеты не ней.

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
%cmake %{?_enable_session:-Denable-desktop-manager=ON}
%make_build -C BUILD

%install
%makeinstall_std -C BUILD

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
%_bindir/%name
%_libdir/*.so.*
%_libdir/%name/libcd-Help.so
%_datadir/%name
%_desktopdir/*.desktop
%_pixmapsdir/*.svg
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_man1dir/*.1.*

%if_enabled session
%_bindir/%name-session
%_datadir/gnome-session/sessions/cairo-dock.session
%exclude %_datadir/xsessions/cairo-dock.desktop
%endif

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Mar 21 2016 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt3
- Added missing buildrequires
- Enabled session.

* Wed Sep 16 2015 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt2
- Small fix in spec

* Wed Sep 09 2015 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- New version 3.4.1
- Updated buildreqs
- Enabled session

* Fri Jul 04 2014 Motsyo Gennadi <drool@altlinux.ru> 3.3.2-alt0.M60T.1
- backport for t6

* Wed Nov 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- 3.3.2
- updated buildreqs

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1.r33
- New version 3.1.0-r33

* Wed Nov 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.1
- Fixed build

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
