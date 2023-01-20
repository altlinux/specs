# build judy
# wait for or drop armh: https://bugzilla.altlinux.org/show_bug.cgi?id=39152
# TODO: pyyaml3, urllib3
# TODO: use cmake?

%def_disable cloud
%def_with prometeus
%def_without nfacct
%def_without pyod

# Please, update here commit id for release, from $ git log v1.5.0 -n 1 --format="%H"
%define release_commit 562101d64137a4c6b3310d4a2fed4a1da1bfce8d

%define netdatauser netdata
Name: netdata
Version: 1.37.1
Release: alt1

Summary: Real-time performance monitoring, done right!

License: GPLv3+
Group: Monitoring
Url: http://netdata.firehol.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/firehol/netdata.git
Source: %name-%version.tar

Source1: netdata.logrotate

BuildRequires(pre): rpm-build-python3
BuildRequires: bash4
BuildRequires: libuuid-devel libuv-devel libprotobuf-devel
BuildRequires: libjudy-devel libcap-devel
BuildRequires: liblz4-devel zlib-devel libssl-devel
BuildRequires: libjson-c-devel

%if_with prometeus
# Prometheus remote write dependencies
BuildRequires: libsnappy-devel
BuildRequires: libprotobuf-devel
%endif


BuildRequires: libcups-devel >= 1.7

Requires: bash4

BuildRequires: rpm-macros-intro-conflicts
BuildRequires: rpm-build-intro >= 2.1.1

%if_with nfacct
BuildRequires: libmnl-devel
BuildRequires: libnetfilter_acct-devel
%endif

%if_enabled cloud
BuildRequires: libwebsockets-devel >= 3.2.2
BuildRequires: libmosquitto-devel >= 1.6.8
%endif

BuildRequires: gcc-c++

Requires: %name-web = %EVR

AutoReq: yes, noshell

%add_python3_lib_path %_libexecdir/%name/python.d

#add_findreq_skiplist %_libexecdir/%name/plugins.d/*.plugin
%add_findreq_skiplist %_libexecdir/%name/charts.d/*.sh

%add_python3_req_skip UserDict

# make optionally (wait for asks)
%add_python3_req_skip pandas netdata_pandas netdata_pandas.data
# make optionally (reqs numpy)
%add_python3_req_skip changefinder


# FIXME netdata-postgres
#python3(python_modules.bases.FrameworkServices.ExecutableService)
%add_python3_req_skip bases.FrameworkServices.SimpleService

# python.d/python_modules/pyyaml3/__init__.py: invalid syntax (line 284)
#add_findreq_skiplist %_libexecdir/%name/python.d/python_modules/*/*.py
#if %_vendor != "alt"
#global __python %__python3
#endif

%description
netdata is the fastest way to visualize metrics. It is a resource
efficient, highly optimized system for collecting and visualizing any
type of realtime timeseries data, from CPU usage, disk activity, SQL
queries, API calls, web site visitors, etc.

netdata tries to visualize the truth of now, in its greatest detail,
so that you can get insights of what is happening now and what just
happened, on your systems and applications.

%package postgres
Summary: PostgreSQL module for %name
Group: Monitoring
Requires: %name = %EVR
#Provides: %name-postgres
#Obsoletes: %name-postgres

%description postgres
PostgreSQL module for %name.

%package web
Summary:  %name web static files
Group: Monitoring
Requires: %name = %EVR
BuildArch: noarch

%description web
%name web static files.

%package plugin-cups
Summary: The Common Unix Printing System (CUPS) plugin for netdata
Group: Monitoring
Requires: cups >= 1.7
Requires: netdata = %EVR

%description plugin-cups
This is the Common Unix Printing System plugin for the netdata daemon.

Use this plugin to enable metrics collection from cupsd, the daemon running when CUPS is enabled on the system

%prep
%setup

%if_enabled cloud
# strange upstream wants static libs
# checking if libmosquitto static lib is present (and builds)... no
# checking if libwebsockets static lib is present... no

subst 's|test -f "externaldeps|test -n "externaldeps|' configure.ac
find -type f | xargs subst "s|externaldeps/mosquitto/libmosquitto.a|-lmosquitto|"
find -type f | xargs subst "s|externaldeps/mosquitto/mosquitto.h|mosquitto.h|"

find -type f | xargs subst "s|externaldeps/libwebsockets/libwebsockets.a|-lwebsockets|"
find -type f | xargs subst "s|externaldeps/libwebsockets/include|%_includedir|"
%endif

