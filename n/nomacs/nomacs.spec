Name:		nomacs
Version:	1.0.2
Release:	alt1
License:	GPLv3
Group:		Graphics
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	A fast and small image viewer
Source0:	http://sourceforge.net/projects/nomacs/files/%name-%version/%name-%version.tar.bz2
Url:		http://www.nomacs.org

BuildRequires: cmake gcc-c++ libexiv2-devel libgomp-devel libopencv-devel libraw-devel-static libqt4-devel

%description
nomacs is a free image viewer small, fast and able to handle the most common
image formats including RAW images. Additionally it is possible to synchronize
multiple viewers. A synchronization of viewers running on the same computer
or via LAN is possible. It allows to compare images and spot the differences
(e.g. schemes of architects to show the progress).

%prep
%setup

%build
cmake \
	-DCMAKE_INSTALL_PREFIX=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags"
%make_build

%install
%make DESTDIR=%buildroot install

%files
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%_datadir/%name/translations/*.qm
%_pixmapsdir/%name.png

%changelog
* Fri Apr 05 2013 Motsyo Gennadi <drool@altlinux.ru> 1.0.2-alt1
- initial build for ALT Linux
