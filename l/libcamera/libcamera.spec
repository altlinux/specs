Name: libcamera
Version: 0.0.20210204
Release: alt3

Summary: A complex camera support library for Linux
License: LGPL-2.1-or-later
Group: Video
Url: https://libcamera.org/

Source: %name-%version-%release.tar

BuildRequires: gcc-c++ meson >= 0.51 openssl boost-devel qt5-tools-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
BuildRequires: pkgconfig(libevent_pthreads)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(udev)
BuildRequires: python3(jinja2)
BuildRequires: python3(yaml)
BuildRequires: python3(ply)

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
%ifarch %e2k
sed -i "s|_symbol('QOpenGLWidget', |(|" src/qcam/meson.build
# workaround for EDG frontend
sed -i "s|g_autofree gchar \*|g_autofree_edg(gchar) |" src/gstreamer/gstlibcamerasrc.cpp
sed -i "s|\"caps\", caps|\"caps\", (GstCaps*)caps|" src/gstreamer/gstlibcameraprovider.cpp
%endif

%ifarch armh
%define platdefs simple,raspberrypi,uvcvideo
%endif
%ifarch aarch64
%define platdefs simple,raspberrypi,rkisp1,uvcvideo
%endif
%ifarch %ix86 x86_64
%define platdefs ipu3,uvcvideo
%endif
%ifnarch armh aarch64 %ix86 x86_64
%define platdefs uvcvideo
%endif

%build
%meson -Dpipelines=%platdefs -Dv4l2=true -Dwerror=false
%meson_build

%install
%meson_install
mkdir -p %buildroot%_libdir/libcamera %buildroot%_datadir/libcamera

%files
%_bindir/cam
%_libexecdir/libcamera/ipa_proxy_linux
%_libdir/libcamera
%_libdir/libcamera.so
%_libdir/v4l2-compat.so
%_datadir/libcamera

%files -n gst-plugins-libcamera1.0
%_libdir/gstreamer-1.0/*

%files -n qcam
%_bindir/qcam

%files devel
%_includedir/libcamera
%_pkgconfigdir/camera.pc

%changelog
* Thu Sep 16 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.0.20210204-alt3
- fixes for Elbrus build

* Fri Apr 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210204-alt2
- fix build with recent gstreamer

* Thu Feb 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210204-alt1
- updated from git.336de7af

* Tue Nov 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20201028-alt1
- initial
