%def_disable snapshot

%define _name clutter-gst
%define ver_major 3.0
%define api_ver 3.0
%define gst_api_ver 1.0

%def_enable gtk_doc
%def_enable introspection
# experimental support for hardware accelerated decoders
%def_enable hw

Name: %_name%api_ver
Version: %ver_major.22
Release: alt1

Summary: Library integrating clutter with GStreamer
License: LGPL v2+
Group: System/Libraries
Url: http://www.clutter-project.org/
%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%define glib_ver 2.18
%define cogl_ver 1.18.2
%define clutter_ver 1.20
%define gst_ver 1.4.0

Requires: gst-plugins-base%gst_api_ver >= %gst_ver
%{?_enable_hw:Requires: gst-plugins-bad%gst_api_ver}

BuildRequires: libgio-devel >= %glib_ver gst-plugins%gst_api_ver-devel >= %gst_ver gtk-doc
BuildRequires: libcogl-devel >= %cogl_ver libclutter-devel >= %clutter_ver
BuildRequires: libgudev-devel
%{?_enable_introspection:BuildRequires: libclutter-gir-devel gst-plugins%gst_api_ver-gir-devel}
# for gstreamer-basevideo
%{?_enable_hw:BuildRequires: gst-plugins-bad%gst_api_ver-devel}

%description
Library integrating clutter with GStreamer

%package -n lib%name
Summary: Library integrating clutter with GStreamer
Group: System/Libraries

%description -n lib%name
Library integrating clutter with GStreamer

%package -n lib%name-devel
Summary: Header files for clutter-gst library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for clutter-gst library

%package -n lib%name-gir
Summary: GObject introspection data for the Clutter-Gst
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Clutter-Gst library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Clutter-Gst
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Clutter-Gst library.

%package -n gst-plugins-clutter%gst_api_ver
Summary: Clutter plugin for Gstreamer-1.0
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n gst-plugins-clutter%gst_api_ver
This package provides Clutter plugin for Gstreamer (1.0 API version)

%package -n lib%name-devel-doc
Summary: Clutter-Gst development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
that use Clutter-Gst libraries.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/libclutter-gst-*.so.*

%files -n lib%name-devel
%_includedir/clutter-*
%_libdir/libclutter-gst-*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/ClutterGst-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/ClutterGst-%api_ver.gir
%endif

%files -n gst-plugins-clutter%gst_api_ver
%_libdir/gstreamer-%gst_api_ver/libgstclutter-%api_ver.so
%exclude %_libdir/gstreamer-%gst_api_ver/libgstclutter-%api_ver.la

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Tue Dec 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.22-alt1
- 3.0.22

* Sat Nov 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.21-alt0.1
- updated to 3.0.20-5-ga71607b (fixed BGO #773810)

* Thu Sep 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.20-alt1
- 3.0.20

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.18-alt1
- 3.0.18

* Sat Feb 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.16-alt1
- 3.0.16

* Sat Oct 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.14-alt1
- 3.0.14

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.12-alt1
- 3.0.12

* Fri Sep 04 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.10-alt1
- 3.0.10

* Sat Jul 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.8-alt1
- 3.0.8

* Sun May 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.6-alt1
- 3.0.6
- moved gstreamer plugin to separate subpackage (BGO #746883)

* Sun Jan 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.99.0-alt1
- first build for Sisyphus

