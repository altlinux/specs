%define _name clutter-gst
%define api_ver 2.0
%define gst_api_ver 1.0

%def_enable introspection
# experimental support for hardware accelerated decoders
%def_disable hw

Name: %_name%api_ver
Version: 1.9.90
Release: alt1

Summary: Library integrating clutter with GStreamer
License: LGPL v2+
Group: System/Libraries
Url: http://www.clutter-project.org/

Source: %_name-%version.tar.xz

BuildRequires: gst-plugins1.0-devel gtk-doc glib2-devel >= 2.18 libclutter-devel >= 1.6.0
%{?_enable_introspection:BuildRequires: libclutter-gir-devel gst-plugins1.0-gir-devel}
# for gstreamer-basevideo
%{?_enable_hw:BuildRequires: gst-plugins1.0-bad-devel}

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

%prep
%setup -n %_name-%version

%build
#%%autoreconf
%configure \
	--enable-gtk-doc \
	--disable-static
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
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/ClutterGst-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/ClutterGst-%api_ver.gir
%endif


%changelog
* Thu Sep 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.9.90-alt1
- first build for Sisyphus

