Name: netdata
Version: 1.5.0
Release: alt1

Summary: Real-time performance monitoring, done right!

License: GPLv3+
Group: File tools
Url: http://netdata.firehol.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/firehol/netdata.git
Source: %name-%version.tar

# manually removed: python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs 
# Automatically added by buildreq on Fri Aug 05 2016
# optimized out: perl pkg-config python-base python-modules python3 python3-base
BuildRequires: rpm-build-intro libuuid-devel zlib-devel bash4

Requires: bash4

# FIXME: wait for new rpm-build-intro in p8
%define _localstatedir /var

%if_with nfacct
BuildRequires: libmnl-devel
BuildRequires: libnetfilter_acct-devel
%endif

%add_findreq_skiplist %_libexecdir/%name/plugins.d/*.plugin
%add_findreq_skiplist %_libexecdir/%name/charts.d/*.sh

# python.d/python_modules/pyyaml3/__init__.py: invalid syntax (line 284)
%add_findreq_skiplist %_libexecdir/%name/python.d/python_modules/*/*.py

%description
netdata is the fastest way to visualize metrics. It is a resource
efficient, highly optimized system for collecting and visualizing any
type of realtime timeseries data, from CPU usage, disk activity, SQL
queries, API calls, web site visitors, etc.

netdata tries to visualize the truth of now, in its greatest detail,
so that you can get insights of what is happening now and what just
happened, on your systems and applications.

%prep
%setup

# https://bugzilla.altlinux.org/show_bug.cgi?id=32663
for i in plugins.d/*.sh ; do
	test -s "$i" || continue
	grep -q "BASH version 4" "$i" || continue
	%__subst "s|^#!/usr/bin/env bash|#!/bin/bash4|g" "$i"
done

%build
%autoreconf
%configure \
	--docdir=%_docdir/%name-%version \
	--with-zlib \
	--with-math \
	%{?with_nfacct:--enable-plugin-nfacct} \
	--with-user=netdata
%make_build

%install
%makeinstall_std
#rm -rf %buildroot%_libexecdir/netdata/python.d/python_modules/pyyaml{2,3}

mkdir -p %buildroot%_sysconfdir/%name/
install -m 644 -p system/netdata.conf %buildroot%_sysconfdir/%name/netdata.conf

#mkdir -p %buildroot%_sysconfdir/%name/charts.d/

mkdir -p %buildroot%_sysconfdir/logrotate.d/
install -m 644 -p system/netdata.logrotate %buildroot%_sysconfdir/logrotate.d/%name

find %buildroot -name .keep | xargs rm

install -d %buildroot%_unitdir/
install -m 644 -p system/netdata.service %buildroot%_unitdir/netdata.service

%pre
getent group netdata > /dev/null || groupadd -r netdata
getent passwd netdata > /dev/null || useradd -r -g netdata -c netdata -s /sbin/nologin -d / netdata

%files
%attr(0700,netdata,netdata) %dir %_localstatedir/cache/%name/
%attr(0700,root,netdata) %dir %_localstatedir/log/%name/
%attr(0700,netdata,netdata) %dir %_localstatedir/lib/%name/
%dir %_sysconfdir/%name/
#config(noreplace) %_sysconfdir/%name/netdata.conf
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/*.conf
%dir %_sysconfdir/%name/node.d/
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/node.d/*
%dir %_sysconfdir/%name/health.d/
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/health.d/*.conf
%dir %_sysconfdir/%name/python.d/
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/python.d/*.conf
%dir %_sysconfdir/%name/charts.d/
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/charts.d/*.conf
%config(noreplace) %_logrotatedir/%name
%_sbindir/%name
%_unitdir/netdata.service
%dir %_libexecdir/%name/
%_libexecdir/%name/charts.d/
%_libexecdir/%name/node.d/
%_libexecdir/%name/plugins.d/
%_libexecdir/%name/python.d/
%dir %_datadir/%name

# override defattr for web files (see netdata.conf for web access user/group)
%defattr(644,root,netdata,755)
%_datadir/%name/web/

%changelog
* Mon Feb 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- pack python modules (ALT bug 32662)
- pack /etc/netdata/charts.d/ (ALT bug 32663)
- set bash4 for bash4 using scripts (ALT bug 32663)

* Sat Oct 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt2
- fix packing

* Sat Oct 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0 (with rpmrb script)

* Mon Sep 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu May 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

* Mon May 16 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.2.0-1
- netdata is now 30%% faster.
- netdata now has a registry (my-netdata menu on the dashboard).
- netdata now monitors Linux containers.
- Several more improvements, new features and bugfixes.
* Wed Apr 20 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.1.0-1
- Several new features (IPv6, SYNPROXY, Users, Users Groups).
- A lot of bug fixes and optimizations.
* Tue Mar 22 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.0.0-1
- First public release.
* Sun Nov 15 2015 Alon Bar-Lev <alonbl@redhat.com> - 0.0.0-1
- Initial add.
