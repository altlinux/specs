Name: libgpiod
Version: 1.2.1
Release: alt1

Summary: C library and tools for interacting with linux GPIO char device
Group: System/Libraries
License: LGPLv2+
Url: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git

BuildRequires: autoconf-archive
BuildRequires: gcc-c++
BuildRequires: python3-devel

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Pavel Nakonechnyi <zorg@altlinux.org>

%description
libgpiod is a C library and tools for interacting with the linux GPIO character
device (gpiod stands for GPIO device) The new character device interface
guarantees all allocated resources are freed after closing the device file
descriptor and adds several new features that are not present in the obsolete
sysfs interface (like event polling, setting/reading multiple values at once or
open-source and open-drain GPIOs).

%package devel
Summary: Development package for libimobiledevice
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files for development using libgpiod.

%package -n python3-module-%name
Summary: Python3 bindings for libgpiod
Group: Development/Python
Requires: %name = %version-%release

%description -n python3-module-%name
Python bindings for libgpiod.

%package c++
Summary: C++ bindings for libgpiod
Group: Development/C++
Requires: %name = %version-%release

%description c++
C++ bindings for libgpiod.

%package tools
Summary: Tools to interact with GPIO from userspace
Group: System/Configuration/Hardware
Requires: %name = %version-%release

Provides: gpiodetect gpioinfo gpioget gpioset gpiofind gpiomon

%description tools
Utilities for interacting with GPIO character devices.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	         --enable-tools=yes \
           --enable-bindings-cxx \
           --enable-bindings-python
%make_build

%install
%makeinstall_std

%files
%_libdir/%{name}.so.*
%doc COPYING NEWS README

%files devel
%_includedir/gpiod.*
%_libdir/%{name}*.so
%_libdir/pkgconfig/*.pc

%files -n python3-module-%name
%python3_sitelibdir/gpiod.so
%exclude %python3_sitelibdir/gpiod.la

%files c++
%_libdir/libgpiodcxx.so.*

%files tools
%_bindir/gpio*

%changelog
* Fri Mar 22 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.1-alt1
- Initial build of version 1.2.1
