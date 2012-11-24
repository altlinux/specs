%define _name gst-plugins
%define ver_major 1.0
%define api_ver 1.0

%define _gst_datadir %_datadir/gstreamer-%api_ver
%define _gst_libdir %_libdir/gstreamer-%api_ver
%define _gtk_docdir %_datadir/gtk-doc/html

%def_enable gtk_doc

Name: %_name-good%api_ver
Version: %ver_major.3
Release: alt2

Summary: A set of GStreamer plugins considered good
Group: System/Libraries
License: LGPL
URL: http://gstreamer.freedesktop.org/

Source: http://download.gnome.org/sources/%_name-good/%ver_major/%_name-good-%version.tar.xz
Patch: gst-plugins-good-0.11.94-alt-intltool.patch

BuildRequires: bzlib-devel gcc-c++ gst-plugins%api_ver-devel gtk-doc intltool libSM-devel libXdamage-devel libXext-devel
BuildRequires: libXv-devel libavc1394-devel libcairo-devel libdv-devel libflac-devel libiec61883-devel libjpeg-devel
BuildRequires: liboil-devel libpulseaudio-devel libshout2-devel libsoup-devel libtag-devel libv4l-devel libwavpack-devel
BuildRequires: python-module-PyXML python-modules-email python-modules-encodings liborc-devel orc libgdk-pixbuf-devel
BuildRequires: libjack-devel libpng-devel libcairo-gobject-devel libgudev-devel libspeex-devel zlib-devel libvpx-devel

%description
GStreamer Good Plug-ins is is a set of plug-ins that the developers consider
to have good quality code, correct functionality, and their preferred license
(LGPL for the plug-in code, LGPL or LGPL-compatible for the supporting
library).

%package devel-doc
Summary: Development documentation for GStreamer Good plugins
Group: Development/C
BuildArch: noarch

%description devel-doc
This package contains development documentation for GStreamer Good Plugins

%prep
%setup -n %_name-good-%version
%patch -p1

%build
%autoreconf
%configure \
	--enable-experimental \
	--disable-examples \
	--disable-valgrind \
	--disable-oss \
	--disable-oss4 \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-debug \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %_name-good-%api_ver

%files -f %_name-good-%api_ver.lang
%dir %_gst_libdir
%_gst_libdir/*.so
%exclude %_gst_libdir/*.la
%_gst_datadir
%doc AUTHORS NEWS README RELEASE

%files devel-doc
%_gtk_docdir/*

%changelog
* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt2
- 1.0.3

* Tue Nov 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- built lost vp8 plugins

* Thu Oct 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Sun Oct 07 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 17 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.99-alt1
- 0.11.99

* Fri Sep 14 2012 Yuri N. Sedunov <aris@altlinux.org> 0.11.94-alt1
- first build for Sisyphus

