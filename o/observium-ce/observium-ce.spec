%global obs_dir /usr/share/observium

%define crontabdir %_sysconfdir/cron.d
%define ngxconfdir %_sysconfdir/nginx/sites-available.d

Name: observium-ce
Version: 20.9
Release: alt0.2
Summary: Low-maintenance auto-discovering network monitoring platform
License: QPL
Group: Monitoring
Url: https://observium.org

Buildarch: noarch

Source0: http://www.observium.org/observium-community-latest.tar
Source1: observium-nginx.conf.in
Source2: observium.cron.in
Patch0: %name-%version-alt-python3-migration.patch
Patch1: %name-%version-alt-config.patch

BuildRequires: rpm-build-python3 perl-RRD perl-Pod-Usage perl-SNMP-Extension-PassPersist perl-Digest-SHA

%package core
Summary: Observium core files and web content
Group: Monitoring

Requires: php7 php7-opcache php7-mysqli php7-gd2
Requires: php7-mcrypt pear-core vixie-cron rrd-utils
Requires: net-snmp-clients fping python3-module-pymysql
Requires: whois ipmitool graphviz ImageMagick-tools

%package agent
Summary: Observium UNIX agent
Group: Monitoring
Requires: xinetd

%package scripts
Summary: Observium maintenance scripts
Group: Monitoring
Requires: %name-core = %EVR

%package nginx
Group: System/Servers
Summary: Observium configuration for nginx
BuildArch: noarch
Requires: %name-core = %EVR
Requires: nginx spawn-fcgi

%description
Observium is a low-maintenance auto-discovering network monitoring platform
supporting a wide range of device types, platforms and operating systems
including Cisco, Windows, Linux, HP, Juniper, Dell, FreeBSD, Brocade,
Netscaler, NetApp and many more.

%description core
Observium is a low-maintenance auto-discovering network monitoring platform
supporting a wide range of device types, platforms and operating systems
including Cisco, Windows, Linux, HP, Juniper, Dell, FreeBSD, Brocade,
Netscaler, NetApp and many more.

This package includes core files and web content

%description agent
Observium UNIX Agent

%description scripts
Observium maintentance scripts

%description nginx
Observium configuration files for nginx

%prep
%setup -n observium
%patch0 -p2
%patch1 -p2
find . -type f -name \*.py -exec subst 's,env\ python,env python3,' '{}' \;
find . -type f -name \*.py -exec subst 's,\/bin\/python,/bin/python3,' '{}' \;
subst 's,env\ python,env python3,' scripts/{logparser,split-mib-definitions}
find . -type f -exec subst 's,\/opt\/observium,%obs_dir,' '{}' \;

%install
mkdir -p %buildroot%obs_dir/rrd
cp -ar . %buildroot%obs_dir
mkdir -p %buildroot{%_bindir,%_sysconfdir/xinetd.d,%prefix/lib/observium_agent/local}
install -m 0755 scripts/observium_agent %buildroot%_bindir
install -m 0640 scripts/observium_agent_xinetd %buildroot/%_sysconfdir/xinetd.d/observium_agent

# Install the nginx configuration file.
install -pD -m644 /dev/null %buildroot%ngxconfdir/%name.conf
sed -e 's|@DATADIR@|%obs_dir|g' \
	%SOURCE1 > %buildroot%ngxconfdir/%name.conf

# Install crontab file
install -pD -m644 /dev/null %buildroot%crontabdir/%name
sed -e 's|@DATADIR@|%obs_dir|g' \
        %SOURCE2 > %buildroot%crontabdir/%name

# Install config file
install -pD -m644 /dev/null %buildroot%_sysconfdir/%name/config.php
cat config.php.default > %buildroot%_sysconfdir/%name/config.php

%files core
%dir %_sysconfdir/%name
%config (noreplace) %attr(0640,root,root) %_sysconfdir/%name/config.php
%crontabdir/%name
%dir %obs_dir
%obs_dir/*
%exclude %obs_dir/scripts

%files agent
%_bindir/observium_agent
%config (noreplace) %attr(0640,root,root) %_sysconfdir/xinetd.d/observium_agent
%dir %prefix/lib/observium_agent/local

%files scripts
%dir %obs_dir/scripts
%obs_dir/scripts/*
%exclude %obs_dir/scripts/observium_agent
%exclude %obs_dir/scripts/observium_agent_xinetd
%exclude %obs_dir/scripts/agent-local

%files nginx
%ngxconfdir/%name.conf

%changelog
* Thu Sep 16 2021 L.A. Kostis <lakostis@altlinux.ru> 20.9-alt0.2
- .spec: optimize requires.

* Mon Sep 13 2021 L.A. Kostis <lakostis@altlinux.ru> 20.9-alt0.1
- Updated to 20.9 CE.
- Removed python2 dependency.
- Update perl BR.
- Added -nginx and cron configuration.
- Use default config location.

* Mon Jun 03 2019 L.A. Kostis <lakostis@altlinux.ru> 18.9.1-alt0.2
- Adopt for ALTLinux.

* Thu Oct 18 2018 Konstantin Lepikhov <konstantin.lepikhov@geant.org> 18.9.1.GN1
- Initial build for GEANT.
