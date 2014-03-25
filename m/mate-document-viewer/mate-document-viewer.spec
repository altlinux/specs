%define _unpackaged_files_terminate_build 1
Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize gcc-c++ libICE-devel libgdk-pixbuf-gir-devel libgio-devel libgtk+2-gir-devel pkgconfig(cairo) pkgconfig(cairo-pdf) pkgconfig(cairo-ps) pkgconfig(gail) pkgconfig(gail-3.0) pkgconfig(gio-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtk+-unix-print-2.0) pkgconfig(gtk+-unix-print-3.0) pkgconfig(gtk+-x11-2.0) pkgconfig(gtk+-x11-3.0) pkgconfig(libxml-2.0) pkgconfig(sm) pkgconfig(x11) pkgconfig(libsecret-1) pkgconfig(zlib) zlib-devel
# END SourceDeps(oneline)
## important!!! # https://bugzilla.altlinux.org/show_bug.cgi?id=28634
Requires: mate-desktop
%define _libexecdir %_prefix/libexec
%define oldname atril
%define apiversion 1.5.0

Name:           mate-document-viewer
Version:        1.8.0
Release:        alt2_0
Summary:        Document viewer
License:        GPLv2+ and LGPLv2+ and MIT
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.8/atril-%{version}.tar.xz
# fix rhbz (#999912)
Patch1:         atril_djvu-fix-case-sensitive-search.patch

BuildRequires:  gtk2-devel
BuildRequires:  libpoppler-glib-devel
BuildRequires:  libXt-devel
BuildRequires:  libsecret-devel
BuildRequires:  libglade2-devel
BuildRequires: libtiffxx-devel libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libspectre-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mate-icon-theme-devel
BuildRequires:  t1lib-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  mate-common
BuildRequires:  libcairo-gobject-devel
BuildRequires:  yelp-tools

# for the xps back-end
BuildRequires:  libgxps-devel
# for the caja properties page
BuildRequires:  mate-file-manager-devel
# for the dvi back-end
BuildRequires:  libkpathsea-devel
# for the djvu back-end
BuildRequires:  libdjvu-devel

Requires: %{name}-libs = %{version}-%{release}
#  fix (#974791)
Requires:       libmate-desktop
Patch33: mate-document-viewer-1.4.0-alt-link.patch
Patch34: evince-2.32.0-alt.patch

%description
Mate-document-viewer is simple document viewer.
It can display and print Portable Document Format (PDF),
PostScript (PS), Encapsulated PostScript (EPS), DVI, DJVU and XPS files.
When supported by the document format, mate-document-viewer
allows searching for text, copying text to the clipboard,
hypertext navigation, table-of-contents bookmarks and editing of forms.

Support for document formats such as DVI and DJVU can be added by
installing additional backends.


%package libs
Group: System/Libraries
Summary: Libraries for the mate-document-viewer

%description libs
This package contains shared libraries needed for mate-document-viewer.


%package devel
Group: Development/C
Summary: Support for developing back-ends for the mate-document-viewer
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
mate-document-viewer back-ends development.


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

%package pixbuf
Summary: Atril backend for graphics files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description pixbuf
This package contains a backend to let evince display graphics files.

%package xps
Summary: Atril backend for xps files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description xps
This package contains a backend to let evince display xps files.

%package impress
Summary: Atril backend for impress files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description impress
This package contains a backend to let evince display impress files.

%package caja
Group: Graphical desktop/MATE
Summary: Mate-document-viewer extension for caja
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: mate-file-manager

%description caja
This package contains the mate-document-viewer extension for the
caja file manager.
It adds an additional tab called "Document" to the file properties dialog.

%prep
%setup -n atril-%{version} -q

%patch1 -p1 -b .djvu
%patch33 -p0
%patch34 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
        --disable-static \
        --disable-schemas-compile \
        --enable-introspection \
        --enable-comics \
        --enable-dvi=yes \
        --enable-djvu=yes \
        --enable-t1lib=yes \
	--enable-pixbuf=yes \
	--enable-xps=yes \
        --with-gtk=2.0 \
        --enable-thumbnailer
