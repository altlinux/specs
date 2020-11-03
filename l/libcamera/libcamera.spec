Name: libcamera
Version: 0.0.20201028
Release: alt1

Summary: A complex camera support library for Linux
License: LGPL-2.1-or-later
Group: Video
Url: https://libcamera.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ meson >= 0.51 openssl qt5-tools-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(udev)
BuildRequires: python3(jinja2)
BuildRequires: python3(yaml)

%package -n gst-plugins-libcamera1.0
Summary: A complex camera support library for Linux
Group: System/Libraries

%package -n qcam
Summary: A complex camera support library for Linux
Group: Video

%package devel
Summary: A complex camera support library for Linux
Group: Development/C

%description
An open source camera stack and framework for Linux, Android, and ChromeOS.

%description -n gst-plugins-libcamera1.0
An open source camera stack and framework for Linux, Android, and ChromeOS.
This package contains libcamera gstreamer plugin.

%description -n qcam
An open source camera stack and framework for Linux, Android, and ChromeOS.
This package contains Qt-based libcamera utility.

%description devel
An open source camera stack and framework for Linux, Android, and ChromeOS.
This package contains development part of libcamera.

%prep
%setup

%ifarch aarch64
%define platdefs simple,uvcvideo,rkisp1
%endif
%ifarch %ix86 x86_64
%define platdefs simple,uvcvideo,ipu3
%endif
%ifnarch aarch64 %ix86 x86_64
%define platdefs simple,uvcvideo
%endif

%build
%meson -Dpipelines=%platdefs -Dv4l2=true
%meson_build

%install
%meson_install

%files
%_bindir/cam
%_libexecdir/libcamera/ipa_proxy_linux
%_libdir/libcamera.so
%_libdir/v4l2-compat.so

%files -n gst-plugins-libcamera1.0
%_libdir/gstreamer-1.0/*

%files -n qcam
%_bindir/qcam

%files devel
%_includedir/libcamera
%_pkgconfigdir/camera.pc

%changelog
* Tue Nov 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20201028-alt1
- initial
