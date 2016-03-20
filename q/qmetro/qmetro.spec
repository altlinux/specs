Name: qmetro
Version: 0.7.1
Release: alt1

Summary: Transport system maps for many city subways
License: GPLv2+
Group: Sciences/Geosciences

Url: https://sourceforge.net/projects/qmetro/
Source: http://downloads.sourceforge.net/%name/%name-%version.zip
Source100: %name.watch
Patch: qmetro-0.7.1-desktop.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: gcc-c++ librsvg-utils unzip
BuildRequires: pkgconfig(QtCore)
BuildRequires: pkgconfig(QtGui)
BuildRequires: pkgconfig(QtNetwork)

%description
Vector metro (subway) map for calculating route and getting information
about transport nodes. It's GPL project for creating analog of pMetro
(Muradov B.) and it's using PMZ format. Maps have an open format and can
easily be edited or created.

Requires qmetro-data-* files.

%files
%doc AUTHORS LICENSE README
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/%name.*
%dir %_datadir/%name/
%dir %_datadir/%name/map/

%prep
%setup
%patch -p1

%build
%qmake_qt4 LIBS+=-lz
%make

%install
make INSTALL_ROOT=%buildroot install

mkdir -p %buildroot%_datadir/%name/map

# Remove Android skin, maps (packaged in qmetro-data-*).
rm -r %buildroot/tmp

# Remove incorrect icon size.
rm -r %buildroot%_iconsdir/hicolor/80x80

# Install icons of various sizes.
for s in 256 128 96 48 32 22 16 ; do
	mkdir -p %buildroot%_iconsdir/hicolor/${s}x${s}/apps
	rsvg-convert -w $s -h $s \
		rc/icons/hicolor/scalable/apps/%name.svg -o \
		%buildroot%_iconsdir/hicolor/${s}x${s}/apps/%name.png
done

%changelog
* Sun Mar 20 2016 Michael Shigorin <mike@altlinux.org> 0.7.1-alt1
- initial build for ALT Linux Sisyphus (based on Rosa package)

* Thu Jan 23 2014 Rosa <rosa@abf.rosalinux.ru> 0.7.1-1
+ Revision: 0e516db
- Automatic import for version 0.7.1-1
