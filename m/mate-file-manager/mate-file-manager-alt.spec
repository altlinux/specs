# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/glib-genmarshal /usr/bin/gtkdocize /usr/bin/mateconftool-2 /usr/bin/perl5 /usr/bin/pkg-config /usr/bin/update-mime-database libICE-devel libSM-devel libXrender-devel libgtk+2-gir-devel pkgconfig(gail) pkgconfig(gio-2.0) pkgconfig(gio-unix-2.0) pkgconfig(gtk+-2.0) pkgconfig(gtk+-3.0) pkgconfig(pango) pkgconfig(unique-3.0) xorg-xproto-devel
# END SourceDeps(oneline)
%define gobject_introspection_version 1.0
%define _libexecdir %_prefix/libexec
%define oldname caja
%define glib2_version 2.25.9
%define pango_version 1.1.3
%define gtk2_version 2.21.2
%define mate_icon_theme_version 1.1.0
%define libxml2_version 2.4.20
%define desktop_file_utils_version 0.7
%define mate_desktop_version 1.1.0
%define redhat_menus_version 0.25
%define startup_notification_version 0.5
%define libexif_version 0.5.12
%define mateconf_version 1.1.0
%define exempi_version 1.99.5
%define unique_version 1.0.4

Name:			mate-file-manager
Summary:    	File manager for MATE
Version:		1.4.0
Release:		alt2_1.1
License:		GPLv2+
Group:          Graphical desktop/Other
Source:			http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
URL: 			http://mate-desktop.org
Requires:		gamin
Requires:       filesystem >= 2.1.1-1
Requires:       altlinux-freedesktop-menu-common >= %{redhat_menus_version}
Requires:       gvfs >= 1.4.0
Requires:       mate-icon-theme >= %{mate_icon_theme_version}
Requires:       libexif >= %{libexif_version}

BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	pango-devel >= %{pango_version}
BuildRequires:	gtk2-devel >= %{gtk2_version}
BuildRequires:	libxml2-devel >= %{libxml2_version}
BuildRequires:  mate-desktop-devel >= %{mate_desktop_version}
BuildRequires:	gamin-devel
BuildRequires:	gvfs-devel
BuildRequires:  intltool >= 0.40.6-2
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  fontconfig
BuildRequires:  desktop-file-utils >= %{desktop_file_utils_version}
BuildRequires:  libtool >= 1.4.2-10
BuildRequires:  libstartup-notification-devel >= %{startup_notification_version}
BuildRequires:  libexif-devel >= %{libexif_version}
BuildRequires:  libexempi-devel >= %{exempi_version}
BuildRequires:  gettext
BuildRequires:  libselinux-devel
BuildRequires:  gtk-doc
BuildRequires:  scrollkeeper
BuildRequires:  gobject-introspection-devel >= %{gobject_introspection_version}
BuildRequires:  libunique-devel
BuildRequires:  mate-conf-devel
BuildRequires:  mate-common
BuildRequires:  libcairo-gobject-devel

Requires(pre): mate-conf >= %{mateconf_version}
Requires(preun): mate-conf >= %{mateconf_version}
Requires(post): mate-conf >= %{mateconf_version}
Requires:	mate-desktop >= %{mate_desktop_version}


# the main binary links against libcaja-extension.so
# don't depend on soname, rather on exact version
Requires:	mate-file-manager-extensions = %{version}-%{release}

Obsoletes:      eel2 < 2.26.0-3
Provides:       eel2 = 2.26.0-3

# Some changes to default config
Patch1:         nautilus-config.patch

Patch7:		caja-rtl-fix.patch

Patch10:        nautilus-gvfs-desktop-key-2.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=519743
Patch17:	nautilus-filetype-symlink-fix.patch

Patch26: caja_remove_mate-bg-crossfade.patch
Patch33: mate-file-manager-1.2.2-alt-fix-linkage.patch
Patch34: nautilus-2.22.1-umountfstab.patch


%description
Caja is the file manager and graphical shell for the MATE desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the GNOME desktop.

