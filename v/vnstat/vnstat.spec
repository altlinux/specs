# SPEC file for vnStat package

Name:    vnstat
Version: 1.11
Release: alt1

Summary: console-based network traffic monitor
Summary(ru_RU.UTF-8): консольная утилита для подсчёта трафика

License: %gpl2only
Group:   Monitoring
URL:     http://humdi.net/vnstat/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.control
Source2: %{name}d.init
Patch0:  %name-1.10-alt-conf.patch
Patch1:  %name-1.10-debian-fix_manpages.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgd2-devel

Requires(pre): vixie-cron
Requires(post): control
Requires(post): iproute2 sed

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
Provides: %name-server = %version-%release

%description server
vnStat  is a console-based network  traffic monitor that keeps a log
of daily network traffic for the selected interface(s).

This package contains optional standalone server for vnstat network
traffice monitor.

%package  vnstati
Summary: optional png image output support for vnstat
Group:   Monitoring
Requires: %name = %version-%release
Provides: %name-vnstati = %version-%release

%description vnstati
vnStat  is a console-based network  traffic monitor that keeps a log
of daily network traffic for the selected interface(s).

This package contains optional vnstati utility to provide PNG image
output support for statistics collected using vnstat.

%prep
%setup -q
%patch0
%patch1 -p 1

mv -f -- COPYING COPYING.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING) COPYING
chmod a-x examples/vnstat.cgi

%build
%make_build
%make -C src vnstati

%install
%make_install DESTDIR=%buildroot install
/bin/install -pD %SOURCE1  %buildroot%_controldir/%name

/bin/install -d %buildroot%_sysconfdir/cron.d/
cat << __EOF__ > %buildroot%cron_file
MAILTO=
0-59/%cron_freq * * * * %name	[ -x %_bindir/%name ] && [ \`/bin/ls %data_dir/ | /bin/wc -l\` -ge 1 ] && %_bindir/%name -u
__EOF__

install -p -D -m 0755 -- %SOURCE2 %buildroot/%_initdir/%{name}d
mkdir -p %buildroot%piddir

%pre
%_sbindir/groupadd -r -f %name &>/dev/null
%_sbindir/useradd -r -g %name -d %data_dir -s /dev/null \
	-c "vnStat database producer" -M -G proc -n %name &>/dev/null ||:

# For upgrade from 1.4-alt1 
/usr/bin/id -Gn %name | /bin/grep -qw proc || %_sbindir/usermod -G proc %name ||:


%post
echo Create %name databases for all found network interfaces...
for iface in $(/sbin/ip link show | /bin/sed -ne '/^[0-9]\+:/ s/^[^:]*: \([^:]\+\):.*$/\1/ p'); do
    %_bindir/%name -u -i "$iface"
done
/bin/chown :%name  %data_dir/*
/bin/chmod 0664    %data_dir/*
/sbin/service crond condreload

%postun
if [ $1 = 0 ]; then
    /sbin/service crond condreload
    echo 'REMEMBER: %name databases still exists in %data_dir directory!'
fi

%post server
%post_service %{name}d

%preun server
%preun_service %{name}d


%files
%doc CHANGES FAQ README
%doc --no-dereference COPYING

%config(noreplace) %cron_file
%config(noreplace) %_sysconfdir/%name.conf

%_bindir/%name
%_man1dir/%{name}.*
%_man5dir/%{name}.*

%_controldir/%name

%attr(1770,root,%name) %data_dir

%files server
%_sbindir/%{name}d
%_man1dir/%{name}d*
%config   %_initdir/%{name}d
%ghost %attr(1775,root,%name) %dir %piddir

%files vnstati
%doc examples/vnstat.cgi
%_bindir/%{name}i
%_man1dir/%{name}i*

%changelog
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
