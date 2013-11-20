Name: primus
Version: 20131119
Release: alt2

Summary: Faster OpenGL offloading for Bumblebee
License: Freely distributable
Group: Graphics

Url: https://github.com/amonakov/primus
Packager: barssc <barssc@altlinux.org>

Source0: primus-master.zip
Source1: primusrun

BuildRequires: unzip libGL-devel gcc4.7-c++ libX11-devel glibc-devel libstdc++4.7-devel

Requires: bumblebee

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
export PRIMUS_libGLa='/usr/$LIB/libGL.so.1'
LIBDIR=lib make

%install
mkdir -p %buildroot%_libdir/%name/
install -pD -m644 lib/libGL.so.1 %buildroot%_libdir/%name/libGL.so.1
install -pD -m755 %SOURCE1 %buildroot%_bindir/primusrun

%files
%doc LICENSE.txt README.md technotes.md
%_libdir/%name/
%_bindir/primusrun

%changelog
* Tue Nov 19 2013 barssc <barssc@altlinux.org> 20131119-alt2
- add doc technotes.md

* Tue Nov 05 2013 barssc <barssc@altlinux.org> 20131105-alt1
- first test build for Sisyphus