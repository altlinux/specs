%define oname cogl

%ifarch %arm
%def_enable gles2
%else
%def_disable gles2
%endif


%def_enable cairo
%def_disable profile

%def_enable glib
%def_enable cogl_pango
%def_enable gdk_pixbuf
%def_disable examples_install
%def_enable gl
%def_enable wayland_egl
%def_disable wayland_server
%def_disable kms_egl
%def_enable xlib_egl

Name: libcogl
Version: 1.16.1
Release: alt0.1
Summary: A library for using 3D graphics hardware to draw pretty pictures

Group: System/Libraries
License: LGPLv2+
Url: http://www.clutter-project.org/

Source: %oname-%version.tar
#Patch: %name-%version-%release.patch

Conflicts: libclutter < 1.8.0

%define glib_ver 2.32.0
%define pangocairo_ver 1.20
%define gi_ver 0.9.5
%define gdk_pixbuf_ver 2.0
%define uprof_ver 0.3
%define gtk_doc_ver 1.13
%define xfixes_ver 3
%define xcomposite_ver 0.4
%define xrandr_ver 1.2
%define cairo_ver 1.10
%define wayland_ver 1.0.0

%{?_enable_cairo:BuildRequires: pkgconfig(cairo) >= %cairo_ver pkgconfig(cairo-gobject)}
%{?_enable_profile:BuildRequires: pkgconfig(uprof-0.3) >= %uprof_ver}
%{?_enable_glib:BuildRequires: pkgconfig(gobject-2.0) pkgconfig(gmodule-no-export-2.0) pkgconfig(glib-2.0)}
%{?_enable_cogl_pango:BuildRequires: pkgconfig(pangocairo) >= %pangocairo_ver}
%{?_enable_gdk_pixbuf:BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= %gdk_pixbuf_ver}
%{?_enable_gles2:BuildRequires: pkgconfig(glesv2)}
%{?_enable_gl:BuildRequires: pkgconfig(x11) pkgconfig(gl)}
%{?_enable_wayland_egl:BuildRequires: pkgconfig(wayland-egl) >= %wayland_ver pkgconfig(wayland-client) >= %wayland_ver}
%{?_enable_kms_egl:BuildRequires: pkgconfig(gbm) pkgconfig(libdrm)}
%{?_enable_wayland_server:BuildRequires: pkgconfig(wayland-server) >= %wayland_ver}
%{?_enable_xlib_egl:BuildRequires: pkgconfig(egl) pkgconfig(x11) pkgconfig(xext) pkgconfig(xfixes) >= %xfixes_ver pkgconfig(xdamage) pkgconfig(xcomposite) >= %xcomposite_ver pkgconfig(xrandr) >= %xrandr_ver}
BuildRequires: gtk-doc >= %gtk_doc_ver
BuildRequires: gobject-introspection-devel >= %gi_ver  gir(GL) = 1.0 gir(GObject) = 2.0 gir(Pango) = 1.0 gir(PangoCairo) = 1.0

%description
Cogl is a small open source library for using 3D graphics hardware to draw
pretty pictures. The API departs from the flat state machine style of
OpenGL and is designed to make it easy to write orthogonal components that
can render without stepping on each others toes.

As well aiming for a nice API, we think having a single library as opposed
to an API specification like OpenGL has a few advantages too; like being
able to paper over the inconsistencies/bugs of different OpenGL
implementations in a centralized place, not to mention the myriad of OpenGL
extensions. It also means we are in a better position to provide utility
APIs that help software developers since they only need to be implemented
once and there is no risk of inconsistency between implementations.

Having other backends, besides OpenGL, such as drm, Gallium or D3D are
options we are interested in for the future.

%package devel
Summary: %oname development environment
Group: Development/C
Requires: %name = %version-%release
Conflicts: libclutter-devel < 1.8.0

%description devel
Header files and libraries for building and developing apps with %oname.

%package gir
Summary: GObject introspection data for the %oname
Group: System/Libraries
Requires: %name = %version-%release
Conflicts: libclutter-gir < 1.8.0

%description gir
GObject introspection data for the %oname

%package gir-devel
Summary: GObject introspection devel data for the %oname
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release %name-devel = %version-%release
Conflicts: libclutter-gir-devel < 1.8.0

%description gir-devel
GObject introspection devel data for the %oname


%package devel-doc
Summary: Development package for %oname
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Contains developer documentation for %oname.

%prep
%setup -n %oname-%version
#%%patch -p1

%build
#NOCONFIGURE=1 ./autogen.sh
%autoreconf
%configure  \
	--disable-static \
	%{subst_enable profile} \
	%{subst_enable cairo} \
	%{subst_enable glib} \
	%{?_enable_cogl_pango:--enable-cogl-pango} \
	%{?_enable_examples_install:--enable-examples-install} \
	--enable-gtk-doc \
	--enable-introspection \
	%{subst_enable gles2} \
	%{?_enable_kms_egl:--enable-kms-egl-platform } \
	%{?_enable_wayland_egl:--enable-wayland-egl-platform} \
	%{?_enable_wayland_server:--enable-wayland-egl-server} \
	%{?_enable_xlib_egl:--enable-xlib-egl-platform}

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %oname

%files -f %oname.lang
%doc COPYING NEWS README ChangeLog
%_libdir/libcogl*.so.*

%files devel
%_includedir/cogl
%_libdir/libcogl*.so
%_pkgconfigdir/*.pc

%files gir
%_typelibdir/*.typelib

%files gir-devel
%_girdir/*.gir

%files devel-doc
%_datadir/gtk-doc/html/*

%changelog
* Wed Dec 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt0.1
- 1.16.1 snapshot (7c7de71f)

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Tue Jul 23 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt3.git.ba5e54
- snapshot upstream/cogl-1.14 ba5e5410babf705f53b591579c104181dd752bec

* Tue Apr 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt2
- enabled wayland-egl backend

* Tue Mar 26 2013 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Wed Jan 09 2013 Alexey Shabalin <shaba@altlinux.ru> 1.12.2-alt1
- 1.12.2

* Wed Dec 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt2
- enable gles2 support for arm (by sbolshakov@)

* Mon Sep 24 2012 Alexey Shabalin <shaba@altlinux.ru> 1.12.0-alt1
- 1.12.0

* Tue Sep 18 2012 Alexey Shabalin <shaba@altlinux.ru> 1.11.6-alt1
- 1.11.6

* Thu Sep 06 2012 Alexey Shabalin <shaba@altlinux.ru> 1.11.4-alt1
- 1.11.4

* Wed Jul 25 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.4-alt1
- 1.10.4

* Mon Apr 23 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.2-alt1
- 1.10.2

* Mon Mar 26 2012 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt1
- 1.10.0

* Tue Oct 25 2011 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt2
- add conflicts with libclutter

* Mon Oct 17 2011 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Oct 04 2011 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- initial build for ALT Linux Sisyphus
