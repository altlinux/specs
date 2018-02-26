%define ver_major 2.20
%define _name gtk-engines
%define engine_prefix libgtk-engine
%define old_engine_prefix gtk-engines
%define engine_namechange_ver 2.8.0-alt3
%define gtk_theme_prefix gtk2-theme
%define old_theme_prefix gtk2-themes
%define theme_namechange_ver 2.8.0-alt4

# Clearlooks animation takes some CPU cycles, so it's done optional.
%def_enable animation

Name: %{engine_prefix}s-default
Version: %ver_major.2
Release: alt2
Serial: 1

Summary: Default GTK+2 theme engines
License: %lgpl2plus
Group: Graphical desktop/GNOME
Url: http://gtk.themes.org/

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.bz2
Patch: %_name-2.20.2-alt-glib_fixes.patch

Obsoletes: %old_engine_prefix <= %engine_namechange_ver
Provides: %old_engine_prefix = %version-%release
Obsoletes: %old_engine_prefix-default <= %engine_namechange_ver
Provides: %old_engine_prefix-default = %version-%release
Obsoletes: %engine_prefix-default <= %engine_namechange_ver
Provides: %engine_prefix-default = %version-%release

%define gtk_ver 2.10.0
%define gtk_binary_ver 2.10.0
%define icon_theme_ver 2.10.0

Requires: %engine_prefix-redmond = %version-%release
Requires: %engine_prefix-hc = %version-%release
Requires: %engine_prefix-crux = %version-%release
Requires: %engine_prefix-mist = %version-%release
Requires: %engine_prefix-thinice = %version-%release
Requires: %engine_prefix-industrial = %version-%release
Requires: %engine_prefix-clearlooks = %version-%release
Requires: %engine_prefix-glide = %version-%release

BuildPreReq: rpm-build-gnome rpm-build-licenses

BuildPreReq: intltool >= 0.31.0
BuildPreReq: libgtk+2-devel >= %gtk_ver
BuildPreReq: liblua5-devel

%description
These are the graphical engines for the various GTK+2 toolkit themes.

# FIXME: Recollect/Find out and explain here why GTK+ engines need
# gnome-icon-theme. Looks rather suspicious.

%package -n %name-common
Summary: Files common to all GTK+ engines
Group: Graphical desktop/GNOME

%description -n %name-common
This package contains files used or referred to by any "standard" GTK+
engine. Don't care about installing it; you will know if some GTK+
engine needs it.

%package -n %engine_prefix-redmond
Summary: GTK+2 theme engine - Redmond95
Group: Graphical desktop/GNOME
License: %lgpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-redmond95
Provides: %old_engine_prefix-redmond95 = %version-%release
Provides: %engine_prefix-redmond95 = %version-%release
Obsoletes: %old_engine_prefix-redmond < %engine_namechange_ver
Provides: %old_engine_prefix-redmond = %version-%release

%description -n %engine_prefix-redmond
A simple theme engine that looks a bit like another OS.

%package -n %gtk_theme_prefix-redmond
Summary: GTK+2 theme - Redmond95
Group: Graphical desktop/GNOME
License: %lgpl2plus
Obsoletes: %old_theme_prefix-redmond < %engine_namechange_ver
Provides: %old_theme_prefix-redmond = %version-%release
# Due to file conflicts
Obsoletes: %old_theme_prefix-redmond = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %gtk_theme_prefix-redmond
A simple theme that looks a bit like another OS.

%package -n %engine_prefix-hc
Summary: A GTK+2 high contrast theme engine
Group: Graphical desktop/GNOME
License: %lgpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-hc < %engine_namechange_ver
Provides: %old_engine_prefix-hc = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %engine_prefix-hc
Engine for high contrast themes, that improves visibility of shadows, edges,
and indicators when theme background and foreground contain near-black
and near-white colors.

%package -n %gtk_theme_prefix-crux
Summary: A GTK+2 theme engine - Crux
Group: Graphical desktop/GNOME
License: %gpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-crux < 2.7.6
Provides: %old_engine_prefix-crux = %version-%release
Obsoletes: %old_theme_prefix-crux < %theme_namechange_ver
Provides: %old_theme_prefix-crux = %version-%release
Provides: %engine_prefix-crux = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %gtk_theme_prefix-crux
This package contains a GTK2+ theme engine named Crux and developed by
Eazel, Inc.

