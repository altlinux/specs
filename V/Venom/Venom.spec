Name: Venom
Summary: graphical user interface for Tox
Version: 0.1.2
Release: alt1.20140813
License: GPLv3
Group: Networking/Instant messaging

BuildRequires: cmake libgtk+3-devel libjson-glib-devel libnotify-devel libsqlite3-devel toxcore-devel vala

Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Source2: %name.watch

Patch: %name-%version-%release.patch
Url: https://github.com/naxuroqa/Venom

%description
%name

%prep
%setup
%patch -p1

%build
mkdir -p build
cd build
%cmake_insource -DENABLE_LIBNOTIFY=1 -DENABLE_QRENCODE=1  .. 
%make_build

%install
cd build
%makeinstall_std
cd ..
%find_lang %name

%files -f %name.lang
%_bindir/venom
%_desktopdir/venom.desktop
%_iconsdir/hicolor/128x128/apps/venom.png
%_iconsdir/hicolor/16x16/apps/venom.png
%_iconsdir/hicolor/256x256/apps/venom.png
%_iconsdir/hicolor/32x32/apps/venom.png
%_iconsdir/hicolor/48x48/apps/venom.png
%_iconsdir/hicolor/64x64/apps/venom.png
%_iconsdir/hicolor/scalable/apps/venom.svg
%_pixmapsdir/venom.png
%_datadir/venom

%changelog
* Wed Aug 13 2014 Denis Smirnov <mithraen@altlinux.ru> 0.1.2-alt1.20140813
- first build for Sisyphus

