Name: dmarc-srg
Version: 2.3.20261008
Release: alt1

Summary: DMARC report parser, viewer and summary generator

License: GPL-3.0-only AND BSD-2-Clause AND LGPL-2.1-only AND MIT
Group: Networking/WWW
Url: https://github.com/liuch/dmarc-srg
# Source-url: https://github.com/liuch/dmarc-srg/archive/be1ff0977fec5382aea86a502846376357db6413.tar.gz
Source: %name-%version.tar
Source1: %name-vendor-%version.tar
Source2: vendor_config.php
Source3: %name@.service
Source4: %name-fetch_reports.timer
Source5: %name-mailbox_cleaner.timer
Source6: %name-reports_cleaner.timer
Source7: %name-reportlog_cleaner.timer
Source8: %name.sysusers.conf
Source9: README.ALT.ru
Patch0: dmarc-srg-imapengine-default.patch

%define defphp php%php_defver

BuildArch: noarch
BuildRequires(pre): rpm-build-php >= 8.4
BuildRequires: %defphp
Requires: %defphp
Requires: %defphp-mbstring %defphp-pdo_mysql %defphp-zip %defphp-openssl %defphp-xmlreader

%description
DMARC aggregate report parser, web viewer and summary report generator.
Reports can be fetched from IMAP mailboxes with the ImapEngine library.
A MariaDB or MySQL database is required and can run on a remote host.
The web document root is /usr/share/dmarc-srg/public.

%description -l ru_RU.UTF-8
Разбор и просмотр агрегированных отчётов DMARC, получение по IMAP и
формирование сводок. База MariaDB или MySQL может находиться на другом сервере.
Корень веб-интерфейса: /usr/share/dmarc-srg/public.

%prep
%setup -a1
%patch0 -p1

%install
install -d %buildroot%_datadir/%name
cp -a classes config public utils vendor init.php template.html \
    %buildroot%_datadir/%name/
install -m644 %SOURCE2 %buildroot%_datadir/%name/config/vendor_config.php
install -Dm640 config/conf.sample.php %buildroot%_sysconfdir/%name/conf.php
install -Dm644 %SOURCE3 %buildroot%_unitdir/%name@.service
for timer in %SOURCE4 %SOURCE5 %SOURCE6 %SOURCE7; do
    install -m644 "$timer" %buildroot%_unitdir/
done
install -Dm644 %SOURCE8 %buildroot%_sysusersdir/%name.conf
install -m644 %SOURCE9 README.ALT.ru

%check
# Validate every installed PHP source with the target interpreter.
find %buildroot%_datadir/%name -name '*.php' -print0 | xargs -0 -n1 %defphp -n -l
%defphp -n -l %buildroot%_sysconfdir/%name/conf.php

%pre
%sysusers_create_package %name %SOURCE8

%files
%doc README.md LICENSE README.ALT.ru
%dir %attr(0750,root,dmarc-srg) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,dmarc-srg) %_sysconfdir/%name/conf.php
%_datadir/%name
%_unitdir/%name@.service
%_unitdir/%name-*.timer
%_sysusersdir/%name.conf

%changelog
* Sun Nov 08 2026 Vitaly Lipatov <lav@altlinux.ru> 2.3.20261008-alt1
- new version 2.3.20261008
- add BuildRequires: php%%php_defver and rpm-build-php; drop php8.3
- use ImapEngine for IMAP access with the default PHP version
- add Requires: php%%php_defver-xmlreader (checked by utils/check_config.php)

* Sun Nov 08 2026 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- initial build for ALT Linux.

