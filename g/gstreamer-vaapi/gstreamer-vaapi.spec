%define ver_major 0.5
%define api_ver 1.0
%define gst_api_ver 1.0
%def_enable wayland
%def_disable gtk_doc

Name: gstreamer-vaapi
Version: %ver_major.9
Release: alt1

Summary: GStreamer plugins to use VA-API video acceleration
Group: System/Libraries
License: LGPLv2.1
Url: http://freedesktop.org/wiki/Software/vaapi/

# VCS: git://gitorious.org/vaapi/gstreamer-vaapi.git
Source: http://www.freedesktop.org/software/vaapi/releases/%name/%name-%version.tar.bz2

%define glib_ver 2.28
%define gst_ver 1.0
%define va_ver 1.1

BuildRequires: glib2-devel >= %glib_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel >= %gst_ver
BuildRequires: libva-devel >= %va_ver
BuildRequires: libdrm-devel libudev-devel libGL-devel libvpx-devel
BuildRequires: gtk-doc
%{?_enable_wayland:BuildRequires: wayland-devel libwayland-client-devel libwayland-server-devel}

%description
A collection of plugins and helper libraries to use VA-API video
acceleration from GStreamer applications.

Includes elements for video decoding, display, encoding and post-processing
using VA API (subject to hardware limitations).

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name helper libraries.

%prep
%setup

%build
%autoreconf
%configure \
	--disable-static \
	--disable-builtin-libvpx \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable wayland}

%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*
%_libdir/gstreamer-%gst_api_ver/*.so
%doc AUTHORS NEWS README

%exclude %_libdir/gstreamer-%gst_api_ver/*.la

%files devel
%_includedir/gstreamer-%gst_api_ver/gst/vaapi/
%_libdir/*.so
%_pkgconfigdir/gstreamer-vaapi*.pc

%changelog
* Mon Nov 17 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.9-alt1
- first build for Sisyphus

