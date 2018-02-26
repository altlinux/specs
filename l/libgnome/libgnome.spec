%define ver_major 2.32
%def_disable static
%def_disable gtk_doc
# from gnome package
%define default_gnome_theme_name Glossy

Name: libgnome
Version: %ver_major.1
Release: alt1

Summary: GNOME base library
License: LGPLv2
Group: System/Libraries
Url: ftp://ftp.gnome.org

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2
Source1: gnome-menu.svg
Source2: gnome-button.png
Source3: desktop_gnome_peripherals_monitor.schemas

# Play system sounds by default
Patch: %name-2.22.0-alt-default_sound_settings.patch
# settings from package gnome-settings
Patch1: libgnome-alt-settings.patch
# have icons in menu and on buttons by default
Patch2: libgnome-2.28.0-alt-default-interface.patch

Patch3: libgnome-2.11.1-scoreloc.patch
# backport from upstream svn 
Patch9: libgnome-im-setting.patch
# from gnome-minimal package
Patch10: libgnome-2.22.0-alt-default_gtk_theme.patch

Patch11: libgnome-2.22.0-alt-default_browser.patch 

Obsoletes: %name-utils
Provides: %name-utils = %version-%release


# From configure.in
%define GConf_ver 2.21.90
%define glib_ver 2.8.0
%define gio_ver 2.16.0
%define gnome_vfs_ver 2.5.3
%define libbonobo_ver 2.13.0
%define gtk_doc_ver 1.0
%define intltool_ver 0.40.0
%define gnome_common_ver 2.8.0
%define gnome_settings_ver 2.6.0

Requires: gnome-audio
PreReq: GConf >= %GConf_ver
Conflicts: gnome-settings

BuildPreReq: rpm-build-gnome

# From configure.in
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %gio_ver
BuildPreReq: gnome-vfs-devel >= %gnome_vfs_ver
BuildPreReq: libbonobo-devel >= %libbonobo_ver
BuildPreReq: libGConf-devel >= %GConf_ver
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: gnome-common >= %gnome_common_ver
BuildPreReq: gtk-doc >= %gtk_doc_ver

BuildRequires: libcanberra-gtk2-devel libpopt-devel

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME. The libgnomeui
package contains X11-dependent GNOME library features.

%package devel
Summary: Libraries and headers for libgnome
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome-devel package
includes the libraries and include files that you will need to
use libgnome.

You should install the libgnome-devel package if you would like to
compile GNOME applications. You do not need to install libgnome-devel
if you just want to use the GNOME desktop environment.

%package devel-doc
Summary: Development documentation for %name
Group: Development/GNOME and GTK+
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
GNOME (GNU Network Object Model Environment) is a user-friendly set of
GUI applications and desktop tools to be used in conjunction with a
window manager for the X Window System. The libgnome package includes
non-GUI-related libraries that are needed to run GNOME.

This package provides development documentation for %name.

%package devel-static
Summary: Static libraries and objects for gnome libs
Group: Development/GNOME and GTK+
Requires: %name-devel = %version-%release

%description devel-static
Static libraries and objects for gnome library infrastructure

%define _gtk_docdir %_datadir/gtk-doc/html
# This is for gnome-open to land in %_bindir
%define _libexecdir %_bindir

%prep
%setup -q
%patch
%patch1 -p1
%patch2
%patch3 -p1 -b .scoreloc
%patch9 -p1 -b .im-setting
%patch10 -p1
%patch11 -p1

%build
%autoreconf
%configure \
    %{subst_enable static} \
    --disable-esd \
    --disable-schemas-install \
    %{?_enable_gtk_doc:--enable-gtk-doc} 

%make_build

%install

%make_install DESTDIR=%buildroot install

install -pD -m644 %SOURCE1 %buildroot%_datadir/pixmaps/gnome-menu.svg
install -m644 %SOURCE2 %buildroot%_datadir/pixmaps/gnome-menu.png
install -m644 %SOURCE3 %buildroot%_sysconfdir/gconf/schemas/

bzip2 -9fk ChangeLog

%find_lang --with-gnome --output=files_list %name-2.0

%define schemas desktop_gnome_accessibility_keyboard desktop_gnome_accessibility_startup desktop_gnome_applications_at_mobility desktop_gnome_applications_at_visual desktop_gnome_applications_browser desktop_gnome_applications_office desktop_gnome_applications_terminal desktop_gnome_applications_window_manager desktop_gnome_background desktop_gnome_file_views desktop_gnome_interface desktop_gnome_lockdown desktop_gnome_peripherals_keyboard desktop_gnome_peripherals_monitor desktop_gnome_peripherals_mouse desktop_gnome_sound desktop_gnome_thumbnail_cache desktop_gnome_thumbnailers desktop_gnome_typing_break

for s in %schemas; do
    echo "%%config %gconf_schemasdir/$s.schemas"
done >>files_list

