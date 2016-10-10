%define ver_major 1.8
%define gst_api_ver 1.0
%define _name gstreamermm

%def_disable plugins_bad
%def_disable examples
%def_disable tests

Name: lib%_name%gst_api_ver
Version: %ver_major.0
Release: alt1

Summary: C++ wrapper for GStreamer (1.0 API) library
Group: System/Libraries
License: LGPLv2+
Url: http://www.gtkmm.org/

Source: http://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.48
%define gst_ver 1.8.0

BuildRequires: mm-common doxygen gcc-c++ libglibmm-devel >= %glib_ver
BuildRequires: gst-plugins%gst_api_ver-devel >= %gst_ver
%{?_enable_plugins_bad:BuildRequires: gst-plugins-bad%gst_api_ver-devel}
%{?_enable_examples:BuildRequires: libgtkmm3-devel}

%description
GStreamermm provides C++ bindings for the GStreamer (1.0 API) streaming multimedia
library (http://gstreamer.freedesktop.org).  With GStreamermm it is possible to
develop applications that work with multimedia in C++.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for developing
GStreamermm applications.

%package doc
Summary: GStreamermm documentation
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description doc
This package contains all API documentation for the GStreamermm library.

%prep
%setup -n %_name-%version

%build
%configure %{subst_enable examples} \
		%{subst_enable tests} \
		%{?_disable_plugins_bad:--disable-plugins-bad}
%make_build

%install
%makeinstall_std

%files
%_libdir/lib%_name-%gst_api_ver.so.*
%{?_enable_plugins_bad:%_libdir/lib%_name-plugins-bad-%gst_api_ver.so.*}
%doc AUTHORS ChangeLog NEWS README

%files devel
%_includedir/gstreamermm-%gst_api_ver/
%_libdir/%_name-%gst_api_ver/
%_libdir/lib%_name-%gst_api_ver.so
%{?_enable_plugins_bad:%_libdir/lib%_name-plugins-bad-%gst_api_ver.so}
%_pkgconfigdir/%_name-%gst_api_ver.pc
%{?_enable_plugins_bad:%_pkgconfigdir/%_name-plugins-bad-%gst_api_ver.pc}

%files doc
%_datadir/devhelp/books/%_name-%gst_api_ver/
%_datadir/doc/%_name-%gst_api_ver/


%changelog
* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- first build for Sisyphus

