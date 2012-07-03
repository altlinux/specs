Name:     oinkmaster
Version:  2.0
Release:  alt2

Summary:  Automated updating of Snort IDS rules 
License:  BSD
Group:    Security/Networking
Url:      http://%name.sourceforge.net
Source:   http://mesh.dl.sourceforge.net/sourceforge/%name/%name-%version.tar.gz

BuildArch: noarch
Requires: snort-base

Summary(ru_RU.KOI8-R): Утилита обновления сигнатур для Snort

%define   myconfdir   %_sysconfdir/snort
%define   myrulesdir  %myconfdir/rules
%define   cron_daily  %_sysconfdir/cron.daily

%description
Oinkmaster is simple Perl script released under the BSD license that
helps you keep your Snort rules current with little or no user
interaction. It has quite a few useful features regarding rules
management, such as ability to enable, disable and modify specified
rules after each update. It will tell you the exact changes from your
previous rules, so you have total control of what's going on.
It may be useful in conjunction with any program that can use Snort
rules, like Snort (doh!) or Prelude-NIDS.

Oinkmaster is most often used to grab the latest official rules tarball
from www.snort.org and apply a set of modifications to them (such as
disabling unwanted ones), but it can just as well be used to manage
your local rules and also third party rules and distribute them to
multiple sensors with ability to fine-tune the rules on each sensor or
group of sensors. Oinkmaster is designed to integrate well with other
scripts and you can easily setup a very powerful rules management system.
See the FAQ for hints and suggestions.

%description -l ru_RU.KOI8-R
Oinkmaster предназначен для обновления базы сигнатур Snort NIDS,
системы обнаружения и блокирования сетевых атак. Возможности:
 * обновление в пакетном режиме без вмешательства администратора,
 * разрешение, запрет или модификация указанных правил после обновления,
 * детальный отчёт по обновлениям,
 * совместное использование локальных и скачиваемых правил,
 * скачивание правил одновременно из нескольких разных источников,
 * готовые примеры настроек для скачивания всех вариантов правил с официального
   сайта (по платной подписке, по свободной регистрации, community-based).

%prep
%setup -q

%build  #..nothing to do

%install
install -pD %name.conf -m 600 %buildroot%_sysconfdir/%name.conf
install -pD %name.pl          %buildroot%_bindir/%name
install -pD %name.1           %buildroot%_man1dir/%name.1

%files
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.conf
%_man1dir/%{name}*
%doc ChangeLog FAQ LICENSE README* contrib

%changelog
* Mon Nov 02 2009 Mikhail Efremov <sem@altlinux.org> 2.0-alt2
- spec cleanup.
- use config(noreplace) for oinkmaster.conf.
- don't package cron.daily script.

* Wed Sep 13 2006 Ilya Evseev <evseev@altlinux.ru> 2.0-alt1
- initial build for ALTLinux

## EOF ##
