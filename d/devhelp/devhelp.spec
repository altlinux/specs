%define ver_major 3.26
%define api_ver 3.0
%define xdg_name org.gnome.Devhelp

Name: devhelp
Version: %ver_major.1
Release: alt1

Summary: Developer's help program
Group: Development/Other
License: %gpl2plus
Url: https://wiki.gnome.org/Apps/Devhelp
#VCS: git://git.gnome.org/devhelp

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define gtk_ver 3.22.0

Requires: lib%name = %version-%release

BuildPreReq: rpm-build-gnome >= 0.6 gnome-common
BuildPreReq: rpm-build-licenses
BuildPreReq: gtk-doc libappstream-glib-devel

# From configure.ac
BuildRequires: pkgconfig(gthread-2.0) >= 2.10.0
BuildRequires: pkgconfig(gtk+-3.0) >= 3.19.3
BuildRequires: pkgconfig(webkit2gtk-4.0) >= 2.6.0
BuildRequires: pkgconfig(gio-2.0) >= 2.40
BuildRequires: zlib-devel
# since 3.23.x
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libwebkit2gtk-gir-devel
BuildRequires: gsettings-desktop-schemas-devel

%description
A developers help program.

%package -n lib%name
Summary: Devhelp widgets library
Group: System/Libraries

%description -n lib%name
This package provides shared library required for Devhelp to work.

%package -n lib%name-devel
Summary: Devhelp widgets headers
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Devhelp widgets.

%package -n lib%name-gir
Summary: GObject introspection data for the Devhelp library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
This package provides GObject introspection data for the Devhelp
library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Devhelp library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
This package provides GObject introspection devel data for the Devhelp
library.

%package -n lib%name-devel-doc
Summary: Development documentation for Devhelp library
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package provides development documentation for the Devhelp library.

%package -n gedit-plugin-%name
Summary: DevHelp integration into GEdit
Group: Development/Other
Requires: %name = %version-%release

%description -n gedit-plugin-%name
This plugin for GEdit enables using DevHelp from inside the editor.

%define _devhelpdir %_datadir/%name
%define  gedit_pluginsdir %_libdir/gedit/plugins

%prep
%setup

%build
# newer libtool required
#%%autoreconf
%configure --disable-static

%make_build

%install
%makeinstall_std

# Create some directories in %name hierarchy
mkdir -p %buildroot%_devhelpdir/{specs,books}

%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_devhelpdir
%_devhelpdir/*
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/devhelp.*
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/GConf/gsettings/*.convert
%_datadir/glib-2.0/schemas/org.gnome.devhelp.gschema.xml
%_man1dir/%name.1.*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/lib%name-*.pc

%files -n lib%name-gir
%_typelibdir/Devhelp-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/Devhelp-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name-*/

