# -*- mode: RPM-SPEC; tab-width: 8; fill-column: 70; -*- 

%define _altdata_dir %_datadir/alterator

Name: alterator-zabbix-server
Version: 0.0.4
Release: alt1

Summary: Alterator module for Zabbix server setup
License: GPL
Group: System/Configuration/Other

Source:%name-%version.tar

Requires: alterator >= 4.7-alt1 alterator-sh-functions >= 0.6-alt5
Requires: alterator-l10n >= 2.9-alt1
Requires: augeas >= 1.2.0
Requires: MySQL-server
Requires: zabbix-server-mysql zabbix-phpfrontend-engine
Requires: php5-fpm-fcgi
Requires: nginx
Requires: alterator-service-functions >= 2.0.0
Requires: php5-sockets php5-gd2 php5-mysqli php5-mbstring
Requires: nginx-webapps-ssl
Conflicts: alterator-lookout < 1.6-alt3
BuildArch: noarch
BuildRequires: alterator


%description
Alterator module for Zabbix server setup

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

%files -f %name.lang
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_sysconfdir/nginx/webapps-available.d/alterator-zabbix-server.conf

%changelog
* Mon Dec 15 2014 Mikhail Efremov <sem@altlinux.org> 0.0.4-alt1
- Use https for Zabbix.

* Wed Nov 26 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt2
- fix typo

* Wed Nov 26 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.3-alt1
- ru_RU web interface, admin pass

* Mon Aug 18 2014 Mikhail Efremov <sem@altlinux.org> 0.0.2-alt1
- Don't expose password in the UI.
- Use nginx-webapps.
- Require some php5 modules.

* Wed Jul 02 2014 Andriy Stepanov <stanv@altlinux.ru> 0.0.1-alt1
- Initial build

