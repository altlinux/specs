Name: libupnp
Version: 1.6.17
Release: alt1

Summary: Linux SDK for UPnP Devices
License: BSD
Group: System/Libraries
Url: http://upnp.sourceforge.net/

Source: %name-%version-%release.tar

%description
The Linux SDK for UPnP Devices (libupnp) provides developers with an API
and open source code for building control points, devices, and bridges that
are compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

UPnP is an architecture that enables discovery, event notification, and
control of devices on a network, independent of operating system, programming
language, or physical network connection. UPnP is based on common Internet
standards and specifications such as TCP/IP, HTTP, and XML. For detailed
information about UPnP, including the UPnP Device Architecture Specification,
please visit the UPnP Forum web site.

%package -n libixml2
Summary: Complementary library for Linux SDK for UPnP Devices
Group: System/Libraries
Conflicts: libupnp < 1.6.7

%package -n libupnp6
Summary: Linux SDK for UPnP Devices
Group: System/Libraries
Requires: libixml2 = %version-%release

%package devel
Summary: Development libraries and header files for libupnp
Group: Development/C
Requires: libupnp6 = %version-%release
Requires: libixml2 = %version-%release

%description -n libixml2
The Linux SDK for UPnP Devices (libupnp) provides developers with an API
and open source code for building control points, devices, and bridges that
are compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%description -n libupnp6
The Linux SDK for UPnP Devices (libupnp) provides developers with an API
and open source code for building control points, devices, and bridges that
are compliant with Version 1.0 of the Universal Plug and Play Device
Architecture Specification.

%description devel
The libupnp-devel package contains libraries and header files needed
to develop applications using libupnp.

%prep
%setup

%build
%autoreconf
%configure --enable-ipv6 --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n libixml2
%_libdir/libixml.so.*

%files -n libupnp6
%doc ChangeLog LICENSE NEWS README TODO
%_libdir/libthreadutil.so.*
%_libdir/libupnp.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*

%changelog
* Sat Jun 23 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.17-alt1
- 1.6.17 released

* Fri Nov 18 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.14-alt1
- 1.6.14 released

* Sat Nov 12 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.13-alt3
- add conflicts: to older libupnp

* Fri Nov 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.13-alt2
- package ixml library separately

* Fri Nov 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.13-alt1
- 1.6.13

* Fri Nov 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt3
- rebuilt as legacy shared lib

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.6-alt2
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.6-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libupnp
  * postun_ldconfig for libupnp
  * postclean-05-filetriggers for spec file

* Mon Jul 14 2008 Sir Raorn <raorn@altlinux.ru> 1.6.6-alt1
- [1.6.6]

* Tue May 30 2006 Andrei Bulava <abulava@altlinux.ru> 1.3.1-alt1
- initial build for ALT Linux
