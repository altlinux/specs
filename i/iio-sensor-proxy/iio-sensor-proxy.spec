%define ver_major 3
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc
%def_disable gtk_tests
# tests passed in hasher on basalt for i586/x86_64 with -j16
# 1/1 iio-sensor-proxy-integration-test OK 17.21s
# but fail in girar for all architectures
# [x86_64] 1/1 iio-sensor-proxy-integration-test TIMEOUT 60.11s
%def_disable check

Name: iio-sensor-proxy
Version: %ver_major.3
Release: alt1.1

Summary: IIO sensors to input device proxy
Group: System/Kernel and hardware
License: GPL-3.0
Url: https://github.com/hadess/%name

Vcs: https://gitlab.freedesktop.org/hadess/iio-sensor-proxy.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

%define meson_ver 0.54
%define glib_ver 2.56
%define gudev_ver 237

BuildRequires(pre): meson >= %meson_ver
BuildRequires: libgio-devel >= %glib_ver pkgconfig(systemd)
BuildRequires: libudev-devel libgudev-devel >= %gudev_ver
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_gtk_tests:BuildRequires: libgtk+3-devel}
%{?_enable_check:
BuildRequires: /proc /dev/pts dbus-tools-gui python3-module-psutil
BuildRequires: python3-module-pygobject3 python3-module-dbusmock typelib(UMockdev) = 1.0}

%description
%name is a framework for accessing the various environmental sensors
(e.g., accelerometer, magnetometer, proximity, or ambient-light sensors)
built in to recent laptops. The proxy is a daemon that listens to the
Industrial I/O (IIO) subsystem and provides access to the sensor readings
over D-Bus.

As of right now, support for ambient-light sensors and accelerometers is
working; other sensor types are in development. The current API is based
on those used by Android and iOS, but may be expanded in the future. "For
future versions, we'll want to export the raw accelerometer readings, so
that applications, including games, can make use of them, which might
bring up security issues. SDL, Firefox, WebKit could all do with being
adapted, in the near future."


%package devel-doc
Summary: Developer documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
Developer documentation for %name.

%prep
%setup
%patch -p1

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	%{?_disable_gtk_tests:-Dgtk-tests=false}
%meson_build

%install
%meson_install

%check
dbus-run-session %__meson_test -t 2

%files
%_libexecdir/%name
%_bindir/monitor-sensor
%_unitdir/%name.service
%_udevrulesdir/80-%name.rules
%_sysconfdir/dbus-1/system.d/net.hadess.SensorProxy.conf
%doc README.md NEWS

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name/
%endif


%changelog
* Fri Dec 10 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1.1
- rebuilt from git

* Tue Aug 17 2021 Yuri N. Sedunov <aris@altlinux.org> 3.3-alt1
- 3.3

* Tue Jun 15 2021 Yuri N. Sedunov <aris@altlinux.org> 3.1-alt1
- 3.1 (ported to Meson build system)
- fixed License tag
- disabled check due timeout on girar infrastructure

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.0-alt1
- 3.0

* Sun Sep 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.8-alt1
- 2.8

* Sat May 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.7-alt1
- 2.7

* Thu Oct 25 2018 Yuri N. Sedunov <aris@altlinux.org> 2.5-alt1
- updated to 2.5-6-gbb35319

* Mon Nov 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.4-alt1
- 2.4

* Sun Sep 24 2017 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3

* Fri Feb 17 2017 Yuri N. Sedunov <aris@altlinux.org> 2.2-alt1
- 2.2

* Sun Feb 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.1-alt1
- 2.1

* Thu Dec 15 2016 Yuri N. Sedunov <aris@altlinux.org> 2.0-alt1
- 2.0

* Mon Sep 26 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3-alt1
- 1.3

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt2
- updated to 1.1-28-gae82958

* Mon Jul 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- 1.1

* Sat May 23 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0-alt1
- first build for Sisyphus

