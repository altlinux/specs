
%define ver_major 1.3
%define libsynthesis_ver 3.4.0.16.8
%define _libexecdir %_prefix/libexec

%def_enable libsoup
%def_enable libcurl
%def_enable xmlrpc
%def_enable bluetooth
%def_enable gnome_bluetooth
%def_enable gnome_keyring
%def_enable akonadi
%def_disable activesync
# experimental now
# sqlite conflicts with the evolution backend
%def_disable sqlite
%def_enable dav
%def_disable qtcontacts

#SySync_ConsolePrintf is expected by libsmltk and has to be provided by caller
%set_verify_elf_skiplist %_libdir/libsmltk.so.0.6.0

Name: syncevolution
Version: %ver_major.2
Release: alt1
Summary: SyncEvolution synchronizes personal information management (PIM) data like contacts, calenders, tasks and memos

Group: Office
License: GPLv2
Url: http://%name.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar
Source2: libsynthesis.tar

Requires: %name-libs = %version-%release
Requires: ca-certificates

BuildRequires: boost-devel boost-signals-devel db2latex-xsl evolution-data-server-devel gcc-c++ intltool libexpat-devel zlib-devel
BuildRequires: libnotify-devel libopenobex-devel libdbus-devel libdbus-glib-devel
BuildRequires: libpcre-devel libpcrecpp-devel cppunit-devel python-module-PyXML python-modules-encodings xsltproc
BuildRequires: libneon-devel kde4pimlibs-devel
BuildRequires: libgtk+3-devel libgio-devel
%{?_enable_libsoup:BuildRequires: libsoup-gnome-devel}
%{?_enable_libcurl:BuildRequires: libcurl-devel}
%{?_enable_bluetooth:BuildRequires: libbluez-devel}
%{?_enable_gnome_bluetooth:BuildRequires: libgnome-bluetooth-devel}
%{?_enable_gnome_keyring:BuildRequires: libgnome-keyring-devel}
%{?_enable_xmlrpc:BuildRequires: libxmlrpc-devel}
%{?_enable_sqlite:BuildRequires: libsqlite3-devel}
%{?_enable_activesync:BuildRequires: libeasclient-devel}
%{?_enable_qtcontacts:BuildRequires: qt4-mobility-devel}


%description
SyncEvolution synchronizes personal information management (PIM) data
such as contacts, appointments, tasks and memos using the Synthesis sync
engine, which provides support for the SyncML synchronization protocol.
SyncEvolution synchronizes with SyncML servers over HTTP and with SyncML
capable phones locally over Bluetooth. Plugins provide access to the
data which is to be synchronized.

%package libs
Summary: GTK gui for SyncEvolution
Group: System/Libraries

%description libs
SyncEvolution synchronizes personal information management (PIM) data
such as contacts, appointments, tasks and memos using the Synthesis sync
engine, which provides support for the SyncML synchronization protocol.
SyncEvolution synchronizes with SyncML servers over HTTP and with SyncML
capable phones locally over Bluetooth. Plugins provide access to the
data which is to be synchronized.

This package provides shared libraries needed for SyncEvolution to work.

%package ui-gtk
Summary: GTK gui for SyncEvolution
Group: Office
Requires: %name = %version-%release

%description ui-gtk
SyncEvolution synchronizes personal information management (PIM) data
such as contacts, appointments, tasks and memos using the Synthesis sync
engine, which provides support for the SyncML synchronization protocol.
SyncEvolution synchronizes with SyncML servers over HTTP and with SyncML
capable phones locally over Bluetooth. Plugins provide access to the
data which is to be synchronized.

This package provides GTK gui for SyncEvolution.

%package devel
Summary: Development files for SyncEvolution
Group: System/Libraries
Requires: %name-libs = %version-%release

%description devel
SyncEvolution synchronizes personal information management (PIM) data
such as contacts, appointments, tasks and memos using the Synthesis sync
engine, which provides support for the SyncML synchronization protocol.
SyncEvolution synchronizes with SyncML servers over HTTP and with SyncML
capable phones locally over Bluetooth. Plugins provide access to the
data which is to be synchronized.

This package provides headers and libraries needed for development
SyncEvolution plugins.

%define pkgdocdir %_docdir/%name-%version

