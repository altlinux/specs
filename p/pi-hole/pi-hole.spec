# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define _name pihole
%define _servicename pi-hole

Name:    pi-hole
Version: 5.18.4
Release: alt2

Summary: The Pi-hole is an advertising-aware DNS/Web server
License: EUPL-1.2
Group:   System/Servers
Url:     https://github.com/pi-hole/pi-hole

BuildArch: noarch

Source: %name-%version.tar
Source1: %name.tmpfile
Source2: %_name.conf
Source3: %name-gravity.timer
Source4: %name-gravity.service
Source5: %name-logtruncate.timer
Source6: %name-logtruncate.service
Source7: mimic_setupVars.conf.sh
Source8: mimic_basic-install.sh

BuildRequires(pre): rpm-macros-systemd

Requires: pi-hole-ftl
Requires: netcat
Requires: iproute2
Requires: bind-utils
Requires: lsof
Requires: procps-ng
Requires: sudo
Requires: firewalld
Requires: iputils

%filter_from_requires /checkout/d

%description
The Pi-hole is an advertising-aware DNS/Web server.

%prep
%setup

%build
sed -i 's!/opt/!%_datadir/!g' pihole gravity.sh advanced/Scripts/*.sh
sed -i 's!/usr/local/!/usr/!g' pihole gravity.sh advanced/Scripts/*.sh

%install
  install -Dm755 %_name %buildroot%_bindir/%_name

  install -dm755 %buildroot%_datadir/%_name
  install -Dm755 gravity.sh %buildroot%_datadir/%_name/gravity.sh
  install -Dm755 advanced/Scripts/version.sh %buildroot%_datadir/%_name/version.sh
  install -Dm755 advanced/Scripts/updatecheck.sh %buildroot%_datadir/%_name/updatecheck.sh
  install -Dm755 advanced/Scripts/piholeLogFlush.sh %buildroot%_datadir/%_name/piholeLogFlush.sh
  install -Dm755 advanced/Scripts/chronometer.sh %buildroot%_datadir/%_name/chronometer.sh
  install -Dm755 advanced/Scripts/list.sh %buildroot%_datadir/%_name/list.sh
  install -Dm755 advanced/Scripts/utils.sh %buildroot%_datadir/%_name/utils.sh
  install -Dm755 advanced/Scripts/webpage.sh %buildroot%_datadir/%_name/webpage.sh
# install -Dm755 advanced/Scripts/wildcard_regex_converter.sh %buildroot%_datadir/%_name/wildcard_regex_converter.sh
  install -Dm755 advanced/Scripts/query.sh %buildroot%_datadir/%_name/query.sh
  install -Dm755 advanced/Scripts/%_name-reenable.sh %buildroot%_datadir/%_name/%_name-reenable.sh
  install -Dm755 advanced/Scripts/piholeARPTable.sh %buildroot%_datadir/%_name/piholeARPTable.sh

  install -Dm755 advanced/Scripts/piholeDebug.sh %buildroot%_datadir/%_name/piholeDebug.sh

  install -Dm644 advanced/Scripts/COL_TABLE %buildroot%_datadir/%_name/COL_TABLE

  mkdir -p %buildroot%_sysconfdir/.pihole/advanced/Templates/
  install -Dm644 advanced/Templates/gravity.db.sql %buildroot%_sysconfdir/.pihole/advanced/Templates/gravity.db.sql
  install -Dm644 advanced/Templates/gravity_copy.sql %buildroot%_sysconfdir/.pihole/advanced/Templates/gravity_copy.sql
  mkdir -p %buildroot%_sysconfdir/.pihole/advanced/Scripts/
  cp -dpr --no-preserve=ownership advanced/Scripts/database_migration %buildroot%_sysconfdir/.pihole/advanced/Scripts/
  mkdir -p "%buildroot%_sysconfdir/.pihole/automated install/"
  install -Dm755 %SOURCE7 "%buildroot%_sysconfdir/.pihole/automated install/mimic_setupVars.conf.sh"
  install -Dm755 %SOURCE8 "%buildroot%_sysconfdir/.pihole/automated install/basic-install.sh"

  install -Dm644 advanced/dnsmasq.conf.original %buildroot%_sysconfdir/dnsmasq.conf
  install -Dm644 %SOURCE2 %buildroot%_sysconfdir/dnsmasq.d/01-pihole.conf
  install -Dm644 advanced/06-rfc6761.conf %buildroot%_sysconfdir/dnsmasq.d/06-rfc6761.conf

  install -Dm644 %SOURCE1 %buildroot%_tmpfilesdir/%name.conf

  install -Dm644 %SOURCE3 %buildroot%_unitdir/%name-gravity.timer
  install -Dm644 %SOURCE4 %buildroot%_unitdir/%name-gravity.service
  install -Dm644 %SOURCE5 %buildroot%_unitdir/%name-logtruncate.timer
  install -Dm644 %SOURCE6 %buildroot%_unitdir/%name-logtruncate.service
  install -dm755 %buildroot%_unitdir/multi-user.target.wants
  ln -s ../%name-gravity.timer %buildroot%_unitdir/multi-user.target.wants/%name-gravity.timer
  ln -s ../%name-logtruncate.timer %buildroot%_unitdir/multi-user.target.wants/%name-logtruncate.timer

  install -dm775 %buildroot%_sysconfdir/%_name
  install -Dm644 advanced/Templates/logrotate %buildroot%_sysconfdir/%_name/logrotate
  sed -i 's/# su #/su pihole pihole/' %buildroot%_sysconfdir/%_name/logrotate
  install -dm755 %buildroot%_datadir/%_name/configs
#  install -Dm644 adlists.list %buildroot%_sysconfdir/%_name/adlists.list

cat >%buildroot%_sysconfdir/%_name/setupVars.conf <<EOF
PIHOLE_INTERFACE=""
IPV4_ADDRESS=
IPV6_ADDRESS=
INSTALL_WEB_INTERFACE=false
QUERY_LOGGING=true
PIHOLE_DNS_1=1.1.1.1
PIHOLE_DNS_2=8.8.8.8
EOF

cat >%buildroot%_sysconfdir/%_name/versions <<EOF
CORE_BRANCH=master
CORE_HASH=891da4da
CORE_VERSION=v%version
GITHUB_CORE_VERSION=v%version
GITHUB_CORE_HASH=2cf046d5
FTL_VERSION=v5.25.2
FTL_BRANCH=master
FTL_HASH=8943e260
GITHUB_FTL_VERSION=v5.25.2
GITHUB_FTL_HASH=8943e260
EOF

%files
%doc *.md LICENSE
%_bindir/*
%config(noreplace)%_sysconfdir/%_name/logrotate
%_sysconfdir/%_name
%_sysconfdir/.pihole
%_datadir/%_name
%_tmpfilesdir/%name.conf
%_sysconfdir/dnsmasq.conf
%_sysconfdir/dnsmasq.d
%_unitdir/*.service
%_unitdir/*.timer
%_unitdir/multi-user.target.wants/*.timer

%changelog
* Wed Jan 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt2
- fix version printing (Closes: #52792)

* Wed Jan 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt1
- v5.18.4

* Tue Nov 12 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.18.3-alt1
- Initial build for ALT.

