%define _libexecdir %_prefix/libexec

%def_enable test
%def_disable check

Name: libcamera
Version: 0.0.2
Release: alt1
Epoch: 1

Summary: A complex camera support library for Linux
License: LGPL-2.1-or-later
Group: Video
Url: https://libcamera.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson >= 0.56
BuildRequires: openssl boost-devel qt5-tools-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
BuildRequires: pkgconfig(libevent_pthreads)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(udev)
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libexif)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(sdl2)
BuildRequires: python3(jinja2)
BuildRequires: python3(yaml)
BuildRequires: python3(ply)
%{?_enable_test:BuildRequires: pkgconfig(gtest)}

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
%patch -p1

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
%add_optflags %(getconf LFS_CFLAGS)
%meson \
    -Dpipelines=%platdefs \
    -Dv4l2=true \
    -Dwerror=false \
    %{?_enable_test:-Dtest=true}
%nil
%meson_build

%install
%meson_install
mkdir -p %buildroot%_libdir/libcamera %buildroot%_datadir/libcamera

%check
%__meson_test -v

%files
%_bindir/cam
%{?_enable_test:%_bindir/lc-compliance
%_libexecdir/libcamera/vimc_ipa_proxy}
%_bindir/libcamerify
%ifarch %ix86 x86_64
%_libexecdir/libcamera/ipu3_ipa_proxy
%endif
%ifarch aarch64
%_libexecdir/libcamera/raspberrypi_ipa_proxy
%_libexecdir/libcamera/rkisp1_ipa_proxy
%endif
%ifarch armh
%_libexecdir/libcamera/raspberrypi_ipa_proxy
%endif
%_libdir/libcamera
%_libdir/libcamera-base.so.*
%_libdir/libcamera.so.*
%_libdir/v4l2-compat.so
%_datadir/libcamera

%files -n gst-plugins-libcamera1.0
%_libdir/gstreamer-1.0/*

%files -n qcam
%_bindir/qcam

%files devel
%_includedir/libcamera
%_libdir/libcamera-base.so
%_libdir/libcamera.so
%_pkgconfigdir/libcamera-base.pc
%_pkgconfigdir/libcamera.pc

%changelog
* Thu Nov 24 2022 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.2-alt1
- 0.0.2

* Mon Oct 17 2022 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.1-alt1
- v0.0.1 release

* Thu Sep 16 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.0.20210204-alt3
- fixes for Elbrus build

* Fri Apr 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210204-alt2
- fix build with recent gstreamer

* Thu Feb 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20210204-alt1
- updated from git.336de7af

* Tue Nov 03 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20201028-alt1
- initial
