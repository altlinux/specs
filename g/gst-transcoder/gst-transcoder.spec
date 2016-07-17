%def_disable snapshot
%define ver_major 1.8
%define api_ver 1.0
%define gst_api_ver 1.0

Name: gst-transcoder
Version: %ver_major.1
Release: alt1

Summary: GStreamer Transcoding library
Group: System/Libraries
License: LGPLv2.1
Url: https://github.com/pitivi/gst-transcoder

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
# VCS: https://github.com/pitivi/gst-transcoder.git
Source: %name/%name-%version.tar
%endif

%define gst_ver 1.8.2

BuildRequires: meson
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
BuildRequires: gst-plugins-bad%gst_api_ver-devel >= %gst_ver
BuildRequires: gobject-introspection-devel gst-plugins%gst_api_ver-gir-devel

%description
This package provides GStreamer Transcoding library, tool and
GStreamer plugin.

%package devel
Summary: Development files for GStreamer Transcoder
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides development files for GStreamer Transcoder.

%prep
%setup

%build
./configure --prefix=%_prefix --libdir=%_lib
%make_build

%install
%makeinstall_std

%files
%_bindir/gst-transcoder-%api_ver
%_libdir/libgsttranscoder-%api_ver.so*
%_typelibdir/GstTranscoder-%api_ver.typelib
%_libdir/gstreamer-%gst_api_ver/*.so

%files devel
%_includedir/gstreamer-%api_ver/gst/transcoder/
#%_libdir/libgsttranscoder-%api_ver.so
%_pkgconfigdir/gst-transcoder-%api_ver.pc
%_girdir/GstTranscoder-%api_ver.gir


%changelog
* Sun Jul 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Fri Jul 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

