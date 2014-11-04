%define _name gnonlin
%define ver_major 1.4
%define api_ver 1.0
%define gst_api_ver 1.0

Name: gst-plugins-gnonlin%gst_api_ver
Version: %ver_major.0
Release: alt1

Summary: GStreamer-%gst_api_ver extension library for non-linear editing
Group: Video
License: LGPL
Url: http://gstreamer.freedesktop.org/

#Source: %_name-%version.tar
Source: http://gstreamer.freedesktop.org/src/%_name/%_name-%version.tar.xz

Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver

BuildRequires: gst-plugins%gst_api_ver-devel
BuildRequires: gst-plugins-base%gst_api_ver
BuildRequires: gst-plugins-good%gst_api_ver
BuildRequires: gtk-doc

%description
Gnonlin is a library built on top of GStreamer-%gst_api_ver which
provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

%package devel-doc
Summary: Gnonlin development documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
Gnonlin is a library built on top of GStreamer-%gst_api_ver which
provides support for writing non-linear audio and video editing
applications. It introduces the concept of a timeline.

This package contains documentation necessary to develop applications
that use Gnonlin.


%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	--with-default-audiosrc=pulsesrc \
	--with-default-audiosink=pulsesink \
	--with-default-videosrc=v4l2src \
	--with-default-videosink=xvimagesink \
	--disable-static \
	--enable-gtk-doc
%make_build

%install
%makeinstall_std

%files
%_libdir/gstreamer-%gst_api_ver/libgnl.so
%doc AUTHORS NEWS RELEASE

%exclude %_libdir/gstreamer-%gst_api_ver/*.la

%files devel-doc
%_datadir/gtk-doc/html/%_name-%api_ver/


%changelog
* Tue Nov 04 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- first build for Sisyphus

