#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1
%define sover 3

Name: cairo-dock
Version: 3.6.0
Release: alt1

Summary: A light and eye-candy system panel to launch your programs easily
Summary(ru_RU.UTF-8): Лёгкая и привлекательная системная панель для удобного запуска программ
License: GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-3.0-or-later
Group: Graphical desktop/Other

URL: https://github.com/Cairo-Dock/cairo-dock-core
VCS: https://github.com/Cairo-Dock/cairo-dock-core

Obsoletes: %name-data < %version

Source: %name-%version.tar

Buildrequires(pre): rpm-macros-cmake
BuildRequires(pre): /proc
BuildRequires: cmake
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(glu)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xtst)
BuildRequires: pkgconfig(xcomposite)
BuildRequires: pkgconfig(xrandr)
BuildRequires: pkgconfig(gtk+-3.0)
#BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(xinerama)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: extra-cmake-modules

%description
Cairo-Dock is a pretty, light and convenient interface to your desktop,
able to replace advantageously your system panel! It features multi-docks,
taskbar, launchers and a lot of useful applets that can be detached from
the dock to act as desktop widgets.

%description -l ru_RU.UTF-8
Cairo-Dock — это красивый, лёгкий и удобный интерфейс для вашего рабочего стола,
способный с успехом заменить системную панель! Он включает в себя мультидоки,
панель задач, лаунчеры и множество полезных апплетов, которые можно отсоединить
от дока и использовать в качестве виджетов рабочего стола.

%package -n libgldi%sover
Summary: Library for cairo-dock
Group: System/Libraries

%description -n libgldi%sover
This package is a library for cairo-dock.

%package devel
Summary: Development files for cairo-dock
Group: Development/Other
Requires: libgldi%sover = %EVR

%description devel
This package provides include files and libraries for cairo-dock functions.

%prep
%setup -n %name-%version

%build
%cmake \
	-DCMAKE_BUILD_TYPE=Release \
	-Denable-desktop-manager=False \
	-Denable-systemd-service=True

%cmake_build

%install
%cmake_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/*.desktop
%_datadir/%name
%_man1dir/*.1.*
%_pixmapsdir/*.svg
%_libdir/%name
%_user_unitdir/*.service

%files -n libgldi%sover
%_libdir/libgldi.so.%sover
%_libdir/libgldi.so.%sover.*

%files devel
%_includedir/%name
%_libdir/libgldi.so
%_pkgconfigdir/*.pc

%changelog
* Sat Nov 1 2025 Polina Poidenko <polipoki@altlinux.org> 3.6.0-alt1
- New version 3.6.0.
- Update License: GPL-2.0-or-later AND LGPL-3.0-or-later.
- Update buildreqs.
- Separate subpackage libgldi3 in accordance with Shared Libs Policy.
- Remove subpackage cairo-dock-data.

* Tue Sep 18 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt6
- drop ubt

* Fri Jan 26 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt5.S1
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
