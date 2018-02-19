# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtk-update-icon-cache /usr/bin/gtkdocize /usr/bin/perl5 /usr/bin/update-mime-database libICE-devel libgio-devel libgtk+3-gir-devel pkgconfig(gail-3.0) pkgconfig(glib-2.0) pkgconfig(gmodule-2.0) pkgconfig(gthread-2.0) pkgconfig(gtk+-3.0) pkgconfig(pango) xorg-xproto-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%define oldname caja
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%oldname and %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name caja
%define version 1.20.0
# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.20

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
%if 0%{?rel_build}
Release:     alt1_3
%else
Release:     alt1_3
%endif
License:     GPLv2+ and LGPLv2+
Group:       Graphical desktop/MATE
URL:         http://mate-desktop.org

# for downloading the tarball use 'spectool -g -R caja.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/%{branch}/%{oldname}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{oldname}/snapshot/%{oldname}-%{commit}.tar.xz#/%{git_tar}}

Patch1:      caja_add-xfce-to-desktop-file.patch
# https://github.com/mate-desktop/caja/pull/917
Patch2:      caja_0001-fix-backgrounds-and-emblems-dialog-content-rendering.patch

BuildRequires:  libdbus-glib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libexempi-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libcairo-gobject-devel
BuildRequires:  libexif-devel
BuildRequires:  libselinux-devel
BuildRequires:  libSM-devel
BuildRequires:  libxml2-devel
BuildRequires:  mate-common
BuildRequires:  mate-desktop-devel
BuildRequires:  libpangox-compat-devel
BuildRequires:  libstartup-notification-devel
BuildRequires:  libnotify-devel libnotify-gir-devel

Requires:   libgamin libgamin-fam
Requires:   filesystem
Requires:   altlinux-freedesktop-menu-common
Requires:   gvfs

# the main binary links against libcaja-extension.so
# don't depend on soname, rather on exact version
Requires:       mate-file-manager-extensions = %{version}-%{release}

# needed for using mate-text-editor as stanalone in another DE
Requires:       mate-file-manager-schemas = %{version}-%{release}
Source44: import.info
Patch33: mate-file-manager-1.9.0-alt-fix-linkage.patch
Patch34: mate-file-manager-1.9.0-umountfstab.patch
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
Requires: %{name} = %{version}-%{release}

%description extensions
This package provides the libraries used by caja extensions.

# needed for using mate-text-editor (pluma) as stanalone in another DE
%package schemas
Group: Development/C
Summary:  Mate-file-manager schemas
License:  LGPLv2+

%description schemas
This package provides the gsettings schemas for caja.

%package devel
Group: Development/C
Summary:  Support for developing mate-file-manager extensions
Requires: %{name} = %{version}-%{release}

%description devel
This package provides libraries and header files needed
for developing caja extensions.


%prep
%if 0%{?rel_build}
%setup -n %{oldname}-%{version} -q
%patch1 -p1
%patch2 -p1
%else
%setup -q -n %{oldname}-%{commit}
%patch1 -p1
%patch2 -p1
%endif

# disable startup notification
sed -i s/StartupNotify=true/StartupNotify=false/g data/caja-computer.desktop.in.in
sed -i s/StartupNotify=true/StartupNotify=false/g data/caja-home.desktop.in.in

%if 0%{?rel_build}
%patch33 -p1
%patch35 -p1
NOCONFIGURE=1 ./autogen.sh
%else # 0%{?rel_build}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}
%patch34 -p1

%build
%configure \
        --disable-static \
        --disable-schemas-compile \
        --disable-update-mimedb

#drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

%make_build V=1

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

# Avoid prelink to mess with caja - rhbz (#1228874)
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/prelink.conf.d
cat << EOF > ${RPM_BUILD_ROOT}%{_sysconfdir}/prelink.conf.d/caja.conf
-b %{_libdir}/caja/
-b %{_libdir}/libcaja-extension.so.*
-b %{_libexecdir}/caja-convert-metadata
-b %{_bindir}/caja
-b %{_bindir}/caja-autorun-software
-b %{_bindir}/caja-connect-server
-b %{_bindir}/caja-file-management-properties
EOF

%find_lang %{oldname} --with-gnome --all-name


%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/*
%{_datadir}/caja
%{_libdir}/caja/
%{_sysconfdir}/prelink.conf.d/caja.conf
%{_datadir}/pixmaps/caja/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/caja.*
%{_datadir}/icons/hicolor/*/emblems/emblem-note.png
%{_mandir}/man1/*
%{_datadir}/appdata/caja.appdata.xml
%{_datadir}/mime/packages/caja.xml
%{_datadir}/dbus-1/services/org.mate.freedesktop.FileManager1.service

%files extensions
%{_libdir}/libcaja-extension.so.*
%{_libdir}/girepository-1.0/*.typelib

%files schemas -f %{oldname}.lang
%{_datadir}/glib-2.0/schemas/org.mate.*.gschema.xml

%files devel
%{_includedir}/caja/
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libcaja-extension


%changelog
* Tue Feb 20 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.20.0-alt1_3
- new fc release

* Mon Oct 16 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.2-alt1_1
- new fc release

* Wed Sep 13 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.1-alt1_2
- new fc release

* Thu Sep 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.19.0-alt1_4
- new fc release

* Wed Oct 26 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.1-alt1_1
- new fc release

* Thu Oct 06 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.16.0-alt1_1
- update to mate 1.16

* Tue Apr 05 2016 Igor Vlasenko <viy@altlinux.ru> 1.12.4-alt1_1
- converted for ALT Linux by srpmconvert tools

* Mon Nov 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.4-alt2_1
- fixed dependencies

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1.10.4-alt1_1
- new version

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

