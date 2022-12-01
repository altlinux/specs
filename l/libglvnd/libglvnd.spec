Name: libglvnd
Version: 1.6.0
Release: alt1
Epoch: 7
Group: System/Libraries
Summary: The GL Vendor-Neutral Dispatch library
Url: https://gitlab.freedesktop.org/glvnd/libglvnd
License: MIT

Provides: libGLdispatch = %epoch:%version-%release
Obsoletes: libGLdispatch < %epoch:%version-%release

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: meson libXext-devel python-modules-compiler python-modules-distutils python-modules-xml xorg-glproto-devel

%description
libglvnd is an implementation of the vendor-neutral dispatch layer for
arbitrating OpenGL API calls between multiple vendors on a per-screen basis

%package devel
Summary: Development files for %name
Group: Development/C
Provides: libGLES-devel = %epoch:%version-%release
Obsoletes: libGLES-devel < %epoch:%version-%release
Conflicts: libGL-devel < 19.2.2

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name

%package -n libOpenGL
Summary: OpenGL support for libglvnd
Group: System/Libraries

%description -n libOpenGL
libOpenGL is the common dispatch interface for the workstation OpenGL API

%package -n libGLES
Summary: GLES support for libglvnd
Group: System/Libraries

%description -n libGLES
libGLESv2 are the common dispatch interface for the GLES API

%package -n libEGL
Summary: EGL support for libglvnd
Group: System/Libraries
Requires: libEGL-mesa

%description -n libEGL
libEGL are the common dispatch interface for the EGL API

%package -n libGLX
Summary: GLX support for libglvnd
Group: System/Libraries
Requires: libGLX-mesa

%description -n libGLX
libGLX are the common dispatch interface for the GLX API

%package -n libGL
Summary: GL support for libglvnd
Group: System/Libraries

%description -n libGL
libGL are the common dispatch interface for the GLX API

%set_verify_elf_method textrel=relaxed

%prep
%setup -q
%patch -p1

%build
%meson \
	-Dgles1=false
%meson_build

%install
%meson_install

mkdir -p %buildroot{%_sysconfdir,%_datadir}/glvnd/egl_vendor.d
mkdir -p %buildroot{%_sysconfdir,%_datadir}/egl/egl_external_platform.d

rm -f %buildroot%_libdir/libGLESv1*
rm -f %buildroot%_pkgconfigdir/glesv1*.pc

%files
%doc README.md
%dir %_sysconfdir/glvnd
%dir %_datadir/glvnd
%_libdir/libGLdispatch.so.*

%files -n libOpenGL
%_libdir/libOpenGL.so.*

%files -n libGLES
%_libdir/libGLES*.so.*

%files -n libGLX
%_libdir/libGLX.so.*

%files -n libGL
%_libdir/libGL.so.*

%files -n libEGL
%dir %_sysconfdir/glvnd/egl_vendor.d
%dir %_datadir/glvnd/egl_vendor.d
%dir %_sysconfdir/egl
%dir %_sysconfdir/egl/egl_external_platform.d
%dir %_datadir/egl
%dir %_datadir/egl/egl_external_platform.d
%_libdir/libEGL.so.*

%files devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%changelog
* Thu Dec 01 2022 Valery Inozemtsev <shrek@altlinux.ru> 7:1.6.0-alt1
- 1.6.0

* Fri Sep 23 2022 Valery Inozemtsev <shrek@altlinux.ru> 7:1.5.0-alt1
- 1.5.0

* Tue Dec 28 2021 Valery Inozemtsev <shrek@altlinux.ru> 7:1.4.0-alt1
- 1.4.0

* Mon Sep 27 2021 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.4-alt1
- 1.3.4 (closes: #41015)

* Wed May 12 2021 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.3-alt1
- 1.3.3

* Tue Jul 07 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.2-alt1
- 1.3.2

* Sat May 30 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.1-alt2
- git snapshot master.3e8684a

* Tue Mar 10 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.1-alt1
- 1.3.1

* Wed Feb 19 2020 Valery Inozemtsev <shrek@altlinux.ru> 7:1.3.0-alt1
- 1.3.0

* Tue Nov 26 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt4
- fixed conflicts between libglvnd-devel and libGLES-devel

* Mon Nov 25 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt3
- git snapshot master.9ba775e

* Wed Oct 30 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt2
- update GL/gl.h to match Mesa

* Thu Oct 10 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.2.0-alt1
- 1.2.0

* Thu Mar 14 2019 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.1-alt1
- 1.1.1

* Thu Nov 01 2018 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.0-alt3
- git snapshot master.012fe39

* Thu Oct 18 2018 Valery Inozemtsev <shrek@altlinux.ru> 7:1.1.0-alt2
- 1.1.0
