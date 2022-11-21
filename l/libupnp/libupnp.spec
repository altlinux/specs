%define soname_upnp 17
%define soname_ixml 11

Name: libupnp
Version: 1.14.15
Release: alt1

Summary: Linux SDK for UPnP Devices
License: BSD
Group: System/Libraries
Url: https://github.com/pupnp/pupnp

Source: %name-%version-%release.tar

%define desc \
The Linux SDK for UPnP Devices (libupnp) provides developers with an API \
and open source code for building control points, devices, and bridges that \
are compliant with Version 1.0 of the Universal Plug and Play Device \
Architecture Specification.

%description %desc
UPnP is an architecture that enables discovery, event notification, and
control of devices on a network, independent of operating system, programming
language, or physical network connection. UPnP is based on common Internet
standards and specifications such as TCP/IP, HTTP, and XML. For detailed
information about UPnP, including the UPnP Device Architecture Specification,
please visit the UPnP Forum web site.

%package -n libixml%soname_ixml
Summary: Complementary library for Linux SDK for UPnP Devices
Group: System/Libraries

%package -n libupnp%soname_upnp
Summary: Linux SDK for UPnP Devices
Group: System/Libraries

%package devel
Summary: Development libraries and header files for libupnp
Group: Development/C

%description -n libixml%soname_ixml %desc

%description -n libupnp%soname_upnp %desc

%description devel %desc
This package contains libraries and header files needed to develop
applications using libupnp.

%prep
%setup

%build
%autoreconf
%configure --enable-ipv6 --enable-reuseaddr --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n libixml%soname_ixml
%_libdir/libixml.so.*

%files -n libupnp%soname_upnp
%_libdir/libupnp.so.*

%files devel
%doc README.md
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Mon Nov 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.15-alt1
- 1.14.15 released

* Thu Oct 06 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.14-alt1
- 1.14.14 released

* Tue Aug 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.13-alt1
- 1.14.13 released

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.12-alt1
- 1.14.12 released

* Mon Sep 20 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.10-alt1
- 1.14.10 released

* Fri Jul 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.5-alt1
- 1.14.5 released (fixes: CVE-2021-28302)

* Tue Mar 23 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.2-alt1
- 1.14.2 released

* Wed Sep 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.0-alt1
- 1.14.0 released

* Sun May 24 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- 1.12.1 released

* Tue Dec 24 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.1-alt1
- 1.10.1 released

* Mon Jul 23 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.25-alt1
- 1.6.25 released

* Mon Dec 26 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.21-alt1
- 1.6.21 released

* Mon Sep 05 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.20-alt1
- 1.6.20 released

* Fri Jan 08 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.19-alt2
- updated from git.83f3b34

* Tue Feb 25 2014 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.19-alt1
- 1.6.19 released

* Wed Feb 06 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.18-alt1
- 1.6.18 released

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
