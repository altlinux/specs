# FIAIF is an Intelligent firewall
#
# RPM specification file.
#
# Author:	Anders Fugmann <afu@fugmann.dhs.org>
#
# FIAIF is an Intelligent firewall
# Copyright (C) 2002-2003 Anders Peter Fugmann
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

%def_with  systemd

Name: fiaif
Version: 1.22.1
Release: alt3

Summary: FIAIF is an Intelligent Firewall for iptables based Linux systems
Summary(ru_RU.UTF-8): FIAIF - интеллектуальный межсетевой экран для Linux-систем с iptables

License: %gpl2plus
Group: Security/Networking
URL: http://www.fiaif.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: %{name}_%version.tar
Source1: zone.venet
Source2: reserved_networks
%if_with systemd
Source3: fiaif.service
%endif

Patch1: %name-1.19.2-alt-fiaif_update.patch
Patch2: %name-1.19.2-alt-test_location.patch
Patch3: %name-1.19.2-alt-fiaif_script_actions.patch
Patch4: %name-1.21.1-alt-CBQ-legacy_support.patch
Patch5: %name-1.21.1-alt-LSB_init.patch
Patch6: %name-1.21.1-alt-autonumbering_note.patch
Patch7: %name-1.21.1-alt-fiaif_venet_zone.patch
Patch8: %name-1.22.1-log_level.patch
Patch9: %name-1.22.1-btime.patch
Patch10: %name-1.22.1-cleanup_rules.patch
Patch11: %name-1.22.1-vlan_devices.patch

Requires: iptables >= 1.2.6a, bash >= 2.04
BuildRequires(pre): rpm-build-licenses
# Automatically added by buildreq on Tue Mar 06 2018
# optimized out: fontconfig python-base python-modules python3 python3-base python3-module-zope ruby ruby-stdlibs tex-common texlive texlive-collection-basic texlive-dist
BuildRequires: texlive-dist


%description
FIAIF is  an  Intellegent  Firewall. The Goal of  FIAIF  is to
provide  a  highly  customizable  script  for  setting  up  an
iptables based firewall.

Unlike  many  other scripts,  FIAIF  can  be truly  customized
allowing multiple  interfaces (or  rather zones). There  is no
limit  on  the number  of  zones.  All configuration  is  done
through configuration files. No  need to understand the script
behind it all.

The script makes heavy use  of state-full firewalling, and all
RELATED and ESTABLISHED packets are accepted on all chains. If
you which  to block  something out,  do not  accept it  in the
first place.

The script is written in BASH.  Though this is not the optimal
program to use, it means that you do not need to install extra
interpreters  on your  firewall.  This allows  you  to have  a
minimalistic installation on your firewall.

Install this package if your machine is ever on the internet.

%description -l ru_RU.UTF-8
FIAIF - скрипт с широкими возможностями настройки для создания
межсетевых экранов на базе iptables.

По сравнению с  многими  другими скриптами,  FIAIF может  быть
сконфигурирован для  поддержки нескольких  сетевых интерфейсов
(или  иначе зон).  В  нём нет  ограничений  на число зон.  Вся
настройка  происходит  через   файлы  конфигурации,  при  этом
изучать приципы работы самого скрипта нет необходимости.

FIAIF  широко использует  возможности iptables по отслеживанию
состояний  установленных  соединений,  RELATED  и  ESTABLISHED
пакеты принимаются  во всех цепочках.  Если Вы хотите что-либо
блокировать какие-либо соединения, просто не принимайте их.

FIAIF написан на BASH.  Хотя bash - не самый  оптимальный язык
для  написания  больших скриптов,  зато  для  работы FIAIF  не
требуется  устанавливать  лишние интерпретаторы  на межсетевом
экране.

%package doc
Summary: FIAIF documentation
Summary(ru_RU.UTF-8): документация к FIAIF
Group: Books/Other

%description doc
FIAIF is  an  Intellegent  Firewall. The Goal of  FIAIF  is to
provide  a  highly  customizable  script  for  setting  up  an
iptables based firewall.

This package contains FIAIF documentation: user guide and FAQ.

