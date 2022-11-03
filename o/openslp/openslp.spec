%define _unpackaged_files_terminate_build 1

Name: openslp
Version: 2.0.0
Release: alt4

Summary: OpenSLP implementation of Service Location Protocol V2
License: BSD-style
Group: Networking/Other
Url: https://sourceforge.net/projects/openslp/
# Source-url: https://download.sourceforge.net/%name/%name-%version.tar.gz
Source: %name-%version.tar
Source1: %name.init
#Patch1: openslp-1.2.1-alt-memcpy-fix.patch
#Patch2: openslp-1.2.1-rh-nullauth.patch
Patch3: openslp-2.0.0-CVE-2016-7567.patch
Patch4: openslp-2.0.0-CVE-2012-4428.patch
Patch5: openslp-2.0.0-cleanup_libslp_namespace.patch
Patch6: openslp-2.0.0-CVE-2016-4912.patch
Patch7: openslp-2.0.0-CVE-2017-17833.patch
Patch8: openslp-2.0.0-openssl_1.1.0.patch
Patch9: openslp-2.0.0-CVE-2019-5544.patch

BuildRequires: flex gcc-c++ libssl-devel zlib-devel

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
%setup -n %name-%version
#%%patch1 -p1
#%%patch2 -p1
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p1
%patch8 -p2
%patch9 -p1
#sed -i '/OPTFLAGS/ s/-O3/$RPM_OPT_FLAGS/' configure.in

%build
%autoreconf
%configure \
	    --localstatedir=/var \
	    --enable-async-api \
	    --enable-slpv2-security \
	    --disable-static
%make_build

%install
%makeinstall_std

install -pDm755 %SOURCE1 %buildroot%_initdir/slpd
ln -s ../../%_initdir/slpd %buildroot%_sbindir/rcslpd
ln -s ../../%_initdir/slpd %buildroot%_sbindir/rcopenslp

mkdir -p %buildroot%_sysconfdir/slp.reg.d

%check
%make check

%post daemon
%post_service slpd

%preun daemon
%preun_service slpd

%files
%_bindir/slptool
%config(noreplace) %_sysconfdir/slp.conf
%config(noreplace) %_sysconfdir/slp.spi

%files daemon
%attr(755,root,root) %config(noreplace) %_initdir/slpd
%config(noreplace) %_sysconfdir/slp.reg
%dir %_sysconfdir/slp.reg.d/
%_sbindir/rcopenslp
%_sbindir/rcslpd
%_sbindir/slpd

%files doc
%doc doc/doc/*

%files -n lib%name
%_libdir/libslp.so.1
%_libdir/libslp.so.1.0.0

%files -n lib%name-devel
%_libdir/libslp.so
%_includedir/slp.h

%changelog
* Thu Nov  3 2022 Alexander Danilov <admsasha@altlinux.org> 2.0.0-alt4
- Fixes changelog.

* Fri Oct 28 2022 Alexander Danilov <admsasha@altlinux.org> 2.0.0-alt3
- Applied security fixes (fixes CVE-2019-5544).

* Sat Dec 01 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2
- Fixed libslp namespace (closes: #35692).
- Enabled SLPv2 Security.
- Enabled testing.
- Applied security fixes (fixes: CVE-2012-4428, CVE-2016-4912, CVE-2016-7567,
  CVE-2017-17833).

* Wed Nov 28 2018 Leontiy Volodin <lvol@altlinux.org> 2.0.0-alt1
- New version (2.0.0) with rpmgs script
- Disabled patches because don't applyed for this version
- Adapted spec for new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.1-alt4.qa1
- NMU: rebuilt for debuginfo.

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
