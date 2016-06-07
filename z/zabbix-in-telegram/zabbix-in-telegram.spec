%define z_dir %_sysconfdir/zabbix/alertscripts

Summary: Zabbix Notifications with graphs in Telegram
Name: zabbix-in-telegram
Version: 20160607
Release: alt2
License: MIT
Group: Monitoring
URL: https://github.com/ableev/Zabbix-in-Telegram
Source: %name-%version.tar
Patch: %name-%version-%release.patch

Packager: Evgenii Terechkov <evg@altlinux.org>

Requires: zabbix-server-common > 3.0.0
BuildArch: noarch

%description
Zabbix Notifications with graphs in Telegram

%prep
%setup

%build

%install
mkdir -p %buildroot%z_dir
install -p -m 755 zbxtg.py %buildroot%z_dir/zbxtg.py
install -p -m 644 zbxtg_settings.example.py %buildroot%z_dir/zbxtg_settings.py

%files
%z_dir/zbxtg.py
%config(noreplace) %z_dir/zbxtg_settings.py
%doc README.md LICENSE.txt

%changelog
* Tue Jun  7 2016 Terechkov Evgenii <evg@altlinux.org> 20160607-alt2
- c23673b

* Tue Jun  7 2016 Terechkov Evgenii <evg@altlinux.org> 20160607-alt1
- Initial build for ALT Linux Sisyphus (77e163b)

