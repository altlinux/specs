%define defphp php%php_defver

Name: eterban
Version: 0.12
Release: alt2

Summary: Etersoft ban service

License: AGPL-3.0-only
Group: Development/Other
Url: http://wiki.etersoft.ru/eterban

# Source-git: https://gitlab.eterfund.ru/diff/eterban.git
Source: %name-%version.tar

BuildArchitectures: noarch

# error: File must begin with "/": %webserver_htdocsdir/maintenance/
BuildRequires(pre): rpm-macros-webserver-common
BuildRequires(pre): rpm-build-python3 rpm-build-php
BuildRequires: wget

#Requires: python3 python3-module-redis-py
%add_python3_lib_path /usr/share/eterban

%description
Etersoft ban service.

%package common
Summary: Etersoft ban service: common
Group: Development/Other

%description common
Etersoft ban service. Common files.

%package gateway
Summary: Etersoft ban service: gateway
Group: Development/Other
Requires: eterban-common = %EVR
Requires: iptables ipset conntrack-tools
Requires: crontabs logrotate
Requires: python3

%description gateway
Etersoft ban service.

%package web
Summary: Etersoft ban service: web
Group: Development/Other
Requires: eterban-common = %EVR
Requires: nginx
Requires: %defphp-redis
Requires: %defphp-fpm-fcgi
Requires: %defphp-openssl

%description web
Etersoft ban service.

%package fail2ban
Summary: Etersoft ban service: fail2ban
Group: Development/Other
Requires: eterban-common = %EVR
Requires: fail2ban

%description fail2ban
Etersoft ban service.

%post common
if [ -f /etc/%name/settings.ini ]; then
    if rpm -q --quiet %name-web && getent group %webserver_group >/dev/null; then
        chown root:%webserver_group /etc/%name/settings.ini
        chmod 640 /etc/%name/settings.ini
    else
        chown root:root /etc/%name/settings.ini
        chmod 600 /etc/%name/settings.ini
    fi
fi

%post web
if [ -f /etc/%name/settings.ini ] && getent group %webserver_group >/dev/null; then
    chown root:%webserver_group /etc/%name/settings.ini
    chmod 640 /etc/%name/settings.ini
fi

%postun web
if [ "$1" = 0 ] && [ -f /etc/%name/settings.ini ]; then
    chown root:root /etc/%name/settings.ini
    chmod 600 /etc/%name/settings.ini
fi

%prep
%setup

%install
#mkdir -p %buildroot%_sysconfdir/nginx/include/limits/
#install -m644 include/*.conf %buildroot/etc/nginx/include/
#install -m644 include/*.inc %buildroot%_sysconfdir/nginx/include/
#install -m644 include/limits/* %buildroot%_sysconfdir/nginx/include/limits/
mkdir -p %buildroot%_datadir/%name/
mkdir -p %buildroot/etc/%name/
mkdir -p %buildroot/etc/cron.hourly/
mkdir -p %buildroot/etc/logrotate.d/
mkdir -p %buildroot/etc/fail2ban/action.d/
mkdir -p %buildroot%systemd_unitdir
mkdir -p %buildroot/var/log/eterban/
mkdir -p %buildroot%webserver_htdocsdir/%name/
mkdir -p %buildroot/etc/nginx/sites-enabled.d/

