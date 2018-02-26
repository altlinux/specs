Name: rp-pppoe
Version: 3.10
Release: alt4

License: %gpl2plus
Url: http://www.roaringpenguin.com/pppoe/
Summary: PPP Over Ethernet (xDSL support)
Summary(ru_RU.CP1251): PPP через Ethernet (поддержка xDSL)
Group: Networking/Other

Source: %name-%version.tar
Source1: alt-tkpppoe.desktop
Source2: tkpppoe.xpm
Source3: firewall-masq-iptables
Source4: firewall-standalone-iptables
Source6: pppoe-wrapper.control
Source7: %name-MINI-HOWTOs.tar

Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildPreReq: ppp
Provides: rp-pppoe

# Automatically added by buildreq on Wed Oct 12 2005
BuildRequires: libpcap-devel

%description
PPPoE (Point-to-Point Protocol over Ethernet) is a protocol used by
many ADSL Internet Service Providers.

%description -l ru_RU.CP1251
PPPoE (Point-to-Point Protocol через Ethernet) это протокол, используемый
многими Поставщиками Услуг Интернет по ADSL.

%package base
Summary: PPP Over Ethernet (xDSL support)
Group: Networking/Remote access

%description base
PPPoE (Point-to-Point Protocol over Ethernet) is a protocol used by
many ADSL Internet Service Providers. Roaring Penguin has a free
client for Linux systems to connect to PPPoE service providers.

This package contains basic utilites.

%package client
BuildArch: noarch
Summary: PPP Over Ethernet (xDSL support)
Summary(ru_RU.CP1251): PPP через Ethernet (поддержка xDSL)
Group: Networking/Other
Requires: ppp >= 2.3.7
Requires: openresolv
Requires: %name-base = %version-%release
Provides: rp-pppoe
Obsoletes: rp-pppoe

%description client
PPPoE (Point-to-Point Protocol over Ethernet) is a protocol used by
many ADSL Internet Service Providers. Roaring Penguin has a free
client for Linux systems to connect to PPPoE service providers.

The client is a user-mode program and does not require any kernel
modifications. It is fully compliant with RFC 2516, the official PPPoE
specification.

%description client -l ru_RU.CP1251
PPPoE (Point-to-Point Protocol через Ethernet) это протокол, используемый
многими Поставщиками Услуг Интернет по ADSL. Roaring Penguin
предоставляет свободного клиента для Linux-систем для установки соединения
с поставщиками услуг PPPoE.

%package server
Summary: PPP Over Ethernet (xDSL support)
Summary(ru_RU.CP1251): PPP через Ethernet (поддержка xDSL)
Group: Networking/Other
Requires: ppp >= 2.3.7
Conflicts: %name-base < %version-%release
Conflicts: %name-base > %version-%release

%description server
pppoe-server is a user-space server for PPPoE (Point-to-Point Protocol over Ethernet)
for Linux and other UNIX systems.

%description server -l ru_RU.CP1251
pppoe-server это PPPoE-сервер (Point-to-Point Protocol over Ethernet) для Linux и других UNIX-систем.

%package gui
Summary: Tk interface for PPP Over Ethernet Client (xDSL support)
Summary(ru_RU.CP1251): Tk интерфейс к Клиенту PPP через Ethernet (поддержка xDSL)
Group: Networking/Other
Requires: %name-client = %version-%release tk

%description gui
This is a graphical wrapper around the rp-pppoe PPPoE client. PPPoE is
a protocol used by many DSL Internet Service Providers.

%description gui -l ru_RU.CP1251
Графическая оболочка для клиента PPPoE. PPPoE это протокол, используемый многими
Поставщиками Услуг Интернет по ADSL.

%prep
%setup -q -a7
%patch0 -p1

%build
pushd src
%autoreconf
%configure
popd
%make_build -C src
%make_build -C gui

%install
%makeinstall_std -C src
%makeinstall_std -C gui

