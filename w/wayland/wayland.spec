%def_disable snapshot
%def_enable doc
%def_enable check
# since mesa-18.0 wayland-egl moved to this wayland package
%define main_ver 1.23.1
%define egl_ver 18.1.0
%define mesa_epoch 4

Name: wayland
Version: %main_ver
Release: alt1.1

Summary: Wayland protocol libraries
Group: System/X11
License: MIT
Url: http://%name.freedesktop.org/

%if_disabled snapshot
Source: https://gitlab.freedesktop.org/%name/%name/-/releases/%version/downloads/%name-%version.tar.xz
%else
Vcs: https://gitlab.freedesktop.org/wayland/wayland.git
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson >= 0.56
BuildRequires: /proc meson gcc-c++ doxygen libexpat-devel libffi-devel
BuildRequires: libxml2-devel xsltproc docbook-style-xsl
%{?_enable_doc:BuildRequires: graphviz >= 2.26 xmlto fonts-ttf-roboto fonts-ttf-google-noto-sans-vf}

%description
Wayland is a project to define a protocol for a compositor to talk to
its clients as well as a library implementation of the protocol. The
compositor can be a standalone display server running on Linux kernel
modesetting and evdev input devices, an X applications, or a wayland
client itself. The clients can be traditional applications, X servers
(rootless or fullscreen) or other display servers.

See https://wayland.freedesktop.org/releases.html for release news.

%package devel
Summary: Common headers for Wayland
Group: Development/C

%description devel
Common headers for Wayland.

%package devel-doc
Summary: Common headers for Wayland
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package provides development documentation for Wayland.

%package -n lib%name-client
Summary: Wayland client library
Group: System/Libraries

%description -n lib%name-client
Wayland client shared library.

%package -n lib%name-client-devel
Summary: Development files for Wayland client library
Group: Development/C
Requires: lib%name-client = %EVR
Requires: %name-devel = %EVR

%description -n lib%name-client-devel
This package provides development files for Wayland client library.

%package -n lib%name-server
Summary: Wayland server library
Group: System/Libraries

%description -n lib%name-server
Wayland server shared library.

%package -n lib%name-server-devel
Summary: Development files for Wayland server library
Group: Development/C
Requires: lib%name-server = %EVR
Requires: %name-devel = %EVR

%description -n lib%name-server-devel
This package provides development files for Wayland server library.

%package -n lib%name-cursor
Summary: Wayland cursor helper library
Group: System/Libraries
Requires: lib%name-client = %EVR

%description -n lib%name-cursor
Wayland cursor helper shared library.

%package -n lib%name-cursor-devel
Summary: Wayland cursor helper library
Group: Development/C
Requires: lib%name-cursor = %EVR
Requires: lib%name-client-devel = %EVR

%description -n lib%name-cursor-devel
This package provides development files for Wayland cursor helper library.

%package -n lib%name-egl
Epoch: %mesa_epoch
Version: %egl_ver
Summary: Wayland-EGL library
Group: System/Libraries
Requires: lib%name-client = %main_ver-%release

%description -n lib%name-egl
EGL library for Wayland

%package -n lib%name-egl-devel
Version: %egl_ver
Epoch: %mesa_epoch
Summary: Wayland-EGL development package
Group: Development/C
Requires: lib%name-egl = %epoch:%egl_ver-%release
Requires: lib%name-client-devel = %main_ver-%release

%description -n libwayland-egl-devel
Wayland-EGL development package

%prep
%setup

%build
%meson \
    %{?_disable_doc:-Ddocumentation=false}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files devel
%_bindir/%name-scanner
%_includedir/%name-util.h
%_includedir/%name-version.h
%_datadir/aclocal/%name-scanner.*
%_pkgconfigdir/%name-scanner.pc
%dir %_datadir/%name
%_datadir/%name/%name-scanner.mk
%_datadir/%name/%name.xml
%_datadir/%name/wayland.dtd

%if_enabled doc
%files devel-doc
%_man3dir/*
%dir %_datadir/doc/%name
%_datadir/doc/%name/Wayland/
%endif

%files -n lib%name-client
%_libdir/lib%name-client.so.*
%doc README* COPYING

%files -n lib%name-client-devel
%_includedir/%name-client*.h
%_includedir/%name-egl-core.h
%_includedir/wayland-egl.h
%_libdir/lib%name-client.so
%_pkgconfigdir/%name-client.pc

%files -n lib%name-server
%_libdir/lib%name-server.so.*

%files -n lib%name-server-devel
%_includedir/%name-server*.h
%_libdir/lib%name-server.so
%_pkgconfigdir/%name-server.pc

%files -n lib%name-cursor
%_libdir/lib%name-cursor.so.*

%files -n lib%name-cursor-devel
%_includedir/%name-cursor.h
%_libdir/lib%name-cursor.so
%_pkgconfigdir/%name-cursor.pc

%files -n lib%name-egl
%_libdir/lib%name-egl.so.*

%files -n lib%name-egl-devel
%_includedir/wayland-egl-backend.h
%_libdir/lib%name-egl.so
%_pkgconfigdir/%name-egl.pc
%_pkgconfigdir/%name-egl-backend.pc


%changelog
* Sun Aug 25 2024 Yuri N. Sedunov <aris@altlinux.org> 1.23.1-alt1.1
- 1.23.1

* Fri May 31 2024 Yuri N. Sedunov <aris@altlinux.org> 1.23.0-alt1.1
- 1.23.0

* Tue Apr 04 2023 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1.1
- 1.22.0

* Fri Jul 01 2022 Yuri N. Sedunov <aris@altlinux.org> 1.21.0-alt1.1
- 1.21.0

* Wed Mar 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1.1
- added some fonts to BR to fix docs build

* Fri Dec 10 2021 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1
- 1.20.0

* Thu Jan 28 2021 Yuri N. Sedunov <aris@altlinux.org> 1.19.0-alt1
- 1.19.0 (ported to Meson build system)
- new devel-doc subpackage

* Wed Feb 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0
- new libwayland-egl* subpackages

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Wed Feb 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.13.0-alt1
- 1.13.0

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.12.0-alt1
- 1.12.0

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 1.11.1-alt1
- 1.11.1

* Wed Jun 01 2016 Yuri N. Sedunov <aris@altlinux.org> 1.11.0-alt1
- 1.11.0

* Wed Feb 17 2016 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Jul 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu Jun 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Sun Feb 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Fri Sep 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Wed May 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Fri Jan 24 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Oct 11 2013 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Aug 25 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sun Jul 14 2013 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Apr 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Wed Mar 06 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Thu Jan 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3
- fixed interpackage dependencies
- TODO: build documentation using publican

* Tue Oct 23 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.0.0-alt1
- 1.0.0

* Mon Sep 10 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.95.0-alt1
- 0.95.0

* Sun Feb 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.85.0-alt1
- first release

* Wed Jan 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

