%def_enable snapshot
%define ver_major 1.26

%def_enable x11_backend
%def_enable gdk_backend
%def_enable egl_backend
%def_disable tslib_input
%def_enable evdev_input
%def_enable xinput
%def_enable gdk_pixbuf
%def_enable installed_tests
%def_enable gtk_doc

# libcogl compiled with --enable-wayland-egl-platform required
%def_enable wayland_backend
# libcogl compiled with --enable-wayland-egl-server required
%def_enable wayland_compositor

Name: clutter
Version: %ver_major.4
Release: alt2

Summary: Clutter Core Library
License: LGPLv2+
Group: System/Libraries
Url: http://www.clutter-project.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.54
%define cogl_ver 1.22.6
%define json_glib_ver 0.12.0
%define atk_ver 2.5.3
%define cairo_ver 1.14
%define pango_ver 1.30
%define gi_version 1.40
%define uprof_ver 0.3
%define gtk_doc_ver 1.20
%define xfixes_ver 3
%define xcomposite_ver 0.4
%define gdk_ver 3.22.6
%define libinput_ver 0.19

BuildRequires: libGL-devel
BuildRequires: pkgconfig(cogl-1.0) >= %cogl_ver pkgconfig(cairo-gobject) >= %cairo_ver pkgconfig(atk) >= %atk_ver pkgconfig(pangocairo) >= %pango_ver pkgconfig(cogl-pango-1.0) pkgconfig(json-glib-1.0) >= %json_glib_ver
BuildRequires: gtk-doc >= %gtk_doc_ver
BuildRequires: gobject-introspection-devel gir(GL) = 1.0 gir(GObject) = 2.0 gir(cairo) = 1.0 libcogl-gir-devel gir(Atk) = 1.0 gir(Json) = 1.0
%{?_enable_x11_backend:BuildRequires: pkgconfig(pangoft2) pkgconfig(x11) pkgconfig(xext) pkgconfig(xfixes) >= %xfixes_ver pkgconfig(xdamage) pkgconfig(xcomposite) >= %xcomposite_ver }
%{?_enable_wayland_backend:BuildRequires: pkgconfig(wayland-client) pkgconfig(wayland-cursor) pkgconfig(xkbcommon) pkgconfig(gdk-pixbuf-2.0)}
%{?_enable_wayland_compositor:BuildRequires: pkgconfig(wayland-server)}
%{?_enable_gdk_backend:BuildRequires: pkgconfig(gdk-3.0) >= %gdk_ver gir(Gdk) = 3.0}
%{?_enable_tslib_input:BuildRequires: pkgconfig(tslib-1.0)}
%{?_enable_evdev_input:BuildRequires: pkgconfig(gudev-1.0) pkgconfig(xkbcommon) pkgconfig(libevdev) libinput-devel >= %libinput_ver}
%{?_enable_xinput:BuildRequires: pkgconfig(xi)}
%{?_enable_gdk_pixbuf:BuildRequires: pkgconfig(gdk-pixbuf-2.0)}

%description
Clutter is an open source software library for creating fast, visually
rich graphical user interfaces. The most obvious example of potential
usage is in media center type applications. We hope however it can be
used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but
with an API which hides the underlying GL complexity from the
developer. The Clutter API is intended to be easy to use, efficient
and flexible.

%package -n lib%name
Summary: Clutter Core Library
Group: System/Libraries

%description -n lib%name
Clutter is an open source software library for creating fast, visually
rich graphical user interfaces. The most obvious example of potential
usage is in media center type applications. We hope however it can be
used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but
with an API which hides the underlying GL complexity from the
developer. The Clutter API is intended to be easy to use, efficient
and flexible.

%package -n lib%name-devel
Summary: Header files for clutter library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for clutter library.

%package -n lib%name-gir
Summary: GObject introspection data for the clutter library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the clutter library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the clutter library
Group: System/Libraries
BuildArch: noarch
Requires: libcogl-gir-devel
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the clutter library

%package -n lib%name-devel-doc
Summary: Development package for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description  -n lib%name-devel-doc
Contains developer documentation for %name.

%package -n lib%name-tests
Summary: Tests for the lib%name package
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-tests
This package provides tests programs that can be used to verify
the functionality of the installed lib%name package.


%prep
%setup

%build
gtkdocize
%autoreconf
%configure \
	--disable-static \
	%{?_enable_x11_backend:--enable-x11-backend} \
	%{?_enable_gdk_backend:--enable-gdk-backend} \
	%{?_enable_wayland_backend:--enable-wayland_backend} \
	%{?_enable_wayland_compositor:--enable-wayland-compositor} \
	%{?_enable_egl_backend:--enable-egl-backend} \
	%{?_enable_tslib_input:--enable-tslib-input} \
	%{?_enable_xinput:--enable-xinput} \
	%{?_enable_evdev_input:--enable-evdev-input} \
	%{?_enable_gdk_pixbuf:--enable-gdk-pixbuf} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--enable-introspection \
	%{?_enable_installed_tests:--enable-installed-tests}

