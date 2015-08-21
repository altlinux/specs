%define _name ges
%define ver_major 1.5
%define gst_api_ver 1.0
%define api_ver 1.0

Name: gstreamer-editing-services
Version: %ver_major.90
Release: alt1

Summary: GStreamer Editing Services (GES)
Group: System/Libraries
License: GPLv2+ and LGPLv2+
Url: http://cgit.freedesktop.org/gstreamer/gst-editing-services/

Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz

%define gst_ver 1.5.2

Requires: lib%_name = %version-%release
Requires: gst-validate >= %gst_ver

BuildRequires: gcc-c++ flex gst-plugins%gst_api_ver-devel >= %gst_ver gst-plugins-base%gst_api_ver
BuildRequires: libgst-validate-devel libxml2-devel
BuildRequires: gobject-introspection-devel gst-plugins%gst_api_ver-gir-devel
BuildRequires: gtk-doc

%description
This is a high-level library for facilitating the creation of audio/video
non-linear editors.

%package -n lib%_name
Summary: GStreamer Editing Services (GES) library
License: LGPLv2+
Group: System/Libraries

%description -n lib%_name
GStreamer Editing Services (GES) is a high-level library for facilitating
the creation of audio/video non-linear editors.

%package -n lib%_name-devel
Summary: Development files for %name
License: LGPLv2+
Group: Development/C
Requires: lib%_name = %version-%release

%description -n lib%_name-devel
This package provides libraries and header files for developing
applications that use %name library.

%package -n lib%_name-devel-doc
Summary: GES development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%_name-devel < %version

%description -n lib%_name-devel-doc
This package contains documentation necessary to develop applications
that use GStreamer Editing Services library.

%package -n lib%_name-gir
Summary: GObject introspection data for the GES
Group: System/Libraries
Requires: lib%_name = %version-%release

%description -n lib%_name-gir
GObject introspection data for the GStreamer Editing Services library.

%package -n lib%_name-gir-devel
Summary: GObject introspection devel data for the GES
Group: Development/Other
BuildArch: noarch
Requires: lib%_name-gir = %version-%release
Requires: lib%_name-devel = %version-%release

%description -n lib%_name-gir-devel
GObject introspection devel data for the GStreamer Editing Services
library.


%prep
%setup

%build
%autoreconf
%configure --enable-gtk-doc
%make_build

%install
%makeinstall_std

%files
%_bindir/%_name-launch-%api_ver
%_datadir/gstreamer-%gst_api_ver/validate-scenario/*.scenario
%doc ChangeLog README RELEASE NEWS AUTHORS

%exclude %_libdir/gst-validate-launcher/

%files -n lib%_name
%_libdir/lib%_name-%api_ver.so.*

%files -n lib%_name-devel
%_includedir/gstreamer-%gst_api_ver/%_name/
%_libdir/*.so
%_pkgconfigdir/gst-editing-services-%api_ver.pc

%files -n lib%_name-gir
%_typelibdir/GES-%api_ver.typelib

%files -n lib%_name-gir-devel
%_girdir/GES-%api_ver.gir

%files -n lib%_name-devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/

%changelog
* Fri Aug 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

