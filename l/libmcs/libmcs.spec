%define oname mcs
Name: libmcs
Version: 0.7.2
Release: alt1

Summary: A library and set of userland tools which abstract the storage of configuration settings

License: BSD
Group: System/Libraries
Url: http://www.atheme.org/projects/mcs.shtml

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://distfiles.atheme.org/%name-%version.tar
Patch: %name-link.patch

# Automatically added by buildreq on Wed Oct 31 2007
BuildRequires: libmowgli-devel

%description
mcs is a library and set of userland tools which abstract the storage
of configuration settings away from userland applications.  It is hoped
that by using mcs, that the applications which use it will generally have
a more congruent feeling in regards to settings.
There have been other projects like this before (such as GConf), but
unlike those projects, mcs strictly handles abstraction. It does not
impose any specific data storage requirement, nor is it tied to any
desktop environment or software suite.
Because mcs is licenced under the BSD licence, it is hoped that many
applications will adopt it's use.

%package devel
Summary: Header files for compiling apps that use %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
This package contains the header files for compiling applications that
use %name.

%prep
%setup

%build
%configure --disable-gconf --disable-kconfig
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README TODO
%_bindir/*
%_libdir/%oname/
%_libdir/%name.so.*

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/*

%changelog
* Mon Apr 18 2011 Vitaly Lipatov <lav@altlinux.ru> 0.7.2-alt1
- new version 0.7.2 (with rpmrb script)

* Fri Nov 26 2010 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Wed Nov 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt3
- cleanup spec

* Sun Jul 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt2
- rebuild with new libmowgli
- cleanup spec

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Wed Oct 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- new version 0.6.0 (with rpmrb script)
- update buildreq, disable gconf/kconfig support

* Wed Mar 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.1-alt1
- initial build for ALT Linux Sisyphus

