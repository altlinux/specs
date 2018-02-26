Name: scanlogd
Version: 2.2.6
Release: alt2

Summary: A tool to detect and log TCP port scans
License: GPL
Group: System/Servers
Url: http://www.openwall.com/scanlogd/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# ftp://ftp.openwall.com/pub/projects/scanlogd/scanlogd-%version.tar.gz
Source: scanlogd-%version.tar
Source1: scanlogd.init

Requires(post): shadow-utils, %post_service
Requires(preun): %preun_service

Summary(ru_RU.KOI8-R): Утилита для обнаружения сканирования TCP-портов

%description
scanlogd detects port scans and writes one line per scan via the
syslog(3) mechanism.  If a source address sends multiple packets to
different ports in a short time, the event will be logged.

%description -l ru_RU.KOI8-R
scanlogd является постоянно работающим сервисом, следящим за сетевыми
портами TCP/IP.  Каждый раз, когда он обнаруживает сканирование портов с
какого-либо внешнего узла, он делает об этом запись в системном журнале
(см. man 3 syslog).  Сканированием считается приход с одного IP-адреса
большого количества сетевых пакетов на большое количество портов в
короткое время.

%prep
%setup -q

%build
make clean
make linux CFLAGS="-c %optflags %optflags_notraceback"

%install
mkdir -p %buildroot{%_sbindir,%_mandir/man8,%_initdir}
install -pm755 scanlogd %buildroot%_sbindir/
install -pm644 scanlogd.8 %buildroot%_man8dir/
install -pm755 %_sourcedir/scanlogd.init %buildroot%_initdir/%name

%post
/usr/sbin/groupadd -r -f %name
/usr/sbin/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:
%post_service %name

%preun
%preun_service %name

%files
%config %_initdir/*
%_sbindir/*
%_mandir/man?/*

%changelog
* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt2
- Minor startup script and specfile tweaks.

* Sun Jun 04 2006 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt1
- Updated to 2.2.6.

* Tue Jan 11 2005 Dmitry V. Levin <ldv@altlinux.org> 2.2.5-alt2
- Fixed URLs back.
- Updated package dependencies.

* Sun Jan  9 2005 Ilya Evseev <evseev@altlinux.ru> 2.2.5-alt1
- Updated to 2.2.5.
- Specfile: added russian summary/description, fixed URLs

* Thu Jun 03 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.4-alt1
- Updated to 2.2.4.

* Wed May 26 2004 Dmitry V. Levin <ldv@altlinux.org> 2.2.2-alt1
- Updated to 2.2.2.

* Tue Apr 29 2003 Dmitry V. Levin <ldv@altlinux.org> 2.2.1-alt1
- Updated to 2.2.1.
- Daemonize properly.
- Rewritten start/stop script to new rc scheme.

* Fri Sep 20 2002 Stanislav Ievlev <inger@altlinux.ru> 2.2-ipl4
- rebuild with gcc3
- update URL

* Thu May 24 2001 Stanislav Ievlev <inger@altlinux.ru> 2.2-ipl3
- Rebuild for use new macros post_service and preun_service

* Thu Feb 08 2001 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl2
- Fixed group tag.

* Fri Nov 10 2000 Dmitry V. Levin <ldv@fandra.org> 2.2-ipl1
- 2.2
- FHSification.

* Fri May 05 2000 Dmitry V. Levin <ldv@fandra.org>
- 2.1

* Thu Mar 16 2000 Dmitry V. Levin <ldv@fandra.org>
- initial revision
