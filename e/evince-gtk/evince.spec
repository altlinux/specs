%define oname evince
%define _libexecdir	%_prefix/libexec
%define major 2.32

%def_disable introspection

Name: evince-gtk
Version: %major.0
Release: alt4.1
Summary: A document viewer
License: GPL
Group: Office
Url: http://www.gnome.org/projects/evince/
Packager: Lenar Shakirov <snejok@altlinux.org>

Requires: lib%name = %version-%release

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Conflicts: %oname

BuildRequires(Pre): libGConf-devel

BuildRequires: GConf gcc-c++ gnome-common gnome-doc-utils-xslt gtk-doc gnome-icon-theme intltool libSM-devel libdbus-glib-devel
BuildRequires: libdjvu-devel libgnome-keyring-devel libnautilus-devel libpoppler-glib-devel libspectre-devel libtiff-devel
BuildRequires: libxml2-devel libkpathsea-devel libgail-devel zlib-devel
%if_enabled introspection
BuildRequires: gobject-introspection-devel libpango-gir-devel
%endif

%description
Evince is a document viewer capable of displaying multiple and single page
document formats like PDF and Postscript. (version without GNOME)

%package dvi
Summary: Evince backend for dvi files
Group: Office
Requires: %name = %version-%release

%description dvi
A backend to let evince display dvi files

%package -n lib%name
Summary: Library for the %name project
Group: Office
Conflicts: lib%oname

%description -n lib%name
Library for %name project

%package -n lib%name-gir
Summary: GObject introspection data for the Evince library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Evince library

%package -n lib%name-devel
Summary: Development tools for the %name
Group: Development/C
Requires: lib%name = %version-%release
Conflicts: lib%oname-devel

%description -n lib%name-devel
Header files for %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Evince library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Evince library

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--enable-pdf \
	--enable-tiff \
	--enable-djvu \
	--disable-dvi \
	--enable-pixbuf \
	--enable-comics \
	--enable-impress \
	--enable-pixbuf \
	--enable-gtk-doc \
	--disable-nautilus \
	--without-libgnome \
	--without-keyring \
	--with-print=gtk \
	--enable-dbus \
	%{subst_enable introspection} \
	--disable-static
%make

%install
%make DESTDIR=%buildroot install

subst '/NoDisplay/d' %buildroot%_desktopdir/%oname.desktop
sed 's/Categories=.*/Categories=Viewer;Office;GTK;/' -i %buildroot%_desktopdir/%oname.desktop

%find_lang %oname --with-gnome

%define desktop_schemas %oname-thumbnailer %oname-thumbnailer-ps %oname-thumbnailer-comics

%post
%gconf2_install %desktop_schemas

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %desktop_schemas
fi

%post dvi
%gconf2_install %name-thumbnailer-dvi

%preun dvi
if [ $1 = 0 ]; then
%gconf2_uninstall %name-thumbnailer-dvi
fi

