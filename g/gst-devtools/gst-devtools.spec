%def_disable snapshot

%define _name gstvalidate
%define ver_major 1.20
%define gst_api_ver 1.0
%define api_ver 1.0

%def_disable doc

Name: gst-devtools
Version: %ver_major.5
Release: alt1

Summary: GStreamer development and validation tools
Group: System/Libraries
License: GPLv2+ and LGPLv2+
Url: http://cgit.freedesktop.org/gstreamer/gst-devtools/

%if_disabled snapshot
Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz
%else
Vcs: https://gitlab.freedesktop.org/gstreamer/gst-devtools.git
Source: %name-%version.tar
%endif

%define gst_ver %version

Obsoletes: gst-validate < 1.17.1
Provides: gst-validate = %EVR

Requires: lib%name = %version-%release
Requires: gst-plugins-base%gst_api_ver

%add_python3_path %_libdir/gst-validate-launcher/python

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson gcc-c++ gst-plugins%gst_api_ver-devel >= %gst_ver gst-plugins-base%gst_api_ver libxml2-devel
BuildRequires: libcairo-devel gobject-introspection-devel gst-plugins%gst_api_ver-gir-devel
BuildRequires: libjson-glib-devel python3-devel
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}

%description
GStreamer development and validation tools including GstValidate, a
testing framework aiming at providing GStreamer developers tools that
check the GstElements they write behave the way they are supposed to.

%package -n lib%name
Summary: GStreamer Validate library
License: LGPLv2+
Group: System/Libraries
Obsoletes: libgst-validate < 1.17.1
Provides: libgst-validate = %EVR

%description -n lib%name
GStreamer Validate library.

%package -n lib%name-devel
Summary: Development files for %name
License: LGPLv2+
Group: Development/C
Requires: lib%name = %EVR
Obsoletes: libgst-validate-devel < 1.17.1
Provides: libgst-validate-devel = %EVR

%description -n lib%name-devel
This package provides libraries and header files for developing
applications that use Gst Validate library.

%package -n lib%name-devel-doc
Summary: Gst Validate development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %version
Obsoletes: libgst-validate-devel-doc < 1.17.1
Provides: libgst-validate-devel-doc = %EVR

%description -n lib%name-devel-doc
This package contains documentation necessary to develop applications
that use Gst Validate library.

%package -n lib%name-gir
Summary: GObject introspection data for the Gst Validate
Group: System/Libraries
Requires: lib%name = %EVR
Obsoletes: libgst-validate-gir < 1.17.1
Provides: libgst-validate-gir = %EVR

%description -n lib%name-gir
GObject introspection data for the Gst Validate library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Gst Validate
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR
Obsoletes: libgst-validate-gir-devel < 1.17.1
Provides: libgst-validate-gir-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the Gst Validate library.

%prep
%setup

%build
%meson %{?_disable_doc:-Ddoc=disabled}
%meson_build

%install
%meson_install
%find_lang %name

%files
%_bindir/gst-validate-launcher
%_bindir/gst-validate-%api_ver
%_bindir/gst-validate-media-check-%api_ver
%_bindir/gst-validate-images-check-%api_ver
%_libdir/gst-validate-launcher/
%_libdir/gstreamer-%gst_api_ver/lib%{_name}tracer.so
%_datadir/gstreamer-%gst_api_ver/validate/

%files -n lib%name -f %name.lang
%_libdir/lib%_name-%api_ver.so.*
%_libdir/lib%_name-default-overrides-%api_ver.so.*
%dir %_libdir/gstreamer-%gst_api_ver/validate/
%_libdir/gstreamer-%gst_api_ver/validate/*.so
%doc ChangeLog NEWS RELEASE

%files -n lib%name-devel
%_includedir/gstreamer-%gst_api_ver/gst/validate/
%_libdir/lib%_name-%api_ver.so
%_libdir/lib%_name-default-overrides-%api_ver.so
%_pkgconfigdir/gst-validate-%api_ver.pc

%files -n lib%name-gir
%_typelibdir/GstValidate-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GstValidate-%api_ver.gir

%if_enabled doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name-%api_ver/
%_datadir/gtk-doc/html/%name-plugins-%api_ver/
%endif

%changelog
* Tue Dec 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.5-alt1
- 1.20.5

* Thu Oct 13 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.4-alt1
- 1.20.4

* Thu Jun 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.3-alt1
- 1.20.3

* Tue May 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.2-alt1
- 1.20.2

* Mon Mar 14 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.1-alt1
- 1.20.1

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1.1
- fixed meson options

* Thu Sep 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.5-alt1
- 1.18.5

* Mon Mar 15 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.4-alt1
- 1.18.4

* Thu Jan 14 2021 Yuri N. Sedunov <aris@altlinux.org> 1.18.3-alt1
- 1.18.3

* Mon Dec 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.2-alt1
- 1.18.2

* Wed Oct 28 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.1-alt1
- 1.18.1

* Tue Sep 08 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0, renamed to gst-devtools, ported to Meson build system

* Wed Dec 04 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.2-alt1
- 1.16.2

* Tue Sep 24 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.1-alt1
- 1.16.1

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Fri Apr 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.90-alt1
- 1.15.90

* Sat Mar 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.15.2-alt1
- 1.15.2

* Fri Oct 05 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.4-alt1
- 1.14.4

* Mon Sep 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.3-alt1
- 1.14.3

* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.2-alt1
- 1.14.2

* Thu May 17 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt1
- 1.14.1

* Tue Mar 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.13.91-alt1
- 1.13.91

* Thu Dec 07 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.4-alt1
- 1.12.4

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.3-alt1
- 1.12.3

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.2-alt1
- 1.12.2

* Tue Jun 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Thu May 04 2017 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Thu Feb 23 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.4-alt1
- 1.10.4

* Mon Jan 30 2017 Yuri N. Sedunov <aris@altlinux.org> 1.10.3-alt1
- 1.10.3

* Tue Nov 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.2-alt1
- 1.10.2

* Thu Nov 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Tue Nov 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Fri Aug 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Jun 09 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Wed Apr 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt2
- rebuilt with libcairo

* Fri Aug 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Tue Nov 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2
- disabled build of incomplete docs for launcher

* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

