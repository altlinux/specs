Name: eterban
Version: 0.8
Release: alt1

Summary: Etersoft ban service

License: AGPLv3
Group: Development/Other
Url: http://wiki.etersoft.ru/eterban

# Source-git: https://gitlab.eterfund.ru/diff/eterban.git
Source: %name-%version.tar

BuildArchitectures: noarch

# error: File must begin with "/": %webserver_htdocsdir/maintenance/
BuildRequires(pre): rpm-macros-webserver-common rpm-build-python3

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

%description gateway
Etersoft ban service.

%package web
Summary: Etersoft ban service: web
Group: Development/Other
Requires: eterban-common = %EVR
Requires: nginx,php7-redis

%description web
Etersoft ban service.

%package fail2ban
Summary: Etersoft ban service: fail2ban
Group: Development/Other
Requires: eterban-common = %EVR
Requires: fail2ban

%description fail2ban
Etersoft ban service.

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
mkdir -p %buildroot/etc/fail2ban/action.d/
mkdir -p %buildroot%systemd_unitdir
mkdir -p %buildroot/var/log/eterban/
mkdir -p %buildroot%webserver_htdocsdir/%name/
mkdir -p %buildroot/etc/nginx/sites-enabled.d/

install -m 755 -D gateway/usr/bin/eterban.sh %buildroot%_bindir/%name
cp -a gateway/usr/share/%name/* %buildroot%_datadir/%name/

install -m 644 common/etc/eterban/* %buildroot/etc/%name/

install -m 644 gateway/etc/systemd/system/* %buildroot/%systemd_unitdir
install -m 644 gateway/etc/cron.hourly/* %buildroot/etc/cron.hourly/

install -m 644 ban-server/data/www/* %buildroot%webserver_htdocsdir/%name/
install -m 644 ban-server/etc/nginx/sites-enabled.d/* %buildroot/etc/nginx/sites-enabled.d/

install -m 644 prod-server/etc/fail2ban/action.d/* %buildroot/etc/fail2ban/action.d/

cp -a prod-server/usr/share/%name/* %buildroot%_datadir/%name/

%post gateway
%post_service %name

%preun gateway
%preun_service %name


%files common
%config(noreplace) /etc/%name/settings.ini

%files gateway
%systemd_unitdir/eterban.service
%_bindir/eterban
%dir /var/log/eterban/
%config(noreplace) /etc/cron.hourly/get_firehol_ip.sh
%dir %_datadir/%name/
%_datadir/%name/eterban_switcher.py
%_datadir/%name/unban.py

%files web
%webserver_htdocsdir/%name/
%config(noreplace) /etc/nginx/sites-enabled.d/eterban.conf

%files fail2ban
%_datadir/%name/ban.py
%config(noreplace) /etc/fail2ban/action.d/eterban.conf

%changelog
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
