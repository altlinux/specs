%define oname cogl

%ifarch %arm
%def_enable gles2
%else
%def_disable gles2
%endif

%def_disable wayland_egl
%def_disable wayland_server
%def_disable kms_egl_platform


Name: libcogl
Version: 1.12.2
Release: alt1
Summary: A library for using 3D graphics hardware to draw pretty pictures

Group: System/Libraries
License: LGPLv2+
Url: http://www.clutter-project.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Conflicts: libclutter < 1.8.0

BuildRequires: libcairo-devel libcairo-gobject-devel
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: libgdk-pixbuf-devel
BuildRequires: gtk-doc
BuildRequires: libXcomposite-devel libXext-devel libXdamage-devel libX11-devel libXfixes-devel
BuildRequires: libGL-devel 
BuildRequires: libpango-devel libpango-gir-devel
%{?_enable_gles2:BuildRequires: libGLES-devel >= 8.0}
%{?_enable_wayland_egl:BuildRequires: libwayland-client-devel libwayland-egl-devel}
%{?_enable_wayland_server:BuildRequires: libwayland-server-devel}
%{?_kms_egl_platform:BuildRequires: libdrm-devel libgbm-devel}

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
%setup -q
%patch -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure  \
	--disable-static \
	--enable-gtk-doc \
	--enable-introspection \
	%{subst_enable gles2} \
	%{?_kms_egl_platform:--enable-kms-egl-platform } \
	%{?_enable_wayland_egl:--enable-wayland-egl-platform} \
	%{?_enable_wayland_server:--enable-wayland-egl-server}

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
