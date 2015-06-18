Name:		mkvextract-gtk
Version:	0.9.2
Release:	alt2.1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	GUI for extracting tracks from MKV files
License:	GPLv2
Group:		Video
Url:		https://bitbucket.org/Leyorus/mkvextract-gtk/
Source0:	%name-%version.tar.xz

Source1:	%name.desktop
Source2:	%name.png


Requires:	/usr/bin/mkvextract

BuildPreReq:	/usr/bin/convert

# Automatically added by buildreq on Thu May 14 2015 (-bi)
# optimized out: cmake-modules elfutils fontconfig fontconfig-devel glib2-devel libatk-devel libatkmm-devel libcairo-devel libcairomm-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libglibmm-devel libgtk+2-devel libpango-devel libpangomm-devel libsigc++2-devel libstdc++-devel libwayland-client libwayland-server pkg-config python-base xz
BuildRequires: boost-devel-headers cmake gcc-c++ libgtkmm2-devel

%description
This software is a simple and efficient GUI for extracting tracks from Matroska (mkv) files.
It is written in C++, using the GTK framework.

For now, it uses the tools provided by the mkvextract command line tool.

%prep
%setup -n %name

%build
mkdir ./build && cd ./build
cmake	-Wno-dev ../src/ \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make_build

%install
cd ./build
install -Dp -m 0755 Project %buildroot%_bindir/%name

# Desktop
install -Dp -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %SOURCE2 %buildroot%_liconsdir/%name.png
convert -resize 32x32 %SOURCE2 %buildroot%_niconsdir/%name.png
convert -resize 16x16 %SOURCE2 %buildroot%_miconsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.9.2-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Thu May 14 2015 Motsyo Gennadi <drool@altlinux.ru> 0.9.2-alt2
- fix build for sisyphus

* Thu May 14 2015 Motsyo Gennadi <drool@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux
