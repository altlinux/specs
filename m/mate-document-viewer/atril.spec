Group: Publishing
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/glib-mkenums /usr/bin/gtkdocize gcc-c++ libICE-devel libgio-devel pkgconfig(cairo) pkgconfig(cairo-pdf) pkgconfig(cairo-ps) pkgconfig(ddjvuapi) pkgconfig(gail) pkgconfig(gail-3.0) pkgconfig(gio-2.0) pkgconfig(gmodule-2.0) pkgconfig(gobject-introspection-1.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(gtk+-unix-print-2.0) pkgconfig(gtk+-unix-print-3.0) pkgconfig(gtk+-x11-2.0) pkgconfig(gtk+-x11-3.0) pkgconfig(libcaja-extension) pkgconfig(libgxps) pkgconfig(libsecret-1) pkgconfig(libspectre) pkgconfig(libxml-2.0) pkgconfig(mate-desktop-2.0) pkgconfig(poppler-glib) pkgconfig(sm) pkgconfig(webkit-1.0) pkgconfig(webkit2gtk-4.0) pkgconfig(x11) pkgconfig(zlib) t1lib-devel zlib-devel
# END SourceDeps(oneline)
## important!!! # https://bugzilla.altlinux.org/show_bug.cgi?id=28634
Requires: mate-desktop
%define _libexecdir %_prefix/libexec
%define oldname atril
%define fedora 22
# %%oldname or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name atril
%define version 1.12.2
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.12

# Settings used for build from snapshots.
%{!?rel_build:%global commit 5bba3723566489763aafaad3669c77f60a23d2e0}
%{!?rel_build:%global commit_date 20140122}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:          mate-document-viewer
Version:       %{branch}.2
%if 0%{?rel_build}
Release:       alt1_1
%else
Release:       alt1_1
%endif
Summary:       Document viewer
License:       GPLv2+ and LGPLv2+ and MIT
URL:           http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  gtk2-devel
BuildRequires:  libpoppler-glib-devel
BuildRequires:  libXt-devel
BuildRequires:  libsecret-devel
BuildRequires:  libglade2-devel
BuildRequires: libtiffxx-devel libtiff-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libspectre-devel
BuildRequires:  desktop-file-utils
BuildRequires:  mate-desktop-devel
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
# for epub back-end
BuildRequires:  webkitgtk-devel

Requires:       mate-document-viewer-libs = %{version}-%{release}
#  fix (#974791)
Requires:       libmate-desktop
Requires:       mathjax

%if 0%{?fedora} && 0%{?fedora} <= 24
Provides: mate-document-viewe%{?_isa} = %{version}-%{release}
Provides: mate-document-viewer = %{version}-%{release}
Obsoletes: mate-document-viewer < %{version}-%{release}
%endif
Source44: import.info
Patch33: mate-document-viewer-1.4.0-alt-link.patch
Patch34: evince-2.32.0-alt.patch

%description
Mate-document-viewer is simple document viewer.
It can display and print Portable Document Format (PDF),
PostScript (PS), Encapsulated PostScript (EPS), DVI, DJVU, epub and XPS files.
When supported by the document format, mate-document-viewer
allows searching for text, copying text to the clipboard,
hypertext navigation, table-of-contents bookmarks and editing of forms.


%package -n mate-document-viewer-libs
Group: System/Libraries
Summary: Libraries for the mate-document-viewer
%if 0%{?fedora} && 0%{?fedora} <= 24
Provides: mate-document-viewer-libs%{?_isa} = %{version}-%{release}
Provides: mate-document-viewer-libs = %{version}-%{release}
Obsoletes: mate-document-viewer-libs < %{version}-%{release}
%endif

%description -n mate-document-viewer-libs
This package contains shared libraries needed for mate-document-viewer.


%package devel
Group: Development/C
Summary: Support for developing back-ends for the mate-document-viewer
Requires: mate-document-viewer-libs = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} <= 24
Provides: mate-document-viewer-devel%{?_isa} = %{version}-%{release}
Provides: mate-document-viewer-devel = %{version}-%{release}
Obsoletes: mate-document-viewer-devel < %{version}-%{release}
%endif

%description devel
This package contains libraries and header files needed for
mate-document-viewer back-ends development.