# https://bugzilla.altlinux.org/show_bug.cgi?id=32663
%if %_vendor == "alt"
for i in plugins.d/*.plugin plugins.d/*.sh charts.d/*.sh ; do
	test -s "$i" || continue
	%__subst "s|^#!/usr/bin/env bash$|#!/bin/bash4|g" "$i"
	%__subst "s|^#!/bin/bash$|#!/bin/bash4|g" "$i"
done
%endif

# TODO: fix in the upstream
%__subst "s|^#!/usr/bin/env python$|#!/usr/bin/env python3|" collectors/python.d.plugin/python_modules/third_party/boinc_client.py

%__subst "s|^pybinary=.*|pybinary=python3|" collectors/python.d.plugin/python.d.plugin.in

%build
%autoreconf
%configure \
	--docdir=%_docdir/%name-%version \
	--with-zlib \
	--with-math \
	--enable-jsonc \
	%{subst_enable cloud} \
	%{?with_nfacct:--enable-plugin-nfacct} \
	--with-user=netdata \
	--disable-dependency-tracking

# TODO
#%ifarch i586 x86_64
#        --enable-plugin-freeipmi \
#%endif

%make_build

%install
%makeinstall_std

# drop python2 version
rm -rf %buildroot%_libexecdir/netdata/python.d/python_modules/pyyaml2/
# drop bundled urllib3
rm -rf %buildroot%_libexecdir/netdata/python.d/python_modules/urllib3/

mkdir -p %buildroot%_sysconfdir/%name/
install -m 644 -p system/netdata.conf %buildroot%_sysconfdir/%name/netdata.conf

# This should be opt-in, not opt-out. I do not believe most users would agree
# with sending usage data to Google Analytics, whether anonymized or not.
# Hence, disable statistics by default.
touch %buildroot%_sysconfdir/%name/.opt-out-from-anonymous-statistics

#mkdir -p %buildroot%_sysconfdir/%name/charts.d/

mkdir -p %buildroot%_logrotatedir/
%if %_vendor == "alt"
install -m 644 -p %SOURCE1 %buildroot%_logrotatedir/%name
%else
install -m 644 -p system/netdata.logrotate %buildroot%_logrotatedir/%name
%endif

#find %buildroot -name .keep | xargs rm

# ###########################################################
# Install cache and log directories
install -m 755 -d %buildroot/var/cache/%name/
install -m 755 -d %buildroot/var/log/%name/

# ###########################################################
# Install registry directory
install -m 755 -d %buildroot/var/lib/%name/registry/


install -d %buildroot%_unitdir/
install -m 644 -p system/netdata.service %buildroot%_unitdir/netdata.service

rm -v %buildroot/usr/lib/netdata/install-service.sh
rm -rv %buildroot%_libdir/netdata/system/

# /run vs /var/run workaround
#__subst "s|/run/netdata/netdata.pid|%_runtimedir/netdata/netdata.pid|" %buildroot%_unitdir/netdata.service

# fill with original commit id for %version release
echo "%release_commit" > %buildroot%_datadir/%name/web/version.txt

%pre
# TODO
#groupadd %netdatauser
#useradd %netdatauser -g %netdatauser -c netdata -s /sbin/nologin -d /
getent group %netdatauser >/dev/null || groupadd -r %netdatauser
getent passwd %netdatauser >/dev/null || useradd -r -g %netdatauser -c "%netdatauser user" -s /sbin/nologin -d / %netdatauser

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE REDISTRIBUTED.md
%attr(0700,%netdatauser,%netdatauser) %dir %_cachedir/%name/
%attr(0770,root,%netdatauser) %dir %_logdir/%name/
%attr(0700,%netdatauser,%netdatauser) %dir %_sharedstatedir/%name/
%attr(0700,%netdatauser,%netdatauser) %dir %_sharedstatedir/%name/registry/
%dir %_sysconfdir/%name/
%_sysconfdir/%name/.opt-out-from-anonymous-statistics
%_sysconfdir/%name/.install-type
%_sysconfdir/%name/edit-config
#config(noreplace) %_sysconfdir/%name/netdata.conf
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/*.conf
#dir %_sysconfdir/%name/node.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/node.d/*
%dir %_sysconfdir/%name/health.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/health.d/*.conf
%dir %_sysconfdir/%name/python.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/python.d/*.conf
#dir %_sysconfdir/%name/charts.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/statsd.d/*.conf
%dir %_sysconfdir/%name/statsd.d/
#config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/charts.d/*.conf
%config(noreplace) %_logrotatedir/%name
%_sbindir/%name
%_sbindir/netdatacli
%_sbindir/netdata-claim.sh
%_unitdir/netdata.service
%dir %_libexecdir/%name/
%_libexecdir/%name/charts.d/
#_libexecdir/%name/node.d/
%_libexecdir/%name/plugins.d/
%_libexecdir/%name/python.d/
%dir %_datadir/%name
%dir %_libdir/%name/
%_libdir/%name/conf.d/

#exclude %_libexecdir/%name/python.d/postgres.chart.py
%exclude %_libexecdir/%name/plugins.d/cups.plugin
%exclude %_libexecdir/%name/python.d/anomalies.chart.py
%exclude %_libexecdir/%name/python.d/__pycache__/anomalies.*

%files web
# override defattr for web files (see netdata.conf for web access user/group)
%defattr(644,root,%netdatauser,755)
%_datadir/%name/web/

#files postgres
#attr(0750,root,%netdatauser) %_libexecdir/%name/python.d/postgres.chart.py

%if_with pyod
%files plugin-anomalies
%attr(0750,root,%netdatauser) %_libexecdir/%name/python.d/anomalies.chart.py
%_libexecdir/%name/python.d/__pycache__/anomalies.*
%endif

%files plugin-cups
%attr(0750,root,%netdatauser) %_libexecdir/%name/plugins.d/cups.plugin


%changelog
* Fri Jan 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.37.1-alt1
- new version 1.37.1 (with rpmrb script)

* Sun Feb 13 2022 Vitaly Lipatov <lav@altlinux.ru> 1.33.0-alt1
- new version 1.33.0 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.32.1-alt1
- new version 1.32.1 (with rpmrb script)

* Tue Aug 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt2
- drop bundled urllib3

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.31.0-alt1
- new version 1.31.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 1.30.1-alt1
- new version 1.30.1 (with rpmrb script)

* Sat Feb 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1.29.3-alt1
- new version 1.29.3 (with rpmrb script)
- build without new anomalies plugin (wait for pyod module)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.26.0-alt1
- new version 1.26.0 (with rpmrb script)

* Mon Oct 12 2020 Vitaly Lipatov <lav@altlinux.ru> 1.25.0-alt2
- use python3 only
- move cups plugin to separate package
- move web static files to separate noarch subpackage
- update BR: libjudy-devel, libcap-devel, libssl-devel, libjson-c-devel

* Tue Sep 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1.25.0-alt1
- new version 1.25.0 (with rpmrb script)

* Mon Aug 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.24.0-alt1
- new version 1.24.0 (with rpmrb script)

* Sat Aug 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.23.2-alt1
- new version 1.23.2 (with rpmrb script)

* Thu Jun 25 2020 Vitaly Lipatov <lav@altlinux.ru> 1.23.0-alt1
- new version 1.23.0 (with rpmrb script)

* Fri May 29 2020 Vitaly Lipatov <lav@altlinux.ru> 1.22.1-alt1
- new version 1.22.1 (with rpmrb script)

* Sat Mar 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1.20.0-alt1
- new version 1.20.0 (with rpmrb script)

* Sun Dec 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.19.0-alt1
- new version (1.19.0) with rpmgs script

* Tue Oct 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1.18.1-alt1
- new version 1.18.1 (with rpmrb script)

* Sat Oct 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.1-alt1
- new version 1.17.1 (with rpmrb script)

* Thu Sep 26 2019 Vitaly Lipatov <lav@altlinux.ru> 1.17.0-alt1
- new version 1.17.0 (with rpmrb script)

* Tue Jul 09 2019 Vitaly Lipatov <lav@altlinux.ru> 1.16.0-alt1
- new version 1.16.0 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.15.0-alt1
- new version 1.15.0 (with rpmrb script)

* Fri May 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1.14.0-alt1
- new version 1.14.0 (with rpmrb script)

* Thu Mar 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0 (with rpmrb script)

* Fri Mar 08 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12.1-alt1
- new version 1.12.1 (with rpmrb script)

* Sun Dec 23 2018 Vitaly Lipatov <lav@altlinux.ru> 1.11.1-alt1
- new version 1.11.1 (with rpmrb script)

* Wed Nov 14 2018 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt2
- adopt logrotate conf for ALT

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1.10.0-alt1
- new version 1.10.0 (with rpmrb script)

* Mon Feb 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt2
- fix pid file path in service file
- cleanup spec

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Wed Dec 20 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt2
- use bash4 for all shells scripts
- cleanup spec, change user/group to %netdatauser

* Tue Oct 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Thu Jul 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- new version (1.7.0) with rpmgs script

* Fri Jun 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- build new version

* Tue Mar 07 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt3
- replace shell to /bin/bash4 only on ALT
- fill version.txt with commit id for the release

* Fri Mar 03 2017 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt2
- split postgres module to a subpackage
- fix log dir permission

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