install -p -m664 -D %SOURCE1 %buildroot%_desktopdir/%name-gui.desktop
install -p -m644 -D %SOURCE2 %buildroot%_niconsdir/tkpppoe.xpm
install -p -m644 %SOURCE3 %buildroot%_sysconfdir/ppp/
install -p -m644 %SOURCE4 %buildroot%_sysconfdir/ppp/
install -p -m755 -D %SOURCE6 %buildroot%_sysconfdir/control.d/facilities/pppoe-wrapper

cat > %buildroot%_sysconfdir/ppp/pppoe-lost << EOF
#!/bin/sh
echo -n \`date +"%%b %%d %%T"\`" " >> /var/log/ppp/pppoe-lost.log
echo "PPPoE session reconnect"  >> /var/log/ppp/pppoe-lost.log
EOF

%files base
%_sbindir/pppoe
%_sbindir/pppoe-sniff
%_sbindir/pppoe-relay
%_man8dir/pppoe.*
%_man8dir/pppoe-relay.*
%_man8dir/pppoe-sniff.*

%files client
%attr(750,root,root) %_sysconfdir/ppp/pppoe-lost
%config(noreplace) %_sysconfdir/ppp/pppoe.conf
%config(noreplace) %_sysconfdir/ppp/firewall*
%config(noreplace) %_initdir/pppoe
%_sbindir/pppoe-connect
%_sbindir/pppoe-start
%_sbindir/pppoe-stop
%_sbindir/pppoe-setup
%_sbindir/pppoe-status
%_man5dir/*
%_man8dir/pppoe-connect.*
%_man8dir/pppoe-setup.*
%_man8dir/pppoe-start.*
%_man8dir/pppoe-stop.*
%_man8dir/pppoe-status.*
%doc doc/CHANGES doc/HOW-TO-CONNECT README USB-ADSL-MINI-HOWTO.sgml

%preun client
/sbin/chkconfig --del pppoe

%files server
%config(noreplace) %_sysconfdir/ppp/pppoe-server-options
%_sbindir/pppoe-server
%_man8dir/pppoe-server.8*
%doc SERVPOET PPPoE-SERVER-MINI-HOWTO.sgml

%files gui
%config %_sysconfdir/control.d/facilities/pppoe-wrapper
%dir %_sysconfdir/ppp/rp-pppoe-gui
%dir %_datadir/tkpppoe
%_bindir/tkpppoe
%attr(4711,root,root) %_sbindir/pppoe-wrapper
%_desktopdir/%name-gui.desktop
%_niconsdir/tkpppoe.xpm
%_datadir/tkpppoe/*.msg
%dir %_docdir/tkpppoe
%_docdir/tkpppoe/*.png
%_docdir/tkpppoe/tkpppoe.html
%_man1dir/*

%pre gui
%pre_control pppoe-wrapper

%post gui
%post_control pppoe-wrapper

%changelog
* Tue Jun 21 2011 Mikhail Efremov <sem@altlinux.org> 3.10-alt4
- Check HELP_BROWSER variable and don't run browser as root.

* Tue Mar 29 2011 Mikhail Efremov <sem@altlinux.org> 3.10-alt3
- Desktop file: don't use extension for icon name (thx repocop).

* Mon Mar 28 2011 Mikhail Efremov <sem@altlinux.org> 3.10-alt2
- gui: Fix manual page showing (by Boris Revyakin).
- pppoe-stop: Give pppd time for clean exit (closes: #17762).
- Fix Group.
- Fix License.
- gui: Replace Debian menu entry with desktop file
    (thanks Igor Vlasenko).
- init script: fix exit status (closes: #9504).
- own /usr/share/doc/tkpppoe.

* Thu Aug 13 2009 Mikhail Efremov <sem@altlinux.org> 3.10-alt1
- set 'BuildArch: noarch' for client subpackage.
- client subpackage: added resolvconf support.
- use fno-strict-aliasing compiler option.
- configure.in: fixed AC_DEFINE macroses.
- spec updated and cleanup.
- new version 3.10.
- applied repocop patch.

* Sun Dec 25 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.7-alt2
- Corrected trouble with resolver working in the chrooted environment.
- Updated patches.

* Sat Dec 03 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.7-alt1
- 3.7

* Wed Oct 12 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.6-alt2
- package rp-pppoe-client splitted into two subpackage: "base" and "client"

* Sun Oct 09 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.6-alt1
- 3.6
- Changed startup scripts names

* Sun May 29 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt16
- Updated patch3

* Thu Apr 14 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt15
- Updated patch3

* Wed Dec 22 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt14
- Added %%post script.

* Mon Dec 20 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt13
- Removed resolv.conf linking.

* Tue May 25 2004 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt12
- Added BuildRequires and BuildPreReq

* Sun May 23 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt11
- Added %%post script which solves cyclic reference on resolv.conf
- Removed enforced assignment of the network address for eth?
- updated spec

* Wed Oct 08 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt10
- Added /etc/ppp/adsl-lost script

* Tue Sep 30 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt9
- Added patch permitting operation with the resolver working in chrooted environment

* Fri Sep 12 2003 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt8
- Updated BuildRequires
- Added rp-pppoe-3.5-ALT-tkppoe.patch which corrects find-requires problem

* Tue Mar 11 2003 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt7
- Changed startup priority
- Removed obsoleted SOURCE5

* Sat Nov 30 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt6
- Added MINI-HOWTO's
- Disabled kernel mode plugin
- Removed obsoleted pppd headers

* Thu Nov 14 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt5
- Fixed %%install errors
- Added genericname for menu

* Tue Oct 22 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 3.5-alt4
- updated spec with new macros
- added control support for pppoe-wrapper

* Tue Oct 01 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt3
- updated rp-pppoe-3.5-alt-adsl-connect.patch
- removed unused source files from ppp-source
- upgraded included ppp-source to ppp-headers-cvs-20020929
- removed unused Source6 - modules.conf
- updated package requires
- updated groups

* Sat Jul 13 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt2
- builded with kermel-mode plugins support

* Fri Jul 12 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.5-alt1
- 3.5
- removed package description in obsoleted KOI8-R encoding
- %name-server package added
- %name package renamed into %name-client

* Sat May 25 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.4-alt2
- bugfix release

* Mon May 20 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.4-alt1
- 3.4
- Added firewalling rules for iptables

* Mon Feb 11 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.3-alt5
- updated spec (changed Group)

* Fri Jan 25 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.3-alt4
- updated patch
- removed %post
- added Summary & description in KOI8-R encoding

* Sun Jan 13 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.3-alt3
- added SOURCE2

* Wed Jan  9 2002 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.3-alt2
- added Summary & description in CP1251 encoding

* Wed Nov 14 2001 Aleksandr Blokhin (Sass) <sass@altlinux.ru> 3.3-alt1
- new version
- updated spec
- added patch & source1
- ALT adaptation

* Thu Jul 21 2001 Shigechika AIKAWA <shige@cin.nihon-u.ac.jp>
- merged rp-pppeo.spec and rp-pppoe-gui.spec

* Sat Feb 3 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Oct  5 2000 dam's <damien@mandrakesoft.com> 1.7-3mdk
- added patch0. the bogus connection is cleanly removed.

* Tue Sep  5 2000 Etienne Faure  <etienne@mandraksoft.com> 1.7-2mdk
- rebuilt with _mandir and %%doc macros
- run chkconfig

*Fri Apr  7 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.7-1mdk
- changed group
- new version

*Tue Mar  1 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.6-1mdk
- updated to 1.6
- merged my patches with the author so it's in the distribution

*Sun Feb 20 2000 Jean-Michel Dault <jmdault@mandrakesoft.com> 1.3-1mdk
- First Mandrake release
- require pppoe-linuxconf
