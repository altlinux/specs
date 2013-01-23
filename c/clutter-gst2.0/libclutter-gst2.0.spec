%define _name clutter-gst
%define api_ver 2.0
%define gst_api_ver 1.0

%def_enable gtk_doc
%def_enable introspection
# experimental support for hardware accelerated decoders
%def_disable hw

Name: %_name%api_ver
Version: 2.0.0
Release: alt1

Summary: Library integrating clutter with GStreamer
License: LGPL v2+
Group: System/Libraries
Url: http://www.clutter-project.org/

Source: %_name-%version.tar.xz
Patch: clutter-gst-1.9.90-alt-gtk-doc.patch

BuildRequires: gst-plugins%gst_api_ver-devel gtk-doc glib2-devel >= 2.18 libclutter-devel >= 1.6.0
%{?_enable_introspection:BuildRequires: libclutter-gir-devel gst-plugins%gst_api_ver-gir-devel}
# for gstreamer-basevideo
%{?_enable_hw:BuildRequires: gst-plugins%gst_api_ver-bad-devel}

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
%patch

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/libclutter-gst-*.so.*
%_libdir/gstreamer-%gst_api_ver/libgstclutter.so
%exclude %_libdir/gstreamer-%gst_api_ver/libgstclutter.la

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

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Wed Jan 23 2013 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Sep 26 2012 Yuri N. Sedunov <aris@altlinux.org> 1.9.92-alt1
- 1.9.92

* Sat Sep 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.9.90-alt2
- fixed path to html documentation to avoid conflict with clutter-gst-1.0

* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.9.90-alt1
- first build for Sisyphus

