%define ver_major 3.4
%define api_ver 3.0
%def_disable static
%def_disable gtk_doc
%def_enable introspection

# Whether to build clock applet with evolution-data-server.
%def_enable eds
# This switch controls whether to build some applets as running inside
# gnome-panel process (as for 2.16, these are clock, fish, notification
# area, and window list). Note that if this is on, then a crash of an applet is
# a crash of a panel.
%def_without in_process_applets

Name: gnome-panel
Version: %ver_major.2.1
Release: alt1

Summary: The core programs for the GNOME GUI desktop environment
License: GPLv2+ and LGPLv2+ and GFDL+
Group: Graphical desktop/GNOME
Url: ftp://ftp.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

# https://bugzilla.gnome.org/show_bug.cgi?id=507873
# need  to rework after testing
Patch3: %name-2.9.92-alt-default_setup.patch
Patch5: %name-2.5.93-alt-fish_schemas.patch

# http://bugzilla.gnome.org/show_bug.cgi?id=520111
Patch24: %name-2.21.92-allow-spurious-view-done-signals.patch

# From configure.in
%define gtk_ver 3.3.12
%define desktop_ver 3.3.92
%define libpango_ver 1.15.4
%define glib_ver 2.31.16
%define libwnck_ver 2.91.92
%define GConf_ver 2.6.1
%define gnome_menus_ver 3.3.5
%define eds_ver 2.91.91
%define cairo_ver 1.0
%define tp_glib_ver 0.14
%define gweather_ver 2.91.6
%define nm_ver 0.8.
%define rsvg_ver 2.35.1

Conflicts: gnome-power-manager < 2.15.3

PreReq: GConf >= %GConf_ver
PreReq: librarian
Requires: lib%name = %version-%release

# for Wanda
Requires: fortune-mod
# for clock
Requires: tzdata

BuildPreReq: rpm-build-gnome >= 0.4

# From configure.in
BuildPreReq: gnome-common
BuildPreReq: intltool >= 0.35
BuildPreReq: libgnome-desktop3-devel >= %desktop_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: glib2-devel >= %glib_ver
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libpango-devel >= %libpango_ver
BuildPreReq: libwnck3-devel >= %libwnck_ver
BuildPreReq: libgnome-menus-devel >= %gnome_menus_ver
BuildPreReq: libcairo-devel >= %cairo_ver
BuildPreReq: libtelepathy-glib-devel >= %tp_glib_ver
BuildPreReq: libgweather-devel >= %gweather_ver
%{?_enable_eds:BuildPreReq: evolution-data-server-devel >= %eds_ver}
BuildPreReq: librsvg-devel >= %rsvg_ver
BuildPreReq: libX11-devel libXt-devel libXau-devel libXrandr-devel
BuildPreReq: gtk-doc >= 1.0
BuildPreReq: gnome-doc-utils librarian libxml2-devel
BuildPreReq: NetworkManager-devel >= %nm_ver
BuildRequires: libGConf-devel libdconf-devel libdbus-glib-devel libpolkit-devel libSM-devel perl-XML-Parser
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel libgtk+3-gir-devel libGConf-gir-devel}

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME is based completely on free
software.

The GNOME panel packages provides the gnome panel, menu's and some
basic applets for the panel.

%package -n lib%name
Summary: GNOME panel shared libraries
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
Panel shared libraries for creating GNOME panels.

%package -n lib%name-devel
Summary: GNOME panel libraries, includes, and more
License: LGPLv2+
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
Panel libraries and header files for creating GNOME panels.

%package -n lib%name-devel-static
Summary: GNOME panel static libraries
Group: Development/GNOME and GTK+
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Panel static libraries for creating GNOME panels.

%package -n lib%name-devel-doc
Summary: GNOME Panel development documentation
Group: Development/GNOME and GTK+
Conflicts: lib%name-devel < %version
BuildArch: noarch

