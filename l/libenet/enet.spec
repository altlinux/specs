%define _libname	enet

Name: libenet
Version: 1.2
Release: alt1.qa2
Summary: Thin, simple and robust network layer on top of UDP
Group: System/Libraries
License: MIT
Url: http://enet.bespin.org/
Source0: http://enet.bespin.org/download/%_libname-%version.tar.gz
Packager: Fr. Br. George <george@altlinux.ru>

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

%prep
%setup -q -n %_libname-%version

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure
%make

# Create a shared version
gcc -shared -Wl,-soname,lib%_libname.so.1 *.o \
  -o lib%_libname.so.1

%install
install -dm 755 %buildroot%_libdir
install -m 644 lib%_libname.so.1 \
	%buildroot%_libdir
ln -s lib%_libname.so.1 \
	%buildroot%_libdir/lib%_libname.so

install -dm 755 %buildroot%_includedir/%_libname
install -m 644 include/%_libname/*.h \
	%buildroot%_includedir/%_libname

%files
%doc ChangeLog LICENSE README
%_libdir/lib%_libname.so.*

%files devel
%doc tutorial.txt design.txt
%dir %_includedir/%_libname
%_includedir/%_libname/*
%_libdir/lib%_libname.so

%changelog
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
