Name: libgpiod
Version: 1.4.1
Release: alt1
Summary: C library and tools for interacting with linux GPIO char device

License: LGPLv2+
Group: System/Libraries
Url: https://git.kernel.org/pub/scm/libs/libgpiod/libgpiod.git/
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildRequires: autoconf-archive
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: libkmod-devel
BuildRequires: libstdc++-devel
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: libsystemd-devel

%description
libgpiod is a C library and tools for interacting with the linux GPIO character
device (gpiod stands for GPIO device) The new character device interface
guarantees all allocated resources are freed after closing the device file
descriptor and adds several new features that are not present in the obsolete
sysfs interface (like event polling, setting/reading multiple values at once or
open-source and open-drain GPIOs).

%package utils
Summary: Utilities for GPIO
Group: System/Kernel and hardware
Requires: %name = %EVR

%description utils
Utilities for interacting with GPIO character devices.

%package c++
Summary: C++ bindings for %name
Group: System/Libraries
Requires: %name = %EVR

%description c++
C++ bindings for use with %name.

%package -n python3-module-%name
Summary: Python 3 bindings for %name
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-%name
Python 3 bindings for development with %name.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %EVR

%description devel
Files for development with %name.

%prep
%setup

%build
%autoreconf
%configure \
	--enable-tools=yes \
	--disable-static \
	--enable-bindings-cxx \
	--enable-bindings-python

%make_build

%install
%makeinstall_std

#Remove libtool archives.
find %buildroot -name '*.la' -delete

%files
%doc COPYING README
%_libdir/%name.so.*

%files utils
%_bindir/gpio*

%files c++
%_libdir/libgpiodcxx.so.*

%files -n python3-module-%name
%python3_sitelibdir/gpiod.so

%files devel
%_includedir/gpiod.*
%_pkgconfigdir/libgpiod*.pc
%_libdir/%{name}*.so

%changelog
* Thu Jan 16 2020 Anton Midyukov <antohami@altlinux.org> 1.4.1-alt1
- initial build for ALT
