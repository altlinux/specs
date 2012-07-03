Name: openslp
Version: 1.2.1
Release: alt4

Summary: OpenSLP implementation of Service Location Protocol V2
License: BSD-style
Group: Networking/Other
URL: http://sourceforge.net/projects/openslp/
# http://download.sourceforge.net/%name/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.init
Patch1: openslp-1.2.1-alt-memcpy-fix.patch
Patch2: openslp-1.2.1-rh-nullauth.patch

BuildRequires: flex gcc-c++ libssl-devel

%description
Service Location Protocol is an IETF standards track protocol that
provides a framework to allow networking applications to discover the
existence, location, and configuration of networked services in
enterprise networks.

OpenSLP is an open source implementation of the SLPv2 protocol as
defined

by RFC 2608 and RFC 2614.  This package includes the daemon, libraries,
header files and documentation.

%package daemon
Summary: OpenSLP implementation of Service Location Protocol V2
Group: System/Servers

%description daemon
Service Location Protocol is an IETF standards track protocol that
provides a framework to allow networking applications to discover the
existence, location, and configuration of networked services in
enterprise networks.

This package contains the SLP server. Every system, which provide any
services which should be used via a SLP client must run this server and
register the service.

%package doc
Summary: openslp project documentation
Group: Books/Computer books
BuildArch: noarch

%description doc
The OpenSLP project is an effort to develop an open-source implementation of
Service Location Protocol suitable for commercial and non-commercial
application.  This package contains openslp project documentation.

%package -n lib%name
Summary: openslp project libraries
Group: System/Libraries

%description -n lib%name
The OpenSLP project is an effort to develop an open-source implementation of
Service Location Protocol suitable for commercial and non-commercial
application.  This package contains openslp project libraries.

%package -n lib%name-devel
Summary: openslp project development headers
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The OpenSLP project is an effort to develop an open-source implementation of
Service Location Protocol suitable for commercial and non-commercial
application.  This package contains openslp project development headers.

%prep
%setup -q -n %name-%version
%patch1 -p1
%patch2 -p1
sed -i '/OPTFLAGS/ s/-O3/$RPM_OPT_FLAGS/' configure.in

%build
%autoreconf
%configure \
	    --sharedstatedir=%_datadir \
	    --localstatedir=/var \
	    --enable-slpv1 \
	    --enable-async-api \
	    --enable-slpv2-security \
	    --disable-static
%make_build

%install
%define docdir %_docdir/%name-%version
%makeinstall_std DOC_DIR=%docdir

install -pDm755 %SOURCE1 %buildroot%_initdir/slpd
ln -s ../../%_initdir/slpd %buildroot%_sbindir/rcslpd
ln -s ../../%_initdir/slpd %buildroot%_sbindir/rcopenslp

mkdir -p %buildroot%_sysconfdir/slp.reg.d

%post daemon
%post_service slpd

%preun daemon
%preun_service slpd

%files
%_bindir/*
%config(noreplace) %_sysconfdir/slp.conf
%config(noreplace) %_sysconfdir/slp.spi

%files daemon
%attr(755,root,root) %config(noreplace) %_initdir/slpd
%config(noreplace) %_sysconfdir/slp.reg
%dir %_sysconfdir/slp.reg.d/
%_sbindir/*

%files doc
%docdir/

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%changelog
* Fri Oct 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.1-alt4
- Cleaned up the package a bit.
- Built with libcrypto.so.10.

* Thu Feb 25 2010 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt3
- fix memcpy usage.
- minor spec cleanup
- remove obsoleted macroses call

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.1-alt2.1.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.1-alt2.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Sep 22 2005 Albert R. Valiev <darkstar@altlinux.ru> 1.2.1-alt2
- Spec fixes

* Wed Aug 31 2005 Albert R. Valiev <darkstar@altlinux.ru> 1.2.1-alt1
- New version

* Mon Jun 20 2005 Albert R. Valiev <darkstar@altlinux.ru> 1.1.5-alt4
- Fixed #6753

* Sat Feb 05 2005 Albert R. Valiev <darkstar@altlinux.ru> 1.1.5-alt3
- Added --libdir=%_libdir configure option (#6031)

* Mon Sep 13 2004 Albert R. Valiev <darkstar@altlinux.ru> 1.1.5-alt2
- Added daemon init script
- Added Suse extensions and authentication patches

* Tue Dec 16 2003 Albert R. Valiev <darkstar@altlinux.ru> 1.1.5-alt1
- Initial build