%files -f %oname.lang
%doc AUTHORS NEWS README
%_sysconfdir/gconf/schemas/*.schemas
%_bindir/evince*
%dir %_libdir/evince
%dir %_libdir/evince/3
%dir %_libdir/evince/3/backends
%_libdir/evince/3/backends/*.so
%_libdir/evince/3/backends/*.evince-backend
%_libexecdir/evince*
%_desktopdir/%oname.desktop
%_datadir/dbus-1/services/org.gnome.evince.Daemon.service
%_datadir/%oname
%_datadir/GConf/gsettings/evince.convert
%_datadir/glib-2.0/schemas/org.gnome.Evince.gschema.xml
%_iconsdir/hicolor/*/apps/*
%_man1dir/*.1*

%files -n lib%name
%_libdir/libevdocument.so.*
%_libdir/libevview.so.*

%files -n lib%name-devel
%_includedir/evince
%_libdir/libevdocument.so
%_libdir/libevview.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/%oname
%_datadir/gtk-doc/html/libev*

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir
%endif

%changelog
* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.32.0-alt4.1
- Fixed build

* Thu May 26 2011 Lenar Shakirov <snejok@altlinux.ru> 2.32.0-alt4
- updated to poppler api changes (closes: #25246)

* Mon Apr 11 2011 Lenar Shakirov <snejok@altlinux.ru> 2.32.0-alt3
- fixed build: zlib-devel added to BuildReq

* Tue Feb 22 2011 Lenar Shakirov <snejok@altlinux.ru> 2.32.0-alt2
- spec cleaned: remove dvi subpackage

* Tue Feb 22 2011 Lenar Shakirov <snejok@altlinux.ru> 2.32.0-alt1
- new version of %name

* Tue Feb 15 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt3
- rebuild with libpoppler-glib.so.6

* Wed Oct 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt2
- fixed install gconf schemas

* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Thu Aug 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.3-alt2
- rebuild with libpoppler-glib.so.5

* Sun Jun 27 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.3-alt1
- 2.30.3

* Tue Jun 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.2-alt1
- 2.30.2

* Thu Apr 29 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt2
- make sure dot_dir exists before creating last_settings file (closes: #23402)

* Mon Apr 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt2
- rebuild

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Thu Mar 11 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.92-alt1
- 2.29.92

* Tue Jan 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.4-alt1
- 2.29.4

* Thu Dec 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.2-alt1
- 2.28.2

* Fri Dec 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt2
- rebuild with libkpathsea (closes: #22444)

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Tue Sep 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Mon Sep 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.90-alt2
- updated translations

* Wed Aug 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.90-alt1
- 2.27.90

* Thu Jun 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.3-alt1
- 2.27.3

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.2-alt1
- 2.26.2

* Wed Apr 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.26.1-alt1
- 2.26.1

* Fri Mar 13 2009 Evgeny Sinelnikov <sin@altlinux.ru> 2.25.92-alt1
- new version 2.25.92
- rebuild with new libdjvulibre

* Mon Mar 02 2009 Vitaly Lipatov <lav@altlinux.ru> 2.25.91-alt1
- new version 2.25.91
- split libevince and libevince-devel

* Wed Jan 07 2009 Vitaly Lipatov <lav@altlinux.ru> 2.25.4-alt1
- new version 2.25.4 (with rpmrb script)

* Mon Jan 05 2009 Vitaly Lipatov <lav@altlinux.ru> 2.25.2-alt3
- really pack dvi backend module into evince-dvi, not djvu (fix bug #18444)

* Thu Dec 18 2008 Vitaly Lipatov <lav@altlinux.ru> 2.25.2-alt2
- review spec and merge with some Yury Sedunov's changes from his NMU
- build with libspectre
- split dvi support in evince-dvi subpackage
- remove devel stuffs as unneeded

* Tue Dec 16 2008 Vitaly Lipatov <lav@altlinux.ru> 2.25.2-alt1
- new version 2.25.2 (with rpmrb script)
- disable dvi support (due big tetex-core requires)
- pack missed libdirs
- drop obsoleted post/postun macros

* Mon Nov 24 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Wed Oct 01 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0
- ps support via libspectre
- devel subpackage
- doc-devel subpackage(noarch)

* Sun Jun 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.2-alt1
- new version 2.22.2 (with rpmrb script)

* Thu May 01 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.1.1-alt2
- rebuild with libpoppler 0.8

* Thu Apr 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.22.1.1-alt1
- new version 2.22.1.1 (with rpmrb script)

* Thu Dec 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.21.1-alt1
- new version 2.21.1 (with rpmrb script)

* Tue Nov 27 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.2-alt1
- new version 2.20.2 (with rpmrb script)
- fix gconf2_ macros using (fix bug #13419)

* Wed Nov 14 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt4
- add GConf requires (fix bug #13419)

* Sat Nov 10 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt3
- add Provides: bindir/name
- remove NoDisplay from desktop file (fix bug #13369)
- return dvi support
- update buildreqs

* Mon Nov 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt2
- enable nautilus extension
- add gconf files

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.1-alt1
- new version 2.20.1 (with rpmrb script)
- update buildreq

* Wed Sep 26 2007 Vitaly Lipatov <lav@altlinux.ru> 2.20.0-alt1
- new version 2.20.0 (with rpmrb script)

* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 2.19.92-alt1
- new version 2.19.92 (with rpmrb script)
- build with libpoppler 0.6

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- new version 0.9.3 (with rpmrb script)

* Fri Jul 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt2
- reverted changes for build with libpoppler 0.5.4

* Thu Jul 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- new version 0.9.2 (with rpmrb script)
- add ghostscript build requires
- still wait for libpoppler >= 0.5.9

* Wed Jun 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- new version 0.9.1 (with rpmrb script)

* Sat Jun 09 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9.0-alt1
- new version 0.9.0 (with rpmrb script)
- update buildreqs, fix comics build

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1 (with rpmrb script)

* Wed Mar 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
- bzip ChangeLog (fix bug #11077), thanks icesik@

* Fri Feb 16 2007 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Tue Dec 26 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt0.1
- new version 0.7.0 (with rpmrb script)

* Fri Oct 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt0.1
- new version 0.6.1 (with rpmrb script)

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt0.1
- new version (0.6.0), add icons
- remove debian menu, update buildreqs

* Thu Jul 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt0.1
- new version 0.5.4 (with rpmrb script)

* Sun May 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt0.1
- enable comics support
- fix build with new libpoppler

* Mon Mar 27 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt0.1
- new version (0.5.2)
- update buildreq, use make_build

* Mon Feb 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt0.1
- new version, build with libpoppler 0.4.2, djvu, t1lib
- build with new gnome-doc-utils

* Sun Jul 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt0.1
- first build for ALT Linux Sisyphus
