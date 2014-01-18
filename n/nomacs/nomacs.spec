Name: nomacs
Version: 1.6.3
Release: alt1

License: GPLv3
Group: Graphics
Summary: A fast and small image viewer
Url: http://www.nomacs.org

Source: http://sourceforge.net/projects/nomacs/files/%name-%version/%name-%version.tar.bz2

BuildRequires: cmake gcc-c++ libqt4-devel libexiv2-devel libgomp-devel
BuildRequires: libtiff-devel libopencv-devel libraw-devel-static zlib-devel

%description
nomacs is a free image viewer small, fast and able to handle the most common
image formats including RAW images. Additionally it is possible to synchronize
multiple viewers. A synchronization of viewers running on the same computer
or via LAN is possible. It allows to compare images and spot the differences
(e.g. schemes of architects to show the progress).

%prep
%setup
rm -rf {LibRaw,exiv2,expat,zlib}*

%build
%cmake ../ImageLounge
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
* Sat Jan 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3
- built against libexiv2.so.13

* Fri Apr 05 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux
