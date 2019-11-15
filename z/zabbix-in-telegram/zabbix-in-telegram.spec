%define z_dir %_sysconfdir/zabbix/alertscripts

Name: zabbix-in-telegram
Version: 20160607
Release: alt3

Summary: Zabbix Notifications with graphs in Telegram
License: MIT
Group: Monitoring
URL: https://github.com/ableev/Zabbix-in-Telegram
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: python-tools-2to3
Requires: zabbix-server-common > 3.0.0


%description
Zabbix Notifications with graphs in Telegram

%prep
%setup

## py2 -> py3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
##

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
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 20160607-alt3
- python2 -> python3

* Tue Jun  7 2016 Terechkov Evgenii <evg@altlinux.org> 20160607-alt2
- c23673b

* Tue Jun  7 2016 Terechkov Evgenii <evg@altlinux.org> 20160607-alt1
- Initial build for ALT Linux Sisyphus (77e163b)

