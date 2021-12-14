Name:		arcclock
Version:	1.2.1
Release:	alt1
Summary:	Simple desktop clock
Url:		https://www.linux-apps.com/p/1190699/
Group:		Accessibility
License:	LGPL
Source0:	Simple-Arc-Clock.tar.xz

Provides:	Simple-Arc-Clock

# Automatically added by buildreq on Wed Oct 04 2017 (-bi)
# optimized out: GraphicsMagick GraphicsMagick-common elfutils gcc-c++ libGL-devel libqt5-core libqt5-gui libqt5-widgets libstdc++-devel perl python-base python-modules qt5-base-common xz
BuildRequires: GraphicsMagick-ImageMagick-compat qt5-base-devel

%description
Simple desktop clock that is easy to configure.

%prep
%setup -n Simple-Arc-Clock

%build
qmake-qt5 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
# #subst 's|Utility;|Qt;Utility;|g' %name.desktop
install -Dp -m 0755 %name %buildroot%_bindir/%name
install -Dp -m 0644 %name.desktop %buildroot%_desktopdir/%name.desktop

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 48x48 %name.svg %buildroot%_liconsdir/%name.png
convert -resize 32x32 %name.svg %buildroot%_niconsdir/%name.png
convert -resize 16x16 %name.svg %buildroot%_miconsdir/%name.png
install -Dp -m 0644 ./arcclock.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc README.md
%_bindir/*
%_desktopdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Dec 14 2021 Motsyo Gennadi <drool@altlinux.ru> 1.2.1-alt1
- update

* Fri Oct 06 2017 Motsyo Gennadi <drool@altlinux.ru> 1.2-alt1
- 1.2

* Wed Oct 04 2017 Motsyo Gennadi <drool@altlinux.ru> 1.1-alt1
- initial build for ALT Linux
