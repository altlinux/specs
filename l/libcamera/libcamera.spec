%define _libexecdir %_prefix/libexec

%def_enable qcam
%def_enable test
%def_disable check

Name: libcamera
Version: 0.3.1
Release: alt1.1
Epoch: 1

Summary: A complex camera support library for Linux
License: LGPL-2.1-or-later
Group: Video
Url: https://libcamera.org/

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ meson >= 0.56
BuildRequires: openssl boost-devel
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
BuildRequires: pkgconfig(libevent_pthreads)
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
%if_enabled qcam
BuildRequires: qt6-tools-devel
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6OpenGLWidgets)
BuildRequires: pkgconfig(Qt6Widgets)
%endif
%{?_enable_test:BuildRequires: pkgconfig(gtest)}

%package -n gst-plugins-%{name}1.0
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

%description -n gst-plugins-%{name}1.0
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
sed -i "s|_symbol('QOpenGLWidget', |(|" src/apps/qcam/meson.build
# workaround for EDG frontend
sed -i "s|g_autofree gchar \*|g_autofree_edg(gchar) |" src/gstreamer/gstlibcamera*.cpp
sed -i "s|get(camera_name)|get((gchar*)camera_name)|" src/gstreamer/gstlibcamerasrc.cpp
sed -i "s|\"caps\", caps|\"caps\", (GstCaps*)caps|" src/gstreamer/gstlibcameraprovider.cpp
%endif

%ifarch armh
%define platdefs auto
%endif
%ifarch aarch64
%define platdefs auto
%endif
%ifarch %ix86 x86_64
%define platdefs auto
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
%_libexecdir/%name/vimc_ipa_proxy}
%_bindir/libcamerify
%ifarch %ix86 x86_64
%_libexecdir/%name/ipu3_ipa_proxy
%endif
%ifarch aarch64
%_libexecdir/%name/raspberrypi_ipa_proxy
%_libexecdir/%name/rkisp1_ipa_proxy
%endif
%ifarch armh
%_libexecdir/%name/raspberrypi_ipa_proxy
%_libexecdir/%name/rkisp1_ipa_proxy
%endif
%ifnarch ppc64le
%_libexecdir/%name/soft_ipa_proxy
%endif
%_libdir/%name
%_libdir/%name-base.so.*
%_libdir/%name.so.*
# moved to libexecdir since 0.1.0
%_libexecdir/%name/v4l2-compat.so
%_datadir/%name/

%files -n gst-plugins-%{name}1.0
%_libdir/gstreamer-1.0/*

%if_enabled qcam
%files -n qcam
%_bindir/qcam
%endif

%files devel
%_includedir/%name
%_libdir/%name-base.so
%_libdir/%name.so
%_pkgconfigdir/%name-base.pc
%_pkgconfigdir/%name.pc

%changelog
* Wed Jul 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1:0.3.1-alt1.1
- no soft_ipa_proxy for ppc64le

* Wed Jul 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1:0.3.1-alt1
- updated to v0.3.1-4-g98b01768

* Thu May 23 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1:0.3.0-alt2
- fix e2k build

* Mon May 20 2024 Yuri N. Sedunov <aris@altlinux.org> 1:0.3.0-alt1
- 0.3.0

* Thu Jan 11 2024 Yuri N. Sedunov <aris@altlinux.org> 1:0.2.0-alt1
- 0.2.0

* Fri Jul 21 2023 Yuri N. Sedunov <aris@altlinux.org> 1:0.1.0-alt2
- set 'pipelines' to 'auto' for %%ix86, x86_64, aarch64 and armh

* Thu Jul 20 2023 Yuri N. Sedunov <aris@altlinux.org> 1:0.1.0-alt1
- 0.1.0

* Tue May 02 2023 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.5-alt1.1
- 0.0.5

* Thu Apr 27 2023 Michael Shigorin <mike@altlinux.org> 1:0.0.4-alt1.1
- E2K: updated sed patch

* Sun Feb 05 2023 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.4-alt1
- 0.0.4

* Mon Dec 26 2022 Yuri N. Sedunov <aris@altlinux.org> 1:0.0.3-alt1
- updated to v0.0.3-10-g0a8ac1ee

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
