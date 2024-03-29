%define binname XyGrib

Name: xygrib
Version: 1.2.7
Release: alt1

Summary: Visualisation of meteo data from files in GRIB formats

License: GPL-3.0-only
Group: Networking/Other
Url: https://opengribs.org
Source0: %binname-%version-20220516.tar.gz
Source1: %binname.desktop

Patch1: XyGrib-1.2.6-71e6ce91da79.diff
Patch2: XyGrib-1.2.6-c3fd4c5b0a41.diff
Patch3: XyGrib-1.2.6-Qt-5.15.patch
Patch4: XyGrib-1.2.6-openjpeg-2.4.patch
Patch5: XyGrib-1.2.6-openjpeg-2.5.patch

Requires: fonts-ttf-liberation
Requires: %name-data = %version-%release

BuildRequires(pre): rpm-build-licenses

BuildRequires: cmake qt5-base-devel qt5-tools-devel libpng-devel libopenjpeg2.0-devel libnova-devel libproj-devel zlib-devel bzlib-devel

%description
Visualization of meteo data from files in GRIB formats v1 and v2.
GRIB data are used to display weather data in detailed format for
a certain area of sea or land. XyGrib is a fork of zyGrib 8.0.1.

%package data
Summary: Architecture independent files for XyGrib.
Group: Networking/Other
BuildArch: noarch

%description data
Architecture independent files for XyGrib.

Included low resolution maps for XyGrib (25 km, 5 km and 1 km)
and cities with population from 3000 to 10000 and more 10000.

data/gis/* have another license: CC-BY-3.0
home page: http://www.geonames.org/

%prep

%setup -q -n %binname-%version-20220516

#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1

sed -i 's/PATH_SUFFIXES openjpeg-2.3 openjpeg-2.2 openjpeg-2.1/PATH_SUFFIXES openjpeg-2.5 openjpeg-2.4 openjpeg-2.3 openjpeg-2.2 openjpeg-2.1/' CMakeLists.txt

%build
# -DNO_UPDATE=1 deactivates XyGrib internal SW update
%cmake \
    -DCMAKE_INSTALL_PREFIX=%_datadir/openGribs \
    -DCMAKE_CXX_FLAGS="%optflags -DNO_UPDATE=1"

#cd BUILD
#make
%cmake_build

%install

#cd BUILD
#make install DESTDIR=%buildroot
%cmake_install

mkdir %buildroot/%_bindir
mv %buildroot/%_datadir/openGribs/XyGrib/%binname %buildroot/%_bindir/%binname

mkdir -p -m 755 %buildroot/%_datadir/pixmaps
cp %buildroot/%_datadir/openGribs/XyGrib/data/img/xyGrib_32.xpm %buildroot/%_datadir/pixmaps
mkdir -p -m 755 %buildroot/%_datadir/applications
install -m 644 %SOURCE1 %buildroot/%_datadir/applications

find %buildroot \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%doc README.md LICENSE
%_bindir/%binname
%_datadir/pixmaps/*
%_datadir/applications/%binname.desktop

%files data
%_datadir/openGribs

%changelog
* Wed Oct 26 2022 Sergey Y. Afonin <asy@altlinux.org> 1.2.7-alt1
- New (development) version, 20221025 snapshot

* Mon May 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt4
- fixed build with openjpeg 2.5 (XyGrib-1.2.6-openjpeg-2.5.patch)

* Sat Apr 10 2021 Sergey Y. Afonin <asy@altlinux.org> 1.2.6-alt3
- fixed build with openjpeg 2.4 (XyGrib-1.2.6-openjpeg-2.4.patch)

* Sat Sep 19 2020 Sergey Y. Afonin <asy@altlinux.org> 1.2.6-alt2
- fixed build with Qt 5.15 (based on Gentoo's bug 732732)
- updated License tag to SPDX syntax

* Tue Jul 16 2019 Sergey Y. Afonin <asy@altlinux.org> 1.2.6-alt1
- New version

* Fri Jun 28 2019 Sergey Y. Afonin <asy@altlinux.ru> 1.2.4-alt1
- Initial build for AltLinux