%prep
%setup -q -a2
sed -i '/^ACLOCAL_AMFLAGS/{ /m4-repo/!s/$/ -I m4-repo/ }' Makefile*.am

%build
./autogen.sh
pushd libsynthesis
mkdir m4
./autogen.sh
popd

export LDFLAGS="$LDFLAGS -ldl -L%_libdir/kde4/devel"
%configure \
	--enable-shared \
	--disable-static \
	--with-synthesis-src=libsynthesis \
	--enable-dbus-service \
	--with-gio-gdbus \
	--enable-gui=gtk \
	--enable-gtk=3 \
	%{subst_enable libsoup} \
	%{subst_enable libcurl} \
	%{subst_enable xmlrpc} \
	%{subst_enable sqlite} \
	%{subst_enable bluetooth} \
	%{subst_enable akonadi} \
	%{subst_enable activesync} \
	%{subst_enable dav} \
	%{subst_enable qtcontacts} \
	%{?_enable_gnome_keyring:--enable-gnome-keyring} \
	%{?_enable_gnome_bluetooth:--enable-gnome-bluetooth-panel-plugin} \
	--with-ca-certificates=%_datadir/ca-certificates/ca-bundle.crt \
	--docdir=%pkgdocdir

%make_build

%install
%make_install install DESTDIR=%buildroot

install -p -m 644 HACKING AUTHORS ChangeLog %buildroot/%pkgdocdir/
rm -f %buildroot%_libdir/*.{a,la}
rm -f %buildroot%_libdir/*/*.{a,la}
rm -f %buildroot%_libdir/*/*/*.{a,la}

%find_lang %name

%check
# FAILS currently
#make check

%files -f %name.lang
%_bindir/*
%_libexecdir/*
%dir %_libdir/%name
# some backends not linked properly, test needed
#FIXME: divide backends
%_libdir/%name/backends
%_libdir/gnome-bluetooth/plugins/libgbt%name.so
%_datadir/%name

%exclude %_bindir/sync-ui
%exclude %_datadir/%name/sync-*
%exclude %_datadir/%name/ui.xml

%_datadir/dbus-1/services/org.%name.service
%_sysconfdir/xdg/autostart/syncevo-dbus-server.desktop
%doc %pkgdocdir/

%files libs
%_libdir/*.so.*

%files devel
%_includedir/syncevo
%_includedir/syncevo-dbus
%_includedir/synthesis
%_libdir/*.so
%_pkgconfigdir/*

%files ui-gtk
%_bindir/sync-ui
%_datadir/%name/sync-*
%_datadir/%name/ui.xml
%_datadir/applications/sync.desktop
%_iconsdir/hicolor/48x48/apps/sync.png

%changelog
* Wed Nov 28 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Oct 02 2012 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- disable activesync

* Thu Sep 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.99.4-alt3
- build to sisyphus

* Wed Sep 05 2012 Ildar Mulyukov <ildar@altlinux.ru> 1.2.99.4-alt2
- upstream/syncevolution: new snapshot
- added and enabled new backends
- disabled sqlite and qtcontacts backends

* Fri Aug 31 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.99.4-alt1
- 1.2.99.4
- build with gtk+-3

* Sat Mar 31 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Fri Oct 28 2011 Alexey Shabalin <shaba@altlinux.ru> 1.2-alt1
- 1.2

* Wed Aug 31 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.99.6-alt1
- 1.1.99.6

* Wed Apr 13 2011 Alexey Shabalin <shaba@altlinux.ru> 1.1.1-alt1
- 1.1.1a

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 1.0.99.7-alt1
- 1.0.99.7
- define _libexecdir as /usr/libexec

* Wed Jun 23 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt3
- specified location of system CA certificates

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt2
- rebuild against libedataserver-1.2.so.13 (e-d-s-2.30.2)

* Thu Jun 17 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- 1.0
- rewrite spec

* Mon May 25 2009 Lebedev Sergey <barabashka@altlinux.org> 0.8.1-alt2
- fixed build with new toolchain

* Tue Nov 25 2008 Lebedev Sergey <barabashka@altlinux.org> 0.8.1-alt1
- new upstream version

* Tue Aug 05 2008 Lebedev Sergey <barabashka@altlinux.org> 0.7-alt1
- Init build

