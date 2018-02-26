Name: scanssh
Version: 2.1
Release: alt3
Epoch: 1

Summary: Network scaner for SSH servers and open proxies
License: BSD-style
Group: Monitoring
Url: http://www.monkey.org/~provos/scanssh/

# http://www.monkey.org/~provos/scanssh-%version.tar.gz
Source: scanssh-%version.tar
Source1: scanssh.control
Patch1: scanssh-2.0-alt-configure.patch
Patch2: scanssh-2.0-alt-log.patch
Patch3: scanssh-2.1-alt-warnings.patch

Requires: control >= 0.6.1
BuildRequires: libdnet-devel libevent-devel libpcap-devel

Summary(ru_RU.UTF-8): Сетевой сканер SSH-серверов и открытых прокси

%description
ScanSSH supports scanning a list of addresses and networks for open
proxies, SSH protocol servers, Web and SMTP servers.  Where possible
ScanSSH, displays the version number of the running services.  ScanSSH
protocol scanner supports random selection of IP addresses from large
network ranges and is useful for gathering statistics on the deployment
of SSH protocol servers in a company or the Internet as whole.

%description -l ru_RU.UTF-8
ScanSSH сканирует сеть по заданным адресам, выводя адреса узлов
с обнаруженными работающими сервисами SSH, WWW, SMTP и Веб-прокси.
Там, где это возможно, выводится также номер версии сервиса.
Данная утилита полезна для сбора статистики об использовании сервисов
и проверки их версий в большой локальной сети.

По функциональности ScanSSH отчасти пересекается
с более известной утилитой nmap, которая выдаёт информацию
по большему количеству сервисов, но с меньшей детальностью.
Используйте ScanSSH либо для проверки фиксированной конфигурации,
либо получив предварительные результаты через nmap.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%configure
%make_build

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
%makeinstall_std
chmod 700 %buildroot%_bindir/scanssh
install -pD -m755 %_sourcedir/scanssh.control %buildroot%_controldir/scanssh

%pre
%pre_control scanssh

%post
/usr/sbin/groupadd -r -f netadmin
%post_control -s netadmin scanssh

%files
%config %_controldir/scanssh
%_bindir/*
%_mandir/man?/*
%doc README

%changelog
* Wed Jun 15 2011 Dmitry V. Levin <ldv@altlinux.org> 1:2.1-alt3
- Fixed %%post script.
- Rebuilt with libevent2.

* Fri Apr 13 2007 Dmitry V. Levin <ldv@altlinux.org> 1:2.1-alt2
- Added summary to control script.
- Fixed some compilation warnings.

* Thu Jan  5 2006 Ilya Evseev <evseev@altlinux.ru> 1:2.1-alt1
- Updated to version 2.1
- Specfile changes:
   + added russian summary/description,
   + added strict dependency to control version 0.6.1,
     needed for new_help in control helper.

* Mon Feb 28 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.0-alt2
- Rebuilt with libdnet.so.1.

* Sun Feb 13 2005 Dmitry V. Levin <ldv@altlinux.org> 1:2.0-alt1
- Updated to 2.0.
- Updated patches, description and dependencies.
- The scanssh utility is now privileged, so added control support.

* Sun Feb 01 2004 Dmitry V. Levin <ldv@altlinux.org> 1:1.6b-alt4
- Rebuilt with libpcap.so.0.8.

* Thu Oct 31 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.6b-alt3
- Rebuilt in new environment.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6b-alt2
- Rebuilt with libpcap-0.7.1.

* Wed Dec 05 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.6b-alt1
- 1.6b (added serial).

* Sun Nov 11 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.6-alt1
- 1.6

* Tue Apr 10 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.55-alt1
- 1.55

* Sat Mar 10 2001 Dmitry V. Levin <ldv@fandra.org> 1.5-ipl1
- 1.5

* Wed Feb 21 2001 Dmitry V. Levin <ldv@fandra.org> 1.4-ipl1
- 1.4

* Wed Feb 14 2001 Dmitry V. Levin <ldv@fandra.org> 1.3a-ipl1
- Initial revision.
