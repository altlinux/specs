Name: ustreamer
Version: 5.38
Release: alt1

Summary: Lightweight MJPEG stream server
License: GPLv3
Group: Video
Url: https://github.com/pikvm/ustreamer

Source0: %name-%version-%release.tar

%package plugin-janus
Summary: Ustreamer plugin for Janus
Group: Networking/Other

%package -n python3-module-ustreamer
Summary: Python bindings for ustreamer
Group: Development/Python

BuildRequires: kvmd-janus-devel
BuildRequires: libalsa-devel
BuildRequires: libbsd-devel
BuildRequires: libevent-devel
BuildRequires: libgpiod-devel
BuildRequires: libjansson-devel
BuildRequires: libjpeg-devel
BuildRequires: libopus-devel
BuildRequires: libspeexdsp-devel
BuildRequires: libsystemd-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%define desc uStreamer is a lightweight and very quick server \
to stream MJPEG video from any V4L2 device to the net.\
All new browsers have native support of this video format,\
as well as most video players such as mplayer, VLC etc.

%description
%desc

%description plugin-janus
%desc
This package contains plugin for Janus WebRTC Server

%description -n python3-module-ustreamer
%desc
This package contains Python bindings.

%define defs WITH_GPIO=1 WITH_SYSTEMD=1 WITH_JANUS=1

%prep
%setup
grep -Elr '^#include\s+<janus' janus/ |xargs sed -i 's,<janus/,<kvmd-janus/,'
sed -ri -e '/^_CFLAGS/ s,$, -I/usr/include/kvmd-janus,' \
        -e 's,/lib/ustreamer/janus,/%_lib/kvmd-janus/plugins,' \
janus/Makefile

%build
make %defs
%pyproject_build python

%install
make install %defs DESTDIR=%buildroot PREFIX=%prefix
%pyproject_install python/dist/*.whl

%files
%doc README*
%_bindir/ustreamer
%_bindir/ustreamer-dump
%_man1dir/ustreamer.1*
%_man1dir/ustreamer-dump.1*

%files plugin-janus
%_libdir/kvmd-janus/plugins/*.so

%files -n python3-module-ustreamer
%python3_sitelibdir/ustreamer-%version.dist-info
%python3_sitelibdir/ustreamer.*.so

%changelog
* Wed Mar 01 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.38-alt1
- 5.38 released

* Thu Jan 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.36-alt1
- 5.36 released

* Thu Dec 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.35-alt1
- 5.35 released

* Wed Dec  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 5.34-alt1
- 5.34 released
