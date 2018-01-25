Name: nomacs
Version: 2.4.6
Release: alt5

License: GPLv3
Group: Graphics
Summary: A fast and small image viewer
Url: http://www.nomacs.org

Source: https://github.com/%name/%name/archive/%name-%version.tar.bz2

BuildRequires: cmake gcc-c++ libqt4-devel libexiv2-devel libgomp-devel
BuildRequires: libtiff-devel libopencv-devel libraw-devel libgomp-devel
BuildRequires: zlib-devel libwebp-devel libquazip-devel libtbb-devel
#BuildRequires: libqpsd-devel

%description
nomacs is a free image viewer small, fast and able to handle the most common
image formats including RAW images. Additionally it is possible to synchronize
multiple viewers. A synchronization of viewers running on the same computer
or via LAN is possible. It allows to compare images and spot the differences
(e.g. schemes of architects to show the progress).

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release" \
	-DUSE_SYSTEM_LIBQPSD:BOOL=OFF \
	-DUSE_SYSTEM_QUAZIP:BOOL=ON \
	-DUSE_SYSTEM_WEBP:BOOL=ON

%cmake_build

%install
%cmakeinstall_std

%find_lang --with-qt %name

%files -f %name.lang
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%dir %_datadir/%name/translations
%_pixmapsdir/%name.png

%changelog
* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.6-alt5
- Fixed build.

* Wed Jul 05 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.6-alt4
- Updated build dependencies

* Thu Dec 29 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt3
- rebuilt against libraw.so.16

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt2
- rebuilt against libwebp.so.6

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt1
- 2.4.6

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt2
- rebuilt against libraw.so.15

* Wed Jul 01 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.6.3-alt2.1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Mar 13 2014 Dmitry Derjavin <dd@altlinux.org> 1.6.3-alt2.1
- NMU: rebuild with libopencv-2.4.8.1;

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt2
- rebuilt against libraw.so.10

* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3
- built against libexiv2.so.13

* Fri Apr 05 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux
