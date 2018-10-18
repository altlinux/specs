%define rname libglvnd

Name: libglvnd0-dummy
Version: 1.1.0
Release: alt0.1
Group: System/Libraries
Summary: The GL Vendor-Neutral Dispatch library
Url: https://github.com/NVIDIA/libglvnd
License: MIT

#Provides: libGLdispatch = %version-%release
#Obsoletes: libGLdispatch < %version-%release

Source: %rname-%version.tar

BuildRequires: libXext-devel python-modules-compiler python-modules-xml xorg-glproto-devel

%description
libglvnd is an implementation of the vendor-neutral dispatch layer for
arbitrating OpenGL API calls between multiple vendors on a per-screen basis

%package devel
Summary: Development files for %name
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name

%package opengl
Summary: OpenGL support for libglvnd
Group: System/Libraries

%description opengl
libOpenGL is the common dispatch interface for the workstation OpenGL API

%package gles
Summary: GLES support for libglvnd
Group: System/Libraries

%description gles
libGLESv2 are the common dispatch interface for the GLES API

%package egl
Summary: EGL support for libglvnd
Group: System/Libraries

%description egl
libEGL are the common dispatch interface for the EGL API

%package glx
Summary: GLX support for libglvnd
Group: System/Libraries
Provides: libGLX = %version-%release
Obsoletes: libGLX < %version-%release

%description glx
libGLX are the common dispatch interface for the GLX API

%package -n libGL
Summary: GL support for libglvnd
Group: System/Libraries

%description -n libGL
libGL are the common dispatch interface for the GLX API

%set_verify_elf_method textrel=relaxed

%prep
%setup -q -n %rname-%version

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot{%_sysconfdir,%_datadir}/glvnd/egl_vendor.d
mkdir -p %buildroot{%_sysconfdir,%_datadir}/egl/egl_external_platform.d

rm -f %buildroot%_libdir/libGLESv*
rm -f %buildroot%_libdir/libGL.so*
rm -f %buildroot%_libdir/libEGL.so*

%files
%doc README.md
%dir %_sysconfdir/glvnd
%dir %_datadir/glvnd
%_libdir/libGLdispatch.so.0*

#%files opengl
%_libdir/libOpenGL.so.*

#%files gles
#%_libdir/libGLESv2.so.*

#%files glx
%_libdir/libGLX.so.*

#%files -n libGL
#%_libdir/libGL.so.*

#%files egl
%dir %_sysconfdir/glvnd/egl_vendor.d
%dir %_datadir/glvnd/egl_vendor.d
%dir %_sysconfdir/egl
%dir %_sysconfdir/egl/egl_external_platform.d
%dir %_datadir/egl
%dir %_datadir/egl/egl_external_platform.d
#%_libdir/libEGL.so.*

%files devel
%_includedir/glvnd
%_libdir/lib*.so
%_pkgconfigdir/%rname.pc

%changelog
* Wed Aug 29 2018 Valery Inozemtsev <shrek@altlinux.ru> 1.1.0-alt0.1
- 1.1.0
