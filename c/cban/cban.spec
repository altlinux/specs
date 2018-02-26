Summary:	Current BANdwidth by Nicu Pavel
Summary(ru_RU.UTF8): Current BANdwidth - утилита отображения сетевого трафика
Name:		cban
Version:	0.1.8
Release:	alt2.2
License:	GPLv2
Group:		Monitoring
Url:		http://panic.eu.org/linux/cban/
Source0:	http://panic.eu.org/linux/cban/%name-%version-0.tgz
Source1:	readme_alt.cp1251
Patch0:		%name-0.1.8-alt_optflags-int.diff
Packager:	Motsyo Gennadi <drool@altlinux.ru>

%description
Current Bandwidth (CBan) displays current traffic
on a selected interface. Traffic can be seen in
(kilo)bytes/bits in console in an output suitable
for mrtg (config file included) or sent to a RRDTOOL
database (database creation, stats.cgi, and cron
examples included)

%description -l ru_RU.UTF8
Current Bandwidth (CBan) показывает текущий трафик через выбранный интерфейс.
Трафик может быть отображён в (кило)байтах или (кило)битах в консоли, в виде, 
пригодном для mrtg (конфигурационный файл включён в пакет), или отправлен в 
базу данных RRDTOOL (примеры создания базы данных, stats.cgi, и конфиграции 
cron также включены в пакет).

Автор: Nicu Pavel

%prep
%setup -q -n %name
%patch0 -p1

%build
%__install -Dp -m 0644 %SOURCE1 ./readme_alt.cp1251
cd src
make clean
export OPTFLAGS='%optflags'
%make_build

%install
%__install -Dp -m 0755 src/%name %buildroot%_sbindir/%name

%files
%doc AUTHORS COPYING Changelog KnownBUGS INSTALL etc readme_alt.cp1251
%_sbindir/%name

%changelog
* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt2.2
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt2.1
- added russian description and summary (fixed #22086). Thanks to Phantom.

* Sun Dec 09 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt2
- add Url for Source

* Wed Oct 03 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt1
- build for Sisyphus
- add readme_alt.cp1251 by Valery V. Rusnak <xacan1 at ukr.net>

* Tue Oct 02 2007 Motsyo Gennadi <drool@altlinux.ru> 0.1.8-alt0.M40.1
- initial build for ALT Linux (M40)
