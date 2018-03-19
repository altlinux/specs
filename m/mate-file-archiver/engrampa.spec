%define _libexecdir %_prefix/libexec
%define rname engrampa

Name: mate-file-archiver
Version: 1.20.0
Release: alt1
Epoch: 1
Summary: MATE Desktop file archiver
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/MATE
Url: http://mate-desktop.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Requires: p7zip zip

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: mate-common intltool itstool libSM-devel libjson-glib-devel libmagic-devel mate-file-manager-devel yelp-tools

%description
Mate File Archiver is an application for creating and viewing archives files,
such as zip, xv, bzip2, cab, rar and other compress formats.

%package -n mate-file-manager-archiver
Summary: Mate-file-manager extension for mount archiver
Group: Graphical desktop/MATE

%description -n mate-file-manager-archiver
Mate-file-manager extension for mount archiver

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-static \
	--enable-caja-actions \
	--enable-magic \
	--disable-packagekit

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %rname --with-gnome --all-name

%files -f %rname.lang
%doc README COPYING NEWS AUTHORS
%_bindir/%rname
%_libexecdir/%rname
%_libexecdir/%rname-server
%_datadir/%rname
%_datadir/appdata/engrampa.appdata.xml
%_desktopdir/%rname.desktop
%_datadir/dbus-1/services/org.mate.Engrampa.service
%_iconsdir/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%_man1dir/*.1*

%files -n mate-file-manager-archiver
%_libdir/caja/extensions-2.0/libcaja-engrampa.so
%_datadir/caja/extensions/libcaja-engrampa.caja-extension

%changelog
* Mon Mar 19 2018 Valery Inozemtsev <shrek@altlinux.ru> 1:1.20.0-alt1
- initial build from git.mate-desktop.org

* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_1
- new fc release
