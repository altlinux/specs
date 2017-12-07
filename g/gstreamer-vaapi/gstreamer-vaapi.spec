%define ver_major 1.12
%define api_ver 1.6
%define gst_api_ver 1.0

%def_enable wayland
%def_enable gtk_doc

Name: gstreamer-vaapi
Version: %ver_major.4
Release: alt1

Summary: GStreamer plugins to use VA-API video acceleration
Group: System/Libraries
License: LGPLv2.1
Url: http://gstreamer.freedesktop.org/modules/gstreamer-vaapi.html

# VCS: git://anongit.freedesktop.org/gstreamer/gstreamer-vaapi
# Source: %name/%name-%version.tar
Source: http://gstreamer.freedesktop.org/src/%name/%name-%version.tar.xz
# VA/GLX specific APIs dropped in 5.10
Patch: %name-0.6.1-alt-pkgconfig.patch

%define glib_ver 2.28
%define gst_ver 1.6
%define va_ver 1.1

BuildRequires: glib2-devel >= %glib_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel >= %gst_ver
BuildRequires: libva-devel >= %va_ver
BuildRequires: libdrm-devel libudev-devel
BuildRequires: libGL-devel libXrandr-devel libXrender-devel
BuildRequires: gtk-doc
%{?_enable_wayland:BuildRequires: wayland-devel libwayland-client-devel libwayland-server-devel}

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
#%%patch

%build
%autoreconf
%configure \
	--disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable wayland}

%make_build

%install
%makeinstall_std

%files
%_libdir/gstreamer-%gst_api_ver/*.so
%doc AUTHORS NEWS README

%exclude %_libdir/gstreamer-%gst_api_ver/*.la

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name-plugins-%gst_api_ver/
%endif

%changelog
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

