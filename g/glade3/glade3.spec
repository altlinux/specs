%define ver_major 3.7

Name:    glade3
Version: %ver_major.0
Release: alt2.2

Summary: GTK+ / GNOME widget builder
Group:   Development/GNOME and GTK+
License: %gpl2plus, %lgpl2plus
URL:     http://glade.gnome.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

# Sonames of libgladeui don't change with each release. Although ABI does
# not change either, it is better to upgrade libgladeui along with glade3.
Requires: libgladeui = %version-%release

BuildPreReq: rpm-build-licenses rpm-build-gnome

# From configure.ac
BuildPreReq: intltool >= 0.35.0
BuildPreReq: gnome-common
BuildPreReq: gettext-tools
BuildPreReq: gtk-doc >= 1.9
BuildPreReq: libgtk+2-devel >= 2.20.0
BuildPreReq: glib2-devel
BuildPreReq: libxml2-devel >= 2.4.0
BuildPreReq: libbonoboui-devel libgnomeui-devel
BuildPreReq: python-module-pygtk-devel >= 2.10.0
BuildPreReq: gnome-doc-utils >= 0.9.0

%description
Glade 3 is a Widget builder for Gtk/gnome.
It allows to create a gtk/gnome interface files
that can be loaded with libglade.

%package -n libgladeui
Summary: GTK+ / GNOME 3 widget builder library
Group:   Development/GNOME and GTK+
Obsoletes: libgladeui3.6
Obsoletes: libgladeui3.7

%description -n libgladeui
Glade 3 is a Widget builder for Gtk/gnome.
It allows to create a gtk/gnome interface files
that can be loaded with libglade.

This is library that can be used for embed builder
into other application.

%package -n libgladeui-devel
Summary: GTK+ / GNOME widget builder library
Group:   Development/GNOME and GTK+
Requires: libgladeui = %version-%release
Obsoletes: libgladeui3.6-devel
Obsoletes: libgladeui3.7-devel

%description -n libgladeui-devel
Glade 3 is a Widget builder for Gtk/gnome.
It allows to create a gtk/gnome interface files
that can be loaded with libglade.

This package contains development files for library.

%prep
%setup -q

%build
%configure --disable-dependency-tracking \
	--disable-scrollkeeper \
	--enable-gtk-doc
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
export LD_LIBRARY_PATH=$PWD/gladeui/.libs

# SMP-incompatible build
%make

%install
%makeinstall_std

%find_lang --with-gnome %name
%find_lang --with-gnome glade

cat %name.lang glade.lang > lang

bzip2 -fk9 ChangeLog

%files -f lang
%doc AUTHORS COPYING ChangeLog.bz2 NEWS README TODO
%_bindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg

%files -n libgladeui
%dir %_libdir/%name
%dir %_libdir/%name/modules
%_libdir/%name/modules/*.so
%_libdir/*.so.*
%dir %_datadir/%name
%dir %_datadir/%name/catalogs
%_datadir/%name/catalogs/*.xml
%_datadir/%name/catalogs/*.xml.in
%_datadir/%name/catalogs/glade-catalog.dtd
%_datadir/%name/pixmaps

%files -n libgladeui-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gtk-doc/html/*

%exclude %_libdir/glade3/modules/*.la

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2.2
- Removed bad RPATH

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Apr 12 2010 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt2
- s/libgladeui3.7/libgladeui (ALT #23310)

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 3.7.0-alt1
- 3.7.0

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.6-alt1.1
- Rebuilt with python 2.6

* Sat Jun 27 2009 Alexey Rusakov <ktirf@altlinux.org> 3.6.6-alt1
- New version (3.6.6)

* Sat Jun 13 2009 Alexey Rusakov <ktirf@altlinux.org> 3.6.5-alt1
- New version (3.6.5)

* Sun May 17 2009 Alexey Rusakov <ktirf@altlinux.org> 3.6.3-alt1
- 3.6.3

* Sat Apr 11 2009 Alexey Rusakov <ktirf@altlinux.org> 3.6.1-alt1
- 3.6.1
- Added Packager tag, urlified Source
- Updated buildreqs and files list
- Removed obsolete post/postun scripts, cleaned up the specfile
- Fixed the License (it is %gpl2plus, with some parts under %lgpl2plus)
- Bzipped the ChangeLog
- Created a libgladeui3.6 package due to soname change

* Fri May 09 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.4.5-alt1
- 3.4.5

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 3.4.3-alt1.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for glade3

* Tue Mar 11 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.4.3-alt1
- 3.4.3

* Mon Jan 14 2008 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Thu Sep 20 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Tue Aug 14 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.2.2-alt2
- Build fix

* Tue May 29 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.2.2-alt1
- 3.2.2

* Mon May 07 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.2.1-alt1
- 3.2.1

* Wed Mar 14 2007 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.2.0-alt0.1
- 3.2.0

* Wed Dec 20 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Tue Oct 03 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.0.2-alt1
- 3.0.2

* Mon Aug 28 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.0.1-alt1
- 3.0.1 (bugfixes)

* Tue Aug 15 2006 Sergey N. Yatskevich <syatskevich@altlinux.ru> 3.0.0-alt0.1
- Initial release
