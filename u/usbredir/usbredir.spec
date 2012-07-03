%def_disable static

Name: usbredir
Version: 0.4.2
Release: alt1
Summary: USB network redirection protocol libraries
Group: System/Libraries
License: LGPLv2+
# I've requested a fedorahosted project once that is in place these 2 should
# be updated to point there
Url: http://cgit.freedesktop.org/~jwrdegoede/usbredir/

Source: %name-%version.tar
BuildRequires: libusb-devel >= 1.0.9

%description
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. This package contains a number of libraries to help implementing
support for usbredir:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the usb-host side of a usbredir connection.
All that an application wishing to implement an usb-host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers

%package -n lib%name
Summary: USB network redirection protocol libraries
Group: System/Libraries
License: LGPLv2+

%description -n lib%name
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. This package contains a number of libraries to help implementing
support for usbredir:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the usb-host side of a usbredir connection.
All that an application wishing to implement an usb-host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use %name.

%package server
Summary: Simple usb-host tcp server
Group: Networking/Other
License: GPLv2+
Requires: lib%name = %version-%release

%description server
A simple usb-host tcp server, using libusbredirhost.

%prep
%setup

%build
%autoreconf
%configure \
	%{subst_enable static}
%make_build

%install
%make DESTDIR=%buildroot install

%files  -n lib%name
%doc ChangeLog COPYING.LIB README TODO
%_libdir/*.so.*

%files  -n lib%name-devel
%doc usb-redirection-protocol.txt
%_includedir/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files server
%doc COPYING
%_sbindir/usbredirserver

%changelog
* Sun Mar 11 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Thu Mar 01 2012 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Fri Feb 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Tue Jan 10 2012 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Tue Nov 15 2011 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1.git.a897d
- initial build for ALT Linux Sisyphus
