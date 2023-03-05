%define _name gst-rtsp-server
%define ver_major 1.22
%define gst_api_ver 1.0
%define api_ver 1.0

%def_disable doc
%def_enable introspection
%def_with tests_package
%{?_with_test_package:%def_enable examples}

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: GStreamer-%api_ver RTSP server library
Group: System/Libraries
License: LGPLv2+
Url: https://gstreamer.freedesktop.org/modules/%_name-server.html

Source: https://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz

%define glib_ver 2.44.0
%define gst_ver %version

Requires: gst-plugins-base%api_ver >= %gst_ver gst-plugins-good%api_ver gst-plugins-bad%api_ver

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson glib2-devel >= %glib_ver
BuildRequires: gstreamer%api_ver-devel >= %gst_ver
BuildRequires: gst-plugins%api_ver-devel >= %gst_ver gst-plugins-good%api_ver gst-plugins-bad%api_ver-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gst-plugins%api_ver-gir-devel}
BuildRequires: libcgroup-devel
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}

%description
A GStreamer-based RTSP server library.

%package devel
Summary: Development files for %_name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for the GStreamer RTSP server library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides developer documentation for %name.

%package gir
Summary: GObject introspection data for %_name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GStreamer RTSP server library.

%package gir-devel
Summary: GObject introspection devel data for %_name
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GStreamer RTSP server library.

%package tests
Summary: Tests programms from %name package
Group: System/Libraries
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the GStreamer-based RTSP server library.

%prep
%setup -n %_name-%version

%build

%meson \
	%{?_disable_introspection:-Dintrospection=disabled} \
	%{?_disable_doc:-Ddoc=disabled} \
	%{?_enable_examples:-Dexamples=enabled}
%nil
%meson_build

%install
%meson_install

%if_with tests_package
mkdir -p %buildroot%_bindir
pushd %{_target_platform}/examples
for f in test-* ; do
[ -f $f ] && install -pm755 $f %buildroot%_bindir/gst-rtsp-$f; done
popd
%endif

%files
%_libdir/libgstrtspserver-%api_ver.so.*
%_libdir/gstreamer-%gst_api_ver/libgstrtspclientsink.so
%doc README* TODO NEWS RELEASE

%files devel
%_includedir/gstreamer-%api_ver/gst/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled doc
%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/
%endif

%if_enabled introspection
%files gir
%_typelibdir/GstRtspServer-%api_ver.typelib

%files gir-devel
%_girdir/GstRtspServer-%api_ver.gir
%endif

%if_with tests_package
%files tests
%_bindir/*-test-*
%endif

%changelog
* Sat Mar 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.1-alt1
- 1.22.1

* Wed Jan 25 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

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
- 1.18.0 (ported to Meson build system)

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

* Thu Apr 19 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt2
- new optional -tests subpackage (ALT #34828)

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

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Oct 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Sat Sep 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sat Sep 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.91-alt1
- 1.5.91

* Thu Aug 20 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Mon Jun 08 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Sun Dec 28 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.5-alt1
- 1.4.5

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- first build for Sisyphus