%package -n %gtk_theme_prefix-mist
Summary: A GTK+2 theme engine - Mist
Group: Graphical desktop/GNOME
License: %gpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-mist < 2.7.6
Provides: %old_engine_prefix-mist = %version-%release
Obsoletes: %old_theme_prefix-mist < %theme_namechange_ver
Provides: %old_theme_prefix-mist = %version-%release
Provides: %engine_prefix-mist = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %gtk_theme_prefix-mist
Author named this after the song he was listening to when he named it
(Opeth's "In Mist She Was Standing").
This package provides Mist GTK+2 theme engine.

%package -n %gtk_theme_prefix-clearlooks
Summary: A GTK+2 theme engine - ClearLooks
Group: Graphical desktop/GNOME
License: %gpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-clearlooks < 2.7.6
Provides: %old_engine_prefix-clearlooks = %version-%release
Obsoletes: %old_theme_prefix-clearlooks < %theme_namechange_ver
Provides: %old_theme_prefix-clearlooks = %version-%release
Provides: %engine_prefix-clearlooks = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %gtk_theme_prefix-clearlooks
ClearLooks is new modern looking engine for GTK+2, based on Bluecurve.
It has the looks of various themes blended together, resulting in a
theme that's easy on the eyes and visually pleasing.

This package contains Clearlooks theme and engine.

%package -n %gtk_theme_prefix-thinice
Summary: A GTK+2 theme engine - Thin Ice
Group: Graphical desktop/GNOME
License: %gpl2plus
Requires: %name-common = %version-%release
Obsoletes: %engine_prefix-thinice-devel
Obsoletes: %old_engine_prefix-thinice < 2.7.6
Provides: %old_engine_prefix-thinice = %version-%release
Obsoletes: %old_theme_prefix-thinice < %theme_namechange_ver
Provides: %old_theme_prefix-thinice = %version-%release
Provides: %engine_prefix-thinice = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %gtk_theme_prefix-thinice
This package contains a GTK2+ theme engine Thin Ice.

%package -n %gtk_theme_prefix-industrial
Summary: A GTK+2 theme engine - Industrial
Group: Graphical desktop/GNOME
License: %gpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-industrial < 2.7.6
Provides: %old_engine_prefix-industrial = %version-%release
Obsoletes: %old_theme_prefix-industrial < %theme_namechange_ver
Provides: %old_theme_prefix-industrial = %version-%release
Provides: %engine_prefix-industrial = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %gtk_theme_prefix-industrial
This package contains a GTK2+ engine Industrial developed by Ximian, Inc. as
the default apearance for its Desktop. Industrial is a highly popular
look which provides a simple, consistant, and highly cohesive appearance
for applications.

%package -n %engine_prefix-glide
Summary: A GTK+2 theme engine - Glide
Group: Graphical desktop/GNOME
License: %lgpl2plus
Requires: %name-common = %version-%release
Obsoletes: %old_engine_prefix-glide < %engine_namechange_ver
Provides: %old_engine_prefix-glide = %version-%release
Requires: gnome-icon-theme >= %icon_theme_ver

%description -n %engine_prefix-glide
This package contains a GTK2+ theme engine Glide (used by Glider GNOME theme).

%package -n %engine_prefix-lua
Summary: A Lua scripting engine for GTK+ themes
Group: Graphical desktop/GNOME

%description -n %engine_prefix-lua
This package contains an engine that enables Lua scripting in GTK+ themes. Unless some GTK+ theme depends on this package, you don't need it.

%package -n %{engine_prefix}s-devel
Summary: Development files for %_name
Group: Development/GNOME and GTK+
Obsoletes: %old_engine_prefix-default-devel < %engine_namechange_ver
Provides: %old_engine_prefix-default-devel = %version-%release

%description -n %{engine_prefix}s-devel
This package contains development files for %_name

%prep
%setup -q -n %_name-%version
%patch -p1

%build
%autoreconf
%configure \
    --enable-lua \
    --with-system-lua \
    %{subst_enable animation} \

%make
%make check

%install
%make DESTDIR=%buildroot install
%find_lang %_name

%define engines_dir %_libdir/gtk-2.0/%gtk_binary_ver/engines/
%define engines_data_dir %_datadir/%_name/

%files

%files -n %name-common -f %_name.lang
%dir %_datadir/%_name
%doc AUTHORS README ChangeLog COPYING*

%files -n %engine_prefix-redmond
%engines_dir/libredmond95.so
%engines_data_dir/redmond95.xml

%files -n %gtk_theme_prefix-redmond
%dir %_datadir/themes/Redmond/
%dir %_datadir/themes/Redmond/gtk-2.0
%_datadir/themes/Redmond/gtk-2.0/gtkrc
#dir %_datadir/themes/Redmond/gtk
#_datadir/themes/Redmond/gtk/gtkrc
%doc engines/redmond/AUTHORS

%files -n %engine_prefix-hc
%engines_dir/libhcengine.so
%engines_data_dir/hcengine.xml

%files -n %gtk_theme_prefix-crux
%engines_dir/*crux*.so
%engines_data_dir/crux-engine.xml
%dir %_datadir/themes/Crux
%dir %_datadir/themes/Crux/gtk-2.0
%_datadir/themes/Crux/gtk-2.0/gtkrc

%files -n %gtk_theme_prefix-clearlooks
%engines_dir/*clearlooks.so
%engines_data_dir/clearlooks.xml
%dir %_datadir/themes/Clearlooks
%dir %_datadir/themes/Clearlooks/gtk-2.0
%_datadir/themes/Clearlooks/gtk-2.0/gtkrc

%files -n %gtk_theme_prefix-mist
%engines_dir/libmist.so
%engines_data_dir/mist.xml
%dir %_datadir/themes/Mist
%dir %_datadir/themes/Mist/gtk-2.0
%_datadir/themes/Mist/gtk-2.0/gtkrc

%files -n %gtk_theme_prefix-thinice
%engines_dir/*thinice.so
%engines_data_dir/thinice.xml
%dir %_datadir/themes/ThinIce
%dir %_datadir/themes/ThinIce/gtk-2.0
%_datadir/themes/ThinIce/gtk-2.0/gtkrc

%files -n %gtk_theme_prefix-industrial
%engines_dir/libindustrial.so
%engines_data_dir/industrial.xml
%dir %_datadir/themes/Industrial
%dir %_datadir/themes/Industrial/gtk-2.0
%_datadir/themes/Industrial/gtk-2.0/gtkrc

%files -n %engine_prefix-glide
%engines_dir/libglide.so
%engines_data_dir/glide.xml

%files -n %{engine_prefix}-lua
%engines_dir/libluaengine.so

%files -n %{engine_prefix}s-devel
%_pkgconfigdir/*.pc

%exclude %engines_dir/*.la

%changelog
* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1:2.20.2-alt2
- fixed build against glib-2.32

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.20.2-alt1
- 2.20.2

* Sat Apr 17 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.20.1-alt1
- 2.20.1

* Tue Mar 30 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.20.0-alt1
- 2.20.0

* Tue Jan 12 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.19.0-alt1
- 2.19.0

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1:2.18.5-alt1
- new version

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.18.4-alt1
- 2.18.4

* Tue Sep 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.18.3-alt1
- 2.18.3
- build against system lua

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.18.2-alt1
- 2.18.2

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.18.1-alt1
- 2.18.1

* Tue Mar 17 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.18.0-alt1
- 2.18.0

* Tue Mar 03 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.17.4-alt1
- 2.17.4

* Tue Feb 17 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.17.3-alt1
- 2.17.3

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 1:2.17.2-alt1
- 2.17.2

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 1:2.16.1-alt1
- 2.16.1

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.16.0-alt1
- new version (2.16.0)
- removed the smooth engine

* Tue Jul 01 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.14.3-alt1
- new version (2.14.3)

* Fri May 30 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.14.2-alt1
- new version (2.14.2)

* Tue Apr 08 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.14.1-alt1
- new version (2.14.1)

* Mon Mar 17 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.14.0-alt1.1
- build for Sisyphus

* Fri Mar 14 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.14.0-alt1
- new version (2.14.0)

* Wed Mar 05 2008 Alexey Shabalin <shaba@altlinux.ru> 1:2.13.6-alt1
- new version (2.13.6)

* Wed Oct 17 2007 Alexey Rusakov <ktirf@altlinux.org> 1:2.12.2-alt2
- gtk-themes-redmond -> %gtk_theme_prefix-redmond, due to passing away of
  Gtk+1 theme.

* Tue Oct 16 2007 Alexey Rusakov <ktirf@altlinux.org> 1:2.12.2-alt1
- new version (2.12.2)
- use rpm-build-gnome and rpm-build-licenses.
- updated license tags per-package according to COPYING file included in
  the tarball.
- updated files list (some .xml files renamed, no more gtk1 Redmond theme).

* Fri Jun 01 2007 Alexey Rusakov <ktirf@altlinux.org> 1:2.10.2-alt1
- new version (2.10.2)
- added 'make check' invocation.
- introduced Lua scripting engine.
- updated files list (engines got some metadata in /usr/share/gtk-engines).
- introduced -common subpackage, since gtk-engines now have localized strings.
  Package documentation also resides in -common from now on.

* Wed Jan 24 2007 Alexey Rusakov <ktirf@altlinux.org> 1:2.8.2-alt1
- new version (2.8.2)
- libgtk-engine-redmond now obsoletes (and not provides) gtk2-themes-redmond
  (Bug #10329)

* Sun Oct 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.8.1-alt1
- new version (2.8.1)
- removed no more needed subst

* Fri Oct 13 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.8.0-alt4
- GTK+ themes are now prefixed with gtk2-theme instead of gtk2-themes.

* Wed Oct 11 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.8.0-alt3
- replaced 'gtk-engines' prefix with 'libgtk-engine' prefix, to better
  reflect the nature of an engine and to clearly separate it from
  a gtk-theme (ah, and to frighten a user with 'lib' prefix, too).
- renamed the main package to libgtk-engines-default, and development
  subpackage to libgtk-engines-devel.

* Tue Sep 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.8.0-alt2
- cleaning up the mess between gtk-engines and gnome-themes.

* Sun Sep 10 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.8.0-alt1
- new version 2.8.0 (with rpmrb script)

* Sun Sep 03 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.7.8-alt1
- new version 2.7.8 (with rpmrb script)

* Thu Aug 17 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.7.7-alt1
- new version (2.7.7)

* Sat Aug 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.7.6-alt1
- new version (2.7.6)
- no more Metal and Lighthouse Blue engines and themes.
- a new engine, Glide.
- renamed packages, that contain themes, to gtk2-themes-*.
- spec cleanup.

* Sun Feb 12 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.7.4-alt1
- new version
- spec cleanup

* Sat Jan 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.7.3-alt1
- new version

* Sun Jan 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 1:2.7.2-alt1
- new version

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 1:2.6.5-alt1
- 2.6.5

* Wed Apr 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 1:2.6.3-alt1
- 2.6.3
- new subpackage with Clearlooks engine.

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 1:2.6.2-alt1
- 2.6.2

* Tue Feb 08 2005 Yuri N. Sedunov <aris@altlinux.ru> 1:2.6.1-alt1
- 2.6.1

* Wed Dec 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 1:2.6.0-alt1
- 2.6.0

* Tue Dec 07 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt2.7
- do not build pixmap engine that provided by GTK+ since 2.5.6

* Wed Mar 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt2.6
- rebuild with gtk-2.4.

* Sat Jan 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt2.4
- 2.2.0
- devel subpackage.

* Wed Dec 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt2.4
- Rebuilt with gtk-2.1.5

* Fri Dec 06 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt2.3
- Rebuilt with gtk-2.1.3.

* Sun Nov 03 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt2.2
- Rebuilt with new gtk2.

* Thu Oct 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt2.1
- Rebuilt with new gtk2.

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt2
- Package renamed.

* Wed Oct 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.9.0-alt1
- First build for Sisyphus.