install -m 755 -D gateway/usr/bin/eterban.sh %buildroot%_bindir/%name
install -m 755 gateway/usr/share/%name/*.py %buildroot%_datadir/%name/
install -m 644 ban-internal-server/data/www/int2.py %buildroot%_datadir/%name/eterban_internal.py

install -m 644 common/etc/eterban/settings.ini %buildroot/etc/%name/settings.ini
install -m 644 common/etc/eterban/whitelist.txt %buildroot/etc/%name/whitelist.txt

install -m 644 gateway/etc/systemd/system/* %buildroot/%systemd_unitdir
install -m 755 gateway/etc/cron.hourly/get_firehol_ip.sh %buildroot/etc/cron.hourly/get_firehol_ip.sh
install -m 644 gateway/etc/logrotate.d/eterban-gateway %buildroot/etc/logrotate.d/eterban-gateway

install -m 644 ban-server/data/www/* %buildroot%webserver_htdocsdir/%name/
install -m 644 ban-server/etc/nginx/sites-enabled.d/* %buildroot/etc/nginx/sites-enabled.d/
sed -i 's|@PHP_FPM_SOCKET@|/var/run/php%php_defver-fpm/php%php_defver-fpm.sock|' %buildroot/etc/nginx/sites-enabled.d/eterban.conf

install -m 644 prod-server/etc/fail2ban/action.d/* %buildroot/etc/fail2ban/action.d/

cp -a prod-server/usr/share/%name/* %buildroot%_datadir/%name/

%post gateway
%post_service %name
%post_service %name-api
%post_service %name-internal

%preun gateway
%preun_service %name
%preun_service %name-api
%preun_service %name-internal

%files common
%config(noreplace) %attr(0600,root,root) /etc/%name/settings.ini
%config(noreplace) /etc/%name/whitelist.txt
%_datadir/%name/ban.py

%files gateway
%systemd_unitdir/eterban.service
%_bindir/eterban
%dir /var/log/eterban/
/etc/cron.hourly/get_firehol_ip.sh
%config(noreplace) /etc/logrotate.d/eterban-gateway
%dir %_datadir/%name/
%_datadir/%name/eterban_switcher.py
%_datadir/%name/unban.py
%_datadir/%name/autoban_manager.py
%_datadir/%name/autoban_cli.py
%_datadir/%name/eterban_api.py
%_datadir/%name/eterban_internal.py
%_datadir/%name/filter_firehol.py
%systemd_unitdir/eterban-api.service
%systemd_unitdir/eterban-internal.service
%exclude %_datadir/%name/__pycache__/*

%files web
%webserver_htdocsdir/%name/
%config(noreplace) /etc/nginx/sites-enabled.d/eterban.conf

%files fail2ban
%config(noreplace) /etc/fail2ban/action.d/eterban.conf

%changelog
* Wed Nov 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt2
- gateway: add ban_server_internal for the internal ban page address
- README: document a separate web node and cleanup of local files

* Wed Nov 11 2026 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- gateway: exempt whitelisted destinations from internal ban DNAT
- gateway: drop whitelisted networks when importing firehol_level1
- gateway: remove CLI unbans from the Redis active bans set
- eterban: do not fail count and list on IPv4-only gateways

* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt3
- gateway: do not restore legacy ipset snapshots over active sets

* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt2
- gateway: restore Redis Stream command consumption after reconnect
- gateway: send public and internal ban redirects to separate ports
- packaging: harden services and correct installed file ownership

* Wed Jul 08 2026 Vitaly Lipatov <lav@altlinux.ru> 0.11-alt1
- gateway: support list of WAN interfaces via i_interfaces config option
- spec: add whitelist.txt to common package

* Thu Jan 29 2026 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- eterban_switcher.py: return error on redis connection error
- add auto-unban with exponential backoff
- spec: use phpphp_defver macro instead of hardcoded php8.1

* Sat Aug 12 2023 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- switch to php8.1-redis (ALT bug 46925)
- eterban: improve count output
- eterban: add clear command

* Sun Jan 29 2023 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add i_interface2 support
- index.html: update text
- add IPv6 support
- eterban.service: add Restart=always
- eterban.service: add After:
- eterban.spec: add post/preun service section

* Wed Sep 07 2022 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- eterban.sh: add ban for ban manually
- eterban_switcher: increase maxelem

* Sun Mar 27 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- add unban.py for gateway target
- add eterban cli for gateway target

* Sat Mar 26 2022 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt2
- fix fail2ban require

* Sat Mar 26 2022 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- update README.md
- ban.php: get ip font settings.ini
- ban.py: drop config creating
- cleanup packing

* Fri Mar 13 2020 Ruzal Gimazov <diff@etersoft.ru> 0.4-eter2
- create common package

* Fri Mar 13 2020 Ruzal Gimazov <diff@etersoft.ru> 0.4-eter1
- Update settings.ini
- update README.md
- Create ipset dump before exit and restore after start

* Wed Mar 11 2020 Ruzal Gimazov <diff@etersoft.ru> 0.3-eter2
- Add requires python.

* Wed Mar 11 2020 Ruzal Gimazov <diff@etersoft.ru> 0.3-eter1
- add name to jail.conf
- create normalin jail for ban
- remove fail2ban from my project. Update eterban_switcher.py
- add /etc/nginx/sites-enabled/eterban.conf
- update hostname in ban.py

* Sun Nov 10 2019 Ruzal Gimazov <diff@etersoft.ru> 0.2-eter1
- remove eterban.service on the prod-server
- create rule on prod-serv in jail.d
- add configparser, 2 functions with it, changed config name to settings.ini, created logfile
- added configparser, renamed configfile to settings.ini, added new message to chanal 'by'
- changed config

* Sat Sep 07 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
