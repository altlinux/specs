Name: kunit
Version: 0.5
Release: alt9

Summary: KUnit - units converter
Summary(ru-Ru.KOI8-R): Конвертер физических величин
Group: Sciences/Physics
License: GPL
Url: http://www.netmeister.org

Packager: Andrey Cherepanov <cas@altlinux.ru>
Source:  %name-%version.tar.bz2
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: %name-64.png
Source5: %name-128.png
Source6: %name.svg
Source7: %name.desktop
Source8: %name.docbook

Patch1: kunit-0.5-qt_no_compat.patch
Patch2: kunit-build.patch
Patch3: kunit-fix_deprecated_headers.patch

BuildPreReq: menu-devel desktop-file-utils
BuildRequires: gcc-c++ kdelibs-devel libqt3-devel libpng-devel libjpeg-devel
Requires(post,postun): desktop-file-utils

%description
KUnit is a simple program to convert various units.
KUnit currently converts the following categories:
acceleration, angle, angular acceleration, angular velocity, area, bits
and bytes, capacitance, charge, colors, current, energy, force,
illuminance, inductance, length, luminance, magnetic flux, mass (or
weight), power, pressure, Shoe Sizes, SI prefixes, specific heat,
temperature, thermal conductivity, time, torque, velocity, viscosity
(dynamic), viscosity (kinematic), voltage, volume.

%description -l ru-RU.KOI8-R
KUnit - программа пересчета физических величин в различные системы
единиц измерения. Программа позволяет пересчитывать
ускорение, угловые величины, угловое ускорение, угловую скорость,
площадь, биты и  байты, электрическую емкость, заряд, цвета (RGB, HEX),
силу тока, энергию, силу, освещенность, индуктивность, длину, яркость,
магнитный поток, массу и вес, мощность, давление, размер обуви,
десятичные приставки СИ, теплоемкость, температуру, теплопроводность,
время, крутящий момент, скорость, динамическую и киниматическую
вязкость, напряжение, объем.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p2

%build
%add_optflags -DQT_CLEAN_NAMESPACE -DQT_NO_COMPAT
%make_build \
	QTDIR=%_libdir/qt3 \
	CFLAGS="%optflags" \
	CXXFLAGS="%optflags"

%install
%__install -pD kunit/%name %buildroot%_bindir/%name
%__install -pD %SOURCE8 %buildroot%_docdir/HTML/en/%name/index.docbook
/usr/bin/meinproc --check --cache %buildroot%_docdir/HTML/en/%name/index.cache.bz2 %buildroot%_docdir/HTML/en/%name/index.docbook
%__ln_s ../common %buildroot/%_docdir/HTML/en/%name/common

#icons
%__install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
%__install -pD -m644 %SOURCE2 %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
%__install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.png
%__install -pD -m644 %SOURCE4 %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
%__install -pD -m644 %SOURCE5 %buildroot%_iconsdir/hicolor/128x128/apps/%name.png
%__install -pD -m644 %SOURCE6 %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
%__install -pD -m644 %SOURCE7 %buildroot%_datadir/applications/kde/%name.desktop

%files
%doc README AUTHORS
%doc %_docdir/HTML/*/%name
%_bindir/%name
%_datadir/applications/kde/*
%_liconsdir/%name.png
%_iconsdir/*/*/*/%name.png
%_iconsdir/*/*/*/%name.svg
%_miconsdir/%name.png

%changelog
* Tue Nov 25 2008 Andrey Cherepanov <cas@altlinux.org> 0.5-alt9
- Fix kunit.desktop file 

* Fri Nov 21 2008 Andrey Cherepanov <cas@altlinux.org> 0.5-alt8
- Remove deprecated update-desktop-database and update-menus macros 

* Wed Oct 29 2008 Andrey Cherepanov <cas@altlinux.org> 0.5-alt7
- Fix deprecated C++ headers 

* Wed Jan 30 2008 Andrey Cherepanov <cas@altlinux.ru> 0.5-alt6
- Return from orphaned packages
- New icons (both scalable and pixmaps)
- Convert documentation to Docbook

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.5-alt5.1
- Rebuilt with libstdc++.so.6.

* Thu Sep 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt5
- rebuild. 

* Fri Oct 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt4
- Rebuild with new qt3.

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5-alt3
- build with gcc3.2 , Qt3

* Mon Jan 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt2
- cleanups

* Wed Dec 5 2001 Yuri N. Sedunov <aris@altlinux.ru> 0.5-alt1
- first build for Sisyphus
