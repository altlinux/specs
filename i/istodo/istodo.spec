Name:		istodo
Version:	1.3.0
Release:	alt1
Group:		Office
License:	GPLv3
Summary:	Organizer for students
Source:		v%version.tar.gz
URL:		http://istodo.ru/

# Automatically added by buildreq on Wed Sep 17 2014
# optimized out: libGL-devel libcloog-isl4 libqt5-core libqt5-gui libqt5-network libqt5-sql libqt5-widgets libqt5-xml libstdc++-devel
BuildRequires: gcc-c++ qt5-base-devel

%description
iStodo is an organizer for students with scheduling and planning features.

%prep
%setup

sed -i 's/iOS//' iStodo.pro

%build
%qmake_qt5
%make_build STRIP=touch

%install
##makeinstall
install -D desktop/iStodo %buildroot%_bindir/istodo
install -D updaterServer/updaterServer %buildroot%_bindir/updaterServer
for N in 32 48 64 128 256; do
	install -D	linux*/source*/icons/${N}x${N}/istodo.png \
			%buildroot%_iconsdir/hicolor/${N}x${N}/apps/istodo.png
done
install -D linux*/source*/istodo.desktop %buildroot%_desktopdir/istodo.desktop

%files
%_bindir/*
%_iconsdir/*/*/*/*
%_desktopdir/*

%changelog
* Wed Sep 17 2014 Fr. Br. George <george@altlinux.ru> 1.3.0-alt1
- Initial build

