Name: libgpiod
Version: 2.3
Release: alt1

Summary: Linux GPIO interacting library
License: LGPL-2.1
Group: System/Libraries
URL: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git

Source: %name-%version.tar

BuildRequires: gcc-c++ meson /proc
BuildRequires: pkgconfig(libedit)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(systemd)
BuildRequires: /usr/bin/glib-mkenums
BuildRequires: /usr/bin/gdbus-codegen
BuildRequires: /usr/bin/g-ir-scanner
BuildRequires: /usr/bin/g-ir-compiler
BuildRequires: /usr/bin/help2man

%package -n libgpiod2
Summary: Linux GPIO interacting library
Group: System/Libraries

%package -n libgpiodbus
Summary: Linux GPIO DBus library
Group: System/Libraries

%package -n libgpiotools
Summary: Linux GPIO tooling library
Group: System/Libraries

%package c++
Summary: C++ bindings for libgpiod
Group: System/Libraries

%package glib
Summary: GLib bindings for libgpiod
Group: System/Libraries

%package glib-gir
Summary: GObject introspection data for libgpiod
Group: System/Libraries

%package devel
Summary: Linux GPIO interacting library
Group: Development/C

%package glib-devel
Summary: GLib bindings for libgpiod
Group: Development/C

%package glib-gir-devel
Summary: GLib bindings for libgpiod
Group: Development/C

%package -n gpio-tools
Summary: Linux GPIO interacting tools
Group: System/Kernel and hardware
Provides: libgpiod-utils = %EVR
Obsoletes: libgpiod-utils

%package -n gpio-manager
Summary: GPIO D-Bus manager
Group: System/Servers

%define desc C library and tools for interacting with the linux GPIO \
character device (gpiod stands for GPIO device).\
Since linux 4.8 the GPIO sysfs interface is deprecated. User space should use\
the character device instead. This library encapsulates the ioctl calls and\
data structures behind a straightforward API.

%description
%desc

%description -n libgpiod2
%desc
This package contains libgpiod shared library.

%description -n libgpiodbus
%desc
This package contains libgpiodbus shared library.

%description -n libgpiotools
%desc
This package contains libgpiotools shared library.

%description c++
%desc
This package contains C++ bindings for libgpiod.

%description glib
%desc
This package contains GLib bindings for libgpiod.

%description glib-gir
%desc
This package contains GLib bindings for libgpiod.

%description devel
%desc
This package contains development part of libgpiod.

%description glib-devel
%desc
This package contains development part of libgpiod-glib.

%description glib-gir-devel
%desc
This package contains development part of libgpiod-glib.

%description -n gpio-tools
%desc
This package contains command-line tools.

%description -n gpio-manager
%desc
This package contains GPIO D-Bus manager.

%prep
%setup

%build
%meson -Dtests=disabled
%meson_build

%install
%meson_install
install -pm0644 -D dbus/data/gpio.conf %buildroot%_sysusersdir/gpio.conf
install -pm0644 dbus/data/gpio-manager.conf %buildroot%_sysusersdir/
rm -vf %buildroot%_libdir/*.a

%files -n libgpiod2
%_udevrulesdir/90-gpio.rules
%_sysusersdir/gpio.conf
%_libdir/libgpiod.so.*

%files -n libgpiodbus
%_libdir/libgpiodbus.so.*

%files -n libgpiotools
%_libdir/libgpiotools.so.*

%files c++
%_libdir/libgpiodcxx.so.*

%files glib
%_libdir/libgpiod-glib.so.*

%files glib-gir
%_typelibdir/Gpiodglib-1.0.typelib

%files devel
%_includedir/gpiod.h
%_includedir/gpiod.hpp
%_includedir/gpiodcxx
%_includedir/gpiotools.h
%_libdir/libgpiod.so
%_libdir/libgpiodbus.so
%_libdir/libgpiodcxx.so
%_libdir/libgpiod-glib.so
%_libdir/libgpiotools.so
%_pkgconfigdir/gpiod-glib.pc
%_pkgconfigdir/libgpiod.pc
%_pkgconfigdir/libgpiodcxx.pc
%_pkgconfigdir/libgpiotools.pc

%files glib-devel
%_includedir/gpiod-glib.h
%_includedir/gpiod-glib

%files glib-gir-devel
%_girdir/Gpiodglib-1.0.gir

%files -n gpio-tools
%doc COPYING NEWS README* TODO
%_bindir/gpiodetect
%_bindir/gpioget
%_bindir/gpioinfo
%_bindir/gpiomon
%_bindir/gpionotify
%_bindir/gpioset
%_man1dir/gpiodetect.1*
%_man1dir/gpioget.1*
%_man1dir/gpioinfo.1*
%_man1dir/gpiomon.1*
%_man1dir/gpionotify.1*
%_man1dir/gpioset.1*

%files -n gpio-manager
%_sysconfdir/dbus-1/system.d/io.gpiod1.conf
%_bindir/gpio-manager
%_bindir/gpiocli
%_unitdir/gpio-manager.service
%_sysusersdir/gpio-manager.conf
%_datadir/dbus-1/interfaces/io.gpiod1.xml
%_man1dir/gpio-manager.1*
%_man1dir/gpiocli-*.1*
%_man1dir/gpiocli.1*

%changelog
* Wed Jun 17 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.3-alt1
- 2.3 released

* Tue Jun 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.5-alt1
- 2.2.5 released

* Tue Apr 14 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.4-alt2
- built without python bindings

* Fri Apr 10 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.4-alt1
- 2.2.4 released

* Thu Feb 26 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.3-alt1
- 2.2.3 released

* Thu Oct 24 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2.1.3-alt1
- 2.1.3 released

* Tue Mar 19 2024 Stanislav Levin <slev@altlinux.org> 2.1.1-alt1.1
- NMU: added missing build dependency on setuptools.

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.1-alt1
- 2.1.1 released

* Mon Mar 11 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1-alt1
- 2.1 released

* Thu Sep 21 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt1
- 2.0.2 released

* Fri Feb 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.4-alt1
- 1.6.4 released

* Fri Mar 26 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 reelased

* Mon Dec 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt1
- 1.6.2 released

* Wed Sep 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.4-alt1
- 1.4.4 released

* Thu Jan 16 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- initial build for ALT
