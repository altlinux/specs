Name: ifplugd
Version: 0.28
Release: alt5

Summary: Detect and perform actions when an ethernet cable is (un)plugged
License: GPL
Group: System/Configuration/Networking

Url: http://0pointer.de/lennart/projects/ifplugd/
Source0: %url/%name-%version.tar.gz
Source1: %name.init
Patch0:	ifplugd-0.28-alt-etcnet.patch
Patch1:	ifplugd-0.28-interface.patch

Packager: Denis Ovsienko <pilot@altlinux.ru>

BuildRequires: gcc-c++ hostinfo libdaemon-devel >= 0.4 mailcap pkgconfig
Requires: libdaemon service coreutils util-linux network-config-subsystem

Summary(ru_RU.UTF-8): Конфигурирование сетевого интерфейса при наличии кабеля

%description
%name is a service which will automatically configure your ethernet device
when a cable is plugged in and automatically unconfigure it if the cable is
pulled.

This is useful on laptops with onboard network adapters, since it will only
configure the interface when a cable is really connected.

NB: not every Linux ethernet driver is capable of reporting link status.
Use ifplugstatus to find out.

%description -l ru_RU.UTF-8
%name -- сервис, отвечающий за автоматическое конфигурирование сетевого
интерфейса при подключении кабеля и деактивацию -- при отключении.

Полезен на ноутбуках с сетевыми картами, т.к. при этом интерфейс будет
активирован только при включении сетевого кабеля.

NB: не каждый драйвер Ethernet в Linux выдаёт статус линка.
Используйте ifplugstatus, чтобы выяснить это.

%prep
%setup
%patch0 -p1
%patch1 -p0
sed -i 's@/usr/local@@' man/*.[58]

%build
%configure \
	--sbindir=%_sbindir \
	--disable-lynx \
	--disable-xmltoman \
	--disable-subversion
%make

%install
sed -i 's,^ARGS="-,&q,' conf/ifplugd.conf
%makeinstall sysinitdir=%buildroot%_initdir
install -pDm755 %SOURCE1 %buildroot%_initdir/%name

%post
%post_service ifplugd

%preun
%preun_service ifplugd

%files
%doc doc/README doc/README.html
%doc doc/NEWS doc/SUPPORTED_DRIVERS doc/style.css
%_sbindir/*
%_initdir/*
%_mandir/*/*
%dir %_sysconfdir/ifplugd/
%config(noreplace) %_sysconfdir/ifplugd/ifplugd.conf
%config(noreplace) %_sysconfdir/ifplugd/ifplugd.action

# TODO:
# - import Debian's apm script (suspend/resume ifplugd)

%changelog
* Tue Jun 05 2018 Michael Shigorin <mike@altlinux.org> 0.28-alt5
- converted spec to ru_RU.UTF-8
- minor spec cleanup

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.28-alt4.qa1
- NMU: rebuilt for debuginfo.

* Mon Jan 21 2008 Michael Shigorin <mike@altlinux.org> 0.28-alt4
- added Gentoo patch to fix build with current includes
- small spec cleanups

* Mon Dec 19 2005 Denis Ovsienko <pilot@altlinux.ru> 0.28-alt3
- Requires and BuildReq cleanup should fix broken build

* Wed Aug 03 2005 Denis Ovsienko <pilot@altlinux.ru> 0.28-alt2
- new ALT patch for /etc/net 0.7.10

* Fri Jun 24 2005 Denis Ovsienko <pilot@altlinux.ru> 0.28-alt1
- new version
- fixed #7092

* Mon Jan 03 2005 Denis Ovsienko <pilot@altlinux.ru> 0.26-alt2
- eliminated false net-scripts dep again (thanks to previous enhancement)

* Mon Dec 20 2004 Denis Ovsienko <pilot@altlinux.ru> 0.26-alt1
- new version
- CONFMETHOD moves to /etc/sysconfig/network (network-config-subsystem)

* Sun Nov 14 2004 Denis Ovsienko <pilot@altlinux.ru> 0.25-alt4
- eliminated false net-scripts dependency

* Thu Nov 11 2004 Denis Ovsienko <pilot@altlinux.ru> 0.25-alt3
- /etc/net integration

* Thu Jun 10 2004 Michael Shigorin <mike@altlinux.ru> 0.25-alt2
- service turned off by default (fixes #4223)
  thanks to Denis Ovsienko (pilot@) for insisting on providing
  safe default setup where it wasn't quite so

* Tue May 11 2004 Michael Shigorin <mike@altlinux.ru> 0.25-alt1
- 0.25

* Mon Apr 12 2004 Michael Shigorin <mike@altlinux.ru> 0.24-alt1
- 0.24 (includes IFF_RUNNING support)

* Thu Apr 08 2004 Michael Shigorin <mike@altlinux.ru> 0.23-alt1
- 0.23
- fixed silly thinko relating multiple logfiles
  (manifested with >1 interfaces monitored)

* Tue Jan 27 2004 Michael Shigorin <mike@altlinux.ru> 0.21b-alt1
- 0.21b (better compact with wireless devices and newer kernels)
- versionized libdaemon dependency as it's tied down

* Mon Nov 10 2003 Michael Shigorin <mike@altlinux.ru> 0.20-alt1
- 0.20

* Sun Oct 26 2003 Michael Shigorin <mike@altlinux.ru> 0.19-alt1
- 0.19
- fixed #3198 (+initscript cleanup/update from deb's one)

* Sun Sep 14 2003 Michael Shigorin <mike@altlinux.ru> 0.17b-alt1
- 0.17b (not beta :)

* Thu Sep 11 2003 Michael Shigorin <mike@altlinux.ru> 0.16-alt1
- built for ALT Linux
- spec adapted from Cooker with large cleanups and sanitization
  (credits: Per ьyvind Karlsen <peroyvind@sintrax.net>,
            Frederic Lepied <flepied@mandrakesoft.com>)
- new and shiny initscript
