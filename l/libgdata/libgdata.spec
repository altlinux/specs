%def_enable gnome
%def_enable goa

Name: libgdata
Version: 0.14.1
Release: alt1

Summary: Library for the GData protocol
Group: System/Libraries
License: LGPLv2+
URL: http://live.gnome.org/libgdata
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar.xz

%define soup_ver 2.37.91
%define goa_ver 3.7.90

BuildRequires: gnome-common gtk-doc intltool
BuildRequires: libgdk-pixbuf-devel libgtk+3-devel liboauth-devel gobject-introspection-devel
%{?_enable_gnome:BuildRequires: gcr-libs-devel libxml2-devel libsoup-gnome-devel >= %soup_ver libsoup-gnome-gir-devel}
%{?_enable_goa:BuildRequires: libgnome-online-accounts-devel >= %goa_ver libgnome-online-accounts-gir-devel}

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
%setup
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	%{subst_enable gnome} \
	%{subst_enable goa} \
	--enable-introspection \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang gdata

%check
# network connection required for tests
#%%make check

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
* Thu Dec 19 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Thu Aug 29 2013 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Tue Feb 26 2013 Yuri N. Sedunov <aris@altlinux.org> 0.13.3-alt1
- 0.13.3

* Sun Sep 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.2-alt1
- 0.13.2

* Mon Jul 30 2012 Yuri N. Sedunov <aris@altlinux.org> 0.13.1-alt1
- 0.13.1

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

