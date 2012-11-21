# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/perl5 /usr/bin/pkg-config /usr/bin/update-mime-database gobject-introspection-devel libICE-devel libSM-devel libX11-devel libXrender-devel libgtk+2-gir-devel libselinux-devel pkgconfig(gail) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pango) pkgconfig(unique-3.0) xorg-xproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:		mate-file-manager
Summary:	File manager for MATE
Version:	1.5.0
Release:	alt2_4
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/Other
URL:		http://mate-desktop.org
Source0:	http://vicodan.fedorapeople.org/%{name}-%{version}-GIT.tar.gz

Requires:	gamin
Requires:	filesystem
Requires:	altlinux-freedesktop-menu-common
Requires:	gvfs
Requires:	mate-icon-theme
Requires:	gsettings-desktop-schemas

BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(libselinux)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(unique-1.0)
BuildRequires:	mate-common
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(pangox)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)


# the main binary links against libcaja-extension.so
# don't depend on soname, rather on exact version
Requires:	%{name}-extensions%{?_isa} = %{version}-%{release}
Source44: import.info
Patch33: mate-file-manager-1.2.2-alt-fix-linkage.patch
Patch34: nautilus-2.22.1-umountfstab.patch
Patch35: mate-file-manager-1.5.0-alt-desktop-labels-po-ru.patch

# Some changes to default config
#Patch0:	caja-config.patch

#Patch1:	caja-rtl-fix.patch

#Patch2:	caja-gvfs-desktop-key-2.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=519743
#Patch3:	caja-filetype-symlink-fix.patch

#Patch5:	no_session_delay.patch
#Patch6:	signal_curtain.patch

# upstreamable, don't reference non-existent doc xml file
#Patch7:	mate-file-manager-1.4.0-docfix.patch

# http://git.gnome.org/browse/nautilus/commit/?id=d3ab8e137ae957e5afef54bf0ec1e275b96caab5
# https://github.com/mate-desktop/mate-file-manager/issues/29
#Patch8:	close_earlier.patch


%description
Caja (mate-file-manager) is the file manager and graphical shell
for the MATE desktop,
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote file systems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the MATE desktop.

%package extensions
Summary:	Mate-file-manager extensions library
License:	LGPLv2+
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description extensions
This package provides the libraries used by caja extensions.

%package devel
Summary:	Support for developing mate-file-manager extensions
License:	LGPLv2+
Group:		Development/C
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides libraries and header files needed
for developing caja extensions.

%prep
%setup -q
sed -i -e 's,Categories=MATE,Categories=X-MATE,g' src/mate-network-scheme.desktop.in data/caja*desktop*

#patch0 -p1 -b .config
#patch1 -p1 -b .caja-rtl-fix
#patch2 -p1 -b .gvfs-desktop-key
#patch3 -p0 -b .symlink
#patch5 -p1 -b .no_session_delay
#patch7 -p1 -b .docfix
#patch8 -p1 -b .close_earlier

%patch33 -p1
%patch35 -p1
NOCONFIGURE=1 ./autogen.sh
%patch34 -p1

%build
%configure				\
	--disable-static		\
	--with-gnu-ld			\
	--with-x			\
	--disable-schemas-compile	\
	--enable-unique			\
	--enable-introspection		\
	--disable-gtk-doc		\
	--disable-update-mimedb


# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags} V=1


%install
make DESTDIR=%{buildroot} install

find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

rm -f %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
rm -f %{buildroot}%{_datadir}/icons/hicolor/.icon-theme.cache

mkdir -p %{buildroot}%{_libdir}/caja/extensions-2.0

desktop-file-validate %{buildroot}/%{_datadir}/applications/caja-file-management-properties.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/caja-computer.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/caja-browser.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/caja-home.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/mate-network-scheme.desktop

%find_lang caja

%files -f caja.lang
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB NEWS README
%{_bindir}/*
%{_datadir}/caja/
%{_libdir}/caja/extensions-2.0/
%{_datadir}/pixmaps/caja/
%{_datadir}/applications/caja-*.desktop
%{_datadir}/applications/caja.desktop
%{_datadir}/applications/mate-network-scheme.desktop
%{_datadir}/icons/hicolor/*/apps/caja.png
%{_datadir}/icons/hicolor/scalable/apps/caja.svg
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml
%{_mandir}/man1/caja*.1.*
%{_libexecdir}/caja-convert-metadata
%{_datadir}/mime/packages/caja.xml

%files extensions
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB NEWS README
%{_libdir}/libcaja-extension.so.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/libcaja-extension/
%{_includedir}/caja
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir


%changelog
* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_4
- added desktop label localization patch

* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_4
- new bugfix fc release

* Fri Nov 16 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_3
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_2
- 20120622 mate snapshot

* Tue May 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- converted by srpmconvert script

