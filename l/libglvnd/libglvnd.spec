
%set_verify_elf_method textrel=relaxed
%def_disable package_all

Name: libglvnd
Version: 0.0.0
Release: alt2

Group: System/Libraries
Summary: OpenGL vendor-neutral dispatch layer
Url: http://projects.kde.org/projects/kde/kdeedu/libkcddb
License: LGPLv2

Source: %name-%version.tar
Patch1: alt-x11glvnddir.patch

# Automatically added by buildreq on Sat Feb 20 2016 (-bi)
# optimized out: elfutils gnu-config libX11-devel libpciaccess-devel libpixman-devel libstdc++-devel pkg-config python-base python-modules python3 python3-base ruby ruby-stdlibs xorg-dri3proto-devel xorg-inputproto-devel xorg-kbproto-devel xorg-presentproto-devel xorg-randrproto-devel xorg-renderproto-devel xorg-videoproto-devel xorg-xextproto-devel xorg-xineramaproto-devel xorg-xproto-devel
#BuildRequires: gcc-c++ glibc-devel-static imake libGL-devel libXext-devel python-module-google python-modules-compiler python-modules-xml rpm-build-python3 rpm-build-ruby xorg-cf-files xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-sdk
BuildRequires: gcc-c++ glibc-devel imake libGL-devel libXext-devel xorg-cf-files xorg-resourceproto-devel xorg-scrnsaverproto-devel xorg-sdk xorg-glproto-devel python-modules-xml

%description -n libglvnd
Implementation of the vendor-neutral dispatch layer
for arbitrating OpenGL API calls between multiple vendors on a per-screen basis.

%package devel
Summary: Development files for %name
Group: Development/KDE and QT
%description devel
Development files for %name

%package -n glvnd
Group: System/Libraries
Summary: %name utils
%description -n glvnd
%name utils

%package -n libGLdispatch
Group: System/Libraries
Summary: Thin wrapper around Mesa's glapi
%description -n libGLdispatch
Thin wrapper around Mesa's glapi that tries to hide most of the complexity of managing dispatch tables.

%package -n libGL
Group: System/Libraries
Summary: GL wrapper library
%description -n libGL
Wrapper libraries for libGLX and libGLdispatch.

%package -n libOpenGL
Group: System/Libraries
Summary: GL wrapper library
%description -n libOpenGL
Wrapper libraries for libGLX and libGLdispatch.

%package -n libGLX
Group: System/Libraries
Summary: GLX window-system API library
%description -n libGLX
GLX window-system API library.

%package -n libGLES
Group: System/Libraries
Summary: Static GL entrypoints
%description -n libGLES
Static GL entrypoints which use the context defined in libGLdispatch, while EGL will contain libEGL, which may be implemented similarly to libGLX.

%package -n libGLES1
Group: System/Libraries
Summary: Static GL entrypoints
%description -n libGLES1
Static GL entrypoints which use the context defined in libGLdispatch, while EGL will contain libEGL, which may be implemented similarly to libGLX.

%prep
%setup -q
%patch1 -p1
./autogen.sh

%build
%add_optflags %optflags_shared
%configure \
    --disable-static \
    --enable-shared \
    #
%make_build

%install
%make install DESTDIR=%buildroot

%files -n glvnd
%_libdir/X11/modules/extensions/x11glvnd.so

%if_enabled package_all
%files -n libGLES1
%_libdir/libGLESv1_CM.so.1
%_libdir/libGLESv1_CM.so.1.*
%files -n libGL
%_libdir/libGL.so.1
%_libdir/libGL.so.1.*
%files -n libGLES
%_libdir/libGLESv2.so.2
%_libdir/libGLESv2.so.2.*
%endif

%files -n libOpenGL
%_libdir/libOpenGL.so.0
%_libdir/libOpenGL.so.0.*
%files -n libGLX
%_libdir/libGLX.so.0
%_libdir/libGLX.so.0.*

%files -n libGLdispatch
%_libdir/libGLdispatch.so.0
%_libdir/libGLdispatch.so.0.*

%files devel
%if_enabled package_all
%_libdir/lib*.so
%else
%_libdir/libGLdispatch.so
%_libdir/libOpenGL.so
%_libdir/libGLX.so
%endif
%_includedir/glvnd/
%_pkgconfigdir/libglvnd.pc

%changelog
* Fri Mar 04 2016 Sergey V Turchin <zerg@altlinux.org> 0.0.0-alt2
- update from master branch

* Sat Feb 20 2016 Sergey V Turchin <zerg@altlinux.org> 0.0.0-alt1
- initial build
