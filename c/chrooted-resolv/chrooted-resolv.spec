Name: chrooted-resolv
Version: 0.3.1
Release: alt2

Summary: Chrooted environment with all required for resolver
Summary(ru_RU.KOI8-R): Chrooted environment со всем необходимым для resolver'a
License: GPL
Group: System/Base
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source0: resolv.chroot.all
Source1: resolv.chroot.conf
Source2: resolv.chroot.lib

# due to dnsdomainname call in copy_resolv_conf
Requires(post): /bin/hostname
Requires: glibc-nss

%define ROOT /var/resolv
Provides: %ROOT

# due to copy_resolv_conf/copy_resolv_lib
BuildPreReq: chrooted >= 0.3

%description
This package provides readonly chrooted environment with all stuff
required for resolver to work properly.

%install
for n in all conf lib; do
	install -pD -m750 "%_sourcedir/resolv.chroot.$n" \
		"%buildroot%_sysconfdir/chroot.d/resolv.$n"
done
sed -i 's,%%ROOT,%ROOT,g' "%buildroot%_sysconfdir/chroot.d/"*

mkdir -p %buildroot%ROOT{%_sysconfdir,/%_lib,/var/{nis,yp/binding}}
touch %buildroot%ROOT{%_sysconfdir/{localtime,hosts,services,{host,nsswitch,resolv}.conf},/var/nis/NIS_COLD_START}

%post
%_sysconfdir/chroot.d/resolv.all

%preun
if [ $1 = 0 ]; then
	%__rm -f %ROOT/%_lib/* %ROOT/var/yp/binding/*
fi

%files
%config %_sysconfdir/chroot.d/*
%dir %ROOT
%dir %ROOT/%_lib
%dir %ROOT%_sysconfdir
%ghost %ROOT%_sysconfdir/localtime
%ghost %ROOT%_sysconfdir/hosts
%ghost %ROOT%_sysconfdir/services
%ghost %ROOT%_sysconfdir/*.conf
%dir %ROOT/var
%dir %ROOT/var/nis
%ghost %config(missingok) %verify(not md5 mtime size) %ROOT/var/nis/NIS_COLD_START
%dir %ROOT/var/yp
%dir %ROOT/var/yp/binding

%changelog
* Tue Apr 10 2007 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt2
- Add requirement on glibc-nss (#10192).

* Mon Sep 05 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3.1-alt1
- Added multilib support (#7364).

* Mon Apr 18 2005 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt2
- Disabled %%verify check for %ROOT/var/nis/NIS_COLD_START.
- Updated package dependencies (hostname).

* Sun Feb 15 2004 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt1
- Updated for chrooted-0.3.

* Wed Nov 20 2002 Dmitry V. Levin <ldv@altlinux.org> 0.2-alt3
- Minor specfile cleanup.

* Wed Apr 17 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2-alt2
- Fixed %%post (no need to force).

* Sat Apr 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.2-alt1
- Added NIS/NIS+ support (thanks to Sergey V. Degtiarenko).

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 0.1-alt1
- Initial revision.
