Version:	0.2.1
Name:		netfleet
Release:	alt1
Summary:	NetFleet is a multi-threaded(!) download utility
License: 	GPLv3
Group: 		Networking/File transfer
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://netfleet.sourceforge.net/
Source0:	http://netfleet.googlecode.com/files/%{name}_%{version}.tar.bz2
Source1:	%name.desktop

# Automatically added by buildreq on Fri Nov 27 2009 (-bi)
BuildRequires: ImageMagick-tools gcc-c++ libqt4-devel

%description
NetFleet is a Open Source cross-platform and multi-threaded(!)
download utility. This program tries to accelerate the downloading
process by using multiple connections for one file.

%prep
%setup -n %name

%build
rm -rf translations/*.qm && lrelease-qt4 translations/*.ts
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build VERBOSE=1

%install
%make INSTALL_ROOT=%buildroot install
install -Dp -m 0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 images/%name.xpm %buildroot%_liconsdir/%name.png
convert -resize 32x32 images/%name.xpm %buildroot%_niconsdir/%name.png
convert -resize 16x16 images/%name.xpm %buildroot%_miconsdir/%name.png

%files
%_bindir/*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Nov 27 2009 Motsyo Gennadi <drool@altlinux.ru> 0.2.1-alt1
- initial build for ALT Linux
