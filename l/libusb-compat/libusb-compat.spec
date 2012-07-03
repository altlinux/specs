Name: libusb-compat
Version: 0.1.3
Release: alt3

Summary: Libusb is a library which allows userspace access to USB devices
License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/libusb/
Packager: Alexander Bokovoy <ab@altlinux.org>

Prereq: libusb >= 1.0.1-alt1

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: libusb-devel >= 1.0-alt2

%description
Libusb is a library which allows userspace access to USB devices.
Libusb-compat implements compatibility interfaces of libusb 0.1.

%package devel
Summary: Libusb-compat is a wrapper which allows userspace access to USB devices via older (0.1.0) API of libusb
Group: Development/C
Requires: %name = %version-%release

%description devel
Libusb-compat is a wrapper which allows userspace access to USB devices via older (0.1.0) API of libusb

This package contains header files needed for the development of programs that
use libusb.

Use of 0.1.0 API of libusb is discouraged, please port your applications to libusb 1.0 API!

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot/%_lib
for f in %buildroot%_libdir/lib*.so; do
	t=$(readlink "$f")
	ln -sf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib*.so.* %buildroot/%_lib/

%files
%doc AUTHORS README NEWS
/%_lib/libusb-0.1.so.*

%files devel
%_includedir/usb.h
%_bindir/libusb-config
%_libdir/libusb.so
%_pkgconfigdir/libusb.pc

%changelog
* Wed Mar 09 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt3
- rebuilt for debuginfo

* Tue Nov 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt2
- rebuild

* Tue Feb 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Wed May 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt3
- Move libusb-0.1.so.* to /lib to accompany main libusb-1.0.so.*

* Sun Mar 29 2009 Alexander Bokovoy <ab@altlinux.org> 0.1.0-alt2
- Package libusb-compat-0.1 separately from libusb
- Include ALT-specific fixes

