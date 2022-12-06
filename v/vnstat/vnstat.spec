# SPEC file for vnStat package

Name:    vnstat
Version: 2.10
Release: alt1

Summary: console-based network traffic monitor
Summary(ru_RU.UTF-8): консольная утилита для подсчёта трафика

License: %gpl2only
Group:   Monitoring
URL:     http://humdi.net/vnstat/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.control
Source2: %{name}d.init
Source3: %name.cron
Source4: %{name}d.tmpfiles
Source5: %{name}-update.sh

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu May 09 2019
# optimized out: fontconfig gem-power-assert glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config pkg-config python-base python-modules python3 python3-base python3-dev ruby ruby-coderay ruby-method_source ruby-pry ruby-rake ruby-rdoc ruby-stdlibs sh4 tzdata
BuildRequires: libgd3-devel libsqlite3-devel

%define cron_freq    5
%define cron_file    %_sysconfdir/cron.d/%name
%define data_dir     %_localstatedir/%name
%define piddir       /var/run/%{name}d

%description
vnStat  is a console-based network  traffic monitor that keeps a log
of daily network traffic for the selected interface(s). vnStat isn't
a packet sniffer. The traffic information is analyzed from the /proc
filesystem. vnStat runs under unprivileged user account and does not
need any system's tuning, but can account only a total interface's
traffic with some issues on accuracy.

%description -l ru_RU.UTF-8
vnStat собирает и выводит статистику потребления трафика.
Для получения информации он использует файловую систему /proc.

Достоинством такого подхода является возможность собирать информацию
с привилегиями рядового пользователя. С другой стороны, при этом не
учитываются такие подробности, как IP-адреса клиентов, типы соединений
и т.д. Отчёты содержат только общее количество принятых и переданных
байт, упорядоченное по периодам времени и сетевым интерфейсам.

Для накопления статистики vnStat вызывает себя через Cron каждые
%cron_freq минут; для сохранения статистики используется база несложного
собственного формата. При запуске из консоли vnStat читает её и выводит
отчёт по заданным критериям.

%package server
Summary: optional server for vnstat network traffic monitor
#Summary(ru_RU.UTF-8): 
Group:   Monitoring
Requires: %name = %version-%release

%description server
vnStat  is a console-based network  traffic monitor that keeps a log
of daily network traffic for the selected interface(s).

This package contains optional standalone server for vnstat network
traffice monitor.

%package  vnstati
Summary: optional png image output support for vnstat
Group:   Monitoring
Requires: %name = %version-%release

%description vnstati
vnStat  is a console-based network  traffic monitor that keeps a log
of daily network traffic for the selected interface(s).

This package contains optional vnstati utility to provide PNG image
output support for statistics collected using vnstat.

%prep
%setup -q
%patch0 -p1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING
chmod a-x examples/vnstat.cgi

%build
%configure
%make_build

%install
%makeinstall
/bin/install -pD %SOURCE1  %buildroot%_controldir/%name
/bin/install -pD -m 0664 %SOURCE3  %buildroot%cron_file
/bin/sed -e 's#%%cron_freq#%{cron_freq}#' -i %buildroot%cron_file
/bin/install -pD %SOURCE4  %buildroot%_tmpfilesdir/%{name}d.conf

/bin/install -pD %SOURCE5  %buildroot%_sbindir/%{name}-update

install -pD -m 0755 -- %SOURCE2 %buildroot/%_initdir/%{name}d
install -pD -m 0755 examples/systemd/vnstat.service %buildroot%_unitdir/%{name}d.service

mkdir -p %buildroot%piddir
mkdir -p %buildroot%data_dir


%pre
%_sbindir/groupadd -r -f %name &>/dev/null
%_sbindir/useradd -r -g %name -d %data_dir -s /dev/null \
	-c "vnStat database producer" -M -G proc -n %name &>/dev/null ||:

# For upgrade from 1.4-alt1 
/usr/bin/id -Gn %name | /bin/grep -qw proc || %_sbindir/usermod -G proc %name ||:

%post
# Replace unknown Interface in the configuration
%_sbindir/%{name}-update config-unknown


%post server
# Create databases for all found network interfaces
%_sbindir/%{name}-update bases
%post_service %{name}d

%postun server
[ $1 = 0 ] && echo 'NOTE: %name databases still exists in %data_dir directory!'
%preun_service %{name}d


%files
%doc CHANGES FAQ README
%doc --no-dereference COPYING

%config(noreplace) %cron_file
%config(noreplace) %_sysconfdir/%name.conf

%_bindir/%name
%_sbindir/%{name}-update
%_man1dir/%{name}.*
%_man5dir/%{name}.*

%attr(1770,root,%name) %data_dir

%files server
%_sbindir/%{name}d
%_man8dir/%{name}d*
%config   %_initdir/%{name}d
%_unitdir/%{name}d.service
%_tmpfilesdir/%{name}d.conf
%_controldir/%name

%ghost %attr(1775,root,%name) %dir %piddir

%files vnstati
%doc examples/vnstat.cgi
%_bindir/%{name}i
%_man1dir/%{name}i*

%changelog
* Tue Dec 06 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.10-alt1
- New version

* Tue Feb 01 2022 Nikolay A. Fetisov <naf@altlinux.org> 2.9-alt1
- New version

* Wed Oct 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.8-alt1
- New version

* Tue Jun 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 2.7-alt1
- New version

* Wed Nov 11 2020 Nikolay A. Fetisov <naf@altlinux.org> 2.6-alt2
- Remove duplicate self-provides

* Tue Mar 31 2020 Nikolay A. Fetisov <naf@altlinux.org> 2.6-alt1
- New version

* Fri Sep 13 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.4-alt2
- Fix network interface detection in vnstat-update helper script

* Mon Aug 26 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.4-alt1
- New version

* Thu Jul 18 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.3-alt1
- New version

* Thu May 09 2019 Nikolay A. Fetisov <naf@altlinux.org> 2.2-alt1
- New version

* Sat Aug 25 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.18-alt1
- New version
- Move cron script to -server package and disable it by default (Closes: 31477)
- Add vnstat-update script for databases and configuration updates

* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 1.14-alt1
- New version 1.14

* Wed Sep 17 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.12-alt1
- New version 1.12

* Tue Jun 21 2011 Nikolay A. Fetisov <naf@altlinux.ru> 1.11-alt1
- New version 1.11

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.10-alt1
- New version 1.10
- New subpackage for vnstati utility
- Set default MaxBandwidth to 1 GiB/s (Closes: 22996)

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.9-alt1
- New version 1.9
- Fix repocop warning for /var/run/vnstatd/ directory

* Sat Sep 05 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- New version 1.8 (closes: #19950)

* Mon May 25 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.7-alt0.1
- New version 1.7

* Wed Dec 10 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.6-alt1
- New version 1.6
- Fix rights on /var/lib/vnstat/* files

* Thu Aug  4 2005 Ilya G. Evseev <evseev@altlinux.ru> 1.4-alt3
- suppress mail sending on each invocation via crontab
- execute cron job under non-privileged account;
  change previous root ownership on existing databases

* Mon Aug  1 2005 Ilya G. Evseev <evseev@altlinux.ru> 1.4-alt2
- create statistic databases automatically on install
  for all found network interfaces
- added control facility for accessing database directory
- override default cron calling time (5 minutes) by our own value
  (15 minutes, may be changed via rpmbuild --define 'cron_freq ...')
- specfile: better russian description

* Tue Jul 12 2005 Ilya G. Evseev <evseev@altlinux.ru> 1.4-alt1
- Initial build

## EOF ##
