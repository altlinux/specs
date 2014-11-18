%define _name gstvalidate
%define ver_major 1.4
%define gst_api_ver 1.0
%define api_ver 1.0

Name: gst-validate
Version: %ver_major.0
Release: alt2

Summary: GStreamer Validate Tools and Library
Group: System/Libraries
License: GPLv2+ and LGPLv2+
Url: http://cgit.freedesktop.org/gstreamer/gst-devtools/

Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz

%define gst_ver 1.4.0

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ gst-plugins%gst_api_ver-devel >= %gst_ver gst-plugins-base%gst_api_ver libxml2-devel
BuildRequires: gobject-introspection-devel gst-plugins%gst_api_ver-gir-devel
BuildRequires: gtk-doc

%description
The goal of GstValidate is to be able to detect when elements are not
behaving as expected and report it to the user so he knows how things are
supposed to work inside a GstPipeline. In the end, fixing issues found by
the tool will ensure that all elements behave all together in the
expected way.

%package -n lib%name
Summary: GStreamer Validate library
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
GStreamer Validate library.

%package -n lib%name-devel
Summary: Development files for %name
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides libraries and header files for developing
applications that use Gst Validate library.

%package -n lib%name-devel-doc
Summary: Gst Validate development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
that use Gst Validate library.

%package -n lib%name-gir
Summary: GObject introspection data for the Gst Validate
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Gst Validate library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Gst Validate
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Gst Validate library.


%prep
%setup

%build
%autoreconf
%configure --enable-gtk-doc \
	--disable-sphinx-doc
%make_build

%install
%makeinstall_std

%find_lang %name

%files
%_bindir/%name-launcher
%_bindir/gst-validate-%api_ver
%_bindir/gst-validate-media-check-%api_ver
%_bindir/gst-validate-transcoding-%api_ver
%_libdir/%name-launcher/
%_datadir/gstreamer-%gst_api_ver/validate-scenario/

%files -n lib%name -f %name.lang
%_libdir/lib%_name-%api_ver.so.*
%_libdir/lib%_name-default-overrides-%api_ver.so.*
%doc ChangeLog README

%files -n lib%name-devel
%_includedir/gstreamer-%gst_api_ver/gst/validate/
%_libdir/lib%_name-%api_ver.so
%_libdir/lib%_name-default-overrides-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%files -n lib%name-gir
%_typelibdir/GstValidate-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GstValidate-%api_ver.gir

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/

%changelog
* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- disabled build of incomplete docs for launcher

* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