%files -n gedit-plugin-%name
%gedit_pluginsdir/*

%changelog
* Sat Dec 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sun Sep 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Sep 01 2015 Yuri N. Sedunov <aris@altlinux.org> 3.17.91-alt1
- 3.17.91

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Oct 07 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt2
- rebuild

* Tue Sep 23 2014 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0
- build with webkit2gtk-4.0

* Tue Sep 16 2014 Alexey Shabalin <shaba@altlinux.ru> 3.13.90-alt1
- 3.13.90

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Alexey Shabalin <shaba@altlinux.ru> 3.12.0-alt1
- 3.12.0

* Mon Nov 18 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.2-alt1
- 3.10.2

* Tue Sep 24 2013 Alexey Shabalin <shaba@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Tue Sep 03 2013 Alexey Shabalin <shaba@altlinux.ru> 3.9.91-alt1
- 3.9.91

* Wed May 15 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.2-alt1
- 3.8.2

* Fri Apr 19 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Alexey Shabalin <shaba@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Thu Mar 07 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.91-alt1
- 3.7.91

* Mon Feb 25 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.5-alt1
- 3.7.5

* Wed Nov 14 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Thu Apr 05 2012 Alexey Shabalin <shaba@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.0-alt1.1
- Rebuild with Python-2.7

* Thu May 26 2011 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0

* Thu Mar 31 2011 Alexey Shabalin <shaba@altlinux.ru> 2.91.92-alt1
- 2.91.92

* Fri Oct 08 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt2
- add default value for books_disabled to GConf schema

* Mon Oct 04 2010 Alexey Shabalin <shaba@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Mon Sep 13 2010 Alexey Shabalin <shaba@altlinux.ru> 2.31.92-alt1
- 2.31.92

* Tue Mar 30 2010 Alexey Shabalin <shaba@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Wed Feb 10 2010 Alexey Shabalin <shaba@altlinux.ru> 0.29.90-alt1
- 0.29.90

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.28.1-alt1.1
- Rebuilt with python 2.6

* Tue Oct 20 2009 Alexey Shabalin <shaba@altlinux.ru> 0.28.1-alt1
- 0.28.1

* Mon Sep 28 2009 Alexey Shabalin <shaba@altlinux.ru> 0.28.0.1-alt1
- 0.28.0.1

* Mon Sep 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.28.0-alt1
- 0.28.0

* Tue Aug 18 2009 Alexey Shabalin <shaba@altlinux.ru> 0.23.1-alt1
- 0.23.1

* Fri Apr 10 2009 Alexey Shabalin <shaba@altlinux.ru> 0.23-alt1
- 0.23
- cleanup spec (drop all about cvsdate)

* Sat Dec 06 2008 Yuri N. Sedunov <aris@altlinux.org> 0.22-alt1
- 0.22 (move to WebKit)

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.21-alt2
- 0.21
- fixed build for x86_64

* Thu Oct 02 2008 Yuri N. Sedunov <aris@altlinux.org> 0.20-alt1
- 0.20

* Thu Jul 10 2008 Yuri N. Sedunov <aris@altlinux.org> 0.19.1-alt1
- new version
- build against xulrunner.

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * desktop-mime-entry for devhelp
 * update_menus for devhelp

* Mon Feb 25 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt2
- Rebuilt with Python 2.5.

* Mon Feb 11 2008 Alexey Rusakov <ktirf@altlinux.org> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Tue Jan 08 2008 Alexey Rusakov <ktirf@altlinux.org> 0.17-alt1
- New version (0.17).
- The patch for the .pc file went upstream.
- Updated dependencies.

* Tue Oct 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.16.1-alt1
- new version (0.16.1)
- fixed excess dependencies mentioned in the .pc file.

* Mon Sep 10 2007 Alexey Rusakov <ktirf@altlinux.org> 0.16-alt1
- new version (0.16)
- more macros used, including license macro.

* Sat Jun 09 2007 Alexey Rusakov <ktirf@altlinux.org> 0.14-alt1
- new version (0.14)
- updated dependencies
- package GEdit plugin

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 0.13-alt1
- new version 0.13 (with rpmrb script)

* Tue Dec 19 2006 Alexey Rusakov <ktirf@altlinux.org> 0.12-alt2
- switch Gecko backend to Firefox.
- minor cleanup.

* Fri Jul 28 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.12-alt1
- new version 0.12.
- updated files list (GEdit plugin is not included yet).

* Sat Feb 25 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.11-alt1
- new version (0.11)
- cleaned up the spec, revised dependencies
- introduced gecko_provider switch (choose from mozilla, seamonkey, FF, and TB).
- removed Debian menu support.

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.10-alt1
- 0.10

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Tue Aug 17 2004 Vital Khilko <vk@altlinux.ru> 0.9.1-alt2
- updated belarusian translations.

* Sun Jul 25 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9.1-alt1
- 0.9.1
- use freedesktop2menu.pl to build menu file.
- updated translations.

* Fri Jul 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9-alt1.1
- rebuild against new mozilla-1.7

* Thu Mar 18 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9-alt1
- 0.9

* Fri Feb 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Wed Oct 01 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt2
- fixed buildreqs.

* Sun Jun 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.7-alt1
- 0.7

* Mon Apr 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Mar 03 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.5.0-alt0.7
- 0.5.0

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.4.99-alt0.6cvs20030204
- gnome2 version from cvs crashes on startup.

* Sun May 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.4-alt1
- First build for Sisyphus.
