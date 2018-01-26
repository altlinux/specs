%def_disable session
Name: cairo-dock
Version: 3.4.1
Release: alt5%ubt

Summary: A light and eye-candy dock to launch your programs easily
Summary(ru_RU.UTF-8): Приятный глазу док для простого запуска ваших программ
License: GPLv3+
Group: Graphical desktop/Other
# http://glx-dock.org
Url: https://launchpad.net/cairo-dock-core

Packager: Anton Midyukov <antohami@altlinux.org>
Source: %name-%version.tar
Source1: cairo-dock-16x16.png
Source2: cairo-dock-32x32.png
Source3: cairo-dock-48x48.png

Buildrequires(pre): rpm-build-ubt
Buildrequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gconf-2.0)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libxml-2.0)

%if_enabled session
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(xdamage)
BuildRequires: pkgconfig(xxf86vm)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(xcursor)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(atk-bridge-2.0)
BuildRequires: pkgconfig(atspi-2)
%endif

Requires: %name-data = %EVR

%description
Cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

%description -l ru_RU.UTF-8
Сairo-dock использует cairo для рендеринга приятной графики и Glitz для
задействования аппаратного ускорения. Это полностью настраиваемая и
многофункциональная панель задач. Вы можете легко включить апплеты не ней.

%package data
Summary: Data files for %name
Group: Graphical desktop/Other
BuildArch: noarch

%description data
Data files for %name

%if_enabled session
%package session
Summary: Session for %name
Group: Graphical desktop/Other
BuildArch: noarch
Requires: %name = %EVR

%description session
Session for %name
%endif

%package devel
Summary: Development files for cairo-dock
Group: Development/Other
Requires: %name = %EVR

%description devel
cairo-dock uses cairo to render nice graphics, and Glitz to use hardware
acceleration. It's fully configurable and can be a taskbar too. You can
easily plug applets into it.

This package provides the include files and library for cairo-dock functions.

%prep
%setup -n %name-%version

%build
%cmake %{?_enable_session:-Denable-desktop-manager=ON}
%cmake_build

%install
%cmakeinstall_std

%find_lang %name

mkdir -p %buildroot{%_niconsdir,%_miconsdir,%_liconsdir}
install -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -m644 %SOURCE3 %buildroot%_liconsdir/%name.png
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
%_libdir/%name

%files data
%_datadir/%name
%_desktopdir/*.desktop
%_pixmapsdir/*.svg
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_man1dir/*.1.*

%if_enabled session
%files session
%_bindir/%name-session
%_datadir/gnome-session/sessions/cairo-dock.session
%exclude %_datadir/xsessions/cairo-dock.desktop
%endif

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Jan 26 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt5%ubt
- Fix FTBFS
- Update buildrequires
- Disabled session.

* Mon May 02 2016 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt4
- New package cairo-dock-data
- New package cairo-dock-session.

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