%description -n lib%name-devel-doc
Development documentation for Gnome Panel Applet library.

%package -n lib%name-gir
Summary: GObject introspection data for the GNOME panel library
License: LGPLv2+
Group: System/Libraries

%description -n lib%name-gir
GObject introspection data for the GNOME Panel shared library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GNOME panel library
License: LGPLv2+
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GNOME Panel shared library.


%define _gtk_docdir %_datadir/gtk-doc/html
%define _libexecdir %gnome_appletsdir

%prep
%setup -q
#%%patch5 -p1
%patch24 -p1 -b .allow-spurious-view-done-signals

%build
gnome-doc-common --copy
%autoreconf
%configure \
    %{subst_enable static} \
    %{subst_enable eds} \
    %{?_with_in_process_applets:--with-in-process-applets=all} \
    --disable-schemas-compile \
    --disable-scrollkeeper \
    %{?_enable_gtk_doc:--enable-gtk-doc}

# SMP-incompatible build
%make

%install
%make DESTDIR=%buildroot install

%find_lang --with-gnome --output=%name.lang %name %name-%api_ver clock fish fish-applet-2 window-list workspace-switcher

%post
%gconf2_install clock

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall clock
fi

%files -f %name.lang
%_bindir/*
%dir %gnome_appletsdir
%gnome_appletsdir/*
%dir %_datadir/gnome-panel
%_datadir/gnome-panel/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*x*/apps/%{name}*.png
%_iconsdir/hicolor/scalable/apps/%{name}*.svg
%_man1dir/*
%_datadir/dbus-1/services/org.gnome.panel.applet.ClockAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.FishAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.NotificationAreaAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.WnckletFactory.service
%config %_datadir/glib-2.0/schemas/*.xml
%config %_sysconfdir/gconf/schemas/clock.schemas
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_gtk_docdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif

%changelog
* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2.1-alt1
- 3.4.2.1

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Fri Mar 30 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1.1
- enabled eds again

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0
- eds support temporarily disabled

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt2
- used %%autoreconf to fix RPATH problem

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.1-alt1.1
- Rebuild with Python-2.7

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2
- don't requires gnome-menus anymore

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt3
- marked %%_sysconfdir/gconf/schemas/panel-default-setup.entries
  as %%config(noreplace)

* Sat Mar 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- updated buildreqs

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0.2-alt1
- 2.32.0.2

* Tue Sep 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.31.92-alt1
- 2.31.92

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- rebuild against libedataserver-1.2.so.13 (e-d-s-2.30.2)

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Wed Mar 10 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92.1-alt1
- 2.29.92.1

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Thu Feb 25 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91

* Wed Jan 27 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.6-alt1
- 2.29.6
- new devel-doc noarch subpackage

* Thu Jan 14 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5.1-alt1
- 2.29.5.1

* Wed Jan 13 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.5-alt1
- 2.29.5
- removed obsolete gswitchit from panel

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.28.0-alt2.1
- Rebuilt with python 2.6

* Wed Sep 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt2
- updated lost search.patch

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Wed Sep 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.92-alt1
- 2.27.92

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91
- updated buildreqs

* Fri Aug 07 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt2
- add gswitchit on top panel (closes #20991)

* Wed Jul 01 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Wed May 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2

* Wed Apr 15 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Mon Mar 09 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.92-alt1
- 2.25.92

* Sat Jan 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5
- drop upstreamed patches
- updated buildreqs

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Fri Oct 31 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt2
- fix gnome bug #536915 (patch25), requires patched gnome-session
  (2.24.1-alt2)
- fix gnome bug #554343 (patch26)

* Wed Oct 22 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Sun Sep 28 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- drop some old patches
- update patches - 18,19,20
- don't rebuild development documentation

* Sun Jun 08 2008 Alexey Rusakov <ktirf@altlinux.org> 2.22.2-alt2
- Fixed ALT Bug 15952, along with minor spec cleanup.
- Don't leave unbzipped copies of NEWS and ChangeLog.
- Another attempt to build with PolicyKit.

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.2-alt1
- 2.22.2

* Sat May 03 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1.3-alt1
- 2.22.1.3

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.1-alt1
- 2.22.1
- added a patch for a tasklist on vertical panels (GNOME Bug 86382)

* Thu Mar 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt2
- disabled PolicyKit-gnome support
- removed deps gnome-vfs

* Tue Mar 18 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0
- enabled e-d-s support
- enabled PolicyKit-gnome support

* Mon Mar 10 2008 Alexey Shabalin <shaba@altlinux.ru> 2.21.92-alt1
- new version (2.21.92)
- disabled e-d-s support

* Tue Dec 11 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt2
- fix @DATADIR@ in panel-default-setup.entries after patch3

* Tue Dec 04 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.2-alt1
- new version (2.20.2)

* Thu Nov 22 2007 Alexey Shabalin <shaba@altlinux.ru> 2.20.1-alt1
- new version (2.20.1)
- add Packager
- Copy translations for "Suspend" menu item from gnome-power-manager
- use beagle or tracker if available for search tool
- add patches from fedora

* Sat Aug 25 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt2.1
- rebuilt with evolution-data-server 1.10

* Sat Jul 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt2
- use more path macros
- move all GNOME applets to One Well-known Place (defined by %%gnome_appletsdir
  macro).

* Fri Jul 06 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.3-alt1
- new version (2.18.3)

* Mon Jul 02 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt2
- rebuild with new libwnck.
- disabled making applets in-process to increase robustness of the panel.

* Tue Jun 19 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18.2-alt1
- new version (2.18.2)
- updated dependencies, removed most of the deps from -devel and -devel-static
  subpackages (let pkgconfig do its job).
- spec cleanup (no more %%__ macros).

* Wed Dec 20 2006 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Sun Sep 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.0-alt1
- new version 2.16.0
- updated files list.

* Sun Aug 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.92-alt1
- new version 2.15.92 (with rpmrb script)

* Sun Aug 20 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.91-alt1
- new version (2.15.91)
- patch for clock orientation went upstream.
- temporarily disabled properties menu item patch - it's broken.

* Sun Jul 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt2
- updated the patch for clock orientation.

* Thu Jun 01 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version
- updated the required version of gnome-vfs
- enabled a patch for menu item properties (GNOME Bug 342521).
- added a patch that fixes the clock orientation on vertical panels (GNOME
  Bug 318377), not applied yet, as it is not functional.
- spec cleanup.

* Mon Apr 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt2
- added a patch that shows menu item properties (right-click on an item).

* Wed Apr 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Tue Mar 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Tue Feb 14 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.91-alt1
- new version
- spec cleanup, dependencies revised

* Thu Feb 09 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1.1
- fixed buildreqs for X.org 7.0

* Tue Nov 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.2-alt1
- new version

* Tue Oct 25 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.13.1-alt1
- new version
- updated dependencies from configure.in and .pc files.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Tue Sep 06 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0
- Removed more excess buildreqs.

* Tue Aug 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.11.92-alt1
- 2.11.92
- Removed excess buildreqs.
- Disabled Automake stuff, since it corrupts the existing aclocal.m4.

* Sat Jul 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.2-alt1
- 2.10.2

* Sun Apr 03 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Tue Mar 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Tue Mar 01 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt1
- 2.9.92 release.

* Fri Feb 25 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.92-alt0.1
- 2.9.92 from cvs.

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.91-alt1
- 2.9.91

* Sun Feb 06 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.90-alt1
- 2.9.90.
- do not install /etc/menu-methods/gnome-panel2.

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Tue Sep 14 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0

* Mon Sep 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.7.92-alt1
- 2.7.92

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1
- gnome menu go back (- patch6).

* Tue Mar 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0-alt2.1
- 2.6.0

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.93-alt2.1
- fixed menu.

* Mon Mar 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.93-alt2
- disable system menu
- wanda use /usr/games/fortune.

* Sat Mar 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.93-alt1.1
- rebuild with new libecal.

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.93-alt1
- 2.5.93

* Tue Mar 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.91-alt1
- 2.5.91

* Tue Feb 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.90-alt1
- 2.5.90

* Tue Feb 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.5-alt1
- 2.5.5

* Tue Feb 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt2
- rebuild with new libecal.

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.3.1-alt1
- 2.5.3.1

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt2
- do not package .la files.
- do not build devel-static subpackage by default.
- Wanda requires fortune-mod.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Wed Sep 10 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sat Sep 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.91-alt1
- 2.3.91

* Wed Sep 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.6.2-alt1
- 2.3.6.2

* Wed Jul 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jul 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.3-alt1
- 2.3.3.3

* Tue Jul 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.2-alt1
- 2.3.3.2

* Fri Jun 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3.1-alt1
- 2.3.3.1

* Sun Jun 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3

* Wed May 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2.1-alt1
- 2.3.2.1

* Wed May 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2
- added hack to allow dock qt (non-gtk) applications, we will need it
  for rhn-applet like programs (security update notificator) (inger)

* Mon May 05 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Apr 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt2
- Try to load default settings from gconftool dump.

* Sun Mar 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Feb 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt3
- fixed systray on exit crash (#2228)

* Thu Feb 06 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt2
- fixed systray help call.

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0.1-alt1
- 2.2.0.1

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.90.1-alt1
- 2.1.90.1

* Thu Dec 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt3
- Schemas installation fixed.

* Tue Dec 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt2
- made gnome2 menus in utf-8, we need it for correct work of Gnome2 in
  ru_RU.CP1251 locale. Thanks to inger.
- Return customization patch back.

* Tue Dec 17 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Tue Dec 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Thu Nov 28 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Mon Nov 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Sat Oct 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt2
- customization patch removed, we use gconf2_* macros.

* Tue Oct 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Oct 11 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.0-alt3
- fix customization patch

* Thu Oct 10 2002 Stanislav Ievlev <inger@altlinux.ru> 2.1.0-alt2
- Added customization for panel (default settings):
  TODO: to add new galeon and evolution

* Thu Oct 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.9-alt1.1
- fixed wrong syntax in %%post (%%gconf2_install)
- removed SMP build

* Wed Sep 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.9-alt1
- 2.0.9

* Thu Jun 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- Adopted for Sisyphus.
- menu_distribution.patch by BlaKe <blake@altlinux.ru>
- (blake)
    + fix lost files
    + added altlinux.png icon for menu
    + added script for support menu
- libname{,-devel{,-static}} packages.
- scrollkeeper-update starts in post.
- (blake) fix error in install
- gen_util_build.patch

* Tue Mar 12 2002 <glynn.foster@sun.com>
- fix up gconf schema install

* Mon Mar  4 2002  <gleblanc@linuxweasel.com>
- made into a proper .spec.in, using the magic version numbers and such

* Mon Feb 18 2002  <gleblanc@linuxweasel.com>
- flagged man pages as documentation

* Mon Feb 18 2002 Gregory Leblanc <gleblanc@linuxweasel.com>
- remove extra tab from header
- added defattr to devel package
- moved defattr to make sure that it owns the random package docs
- moved the idl files into the main package, as when perl bindings arrive, they'll want to use them at run-time
- made it not own the omf dir
- moved the line for the GNOME help stuff back into the section with the rest of the regular files
- changed name of find_lang's output file
- removed some whitespace from the install section
- removed some tabs from the devel package headers
- make release number funky, so that people know it's a snapshot
- use auto* version
- group all BuildRequires together

* Fri Feb 15 2002 Chris Chabot <chabotc@reviewboard.com>
- initial spec file
- cleaned up header
- moved gnome/help to doc section

