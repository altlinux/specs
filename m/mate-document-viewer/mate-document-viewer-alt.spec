# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-mkenums /usr/bin/gtkdocize /usr/bin/mateconftool-2 gcc-c++ libICE-devel pkgconfig(cairo) pkgconfig(cairo-pdf) pkgconfig(cairo-ps) pkgconfig(gail) pkgconfig(gail-3.0) pkgconfig(gio-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtk+-unix-print-2.0) pkgconfig(gtk+-unix-print-3.0) pkgconfig(gtk+-x11-2.0) pkgconfig(gtk+-x11-3.0) pkgconfig(libxml-2.0) pkgconfig(mate-keyring-1) pkgconfig(sm) pkgconfig(x11) zlib-devel
# END SourceDeps(oneline)
%define glib2_version 1.0
%define _libexecdir %_prefix/libexec
%define oldname atril
%global poppler_version 0.14.0
%global glib2_version 2.25.9
%global dbus_version 0.70
%global theme_version 1.1.0

Name:           mate-document-viewer
Version:        1.4.0
Release:        alt2_1.1
Summary:        Document viewer

License:        GPLv2+ and GFDL
Group:          Publishing
URL:            http://pub.mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel >= %{glib2_version}
BuildRequires:  libpoppler-glib-devel >= %{poppler_version}
BuildRequires:  libXt-devel
BuildRequires:  mate-keyring-devel
BuildRequires:  libglade2-devel
BuildRequires:  libtiffxx-devel libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libspectre-devel
BuildRequires:  mate-doc-utils
BuildRequires:  scrollkeeper
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
BuildRequires:  mate-icon-theme >= %{theme_version}
BuildRequires:  libtool
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  t1lib-devel
BuildRequires:  mate-conf-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  libcairo-gobject-devel

# for the caja properties page
BuildRequires: mate-file-manager-devel
# for the dvi backend
BuildRequires: libkpathsea-devel
# for the djvu backend
BuildRequires: libdjvu-devel

Requires: %{name}-libs = %{version}-%{release}
Patch33: mate-document-viewer-1.4.0-alt-link.patch
Patch34: evince-2.32.0-alt.patch

%description
Atril is simple multi-page document viewer. It can display and print
Portable Document Format (PDF), PostScript (PS) and Encapsulated PostScript
(EPS) files. When supported by the document format, evince allows searching
for text, copying text to the clipboard, hypertext navigation,
table-of-contents bookmarks and editing of forms.

 Support for other document formats such as DVI and DJVU can be added by
installing additional backends.


%package libs
Summary: Libraries for the atril document viewer
Group: System/Libraries

%description libs
This package contains shared libraries needed for atril


%package devel
Summary: Support for developing backends for the atril document viewer
Group: Development/C
Requires: %{name}-libs = %{version}-%{release}

%description devel
This package contains libraries and header files needed for atril
backend development.


%package dvi
Summary: Atril backend for dvi files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description dvi
This package contains a backend to let evince display dvi files.


%package djvu
Summary: Atril backend for djvu files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description djvu
This package contains a backend to let evince display djvu files.


%package caja
Summary: Atril extension for nautilus
Group: Graphical desktop/Other
Requires: %{name} = %{version}-%{release}
Requires: mate-file-manager

%description caja
This package contains the evince extension for the caja file manger.
It adds an additional tab called "Document" to the file properties dialog.

%prep
%setup -q -n %{name}-%{version}
NOCONFIGURE=1 ./autogen.sh
%patch33 -p0
%patch34 -p1

%build
%configure \
		--disable-static \
        --disable-scrollkeeper \
        --enable-introspection \
        --enable-comics \
        --enable-dvi=yes \
        --enable-djvu=yes \
        --enable-t1lib=yes \
        --with-gtk=2.0

make %{?_smp_mflags} V=1 LIBTOOL=/usr/bin/libtool

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang evince --all-name

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
/bin/rm -rf $RPM_BUILD_ROOT/var/scrollkeeper
# Get rid of static libs and .la files.
rm -f $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/atril/3/backends/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/atril/3/backends/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# don't ship icon caches
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache


%pre
if [ "$1" -gt 1 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-ps.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-comics.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-djvu.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-djvu.schemas \
	> /dev/null || :
fi

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
	mateconftool-2 --makefile-install-rule \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-ps.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-comics.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-djvu.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-djvu.schemas \
	> /dev/null || :

%preun
if [ "$1" -eq 0 ]; then
  export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
  mateconftool-2 --makefile-uninstall-rule \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-ps.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-comics.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-djvu.schemas \
	%{_sysconfdir}/mateconf/schemas/atril-thumbnailer-djvu.schemas \
	> /dev/null || :
fi

%files
# -f atril.lang
%{_bindir}/*
%{_sysconfdir}/mateconf/schemas/*
%{_datadir}/%{oldname}/
%{_datadir}/applications/%{oldname}.desktop
%{_datadir}/icons/hicolor/*/apps/atril.*
%{_mandir}/man1/atril.1.*
%{_libexecdir}/atril-convert-metadata
%{_libexecdir}/atrild
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
%{_datadir}/MateConf/gsettings/atril.convert

%files libs
%doc README COPYING NEWS AUTHORS
%{_libdir}/libatrilview.so.*
%{_libdir}/libatrildocument.so.*
%dir %{_libdir}/atril
%dir %{_libdir}/atril/3
%dir %{_libdir}/atril/3/backends
%{_libdir}/atril/3/backends/libpdfdocument.so
%{_libdir}/atril/3/backends/pdfdocument.atril-backend
%{_libdir}/atril/3/backends/libpsdocument.so
%{_libdir}/atril/3/backends/psdocument.atril-backend
%{_libdir}/atril/3/backends/libtiffdocument.so
%{_libdir}/atril/3/backends/tiffdocument.atril-backend
%{_libdir}/atril/3/backends/libcomicsdocument.so
%{_libdir}/atril/3/backends/comicsdocument.atril-backend
%{_libdir}/girepository-1.0/AtrilDocument-2.32.typelib
%{_libdir}/girepository-1.0/AtrilView-2.32.typelib
%_datadir/locale/*/*
%{_datadir}/mate/help/atril/*
%{_datadir}/omf/atril/*

%files devel
%dir %{_includedir}/atril
%{_includedir}/atril/2.32
%{_libdir}/libatrilview.so
%{_libdir}/libatrildocument.so
%{_libdir}/pkgconfig/atril-view-2.32.pc
%{_libdir}/pkgconfig/atril-document-2.32.pc
%{_datadir}/gir-1.0/AtrilDocument-2.32.gir
%{_datadir}/gir-1.0/AtrilView-2.32.gir

%files dvi
%{_libdir}/atril/3/backends/libdvidocument.so*
%{_libdir}/atril/3/backends/dvidocument.atril-backend

%files djvu
%{_libdir}/atril/3/backends/libdjvudocument.so
%{_libdir}/atril/3/backends/djvudocument.atril-backend

%files caja
%{_libdir}/caja/extensions-2.0/libatril-properties-page.so

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

