%define rname caja
%define _libexecdir %_prefix/libexec

Name: mate-file-manager
Version: 1.28.0
Release: alt1.1
Epoch: 1
Summary: File manager for MATE
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: %rname = %epoch:%version-%release
Requires: mate-file-manager-extensions mate-file-manager-schemas

Source: %rname-%version.tar
Source1: libegg.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common gtk-doc libSM-devel libexempi-devel libexif-devel libgail3-devel libnotify-devel
BuildRequires: libwayland-client-devel libgtk-layer-shell-devel libselinux-devel libxml2-devel mate-desktop-devel

%description
Caja (mate-file-manager) is the file manager and graphical shell
for the MATE desktop, that makes it easy to manage your files and
the rest of your system. It allows to browse directories on local
and remote file systems, preview files and launch applications
associated with them. It is also responsible for handling the
icons on the MATE desktop.

%package extensions
Group: Graphical desktop/MATE
Summary:  Mate-file-manager extensions library
Provides: %rname-extensions = %epoch:%version-%release

%description extensions
This package provides the libraries used by caja extensions.

%package schemas
Group: Graphical desktop/MATE
Summary:  Mate-file-manager schemas
License:  LGPLv2+
BuildArch: noarch
Provides: %rname-schemas = %epoch:%version-%release

%description schemas
This package provides the gsettings schemas for caja.

%package devel
Group: Development/C
Summary:  Support for developing mate-file-manager extensions
Provides: %rname-devel = %epoch:%version-%release

%description devel
This package provides libraries and header files needed
for developing caja extensions.

%prep
%setup -q -n %rname-%version -a1
%patch -p1

%build
%autoreconf
%configure \
	--enable-wayland \
	--enable-gtk-doc \
	--disable-static \
	--disable-schemas-compile \
	--disable-update-mimedb

%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_libdir/caja/extensions-2.0

%find_lang %rname --with-gnome --all-name

%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%_bindir/*
%_libdir/%rname
%_datadir/%rname
%_datadir/pixmaps/%rname
%_datadir/metainfo/caja.appdata.xml
%_datadir/dbus-1/services/org.mate.freedesktop.FileManager1.service
%_datadir/mime/packages/caja.xml
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_man1dir/*.1*

%files extensions
%_libdir/libcaja-extension.so.*
%_libdir/girepository-1.0/*.typelib

%files schemas -f %rname.lang
%_datadir/glib-2.0/schemas/org.mate.*.gschema.xml

%files devel
%_includedir/%rname
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gir-1.0/*.gir
%_datadir/gtk-doc/html/libcaja-extension

%changelog
* Mon Oct 14 2024 Andrey Cherepanov <cas@altlinux.org> 1:1.28.0-alt1.1
- NMU: added short locale choice in date and time format

* Tue Feb 27 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:1.28.0-alt1
- 1.28.0

* Tue Jan 30 2024 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.1-alt3
- cherry pick upstream fix gfile sort and symlink warnings w glib2.76 or later

* Wed Apr 12 2023 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.1-alt2
- added x-scheme-handler/smb mimetype to caja-folder-handler.desktop

* Wed Apr 12 2023 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.1-alt1
- 1.26.1

* Mon Nov 21 2022 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt2
- updated ru translation

* Fri Aug 06 2021 Valery Inozemtsev <shrek@altlinux.ru> 1:1.26.0-alt1
- 1.26.0

* Tue Feb 25 2020 Valery Inozemtsev <shrek@altlinux.ru> 1:1.24.0-alt1
- 1.24.0

* Wed Oct 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt2
- updated russian translation

* Wed Oct 16 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.2-alt1
- 1.22.2

* Wed Jul 24 2019 Slava Aseev <ptrnine@altlinux.org> 1:1.22.1-alt2
- Support querying files by contained text

* Tue Apr 23 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.1-alt1
- 1.22.1

* Wed Mar 06 2019 Valery Inozemtsev <shrek@altlinux.ru> 1:1.22.0-alt1
- 1.22.0

* Tue Dec 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.3-alt1
- 1.20.3

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.20.2-alt1.qa1
- NMU: applied repocop patch

* Mon Apr 09 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.2-alt1
- 1.20.2

* Tue Mar 27 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.1-alt1
- 1.20.1

* Tue Mar 13 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_3
- new fc release
