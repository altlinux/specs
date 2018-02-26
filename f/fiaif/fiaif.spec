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

Name: fiaif
Version: 1.21.1
Release: alt1

Summary: FIAIF is an Intelligent Firewall for iptables based Linux systems
Summary(ru_RU.UTF-8): FIAIF - интеллектуальный межсетевой экран для Linux-систем с iptables

License: %gpl2plus
Group: Security/Networking
URL: http://www.fiaif.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source0: http://www.fiaif.net/dist/%{name}_%version.tar.gz
Source1: zone.venet

Patch0: %name-1.21.1-alt-reserved_networks.patch

Patch1: %name-1.19.2-alt-fiaif_update.patch
Patch2: %name-1.19.2-alt-test_location.patch
Patch3: %name-1.19.2-alt-fiaif_script_actions.patch
Patch4: %name-1.21.1-alt-CBQ-legacy_support.patch
Patch5: %name-1.21.1-alt-LSB_init.patch
Patch6: %name-1.21.1-alt-autonumbering_note.patch
Patch7: %name-1.21.1-alt-fiaif_venet_zone.patch

Patch20: %name-1.21.1-debian-02-debug_documentation.patch
Patch21: %name-1.21.1-debian-03-configuration_grammar.patch
Patch22: %name-1.21.1-debian-04-improved_error_msg.patch
Patch23: %name-1.21.1-debian-05-fiaif_scan_IN_spaces.patch
Patch24: %name-1.21.1-debian-07-disable_ext_igmp.patch
Patch25: %name-1.21.1-debian-08-use_fancyhdr.patch
Patch26: %name-1.21.1-debian-09-fiaif_update_network_errors.patch
Patch27: %name-1.21.1-debian-10-correct_voip_rule_typo.patch
Patch28: %name-1.21.1-debian-11-man_pages_title.patch
Patch29: %name-1.21.1-debian-12-allow_bash_array_length.patch
Patch30: %name-1.21.1-debian-13-modprobe_remove_modules.patch



Requires: iptables >= 1.2.6a, bash >= 2.04
BuildRequires(pre): rpm-build-licenses
BuildRequires: tetex, tetex-dvips, tetex-latex

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
Requires: %name = %version
Provides: %name-doc = %version-%release
Obsoletes: %name-doc

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
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0
%patch6 -p0

%patch20 -p0
%patch21 -p0
%patch22 -p0
%patch23 -p0
%patch24 -p0
%patch25 -p0
%patch26 -p0
%patch27 -p0
%patch28 -p0
%patch29 -p0
%patch30 -p0

# Fix path to fiaif main script
%__subst 's@/etc/init.d@/etc/rc.d/init.d@' cron/fiaif

# Install sample config for VENET zone
install -m 0644 %SOURCE1 conf/zone.venet
%__subst 's#CONF_FILES=fiaif.conf#CONF_FILES=fiaif.conf zone.venet#' Makefile

%build
DISPLAY=0:0 LANG=RU_ru.KOI8-R %__make fiaif.ps
[ -f fiaif.ps ] && gzip -9 fiaif.ps

%install
make install DESTDIR=$RPM_BUILD_ROOT
make install-config DESTDIR=$RPM_BUILD_ROOT
install -d -- $RPM_BUILD_ROOT{%_sbindir,%_mandir/man8} \
              $RPM_BUILD_ROOT%_sysconfdir/rc.d/init.d
install -- prog/fiaif $RPM_BUILD_ROOT%_initdir/fiaif

# Removing unnecessary but installed files
rm -rf -- $RPM_BUILD_ROOT%_sysconfdir/init.d/%name
rm -rf -- $RPM_BUILD_ROOT%_defaultdocdir/%name

%post
%post_service %name

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

     %attr(0700,root,root) %_sysconfdir/cron.daily/%name
     %_initdir/%name
     %_sbindir/*

%dir %_datadir/%name/
     %_datadir/%name/*

     %_mandir/man?/*

%files doc
%doc fiaif.ps.gz doc/faq.txt

%changelog
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