%description doc  -l ru_RU.UTF-8
FIAIF - скрипт с широкими возможностями настройки для создания
межсетевых экранов на базе iptables.

Данный пакет содержит документацию к FIAIF - руководство
пользователя и FAQ.

%define fiaif_conf  %_sysconfdir/fiaif

%prep
%setup
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0
%patch7 -p0
%patch8 -p0
%patch9 -p0
%patch10 -p0
%patch11 -p0

# Fix path to fiaif main script
subst 's@/etc/init.d@/etc/rc.d/init.d@' cron/fiaif

# Install sample config for VENET zone
install -m 0644 %SOURCE1 conf/zone.venet
subst 's#CONF_FILES=fiaif.conf#CONF_FILES=fiaif.conf zone.venet#' Makefile

# Install fresh reserved_networks
install -m 0644 %SOURCE2 conf/reserved_networks

%build
DISPLAY=0:0 LANG=RU_ru.UTF-8   make fiaif.ps
[ -f fiaif.ps ] && gzip -9 fiaif.ps

%install
make install DESTDIR=$RPM_BUILD_ROOT
make install-config DESTDIR=$RPM_BUILD_ROOT
install -d -- $RPM_BUILD_ROOT{%_sbindir,%_mandir/man8,%_initdir}
install -- prog/fiaif $RPM_BUILD_ROOT%_initdir/fiaif
# Creating link /usr/sbin/fiaif -> %_initdir/fiaif
ln -s %_initdir/%name $RPM_BUILD_ROOT%_sbindir/%name

# Removing unnecessary but installed files
rm -rf -- $RPM_BUILD_ROOT%_sysconfdir/init.d/%name
rm -rf -- $RPM_BUILD_ROOT%_defaultdocdir/%name

%if_with systemd
# Installing systemd unit file
mkdir -p  %buildroot%_unitdir
install -m 0755 %SOURCE3 %buildroot%_unitdir/%name.service
%endif

%post
%post_service %name

# Fix fiaif.conf - replace log level from CRIT to crit, and etc.
# The support of upper-case log levels names had been dropped in iptables >= 1.4.15
# Older iptables versions can handle both upper and lower case names,
# newly ones - only lower case.
sed -e 's/LOG_LEVEL=ALERT/LOG_LEVEL=alert/'     -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=CRIT/LOG_LEVEL=crit/'       -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=DEBUG/LOG_LEVEL=debug/'     -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=EMERG/LOG_LEVEL=emerg/'     -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=ERROR/LOG_LEVEL=error/'     -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=INFO/LOG_LEVEL=info/'       -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=NOTICE/LOG_LEVEL=notice/'   -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=PANIC/LOG_LEVEL=panic/'     -i %fiaif_conf/fiaif.conf
sed -e 's/LOG_LEVEL=WARNING/LOG_LEVEL=warning/' -i %fiaif_conf/fiaif.conf

%preun
%preun_service %name

%files
%doc VERSION changelog
%doc doc/reporting_bugs.txt doc/upgrade.txt doc/DHCP.txt

%dir %attr(0700,root,root) %fiaif_conf/
%dir %attr(0700,root,root) %_var/lib/%name/

%config(noreplace) %fiaif_conf/aliases
%config(noreplace) %fiaif_conf/zone.*
%config(noreplace) %fiaif_conf/fiaif.conf
%config(noreplace) %fiaif_conf/reserved_networks
%config(noreplace) %fiaif_conf/private_networks
%config(noreplace) %fiaif_conf/type_of_services

%if_with systemd
%_unitdir/%name.service
%endif

