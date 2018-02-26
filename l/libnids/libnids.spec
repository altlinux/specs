Name: libnids
Version: 1.24
Release: alt3

Summary: Libnids is a library that provides a functionality of one of NIDS components
License: GPLv2+
Group: Development/C
Url: http://libnids.sourceforge.net

%define srcname %name-%version
# http://prdownloads.sourceforge.net/%name/%srcname%{?rc_ver:%rc_ver}.tar.gz
Source: %srcname%{?rc_ver:%rc_ver}.tar
Patch: libnids-%version-%release.patch

Provides: libnids1 = %version-%release
Provides: libnids2 = %version-%release
Obsoletes: libnids1, libnids2

# Automatically added by buildreq on Wed Oct 30 2002
BuildRequires: libnet2-devel libpcap-devel

%def_disable static

%package devel
Summary: Development library and header files for libnids
Group: Development/C
Provides: libnids1-devel = %version-%release
Provides: libnids2-devel = %version-%release
Obsoletes: libnids1-devel, libnids2-devel
Requires: %name = %version-%release, libnet2-devel, libpcap-devel

%package devel-static
Summary: Static libnids library
Group: Development/C
Provides: libnids1-devel-static = %version-%release
Provides: libnids2-devel-static = %version-%release
Obsoletes: libnids1-devel-static, libnids2-devel-static
Requires: %name-devel = %version-%release, libnet2-devel-static, libpcap-devel-static

%description
Libnids is a library that provides a functionality of one of NIDS
(Network Intrusion Detection System) components, namely E-component.
It means that libnids code watches all local network traffic, cooks
received datagrams a bit (quite a bit ;)), and provides convinient
information on them to analyzing modules of NIDS.  Libnids performs:
+ assembly of TCP segments into TCP streams;
+ IP defragmentation;
+ TCP port scan detection.
More technical info can be found in MISC file.

So, if you intend to develop a custom NIDS, you don't have to build
low-level network code.  If you decide to use libnids, you have got
E-component ready - you can focus on implementing other parts of NIDS.

%description devel
Libnids is a library that provides a functionality of one of NIDS
(Network Intrusion Detection System) components, namely E-component.

This package contains the header files and libraries needed
to develop programs that use the Libnids library.

%description devel-static
Libnids is a library that provides a functionality of one of NIDS
(Network Intrusion Detection System) components, namely E-component.

This package contains Libnids static library.

%prep
%setup -n %srcname
%patch -p1

%build
autoconf
export ac_cv_lib_nsl_gethostbyname=no
%configure --disable-libglib --enable-shared %{subst_enable static}
%make_build %{?_enable_static:static} shared

%install
%makeinstall
%define docdir %_docdir/%srcname
mkdir -p %buildroot%docdir
install -pm644 CHANGES CREDITS MISC README %buildroot%docdir/
install -pm644 doc/API.txt %buildroot%docdir/API
install -pm644 doc/{b*,LINUX,PATCH,PERFORMANCE,TESTS} %buildroot%docdir/

%files
%_libdir/*.so.*
%dir %docdir
%docdir/[CMR]*

%files devel
%_libdir/*.so
%_includedir/*
%_mandir/man?/*
%dir %docdir
%docdir/[bALPT]*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sun Apr 24 2011 Dmitry V. Levin <ldv@altlinux.org> 1.24-alt3
- Rebuilt for debuginfo.

* Sun Nov 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.24-alt2
- Rebuilt for soname set-versions.

* Mon Mar 22 2010 Dmitry V. Levin <ldv@altlinux.org> 1.24-alt1
- Updated to 1.24.

* Tue May 19 2009 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt4
- Fixed build with fresh gcc.

* Sun Dec 14 2008 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt3
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.

* Sun Feb 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt2
- Changed soname back to libnids.so.1.21 (no ABI changes).

* Sat Feb 23 2008 Dmitry V. Levin <ldv@altlinux.org> 1.23-alt1
- Updated to 1.23.

* Sun Jul 22 2007 Dmitry V. Levin <ldv@altlinux.org> 1.22-alt1
- Updated to 1.22.

* Sun Nov 12 2006 Dmitry V. Levin <ldv@altlinux.org> 1.21-alt1
- Updated to 1.21.

* Tue Jun 20 2006 Dmitry V. Levin <ldv@altlinux.org> 1.20-alt2
- Dropped libnids1 and renamed libnids2 back to libnids.

* Sat Jun 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1.20-alt1
- Updated to 1.20.

* Sun Sep 05 2004 Dmitry V. Levin <ldv@altlinux.org> 1.19-alt1
- Updated to 1.19.
- Do not build and package static library by default.

* Tue Jan 13 2004 Dmitry V. Levin <ldv@altlinux.org> 1.18-alt2
- Rebuilt with libpcap.so.0.8.

* Sat Oct 18 2003 Dmitry V. Levin <ldv@altlinux.org> 1.18-alt1
- Updated to 1.18.

* Sun Nov 24 2002 Dmitry V. Levin <ldv@altlinux.org> 1.17-alt0.1.rc1
- Updated to 1.17rc1.
- Dropped all patches (obsolete or merged upstream).
- Fixed -I/usr/include compilation warnings.
- Changed soname and renamed to libnids2.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.16-alt3
- Rebuilt with libpcap-0.7.1.

* Tue Feb 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.16-alt2
- added patches from Owl and PLD.

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 1.16-alt1
- 1.16

* Fri Jan 05 2001 Dmitry V. Levin <ldv@fandra.org> 1.13-ipl1
- FHSification.

* Wed Mar 15 2000 Dmitry V. Levin <ldv@fandra.org>
- Initial revision.
