%define _libname	enet

Name: libenet
Version: 1.3.6
Release: alt1
Summary: Thin, simple and robust network layer on top of UDP
Group: System/Libraries
License: MIT
Url: http://enet.bespin.org/
Source0: http://enet.bespin.org/download/%_libname-%version.tar.gz

%description
ENet is a relatively thin, simple and robust network communication
layer on top of UDP (User Datagram Protocol). The primary feature
it provides is optional reliable, in-order delivery of packets.

ENet is NOT intended to be a general purpose high level networking
library that handles authentication, lobbying, server discovery,
compression, encryption and other high level, often application
level or dependent tasks.

%package devel
Summary: Development files for enet
Group: Development/C
Requires: %name = %version

%description devel
The libenet-devel package contains libraries and header files for
developing applications that use enet.

%package devel-static
Summary: Static library for enet
Group: Development/C
Requires: %name = %version

%description devel-static
Static library for enet

%prep
%setup -n %_libname-%version

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure
%make
gcc -shared -Wl,-soname,%name.so.1 *.o -o %name.so.1

%install
%makeinstall_std
install -pDm644 %name.so.1 %buildroot%_libdir/%name.so.1

install -d %buildroot%_pkgconfigdir
install -m644 *.pc %buildroot%_pkgconfigdir

%files
%doc ChangeLog LICENSE README
%_libdir/%name.so.*

%files devel-static
%_libdir/%name.a

%files devel
%doc docs/html
%_includedir/%_libname
%_libdir/%name.so
%_pkgconfigdir/*

%changelog
* Mon Dec 17 2012 Fr. Br. George <george@altlinux.ru> 1.3.6-alt1
- Autobuild version bump to 1.3.6
- Fix autobuild bug (Closes: 27415)

* Thu Nov 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.5-alt1.1
- Added pkg-config file (ALT #28141)

* Thu Nov 15 2012 Fr. Br. George <george@altlinux.ru> 1.3.5-alt1
- Autobuild version bump to 1.3.5
- Closes: 27415

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.qa3
- Rebuilt for debuginfo

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.qa2
- rebuild using girar-nmu to require/provide setversion
  by request of mithraen@

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libenet
  * postun_ldconfig for libenet
  * postclean-05-filetriggers for spec file

* Mon Nov 24 2008 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from SuSE

* Sat Jun 21 2008 Toni Graffy <toni@links2linux.de> - 1.2-0.pm.2
- fixed Group for libenet-devel
* Fri Feb 15 2008 Toni Graffy <toni@links2linux.de> - 1.2-0.pm.1
- update to 1.2
* Mon Oct 08 2007 Toni Graffy <toni@links2linux.de> - 1.1-0.pm.1
- initial build for packman
- spec adapted from Fedora package from Hans de Goede <j.w.r.degoede@hhs.nl>