%attr(0700,root,root) %_sysconfdir/cron.daily/%name
%_initdir/%name
%_sbindir/*

%dir %_datadir/%name/
%_datadir/%name/*

%_mandir/man?/*

%files doc
%doc fiaif.ps.gz doc/faq.txt

%changelog
* Wed Mar 14 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.22.1-alt3
- Fix BuildRequires for new texlive

* Tue Mar 06 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.22.1-alt2
- Updating BuildRequires due to the new texlive

* Sun Aug 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.22.1-alt1
- New version 1.22.1
- Fix code to work with iptables >= 1.4.15
- Fix code to work with OpenVZ kernel >= 2.6.32-ovz-el-alt70
- Add systemd unit file
- Add support for VLAN interfaces

* Fri Aug 01 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.21.1-alt1
- New version 1.21.1
- Add auto-numbering feature for rule's lists
- Include sample config file for VENET zone
- Apply numerous patches from Debian
- Add LSB header into init script

* Wed Feb 01 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.20.1-alt1
- New version 1.20.1
  * Remove CBQ traffic shaping.
  * Always classify ftp data as bulk traffic
  * Several improvements in traffic shaping algorithms
- Spec file cleanup  
- Adding legacy support for TC_TYPE parameter

* Sun Nov 20 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.19.2-alt3
- Update reserved_networks list in package to the current IANA state.
- Adding patch to HTB shaping code from FIAIF mail list

* Wed Apr 27 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.19.2-alt2
- Spec cleanup
- Add patch for fiaif to support condrestart,condstop and reload actions.
- Update reserved_networks list in package to the current IANA state.

* Fri Feb 04 2005 Nikolay A. Fetisov <naf@altlinux.ru> 1.19.2-alt1
- fix spec-file for meet Sisyphus requirements
- move documantation to the separate package
- initial build for ALT Linux

* Sat Aug 14 2004 Nikolay Fetisov <naf@ssc.ru>
- verify docs section
* Sun Mar 14 2004 Nikolay Fetisov <naf@ssc.ru>
- new version 1.19.2
* Sun Jan 11 2004 Nikolay Fetisov <naf@ssc.ru>
- corrects russian description
* Thu Jan 08 2004 Nikolay Fetisov <naf@ssc.ru>
- new upstream version 1.18
* Wed Apr 09 2003 Anders Fugmann <afu@fugmann.dhs.org>
- new upstream version 1.13.3
* Wed Apr 09 2003 Anders Fugmann <afu@fugmann.dhs.org>
- new upstream version 1.13.2
* Tue Apr 08 2003 Anders Fugmann <afu@fugmann.dhs.org>
- new upstream version 1.13.1
* Mon Apr 07 2003 Anders Fugmann <afu@fugmann.dhs.org>
- new upstream version 1.13.0
* Sun Apr 06 2003 Anders Fugmann <afu@fugmann.dhs.org>
- new upstream version 1.12.2
* Sun Mar 16 2003 Nikolay Fetisov <naf@ssc.ru>
- First build for Sisyphus
* Sun Mar 16 2003 Anders Fugmann <anders@fugmann.dhs.org>
- add aliases.sh
* Sat Mar 08 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.12.1
* Sat Mar 01 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.12.0
* Fri Feb 28 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.11.0
* Sat Feb 22 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.10.0
* Sat Feb 22 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.9.2
* Thu Feb 20 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.9.1
* Mon Feb 17 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.9.0
* Thu Feb 13 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.8.2
* Thu Feb 13 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.8.1
* Tue Feb 11 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.8.0
* Tue Feb 11 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.7.4
* Wed Jan 29 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.7.3
* Wed Jan 29 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.7.2
* Wed Jan 29 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.7.1
- Do not require dia when building
* Wed Jan 29 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.7.0
* Fri Jan 24 2003 Anders Fugmann <anders@fugmann.dhs.org>
- new upstream version 1.6.4
* Thu Jan 23 2003 Anders Fugmann <anders@fugmann.dhs.org>
- New build scripts
* Sat Jan 4 2003 Anders Fugmann <anders@fugmann.dhs.org>
- Dont use _preun_service. It breaks things on RH 8.0
* Mon Dec 30 2002 Anders Fugmann <anders@fugmann.dhs.org>
- Work better with mandrake (Thanks to RИmi Denis-Courmont)
* Thu Oct 24 2002 Anders Fugmann <anders@fugmann.dhs.org>
- Updated spec file based on changes from Sergiusz Pawlowicz.
* Sun Sep 08 2002 Anders Fugmann <anders@fugmann.dhs.org>
- Remove /var/state/fiaif/iptables en upgrading.
* Wed Jun 05 2002 Anders Fugmann <anders@fugmann.dhs.org>
- RPM done.
- See /usr/share/doc/fiaif/changelog for more information
