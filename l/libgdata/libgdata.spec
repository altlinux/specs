Name: libgdata
Version: 0.13.0
Release: alt1

Summary: Library for the GData protocol
Group: System/Libraries
License: LGPLv2+
URL: http://live.gnome.org/libgdata
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source0: %name-%version.tar.xz
#Patch: %name-%version-%release.patch

%define soup_ver 2.37.91

BuildRequires: gnome-common gtk-doc intltool libsoup-gnome-devel >= %soup_ver
BuildRequires: libxml2-devel libgdk-pixbuf-devel libgtk+3-devel liboauth-devel
BuildRequires: libgnome-keyring-devel gobject-introspection-devel libsoup-gnome-gir-devel

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol --- most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package gir
Summary: GObject introspection data for the GData library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GData library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir-devel
Summary: GObject introspection devel data for the GData library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GData library.

%prep
%setup -q
#%patch -p1

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--enable-introspection \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang gdata

%files -f gdata.lang
%doc NEWS README AUTHORS
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc
%_datadir/gtk-doc/html/gdata

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%changelog
* Sat Apr 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Apr 02 2012 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.1-alt1
- 0.11.1

* Mon Mar 12 2012 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Thu Sep 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.10.1-alt1
- 0.10.1

* Sun May 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Tue Dec 14 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.6-alt1
- 0.6.6

* Fri Oct 22 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5-alt2
- updated build dependencies

* Thu Oct 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt2
- rebuild

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Tue Mar 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt2
- rebuild

* Sun Feb 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Tue Feb 16 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Nov 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.0-alt1
- initial release

