# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache /usr/bin/gtkdocize /usr/bin/perl5 /usr/bin/pkg-config /usr/bin/update-mime-database libICE-devel libX11-devel libXrender-devel libgio-devel libgtk+2-gir-devel libgtk+3-gir-devel pkgconfig(gail) pkgconfig(gail-3.0) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pango) pkgconfig(unique-3.0) xorg-xproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja
%define fedora 21
# %oldname or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name caja
%define version 1.8.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.8

# Settings used for build from snapshots.
%{!?rel_build:%global commit ee0a62c8759040d84055425954de1f860bac8652}
%{!?rel_build:%global commit_date 20140223}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{oldname}-%{version}-%{git_ver}.tar.xz}

Name:        mate-file-manager
Summary:     File manager for MATE
Version:     %{branch}.0
Release:     alt1_2
#Release:     0.1%{?git_rel}%{?dist}
License:     GPLv2+ and LGPLv2+
Group:       Graphical desktop/Other
URL:         http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

# upstream patches
# fix https://github.com/mate-desktop/mate-file-manager/issues/122
# http://git.mate-desktop.org/caja/commit/?id=910b9141ac634a86d8f53fda534e33787a160efb
Patch1:    caja_allow-dropping-files-to-bookmarks.patch
# http://git.mate-desktop.org/caja/commit/?id=60d4f83b0fab7633e73e8f4689f4c6931927c2ba
Patch2:    caja_rearranged-caja-sidebar-to-1.4-style.patch
# http://git.mate-desktop.org/caja/commit/?id=4f1e756e08e61840eb9a52de4debee30006ea31e
Patch3:    caja_x-caja-windows-fix.patch
# http://git.mate-desktop.org/caja/commit/?id=06264fc91212150d3b741a723422955e7e97614c
Patch4:    caja_remove-ck-usage.patch

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libexempi-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libexif-devel
BuildRequires:  libselinux-devel
BuildRequires:  libSM-devel
BuildRequires:  libxml2-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  libpangox-compat-devel
BuildRequires:  libstartup-notification-devel
BuildRequires:  libunique-devel

Requires:   gamin
Requires:   filesystem
Requires:   altlinux-freedesktop-menu-common
Requires:   gvfs

# the main binary links against libcaja-extension.so
# don't depend on soname, rather on exact version
Requires:       mate-file-manager-extensions = %{version}-%{release}

# needed for using mate-text-editor as stanalone in another DE
Requires:       mate-file-manager-schemas = %{version}-%{release}

%if 0%{?fedora} && 0%{?fedora} > 20
Provides: mate-file-manager%{?_isa} = %{version}-%{release}
Provides: mate-file-manager = %{version}-%{release}
Obsoletes: mate-file-manager < %{version}-%{release}
%endif
Source44: import.info
Patch33: mate-file-manager-1.2.2-alt-fix-linkage.patch
Patch34: nautilus-2.22.1-umountfstab.patch
Patch35: mate-file-manager-1.5.5-alt-desktop-labels-po-ru.patch

%description
Caja (mate-file-manager) is the file manager and graphical shell
for the MATE desktop,
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote file systems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the MATE desktop.

%package extensions
Group: Development/C
Summary:  Mate-file-manager extensions library
Requires: mate-file-manager = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} > 20
Provides: mate-file-manager-extensions%{?_isa} = %{version}-%{release}
Provides: mate-file-manager-extensions = %{version}-%{release}
Obsoletes: mate-file-manager-extensions < %{version}-%{release}
%endif

%description extensions
This package provides the libraries used by caja extensions.

# needed for using mate-text-editor (pluma) as stanalone in another DE
%package schemas
Group: Development/C
Summary:  Mate-file-manager schemas
License:  LGPLv2+
%if 0%{?fedora} && 0%{?fedora} > 20
Provides: mate-file-manager-schemas%{?_isa} = %{version}-%{release}
Provides: mate-file-manager-schemas = %{version}-%{release}
Obsoletes: mate-file-manager-schemas < %{version}-%{release}
%endif

%description schemas
This package provides the gsettings schemas for caja.

%package devel
Group: Development/C
Summary:  Support for developing mate-file-manager extensions
Requires: mate-file-manager = %{version}-%{release}
%if 0%{?fedora} && 0%{?fedora} > 20
Provides: mate-file-manager-devel%{?_isa} = %{version}-%{release}
Provides: mate-file-manager-devel = %{version}-%{release}
Obsoletes: mate-file-manager-devel < %{version}-%{release}
%endif

%description devel
This package provides libraries and header files needed
for developing caja extensions.

%prep
%setup -n %{oldname}-%{version} -q%{!?rel_build:n %{oldname}-%{commit}}

%patch1 -p1 -b .bookmarks
%patch2 -p1 -b .1.4-style
%patch3 -p1 -b .x-caja-windows-fix
%patch4 -p1 -b .remove-ck-usage

# needed for git snapshots
%patch33 -p1
%patch35 -p1
#NOCONFIGURE=1 ./autogen.sh

# To work around rpath
autoreconf -fi
%patch34 -p1

%build
%configure \
        --disable-static \
        --enable-unique \
        --disable-schemas-compile \
        --with-x \
        --with-gtk=2.0 \
        --disable-update-mimedb

#drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

make %{?_smp_mflags} V=1

%install
%{makeinstall_std}

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/.icon-theme.cache

mkdir -p $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0

desktop-file-install                              \
    --delete-original                             \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

# remove needless gsettings convert file
rm -f  $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/caja.convert

%find_lang %{oldname}


%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/*
%{_datadir}/caja
%{_libdir}/caja/
%{_datadir}/pixmaps/caja/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/caja.png
%{_datadir}/icons/hicolor/scalable/apps/caja.svg
%{_datadir}/icons/hicolor/*/emblems/emblem-note.png
%{_mandir}/man1/*
%{_libexecdir}/caja-convert-metadata
%{_datadir}/mime/packages/caja.xml
%{_datadir}/dbus-1/services/org.mate.freedesktop.FileManager1.service

%files extensions
%{_datadir}/gtk-doc/html/libcaja-extension
%{_libdir}/libcaja-extension.so.*
%{_libdir}/girepository-1.0/*.typelib

%files schemas -f %{oldname}.lang
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml

%files devel
%{_includedir}/caja/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir


%changelog
* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_1
- new fc release

* Mon Aug 19 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_3
- new fc release

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_2
- new fc release

* Mon Jul 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.2-alt1_1
- new fc release

* Tue Jun 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt2_4
- new fc release

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt2_1
- added 0001-Fix-radio-buttons-and-GSettings-in-preferences-windo.patch

* Mon Apr 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.1-alt1_1
- new fc release

* Sat Apr 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_1
- new fc release

* Thu Mar 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.5-alt1_1
- new fc release

* Tue Mar 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.4-alt1_1
- new fc release

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_1
- new fc release

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.3-alt1_0
- new version

* Tue Dec 04 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.2-alt1_1
- new fc release

* Tue Nov 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.1-alt1_2
- new fc release

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

