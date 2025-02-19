%global obs_dir /usr/share/observium

%define crontabdir %_sysconfdir/cron.d
%define ngxconfdir %_sysconfdir/nginx/sites-available.d

%define php_ver 8.3
%define php_user _php_fpm

Name: observium-ce
Version: 24.12
Release: alt0.1
Summary: Low-maintenance auto-discovering network monitoring platform
License: QPL
Group: Monitoring
Url: https://observium.org

Buildarch: noarch

Source0: http://www.observium.org/observium-community-latest.tar
Source1: observium-nginx.conf.in
Source2: observium.cron.in
Patch0: %name-23.1-alt-python3-migration.patch
Patch1: %name-20.9-alt-config.patch
Patch2: %name-24.12-scripts-ifAlias_persist.patch
Patch3: %name-24.12-scripts-distro.patch

BuildRequires: rpm-build-python3 perl-RRD perl-DBI perl-Pod-Usage perl-SNMP-Extension-PassPersist perl-Digest-SHA

%package core
Summary: Observium core files and web content
Group: Monitoring

Requires: php%php_ver php%php_ver-opcache php%php_ver-mysqli php%php_ver-gd2
Requires: php%php_ver-mcrypt php%php_ver-curl pear-core vixie-cron rrd-utils
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
Requires: nginx php%php_ver-fpm-fcgi

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
%autopatch -p2
find . -type f -name \*.py -exec subst 's,env\ python,env python3,' '{}' \;
find . -type f -name \*.py -exec subst 's,\/bin\/python,/bin/python3,' '{}' \;
subst 's,env\ python,env python3,' scripts/{logparser,split-mib-definitions}
find . -type f -exec subst 's,\/opt\/observium,%obs_dir,' '{}' \;
# Explicitly use python3 in hashbangs.
subst '/^#!.*python$/s|python$|python3|' $(grep -Rl '#!.*python$' *)

%install
mkdir -p %buildroot%obs_dir/rrd
cp -ar . %buildroot%obs_dir
mkdir -p %buildroot{%_bindir,%_sysconfdir/xinetd.d,%prefix/lib/observium_agent/local,%_unitdir,%_logdir/%name}
install -m 0755 scripts/observium_agent %buildroot%_bindir
install -m 0640 scripts/observium_agent_xinetd %buildroot/%_sysconfdir/xinetd.d/observium_agent

# Install the nginx configuration file.
install -pD -m644 /dev/null %buildroot%ngxconfdir/%name.conf
sed -e 's|@DATADIR@|%obs_dir|g;s|@PHP_VER@|%php_ver|g' \
	%SOURCE1 > %buildroot%ngxconfdir/%name.conf

# Install crontab file
install -pD -m644 /dev/null %buildroot%crontabdir/%name
sed -e 's|@DATADIR@|%obs_dir|g' \
        %SOURCE2 > %buildroot%crontabdir/%name

# Install config file
install -pD -m644 /dev/null %buildroot%_sysconfdir/%name/config.php
cat config.php.default > %buildroot%_sysconfdir/%name/config.php
ln -sr %buildroot%_sysconfdir/%name/config.php %buildroot%obs_dir/config.php
ln -sr %buildroot%_logdir/%name %buildroot%obs_dir/logs

# systemd services
mv %buildroot%obs_dir/scripts/systemd/* %buildroot%_unitdir/
rm -rf %buildroot%obs_dir/scripts/systemd

%files core
%dir %_sysconfdir/%name
%config (noreplace) %attr(0640,%php_user,%php_user) %_sysconfdir/%name/config.php
%crontabdir/%name
%dir %obs_dir
%obs_dir/*
%_unitdir/observium-notifications.*
%attr(0750,root,root) %_logdir/%name
%exclude %obs_dir/scripts

%files agent
%_bindir/observium_agent
%config (noreplace) %attr(0640,root,root) %_sysconfdir/xinetd.d/observium_agent
%dir %prefix/lib/observium_agent/local
%_unitdir/observium_agent.*

%files scripts
%dir %obs_dir/scripts
%obs_dir/scripts/*
%exclude %obs_dir/scripts/observium_agent
%exclude %obs_dir/scripts/observium_agent_xinetd
%exclude %obs_dir/scripts/agent-local

%files nginx
%ngxconfdir/%name.conf

%changelog
* Wed Feb 19 2025 L.A. Kostis <lakostis@altlinux.ru> 24.12-alt0.1
- Updated to v24.12 CE.
- php8.1->php8.3.
- added systemd services.

* Thu Jul 13 2023 L.A. Kostis <lakostis@altlinux.ru> 23.1-alt0.1
- Updated to v23.1 CE (closes #46907).
- php7->php8.1.
- Update BR (added perl-DBI).

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
