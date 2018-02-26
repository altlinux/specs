# libcogl compiled with --enable-wayland-egl-platform required
%def_disable wayland
# libcogl compiled with --enable-wayland-egl-server required
%def_disable wayland_compositor

Name: clutter
Version: 1.10.8
Release: alt1
Summary: Clutter Core Library
License: LGPLv2+
Group: System/Libraries
Url: http://www.clutter-project.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar
# Patch: %name-%version-%release.patch

%define glib_ver 2.31.19
%define cogl_ver 1.9.8

BuildRequires: gtk-doc
BuildRequires: libGL-devel libXcomposite-devel libXext-devel libXdamage-devel libXi-devel libX11-devel libXfixes-devel
BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: libgio-devel >= %glib_ver libgudev-devel libpango-devel libpango-gir-devel
BuildRequires: gobject-introspection-devel libatk-devel libatk-gir-devel libjson-glib-devel libjson-glib-gir-devel
BuildRequires: libcogl-devel >= %cogl_ver libcogl-gir-devel
%{?_enable_wayland:BuildRequires: libwayland-client-devel libxkbcommon-devel libgdk-pixbuf-devel}
%{?_enable_wayland_compositor:BuildRequires: libwayland-server-devel}

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


%prep
%setup -q
# %%patch -p1

%build
%autoreconf
%configure \
	--enable-xinput \
	--enable-gtk-doc \
	--enable-introspection \
	--disable-static \
	%{?_enable_wayland:--enable-wayland-backend=yes} \
	%{?_enable_wayland_compositor:--enable-wayland-compositor=yes}

%make_build

%install
%make DESTDIR=%buildroot install
%find_lang clutter-1.0

%check
#%%make check

%files -n lib%name -f clutter-1.0.lang
%doc NEWS README
%_libdir/lib%name-*.so.*

%files -n lib%name-devel
%_includedir/%name-*
%_libdir/lib%name-*.so
%_pkgconfigdir/*.pc

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*


%changelog
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

