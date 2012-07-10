Name: 389-adminutil
Version: 1.1.15
Release: alt1
License: LGPLv2
Url: http://port389.org
Group: System/Libraries
Summary: Utility library for directory server administration

# Automatically added by buildreq on Mon Aug 17 2009
BuildRequires: gcc-c++ libicu-devel mozldap-devel

BuildRequires: libsvrcore-devel libsasl2-devel openldap-devel

Provides: fedora-ds-adminutil = %version-%release
Obsoletes: fedora-ds-adminutil < %version-%release

Source: %name-%version-%release.tar

%description
%name is libraries of functions used to administer directory
servers, usually in conjunction with the admin server.  %name is
broken into two libraries - libadminutil contains the basic
functionality, and libadmsslutil contains SSL versions and wrappers
around the basic functions.  The PSET functions allow applications to
store their preferences and configuration parameters in LDAP, without
having to know anything about LDAP.  The configuration is cached in a
local file, allowing applications to function even if the LDAP server
is down.  The other code is typically used by CGI programs used for
directory server management, containing GET/POST processing code as
well as resource handling (ICU ures API).

%package devel
Summary: Development and header files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
Development files and header files necessary to build applications
that use %name.

%prep
%setup

%build
%configure --disable-test- --with-openldap
%make

%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot%_libdir/lib*.a
rm -f %buildroot%_libdir/lib*.la

%files
%doc LICENSE README NEWS
%_libdir/*.so.*
%_datadir/389-adminutil

%files devel
%_pkgconfigdir/%name.pc
%_libdir/*.so
%_includedir/libadminutil
%_includedir/libadmsslutil

%changelog
* Tue Mar 27 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.15-alt1
- 1.1.15

* Fri Aug 05 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.14-alt1
- 1.1.14

* Mon Dec 06 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.13-alt2
- rebuild with icu-4.6

* Tue Nov 16 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.13-alt1
- 1.1.13

* Mon Mar 15 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.10-alt1
- 1.1.10

* Mon Aug 17 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.8-alt3
- spec cleanup

* Thu May 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.8-alt2
- renamed to 389-adminutil

* Fri Apr 03 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.8-alt1
- 1.1.8

* Sat Sep 06 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.7-alt1
- 1.1.7

* Wed May 07 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.6-alt1
- 1.1.6

* Tue Jan 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.5-alt2
- Fedora-DS 1.1 Final release

* Tue Oct 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.5-alt1.20071030
- CVS snapshot 20071030
- bump version to 1.1.5

* Mon Oct 29 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1.20071008.1
- Rebuild with new ICU

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.2-alt1.20071008
- CVS snapshot 20071008

* Wed May 30 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt0
- Initial

* Wed May 23 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.1-3
- more fedora review stuff - use macros consistently
- make sure install preserves timestamps
- use lgpl instead of gpl for acclanglist.c
- fix undefined weak symbols in libadmsslutil

* Fri May 18 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.1-2
- pkgconfig is a requires not a build requires

* Thu May 17 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.1-1
- Many bug fixes - bumped version to 1.1.1
- fixed concerns from Fedora package review

* Wed Mar 28 2007 Rich Megginson <rmeggins@redhat.com> - 1.1.0-1
- Initial version - based largely on svrcore.spec