%make_build

%install
%makeinstall_std
%find_lang clutter-1.0

%check
#%%make check

%files -n lib%name -f clutter-1.0.lang
%doc NEWS README*
%_libdir/lib%name-*.so.*

%files -n lib%name-devel
%_includedir/%name-*
%_libdir/lib%name-*.so
%_pkgconfigdir/*.pc

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%if_enabled installed_tests
%files -n lib%name-tests
%_libexecdir/installed-tests/%name/
%_datadir/installed-tests/%name/
%endif

%exclude %_datadir/%name-1.0/valgrind


%changelog
* Thu Apr 07 2022 Yuri N. Sedunov <aris@altlinux.org> 1.26.4-alt2
- updated to 1.26.4-36-g5b477d43a

* Mon Mar 09 2020 Yuri N. Sedunov <aris@altlinux.org> 1.26.4-alt1
- 1.26.4

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt2
- updated to 1.26.2-56-g401ea54

* Fri May 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.26.2-alt1
- 1.26.2

* Sun Oct 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt2
- updated to 1.26.0-26-g7ab085c

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24.2-alt1
- 1.24.2

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0

* Tue Jun 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.4-alt1
- 1.22.4

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.2-alt1
- 1.22.2

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt0.1
- 1.22.1_8cf629d4

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Mon Sep 29 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt2
- rebuilt against libinput.so.5

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Aug 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4 release

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt0.1
- 1.18.3 snapshot (da66dd01ef)

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Sat Jan 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.16.4-alt1
- 1.16.4

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.16.3-alt0.1
- 1.16.3 snapshot (fixed BGO ##722220, 722188, 719901, 719563...)

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2
- new -tests subpackage

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Tue Jul 23 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.4-alt2.git.74f9d8
- snapshot upstream/clutter-1.14 74f9d8a597acf0fd8458e3d6cb0475b8d9a0a6ba

* Wed May 15 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.4-alt1
- 1.14.4

* Tue Apr 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt2
- enabled wayland backend

* Thu Apr 18 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Tue Mar 26 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Wed Oct 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Tue Sep 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1.11.16-alt1
- 1.11.16

* Thu Sep 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.11.14-alt1
- 1.11.14

* Wed Jun 20 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.8-alt1
- 1.10.8

* Fri Jun 15 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.6-alt1
- 1.10.6

* Wed May 02 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.4-alt1
- 1.10.4

* Tue Apr 17 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- 1.10.2

* Mon Mar 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Mon Jan 30 2012 Alexey Shabalin <shaba@altlinux.ru> 1.8.4-alt1
- 1.8.4

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Oct 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0
- add devel-doc subpackage

* Tue Jun 14 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.16-alt1
- 1.6.16 (ALT #25759)

* Wed Apr 06 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.14-alt1
- 1.6.14

* Wed Mar 23 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.10-alt1
- 1.6.10

* Fri Mar 11 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Fri Feb 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.6-alt1
- 1.6.6

* Tue Feb 08 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Mon Jan 31 2011 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Jan 24 2011 Alexey Shabalin <shaba@altlinux.ru> 1.5.14-alt1
- 1.5.14

* Thu Jan 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1.5.12-alt1
- 1.5.12

* Tue Sep 28 2010 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Sun Sep 26 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.14-alt1
- 1.2.14

* Thu Sep 16 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.12-alt1
- 1.2.12

* Tue May 11 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Tue Apr 20 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Wed Mar 31 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt2
- rebuild with modified rpm-build-gir

* Tue Mar 23 2010 Alexey Shabalin <shaba@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Tue Mar 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt2
- rebuild

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Feb 26 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Thu Feb 18 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.12-alt1
- 1.1.12

* Wed Feb 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.10-alt1
- 1.1.10

* Thu Jan 21 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Thu Jan 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.1.4-alt1
- 1.1.4

* Tue Dec 15 2009 Alexey Shabalin <shaba@altlinux.ru> 1.1.2-alt2
- enabled gobject-introspection

* Sun Oct 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Wed Sep 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.6-alt1
- 1.0.6

* Sat Aug 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Fri Aug 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Aug 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Fri Dec 12 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.4-alt1
- new version 0.8.4 (with rpmrb script)

* Fri Nov 28 2008 Vitaly Lipatov <lav@altlinux.ru> 0.8.2-alt1
- new version 0.8.2 (with rpmrb script)

* Tue May 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)

* Fri Jan 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt1
- new version 0.4.2 (with rpmrb script)

* Fri Jul 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

