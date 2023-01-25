%define _name ges
%define new_name gst-editing-services
%define ver_major 1.22
%define gst_api_ver 1.0
%define api_ver 1.0

%def_disable doc

Name: gstreamer-editing-services
Version: %ver_major.0
Release: alt1

Summary: GStreamer Editing Services (GES)
Group: System/Libraries
License: GPLv2+ and LGPLv2+
Url: http://cgit.freedesktop.org/gstreamer/gst-editing-services/

Source: http://gstreamer.freedesktop.org/src/%new_name/%new_name-%version.tar.xz

%define gst_ver %version

Requires: lib%_name = %EVR
Requires: gst-validate >= %gst_ver

Provides: %new_name = %EVR

# use python3
AutoReqProv: nopython
%define __python %nil
%add_python3_path %_libdir/gst-validate-launcher/python

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson gcc-c++ flex
BuildRequires: python3-devel python3-module-pygobject3-devel
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver gst-plugins-base%gst_api_ver
BuildRequires: gst-plugins-good%gst_api_ver gst-plugins-bad%gst_api_ver-devel
BuildRequires: libgst-devtools-devel libxml2-devel
BuildRequires: gobject-introspection-devel gst-plugins%gst_api_ver-gir-devel
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}

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
Requires: lib%_name = %EVR

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
Requires: lib%_name = %EVR

%description -n lib%_name-gir
GObject introspection data for the GStreamer Editing Services library.

%package -n lib%_name-gir-devel
Summary: GObject introspection devel data for the GES
Group: Development/Other
BuildArch: noarch
Requires: lib%_name-gir = %EVR
Requires: lib%_name-devel = %EVR

%description -n lib%_name-gir-devel
GObject introspection devel data for the GStreamer Editing Services
library.

%prep
%setup -n %new_name-%version

%build
%meson %{?_enable_doc:-Ddoc=disabled}
%meson_build

%install
%meson_install

%files
%_bindir/%_name-launch-%api_ver
%_datadir/gstreamer-%gst_api_ver/validate/scenarios/*.scenario
%_libdir/gstreamer-%gst_api_ver/libgstges.so
%_libdir/gstreamer-%gst_api_ver/libgstnle.so
#%_datadir/bash-completion/completions/%_name-launch-%api_ver
%_man1dir/%_name-launch-*
# gi overrides
%python3_sitelibdir_noarch/gi/overrides/*
%doc ChangeLog README* RELEASE NEWS AUTHORS

# for tests only?
%exclude %_libdir/gst-validate-launcher/python/*

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

%if_enabled doc
%files -n lib%_name-devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/
%endif

%changelog
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

* Fri Aug 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.90-alt1
- 1.5.90

* Thu Jun 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

