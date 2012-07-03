Name: watchdog
Version: 5.9
Release: alt1

Summary: A software watchdog

License: GPL
Group: System/Kernel and hardware
Url: http://www.ibiblio.org/pub/Linux/system/daemons/watchdog/
#Source: http://www.ibiblio.org/pub/Linux/system/daemons/watchdog/%name-%version.tar.bz2
Source:%name-%version.tar.gz
Source1: watchdog
PATCH0: watchdog.conf.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Mon Aug 27 2007
BuildRequires: libnss-mysql postfix

%description
Daemon automatic-reboot.

%prep
%setup -q

patch -p0 -i %PATCH0

%build
%configure
%make_build

%install
%make_install install DESTDIR=%buildroot

install -pD -m 755 %SOURCE1 %buildroot/%_initdir/%name

%files
%_sbindir/*
%config(noreplace) %_sysconfdir/%name.conf
%config %_initdir/%name
%_man5dir/*
%_man8dir/*
%doc README

%changelog
* Sat Jun 30 2012 Ilya Mashkin <oddity@altlinux.ru> 5.9-alt1
- 5.9

* Mon Aug 23 2010 Ilya Mashkin <oddity@altlinux.ru> 5.8-alt2
- try to fix #23888

* Thu Aug 12 2010 Ilya Mashkin <oddity@altlinux.ru> 5.8-alt1
- 5.8

* Fri Apr 10 2009 Ilya Mashkin <oddity@altlinux.ru> 5.6-alt1
- 5.6

* Thu Jan 08 2009 Ilya Mashkin <oddity@altlinux.ru> 5.4-alt1
- 5.4

* Mon Aug 27 2007 Lunar Child <luch@altlinux.ru> 5.3-alt4
- new version

* Fri Apr 13 2007 Lunar Child <luch@altlinux.ru> 5.2.6-alt4
- patching config file.

* Thu Jan 11 2007 Lunar Child <luch@altlinux.ru> 5.2.6-alt3
- fix init script name, fix script placement (fix bug #1024)

* Thu Nov 23 2006 Lunar Child <luch@altlinux.ru> 5.2.6-alt2
- add init script

* Tue Oct 24 2006 Lunar Child <luch@altlinux.ru> 5.2.6-alt1
- First build for ALT Linux Sisyphus

