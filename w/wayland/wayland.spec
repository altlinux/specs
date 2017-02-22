%def_disable snapshot
%def_disable doc

Name: wayland
Version: 1.13.0
Release: alt1

Summary: Wayland protocol libraries
Group: System/X11
License: MIT
Url: http://%name.freedesktop.org/

%if_disabled snapshot
Source: http://%name.freedesktop.org/releases/%name-%version.tar.xz
%else
# git://anongit.freedesktop.org/wayland/wayland
Source: %name-%version.tar
%endif

BuildRequires: /proc doxygen libexpat-devel libffi-devel libxml2-devel xsltproc docbook-style-xsl
%{?_enable_doc:BuildRequires: /proc graphviz xmlto}

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
Common headers for Wayland.

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

%package -n lib%name-cursor
Summary: Wayland cursor helper library
Group: System/Libraries
License: MIT
Requires: lib%name-client = %version-%release

%description -n lib%name-cursor
Wayland cursor helper shared library.

%package -n lib%name-cursor-devel
Summary: Wayland cursor helper library
Group: System/Libraries
License: MIT
Requires: lib%name-cursor = %version-%release
Requires: lib%name-client-devel = %version-%release

%description -n lib%name-cursor-devel
This package provides development files for Wayland cursor helper library.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	%{?_disable_doc:--disable-documentation}
%make_build

%install
%makeinstall_std

%check
%make check

%files devel
#%doc %_docdir/%name-devel
%_bindir/%name-scanner
%_includedir/%name-util.h
%_includedir/%name-version.h
%_datadir/aclocal/%name-scanner.*
%_libdir/pkgconfig/%name-scanner.pc
%dir %_datadir/%name
%_datadir/%name/%name-scanner.mk
%_datadir/%name/%name.xml
%_datadir/%name/wayland.dtd
# too many broken links
%{?_enable_doc:%_man3dir/*}

%files -n lib%name-client
%_libdir/lib%name-client.so.*
%doc README COPYING

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

%changelog
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