%package dvi
Summary: Atril backend for dvi files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description dvi
This package contains a backend to let atril display dvi files.

%package djvu
Summary: Atril backend for djvu files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description djvu
This package contains a backend to let atril display djvu files.

%package pixbuf
Summary: Atril backend for graphics files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description pixbuf
This package contains a backend to let atril display graphics files.

%package xps
Summary: Atril backend for xps files
Group: Publishing
Requires: %{name}-libs = %{version}-%{release}

%description xps
This package contains a backend to let atril display xps files.

%package caja
Group: Graphical desktop/MATE
Summary: Mate-document-viewer extension for caja
Requires: mate-document-viewer = %{version}-%{release}
Requires: mate-file-manager
%if 0%{?fedora} && 0%{?fedora} <= 24
Provides: mate-document-viewer-caja%{?_isa} = %{version}-%{release}
Provides: mate-document-viewer-caja = %{version}-%{release}
Obsoletes: mate-document-viewer-caja < %{version}-%{release}
%endif

%description caja
This package contains the mate-document-viewer extension for the
caja file manager.
It adds an additional tab called "Document" to the file properties dialog.

%package thumbnailer
Group: Publishing
Summary: Atril thumbnailer extension for caja
Requires: mate-document-viewer = %{version}-%{release}
Requires: mate-file-manager
BuildArch: noarch

%description thumbnailer
This package contains the atril extension for the
caja file manager.


%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}

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
        --enable-t1lib=no \
        --enable-pixbuf \
        --enable-xps \
        --with-gtk=2.0 \
        --enable-epub

# remove unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{makeinstall_std}

%find_lang %{oldname} --with-gnome --all-name

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'

# remove of gsetting,convert file, no need for this in fedora
# because MATE starts with gsetting in fedora.
rm -fv $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/atril.convert


%check
desktop-file-validate ${RPM_BUILD_ROOT}%{_datadir}/applications/atril.desktop


%post
/bin/touch --no-create %{_datadir}%{oldname}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ]; then

  /bin/touch --no-create %{_datadir}%{oldname}/icons/hicolor &>/dev/null



fi

%files -f %{oldname}.lang
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
%{_datadir}/appdata/atril.appdata.xml
%{_mandir}/man1/atril-*.1.*
%{_mandir}/man1/atril.1.*

%files -n mate-document-viewer-libs
%{_libdir}/libatrilview.so.*
%{_libdir}/libatrildocument.so.*
%{_libdir}/atril/3/backends/
%{_libdir}/girepository-1.0/AtrilDocument-1.5.0.typelib
%{_libdir}/girepository-1.0/AtrilView-1.5.0.typelib

%exclude %{_libdir}/atril/3/backends/libdvidocument.so*
%exclude %{_libdir}/atril/3/backends/dvidocument.atril-backend
%exclude %{_libdir}/atril/3/backends/libdjvudocument.so
%exclude %{_libdir}/atril/3/backends/djvudocument.atril-backend
%exclude %{_libdir}/atril/3/backends/libxpsdocument.so*
%exclude %{_libdir}/atril/3/backends/xpsdocument.atril-backend
%exclude %{_libdir}/atril/3/backends/libpixbufdocument.so*
%exclude %{_libdir}/atril/3/backends/pixbufdocument.atril-backend

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

%files caja
%{_libdir}/caja/extensions-2.0/libatril-properties-page.so
%{_datadir}/caja/extensions/libatril-properties-page.caja-extension

%files thumbnailer
%{_datadir}/thumbnailers/atril.thumbnailer

%files devel
%dir %{_includedir}/atril/
%{_includedir}/atril/1.5.0/
%{_libdir}/libatrilview.so
%{_libdir}/libatrildocument.so
%{_libdir}/pkgconfig/atril-view-1.5.0.pc
%{_libdir}/pkgconfig/atril-document-1.5.0.pc
%{_datadir}/gir-1.0/AtrilDocument-1.5.0.gir
%{_datadir}/gir-1.0/AtrilView-1.5.0.gir
%{_datadir}/gtk-doc/html/libatrildocument-1.5.0/
%{_datadir}/gtk-doc/html/libatrilview-1.5.0/
%{_datadir}/gtk-doc/html/atril/


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.2-alt1_1
- new version

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

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

