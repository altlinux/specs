%def_disable snapshot

%define ver_major 1.22
%define api_ver 1.6
%define gst_api_ver 1.0

%def_enable wayland
%def_disable doc
%def_disable check

Name: gstreamer-vaapi
Version: %ver_major.1
Release: alt1

Summary: GStreamer plugins to use VA-API video acceleration
Group: System/Libraries
License: LGPLv2.1
Url: http://gstreamer.freedesktop.org/modules/gstreamer-vaapi.html

%if_disabled snapshot
Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz
%else
Vcs: git://anongit.freedesktop.org/gstreamer/gstreamer-vaapi
Source: %name/%name-%version.tar
%endif

%define glib_ver 2.44
%define gst_ver %version
%define va_ver 1.1

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson glib2-devel >= %glib_ver libgtk+3-devel
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel >= %gst_ver
BuildRequires: libva-devel >= %va_ver
BuildRequires: libdrm-devel libudev-devel
BuildRequires: libGL-devel libXrandr-devel libXrender-devel
BuildRequires: libEGL-devel
%{?_enable_wayland:BuildRequires: wayland-devel libwayland-client-devel libwayland-server-devel wayland-protocols}
%{?_enable_doc:BuildRequires: hotdoc gstreamer%api_ver-utils}

%description
A collection of plugins and helper libraries to use VA-API video
acceleration from GStreamer applications.

Includes elements for video decoding, display, encoding and post-processing
using VA API (subject to hardware limitations).

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides development documentation for the collection of
plugins and helper libraries to use VA-API video acceleration from
GStreamer applications.

%prep
%setup

%build
%meson \
	%{?_disable_doc:-Ddoc=disabled} \
	%{?_disable_wayland:-Dwayland=disabled}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test -v

%files
%_libdir/gstreamer-%gst_api_ver/*.so
%doc AUTHORS NEWS README*

%if_enabled doc
%files devel-doc
%_datadir/gtk-doc/html/%name-plugins-%gst_api_ver/
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

* Mon Jun 04 2018 Yuri N. Sedunov <aris@altlinux.org> 1.14.1-alt2
- rebuilt against libva*.so.2

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

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Sun Oct 11 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- 0.6.1

* Mon Nov 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- first build for Sisyphus

