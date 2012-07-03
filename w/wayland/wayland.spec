# enable compilation of wayland-scannner
%def_enable scanner

Name: wayland
Version: 0.85.0
Release: alt1

Summary: Wayland protocol libraries
Group: System/X11
License: GPLv2+
Url: http://%name.freedesktop.org/

# git://anongit.freedesktop.org/wayland/wayland
Source: wayland-%version.tar

BuildRequires: libffi-devel libexpat-devel

%description
Wayland is a project to define a protocol for a compositor to talk to
its clients as well as a library implementation of the protocol. The
compositor can be a standalone display server running on Linux kernel
modesetting and evdev input devices, an X applications, or a wayland
client itself. The clients can be traditional applications, X servers
(rootless or fullscreen) or other display servers.

%package devel
Group: Development/C
Summary: Common headers for Wayland
License: MIT

%description devel
Common headers for Wayland

%package -n lib%name-client
Summary: Wayland client library
Group: System/Libraries
License: MIT

%description -n lib%name-client
Wayland client shared library.

%package -n lib%name-client-devel
Summary: Development files for Wayland client library
Group: Development/C
License: MIT
Requires: lib%name-client = %version-%release
Requires: %name-devel = %version-%release

%description -n lib%name-client-devel
This package provides development files for Wayland client library.

%package -n lib%name-server
Summary: Wayland server library
Group: System/Libraries
License: MIT

%description -n lib%name-server
Wayland server shared library.

%package -n lib%name-server-devel
Summary: Development files for Wayland server library
Group: Development/C
License: MIT
Requires: lib%name-server = %version-%release
Requires: %name-devel = %version-%release

%description -n lib%name-server-devel
This package provides development files for Wayland server library.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{subst_enable scanner}

%make_build

%install
%make DESTDIR=%buildroot install

%files devel
%_bindir/%name-scanner
%_includedir/%name-util.h
%_datadir/aclocal/%name-scanner.*
%doc README TODO

%files -n lib%name-client
%_libdir/lib%name-client.so.*

%files -n lib%name-server
%_libdir/lib%name-server.so.*

%files -n lib%name-client-devel
%_includedir/%name-client*.h
%_includedir/wayland-egl.h
%_libdir/lib%name-client.so
%_pkgconfigdir/%name-client.pc

%files -n lib%name-server-devel
%_includedir/%name-server*.h
%_libdir/lib%name-server.so
%_pkgconfigdir/%name-server.pc

%changelog
* Sun Feb 12 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.85.0-alt1
- first release

* Wed Jan 25 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1-alt1
- first build for Sisyphus