%post
%gconf2_install %schemas

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %schemas
fi

%files -f files_list
%_bindir/*
%_libdir/*.so.*
%_libdir/bonobo/monikers/*.so
%bonobo_serversdir/*.server
%dir %_sysconfdir/sound
%dir %_sysconfdir/sound/events
%_datadir/pixmaps/*
%_datadir/gnome-background-properties/gnome-default.xml
%_man7dir/*
%config %_sysconfdir/sound/events/*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc NEWS ChangeLog*

%files devel-doc
%_gtk_docdir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%_libdir/bonobo/*/*.a
%endif

%exclude %_libdir/bonobo/monikers/*.la

%changelog
* Mon Jan 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Fri Nov 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt2
- rebuild for update dependencies

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0
- useless esd disbled
- updated buildreqs
- spec cleanup

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- enabled icons in menu and on buttons by default (Patch2)

* Wed Sep 23 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Fri Mar 06 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.1-alt1
- 2.25.1
- removed obsolete %%post{,un}_ldconfig

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.24.1-alt1
- 2.24.1
- build devel-doc as noarch

* Wed Aug 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt5
- requires gnome-audio
- set default gtk theme to Glossy (patch10)
- change default browser to epiphany (patch11)
- don't rebuild documentation

* Thu Jul 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.0-alt4
- enable esd to hear system sounds
- play system sounds by default (patch0)

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt3
- new GNOME components need new GConf(#13999)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- moved settings from post-scripts of gnome-settings package to patch1
- fix RH #64908 - patch2 (scoreloc)

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- new version (2.22.0)
- remove patch10 for make gio the default filechooser backend (fixed upstream)

* Tue Mar 04 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.90-alt1
- new version (2.21.90)
- update schemas
- add schema peripherals_monitor(SOURCE3)
- add schema for gtk-im-module GConf key (patch9)
- add patch10 for make gio the default filechooser backend, but don't enable

* Fri Sep 21 2007 Igor Zubkov <icesik@altlinux.org> 2.20.0-alt1
- 2.18.0 -> 2.20.0

* Mon May 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.0-alt1
- new version (2.18.0)

* Sun Sep 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version (2.16.0)

* Sun Aug 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.2-alt1
- new version (2.15.2)
- updated buildreqs
- no Debian menu items
- spec cleanup

* Sun Apr 30 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt2
- fixed bug #9470.

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Fri Mar 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version (2.14.0)

* Mon Mar 06 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.7-alt2
- removed gnome-settings from Requires list (Bug #4130).

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.7-alt1
- new version

* Wed Nov 16 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version
- removed excess buildreqs.

* Sat Sep 10 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0.1-alt1
- 2.12.0
- Removed excess buildreqs.

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.3-alt1
- 2.11.3

* Wed Jul 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.2-alt1
- 2.9.2

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.1-alt1
- 2.9.1.
- development documentation moved to devel-doc subpackage.

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Tue Sep 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1.1-alt1
- 2.6.1.1

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Sun Mar 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.92.1-alt1
- 2.5.92.1

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt2
- do not package .la files.
- do not build devel-static subpackage by default.
- %%_sysconfdir/sound/events owned by libgnome.

* Mon Sep 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6-alt1
- 2.3.6
- remove utils package, help converters in yelp now.

* Tue Jul 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt2
- remove %%preun with %%gconf2_uninstall.

* Sat Jul 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt1
- 2.3.3.1

* Thu Jul 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt2
- remove old dependencies on bonobo-activation.
- %%gconf2_uninstall run in %%preun.

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Sat Mar 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Jan 23 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Wed Jan 22 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Wed Jan 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90-alt1
- 2.1.90

* Mon Dec 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Fri Nov 01 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.0-alt3
- ressurected desktop_gnome_background.schemas. now we are using gconf2_set

* Tue Oct 08 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.0-alt2
- /etc/gconf/schemas/desktop_gnome_background.schema
  moved to gnome-settings package
  now we have all design in the separate package.

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Sun Sep 15 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Mon Jun 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- 2.0.1.
- build process fixed (SMP compatible build)
- ldconfig run in post{,un}.
- Buildprereq list fixed.
- updated buildrequires.
- other small fixes and cleanups.
- (inger)fixed wrong requires

* Wed Jun 05 2002 Igor Androsov <blake@altlinux.ru> 1.117.2-alt1
- New version
- Initial build for AltLinux

* Fri May 24 2002 Igor Androsov <blace@mail.ru> 1.117.1-blk1
- New version

* Wed May 15 2002 Igor Androsov <blace@mail.ru> 1.117.0-blk0.1
- New version from CVS

* Sat May 11 2002 Igor Androsov <blace@mail.ru> 1.116.0-blk0.1
- New version from CVS

* Mon Feb 25 2002 Gregory Leblanc <gleblanc@linuxweasel.com> 1.112.0-1
- new version

