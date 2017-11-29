Name: primus
Version: 20150710
Release: alt3%ubt

Summary: Faster OpenGL offloading for Bumblebee
License: Freely distributable
Group: Graphics

Url: https://github.com/amonakov/primus
Packager: barssc <barssc@altlinux.org>

Source0: primus-master.zip
Source1: primusrun

%set_gcc_version 4.9
BuildRequires(pre): rpm-build-ubt
BuildRequires: unzip gcc%{_gcc_version}-c++ libGL-devel libX11-devel glibc-devel

Requires: bumblebee xorg-dri-intel xorg-drv-intel

%description
Primus is a shared library that provides OpenGL and GLX APIs and
implements low-overhead local-only client-side OpenGL offloading via GLX
forking, similar to VirtualGL. It intercepts GLX calls and redirects GL
rendering to a secondary X display, presumably driven by a faster GPU.
On swapping buffers, rendered contents are read back using a PBO and
copied onto the drawable it was supposed to be rendered on in the first
place.

%prep
%setup -n primus-master

%build
export PRIMUS_libGLd='/usr/$LIB/X11/libGL.so.1'
export PRIMUS_libGLa='/etc/X11/${LIB}_nvidia/current/libGL.so.1'
CXXFLAGS="%optflags" LIBDIR=lib make

%install
mkdir -p %buildroot%_libdir/%name/
install -pD -m644 lib/libGL.so.1 %buildroot%_libdir/%name/libGL.so.1
install -pD -m755 %SOURCE1 %buildroot%_bindir/primusrun

%files
%doc LICENSE.txt README.md technotes.md
%_libdir/%name/
%_bindir/primusrun

%changelog
* Wed Nov 29 2017 Sergey V Turchin <zerg@altlinux.org> 20150710-alt3%ubt
- fix to compile with libstdc++5

* Tue Nov 28 2017 Sergey V Turchin <zerg@altlinux.org> 20150710-alt2%ubt
- fix path to nvidia libGL
- fix build requires

* Fri Jul 10 2015 barssc <barssc@altlinux.org> 20150710-alt1
- new version
- closed bug #31111

* Sat Jan 18 2014 barssc <barssc@altlinux.org> 20140118-alt1
- new version

* Tue Nov 19 2013 barssc <barssc@altlinux.org> 20131119-alt2
- add doc technotes.md

* Tue Nov 05 2013 barssc <barssc@altlinux.org> 20131105-alt1
- first test build for Sisyphus
