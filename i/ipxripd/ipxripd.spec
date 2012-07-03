Name: ipxripd
Version: 0.8
Release: alt6

Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

Summary: IPX RIP/SAP daemon - routing for IPX networks
License: GPL
Group: System/Servers
Url: ftp://ftp.metalab.unc.edu/pub/Linux/system/filesystems/ncpfs

Source0: %url/%name-%version.tar.gz
Source1: %name.init
Patch0: %name-rh5.patch
Patch1: %name-rh61.patch
Patch2: %name-rh71.patch
Patch3: %name-%version-namechange.patch
Patch4: %name-0.8-alt-build-gcc3.patch

Requires: ipxutils

%description
ipxripd is an implementation of Novell's RIP and SAP protocols. It 
automagically builds and updates IPX routing table in the Linux kernel.
Usefull when trying to get a Linux box to act as an IPX router.

%prep
%setup
%patch  -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%make_build CFLAGS="$RPM_OPT_FLAGS"

%install
install -p -m755 -D %_sourcedir/ipxripd.init %buildroot%_initdir/ipxripd
install -p -m755 -D ipxd %buildroot%_sbindir/ipxripd
install -p -m644 -D ipx_ticks %buildroot%_sysconfdir/ipx_ticks
install -p -m644 -D ipxd.8 %buildroot%_mandir/man8/ipxripd.8
install -p -m644 -D ipx_ticks.5 %buildroot%_mandir/man5/ipx_ticks.5

%files
%_initdir/*
%_sbindir/*
%_mandir/man5/*
%_mandir/man8/*
%config(noreplace) %_sysconfdir/ipx_ticks
%doc README %name-%version.lsm

%post
%post_service %name

%preun
%preun_service %name

%changelog
* Mon Aug 25 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.8-alt6
- spec-file fixes - add usage of RPM_OPT_FLAGS at build stage

* Sat Aug 23 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 0.8-alt5
- init-script rewrited according to new policy

* Mon Oct 28 2002 Stanislav Ievlev <inger@altlinux.ru> 0.8-alt4
- real rebuild with gcc3.2

* Sun Oct 27 2002 Dmitry Lebkov <dlebkov@altlinux.ru> 0.8-alt3
- rebuild with gcc3.2

* Fri Jun 21 2002 Dmitry V. Lebkov <dima@sakhalin.ru>
- spec-file fix against intersections with filesytem package

* Thu Jun 6 2002 Dmitry V. Lebkov <dima@sakhalin.ru>
- version 0.8 of ipxripd. Name of daemon changed from ipxd to ipxripd.

* Thu Jan 10 2002 Dmitry V. Lebkov <dima@sakhalin.ru>
- Initial package.