%package extensions
Summary: Caja extensions library
License: LGPLv2+
Group: Development/C
Requires:   %{name} = %{version}-%{release}

%description extensions
This package provides the libraries used by caja extensions.

%package devel
Summary: Support for developing caja extensions
License: LGPLv2+
Group: Development/C
Requires:   %{name} = %{version}-%{release}
Obsoletes:      eel2-devel < 2.26.0-3
Provides:       eel2-devel = 2.26.0-3

%description devel
This package provides libraries and header files needed
for developing caja extensions.

%prep
%setup -q -n %{name}-%{version}
%patch33 -p1
NOCONFIGURE=1 ./autogen.sh

%patch1 -p1 -b .config
%patch7 -p1 -b .caja-rtl-fix
%patch10 -p1 -b .gvfs-desktop-key
%patch17 -p0 -b .symlink
%patch26 -p1 -b .caja_remove_mate-bg-crossfade
%patch34 -p1

%build

# -fno-tree-vrp is needed to avoid gcc-4.4.0 optimization failure
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=39233
CFLAGS="$RPM_OPT_FLAGS -g -DUGLY_HACK_TO_DETECT_KDE -DCAJA_OMIT_SELF_CHECK -fno-tree-vrp"

%configure \
	--disable-static \
	--enable-unique \
	--enable-introspection \
	--enable-gtk-doc \
	--disable-update-mimedb


# drop unneeded direct library deps with --as-needed
# libtool doesn't make this easy, so we do it the hard way
sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0 /g' libtool

export tagname=CC
LANG=en_US make %{?_smp_mflags}

# strip unneeded translations from .mo files
cd po
grep -v ".*[.]desktop[.]in.*\|.*[.]server[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
for p in *.po; do
  msgmerge $p caja.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done
# refresh the files in ./po after touching POTFILES.in
make

%install
export MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
export tagname=CC
LANG=en_US %makeinstall LIBTOOL=/usr/bin/libtool
unset MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

rm -f $RPM_BUILD_ROOT%{_libdir}/matecomponent/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

rm -f $RPM_BUILD_ROOT%{_libdir}/matecomponent/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/icon-theme.cache
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/.icon-theme.cache

mkdir -p $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/mate
mv -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/* $RPM_BUILD_ROOT%{_datadir}/icons/mate

%find_lang caja

%post
export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
mateconftool-2 --makefile-install-rule %{_sysconfdir}/mateconf/schemas/apps_caja_preferences.schemas > /dev/null || :

touch --no-create %{_datadir}/icons/mate >&/dev/null || :

%pre
if [ "$1" -gt 1 ]; then
    export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/apps_caja_preferences.schemas > /dev/null || :
fi

%preun
if [ "$1" -eq 0 ]; then
    export MATECONF_CONFIG_SOURCE=`mateconftool-2 --get-default-source`
    mateconftool-2 --makefile-uninstall-rule %{_sysconfdir}/mateconf/schemas/apps_caja_preferences.schemas > /dev/null || :
fi

%postun
if [ $1 -eq 0 ]; then
  touch --no-create %{_datadir}/icons/mate >&/dev/null || :
fi


%files  -f caja.lang
%doc AUTHORS COPYING COPYING-DOCS COPYING.LIB NEWS README
%{_datadir}/caja
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_bindir}/*
%{_sysconfdir}/mateconf/schemas/*
%{_datadir}/icons/mate/*/apps/caja.png
%{_datadir}/icons/mate/scalable/apps/caja.svg
%{_mandir}/man1/caja-connect-server.1.*
%{_mandir}/man1/caja-file-management-properties.1.*
%{_mandir}/man1/caja.1.*
%{_libexecdir}/caja-convert-metadata
%{_datadir}/mime/*/*

%files extensions
%{_libdir}/libcaja-extension.so.*
%{_libdir}/girepository-1.0/*.typelib
%dir %{_libdir}/caja
%dir %{_libdir}/caja/extensions-2.0

%files devel
%{_includedir}/caja
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/libcaja-extension/*


%changelog
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

