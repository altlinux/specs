Name: clutter-gtk
Version: 0.10.8
Release: alt3
Summary: Library integrating clutter with GTK+
License: LGPL v2+
Group: System/Libraries
Url: http://www.clutter-project.org/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc libclutter-devel gobject-introspection-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires: libclutter-gir-devel libpango-gir-devel libjson-glib-gir-devel

%description
Library integrating clutter with GTK+

%package -n lib%name
Summary: Library integrating clutter with GTK+
Group: System/Libraries

%description -n lib%name
Library integrating clutter with GTK+

%package -n lib%name-devel
Summary: Header files for clutter-gtk library
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for clutter-gtk library

%package -n lib%name-gir
Summary: GObject introspection data for the clutter-gtk library
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: gir-repository libclutter-gir

%description -n lib%name-gir
GObject introspection data for the clutter-gtk library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the clutter-gtk library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: gir-repository-devel libclutter-gir-devel

%description -n lib%name-gir-devel
GObject introspection devel data for the clutter-gtk library

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--enable-introspection \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%doc AUTHORS NEWS
%_libdir/lib%name-*.so.*

%files -n lib%name-devel
%doc %_datadir/gtk-doc/html/*
%_includedir/clutter-*
%_libdir/lib%name-*.so
%_pkgconfigdir/*.pc

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir

%changelog
* Thu Mar 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.8-alt3
- rebuild against libclutter-1.10.0
- removed g_thread_init() call that is now deprecated

* Fri Sep 23 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.8-alt2
- rebuild against libclutter-1.8.0

* Tue Nov 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.8-alt1
- 0.10.8

* Thu Sep 16 2010 Alexey Shabalin <shaba@altlinux.ru> 0.10.6-alt1
- 0.10.6

* Sat Apr 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt7
- fixed build with newer gtk+

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.2-alt6
- rebuild

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.2-alt5
- rebuild

* Sat Mar 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.2-alt4
- fixed build with latest clutter

* Wed Feb 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.10.2-alt3
- src.rpm: renamed to clutter-gtk

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 0.10.2-alt2
- enabled gobject-introspection

* Tue Aug 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.10.2-alt1
- 0.10.2

* Fri Nov 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Tue May 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- new version 0.4.0 (with rpmrb script)

* Sat Jul 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

