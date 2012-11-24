%define _name gst-plugins
%define ver_major 1.0
%define api_ver 1.0

%define _gst_datadir %_datadir/gstreamer-%api_ver
%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_enable gtk_doc

Name: %_name-ugly%api_ver
Version: %ver_major.3
Release: alt1

Summary: A set of encumbered GStreamer plugins
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Requires: gstreamer%api_ver >= 1.0.0
Requires: lib%_name%api_ver >= 1.0.0

Provides: %_name%api_ver-lame = %version-%release
Provides: %_name%api_ver-mad = %version-%release

Source: http://download.gnome.org/sources/%_name-ugly/%ver_major/%_name-ugly-%version.tar.xz
Patch: gst-plugins-ugly-1.0.1-alt-intltool.patch

BuildRequires: gcc-c++ gst-plugins%api_ver-devel gtk-doc intltool liba52-devel libcdio-devel libid3tag-devel
BuildRequires: liblame-devel libmad-devel libmpeg2-devel liboil-devel libx264-devel python-module-PyXML
BuildRequires: python-modules-encodings libopencore-amrnb-devel libopencore-amrwb-devel libdvdread-devel
BuildRequires: liborc-devel orc

%description
GStreamer Ugly Plug-ins is a set of plug-ins that have good quality
and correct functionality, but distributing them might pose problems.
The license on either the plug-ins or the supporting
libraries might not be how the developers would like.
The code might be widely known to present patent problems.

%package devel-doc
Summary: Development documentation for GStreamer Ugly plugins
Group: Development/C
BuildArch: noarch

%description devel-doc
This package contains development documentation for GStreamer Ugly plugin
collection.

%prep
%setup -n %_name-ugly-%version
%patch -p1

%build
%autoreconf
%configure \
	--disable-examples \
	--enable-experimental \
	--enable-gtk-doc \
	--disable-static \
	--with-html-dir=%_gtk_docdir

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name-ugly-%api_ver

%files -f %_name-ugly-%api_ver.lang
%doc AUTHORS NEWS README RELEASE
%_gst_libdir/*.so
%exclude %_gst_libdir/*.la
%_datadir/gstreamer-%api_ver/*

%files devel-doc
%_gtk_docdir/%_name-ugly-plugins-%api_ver/*

%changelog
* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 14 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for Sisyphus

