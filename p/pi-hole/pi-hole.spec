# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define _name pihole
%define _servicename pi-hole

Name:    pi-hole
Version: 6.4.2
Release: alt1

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
  install -Dm755 advanced/Scripts/list.sh %buildroot%_datadir/%_name/list.sh
  install -Dm755 advanced/Scripts/utils.sh %buildroot%_datadir/%_name/utils.sh
# install -Dm755 advanced/Scripts/wildcard_regex_converter.sh %buildroot%_datadir/%_name/wildcard_regex_converter.sh
  install -Dm755 advanced/Scripts/query.sh %buildroot%_datadir/%_name/query.sh
  install -Dm755 advanced/Scripts/piholeNetworkFlush.sh %buildroot%_datadir/%_name/piholeNetworkFlush.sh

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

  # install -Dm644 advanced/dnsmasq.conf.original %buildroot%_sysconfdir/dnsmasq.conf
  # sed -i 's!^#conf-dir=/etc/dnsmasq.d$!conf-dir=/etc/dnsmasq.d!' %buildroot%_sysconfdir/dnsmasq.conf

  install -Dm644 %SOURCE2 %buildroot%_sysconfdir/dnsmasq.d/01-pihole.conf

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
CORE_HASH=341376
CORE_VERSION=v%version
GITHUB_CORE_VERSION=v%version
GITHUB_CORE_HASH=341376
FTL_VERSION=v6.6.2
FTL_BRANCH=master
FTL_HASH=82c58cc4
GITHUB_FTL_VERSION=v6.6.2
GITHUB_FTL_HASH=82c58cc4
EOF

cat >%buildroot%_datadir/%_name/update.sh <<EOF
#!/bin/sh

echo "Update is not supported, use 'apt-get dist-upgrade'"
exit 0
EOF

cat >%buildroot%_datadir/%_name/uninstall.sh <<EOF
#!/bin/sh

echo "Uninstall is not supported, use 'apt-get remove'"
exit 0
EOF

chmod 0755 %buildroot%_datadir/%_name/update.sh %buildroot%_datadir/%_name/uninstall.sh

%files
%doc *.md LICENSE
%_bindir/*
%config(noreplace)%_sysconfdir/%_name/logrotate
%_sysconfdir/%_name
%_sysconfdir/.pihole
%_datadir/%_name
%_tmpfilesdir/%name.conf
#%%_sysconfdir/dnsmasq.conf
%_sysconfdir/dnsmasq.d
%_unitdir/*.service
%_unitdir/*.timer
%_unitdir/multi-user.target.wants/*.timer

%changelog
* Thu Jun 18 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.4.2-alt1
- v6.4.2

* Tue Apr 07 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.4.1-alt1
- v6.4.1

* Thu Feb 19 2026 Andrew A. Vasilyev <andy@altlinux.org> 6.4-alt1
- v6.4

* Fri Nov 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.3-alt1
- v6.3

* Wed Oct 29 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.2.2-alt1
- v6.2.2

* Tue Oct 28 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.2.1-alt1
- v6.2.1

* Tue Aug 05 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.1.4-alt1
- v6.1.4

* Tue Jun 10 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.1.2-alt1
- v6.1.2

* Mon Jun 02 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.1.1-alt1
- v6.1.1

* Thu Apr 03 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0.6-alt1
- v6.0.6

* Mon Mar 10 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0.5-alt1
- v6.0.5

* Wed Feb 19 2025 Andrew A. Vasilyev <andy@altlinux.org> 6.0-alt1
- v6.0

* Fri Feb 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt5
- use only one config dir

* Fri Feb 14 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt4
- use additional config dir by default

* Mon Jan 27 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt3
- print information about update/uninstall actions (Closes: #52794)

* Wed Jan 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt2
- fix version printing (Closes: #52792)

* Wed Jan 22 2025 Andrew A. Vasilyev <andy@altlinux.org> 5.18.4-alt1
- v5.18.4

* Tue Nov 12 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.18.3-alt1
- Initial build for ALT.