# broken
#	--enable-impress=yes \

make %{?_smp_mflags} V=1 LIBTOOL=/usr/bin/libtool

%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang atril

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'
find $RPM_BUILD_ROOT%_libdir -name '*.a' -exec rm -fv {} ';'

# remove of gsetting,convert file, no need for this in fedora
# because MATE starts with gsetting in fedora.
rm -fv $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/atril.convert

# don't ship icon caches
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache


%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/atril.desktop


%files -f atril.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/*
%dir %{_datadir}/atril
%{_datadir}/atril/*
%{_datadir}/applications/atril.desktop
%{_datadir}/icons/hicolor/*/apps/atril.*
%{_libexecdir}/atril-convert-metadata
%{_libexecdir}/atrild
%{_datadir}/dbus-1/services/org.mate.atril.Daemon.service
%{_datadir}/glib-2.0/schemas/org.mate.Atril.gschema.xml
%{_datadir}/thumbnailers/atril.thumbnailer
%dir %{_datadir}/gtk-doc/html
%dir %{_datadir}/gtk-doc/html/atril
%{_datadir}/gtk-doc/html/*
%{_mandir}/man1/atril-*.1.*
%{_mandir}/man1/atril.1.*
#### TODO: LANG!!!
%{_datadir}/help/*/atril

%files libs
%{_libdir}/libatrilview.so.*
%{_libdir}/libatrildocument.so.*
%dir %{_libdir}/atril/
%dir %{_libdir}/atril/3/
%dir %{_libdir}/atril/3/backends/
%{_libdir}/atril/3/backends/libpdfdocument.so
%{_libdir}/atril/3/backends/pdfdocument.atril-backend
%{_libdir}/atril/3/backends/libpsdocument.so
%{_libdir}/atril/3/backends/psdocument.atril-backend
%{_libdir}/atril/3/backends/libtiffdocument.so
%{_libdir}/atril/3/backends/tiffdocument.atril-backend
%{_libdir}/atril/3/backends/libcomicsdocument.so
%{_libdir}/atril/3/backends/comicsdocument.atril-backend
%{_libdir}/girepository-1.0/AtrilDocument-*.typelib
%{_libdir}/girepository-1.0/AtrilView-*.typelib

%files caja
%{_libdir}/caja/extensions-2.0/libatril-properties-page.so

%files devel
%dir %{_includedir}/atril/
%{_includedir}/atril/%apiversion
%{_libdir}/libatrilview.so
%{_libdir}/libatrildocument.so
%{_libdir}/pkgconfig/atril-view-*.pc
%{_libdir}/pkgconfig/atril-document-*.pc
%{_datadir}/gir-1.0/AtrilDocument-*.gir
%{_datadir}/gir-1.0/AtrilView-*.gir

%files dvi
%{_libdir}/atril/3/backends/libdvidocument.so*
%{_libdir}/atril/3/backends/dvidocument.atril-backend

%files djvu
%{_libdir}/atril/3/backends/libdjvudocument.so
%{_libdir}/atril/3/backends/djvudocument.atril-backend

%files xps
%{_libdir}/atril/3/backends/libxpsdocument.so*
%{_libdir}/atril/3/backends/xpsdocument.atril-backend

%files pixbuf
%{_libdir}/atril/3/backends/libpixbufdocument.so*
%{_libdir}/atril/3/backends/pixbufdocument.atril-backend

#%files impress
#%{_libdir}/atril/3/backends/libimpressdocument.so*
#%{_libdir}/atril/3/backends/impressdocument.atril-backend

%changelog
* Tue Mar 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt2_0
- added patch1

* Sun Mar 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new version

* Sun Aug 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_0
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.0-alt1_0.qa1
- NMU: rebuilt with libarchive.so.13.

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_0
- new version

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3_0
- added Req: mate-desktop (closes: 28634)

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
dropped obsolete mate-conf BR:

* Sun Feb 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Tue Nov 20 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1.1.1
- fixed build

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted alt patches

* Mon Aug 06 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

