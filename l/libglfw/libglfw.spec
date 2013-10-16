Name:	libglfw
Version: 2.7.9
Release: alt1
Summary: A cross-platform multimedia library
License: zlib
Group: System/Libraries
Url: http://www.glfw.org/index.html
Source: glfw-%version.tar.bz2
Patch: glfw-2.7.9-alt-include.patch

# Automatically added by buildreq on Wed Oct 16 2013
# optimized out: libGL-devel libX11-devel libXrender-devel xorg-randrproto-devel xorg-renderproto-devel xorg-xproto-devel
BuildRequires: libGLU-devel libXrandr-devel

%description
GLFW is a free, Open Source, multi-platform library for OpenGL
application development that provides a powerful API for handling
operating system specific tasks such as opening an OpenGL window,
reading keyboard, mouse, joystick and time input, creating threads, and
more.

%package devel
Summary: Support for developing C application
Requires: %name =  %version-%release
Group: Development/C

%description devel
The glfw-devel package contains header files for developing glfw
applications.

%prep
%setup -n glfw-%version
%patch -p1

%build
%make x11

%install
%make x11-dist-install PREFIX=%buildroot%_prefix LIBDIR=%_lib
ln -s %name.so.0 %buildroot%_libdir/%name.so

%files
%doc docs/*.pdf
%_libdir/libglfw.so.*

%files devel
%_includedir/GL
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 2.7.9-alt1
- Initial build from scratch
