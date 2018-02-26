Name: libfprint
Version: 0.2.0
Release: alt3
Summary: Tool kit for fingerprint scanner
Group: System/Libraries
License: LGPLv2+
URL: http://www.reactivated.net/fprint/wiki/Main_Page 
# git://anongit.freedesktop.org/libfprint/libfprint
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Sep 02 2010
BuildRequires: libgio-devel libgtk+2-common-devel libnss-devel libusb-devel libImageMagick-devel

%description
The fprint project aims to plug a gap in the Linux desktop: support for 
consumer fingerprint reader devices.
This project provides the drivers for the fingerprint scanner including
the ones with a usb id 08ff:2580.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch -p1

mkdir -p m4

%build
%autoreconf
%configure \
	--disable-static \
	--enable-examples-build
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc INSTALL NEWS TODO THANKS AUTHORS
%_libdir/*.so.*
%_sysconfdir/udev/rules.d/60-fprint-autosuspend.rules

%files devel
%doc HACKING
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/%name.pc

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 0.2.0-alt3
- Rebuild with new libImageMagick

* Mon Sep 13 2010 Anton Farygin <rider@altlinux.ru> 0.2.0-alt2
- rebuild with new libImageMagick

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- new version

* Sat Jun 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.pre2
- 0.1.0-pre2

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt0.pre1
- 0.1.0-pre1

* Fri Nov 14 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.6-alt2
- rebuild with libMagickCore.so.1

* Sat May 24 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.0.6-alt1
- initial release

