Name: dnsmasq
Version: 2.62

%define with_resolvconf with_resolvconf

Release: alt1
Summary: A lightweight caching nameserver
License: %gpl2plus
Group: System/Servers
Url: http://www.thekelleys.org.uk/dnsmasq
Source0: %name-%version.tar
Source1: %name.init.m4
Source2: %name.sysconfig.m4
Patch0: %name-%version-%release.patch
%ifdef %with_resolvconf
Patch1: %name.conf.resolvconf.patch
Requires: openresolv-dnsmasq
%endif
BuildPreReq: m4
BuildPreReq: glibc-kernheaders
BuildRequires(pre): rpm-build-licenses

%define init_script rpm/%name-alt.init
%define sysconfig_file %_sysconfdir/sysconfig/%name
%define sysconfig_file_tmp %name-sysconfig

Summary(ru_RU.KOI8-R): Компактный сервер DNS и DHCP для локальных сетей

%description
Dnsmasq is lightweight, easy to configure DNS forwarder and DHCP server. It
is designed to provide DNS and, optionally, DHCP, to a small network. It can
serve the names of local machines which are not in the global DNS. The DHCP
server integrates with the DNS server and allows machines with DHCP-allocated
addresses to appear in the DNS with names configured either in each host or
in a central configuration file. Dnsmasq supports static and dynamic DHCP
leases and BOOTP for network booting of diskless machines.

%description -l ru_RU.KOI8-R
Dnsmasq - это компактный, простой в настройке сервер DNS и DHCP,
разработанный для использования в небольших сетях.
По умолчанию он использует общесистемные файлы /etc/hosts и /etc/resolv.conf,
поэтому может использоваться без настройки сразу после установки.

Очень удобными функциями являются прозрачное переопределение внешних имён
через /etc/hosts и трансляция имени в наиболее подходящий клиенту IP-адрес,
если для имени определено несколько адресов из разных подсетей.

Dnsmasq не поддерживает пересылку DNS-зон и поэтому не может использоваться
в качестве авторитативного. Для этой цели вам понадобится PowerDNS или BIND.

%prep
%setup -q
%patch0 -p1
%ifdef %with_resolvconf
%patch1 -p2
%endif

# Setup version
sed -r -i "s;-DVERSION=.+;-DVERSION='\\\\\"%version\\\\\"';" Makefile

%build
%make_build

%install
mkdir -p rpm
%ifdef %with_resolvconf
m4 -D%with_resolvconf %SOURCE1 > %init_script
m4 -D%with_resolvconf %SOURCE2 > %sysconfig_file_tmp
%else
m4 %SOURCE1 > %init_script
m4 %SOURCE2 > %sysconfig_file_tmp
%endif
install -pD -m700 src/dnsmasq         %buildroot%_sbindir/%name
install -pD -m744 %init_script        %buildroot%_initdir/%name
install -pD -m600 %sysconfig_file_tmp %buildroot%sysconfig_file
install -pD -m600 %name.conf.example  %buildroot%_sysconfdir/%name.conf
install -pD -m444 man/%name.8         %buildroot%_man8dir/%name.8

%pre
# Upgrade configuration from previous versions
if test -e %sysconfig_file; then
if egrep -q '^[^#]*ALL *=' %sysconfig_file; then
    if ! egrep -q '^[^#]*ALL_DEV *=' %sysconfig_file; then
	echo 'NOTE: You should put ALL_DEV=<interface> to %sysconfig_file'
	echo '      for keeping DHCP broadcasts mode.'
    fi
fi
fi

%post
%post_service %name

%preun
%preun_service %name
%ifndef %with_resolvconf
rm -f %_sysconfdir/*.dnsmasq 2>&1   # fixme! should be more elegant..
%endif

%files
%doc CHANGELOG FAQ doc.html setup.html CHANGELOG.archive
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/%name
%_sbindir/%name
%_man8dir/%{name}*
%doc contrib/dnslist contrib/dynamic-dnsmasq

%changelog
* Thu Jun 07 2012 Mikhail Efremov <sem@altlinux.org> 2.62-alt1
- Updated to new version 2.62.

* Tue May 01 2012 Mikhail Efremov <sem@altlinux.org> 2.61-alt1
- updated to new version 2.61.

* Sun Mar 11 2012 Mikhail Efremov <sem@altlinux.org> 2.60-alt1
- updated to new version 2.60.

* Tue Nov 01 2011 Mikhail Efremov <sem@altlinux.org> 2.59-alt1
- updated to new version 2.59.

* Sat Feb 26 2011 Mikhail Efremov <sem@altlinux.org> 2.57-alt1
- Minor spec cleanup.
- updated to new version 2.57 (closes: #25157).

* Thu Feb 17 2011 Mikhail Efremov <sem@altlinux.org> 2.56-alt1
- init script: Drop ALT Linux version less then M24 support.
- updated to new version 2.56

* Mon Sep 06 2010 Mikhail Efremov <sem@altlinux.org> 2.55-alt2
- init script: fix failure handling during start.

* Tue Jun 08 2010 Mikhail Efremov <sem@altlinux.org> 2.55-alt1
- updated to new version 2.55

* Mon Jun 07 2010 Mikhail Efremov <sem@altlinux.org> 2.53-alt1
- drop -fno-strict-aliasing compiler option.
- updated to new version 2.53

* Mon Mar 01 2010 Mikhail Efremov <sem@altlinux.org> 2.52-alt1
- updated to new version 2.52

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 2.51-alt1
- updated to new version 2.51

* Wed Dec 09 2009 Mikhail Efremov <sem@altlinux.org> 2.46-alt1.3
- require openresolv-dnsmasq.

* Mon Nov 09 2009 Mikhail Efremov <sem@altlinux.org> 2.46-alt1.2
- slightly spec cleanup.
- Don't remove files for resolvconf if dnsmasq under NM is present.

* Mon Jun 22 2009 Mikhail Efremov <sem@altlinux.org> 2.46-alt1.1
- NMU:
- fno-strict-aliasing compiler option is added.
- fixed pointer cast.
- do not start dnsmasq by default.
- init script: condreload is added.
- resolvconf support (closes: #17398, #19369).

* Mon Jan 12 2009 Ilya Evseev <evseev@altlinux.ru> 2.46-alt1
- updated to new version 2.46

* Sun Sep 28 2008 Ilya Evseev <evseev@altlinux.ru> 2.45-alt2
- added packager field, upgrade kernel-headers dependency

* Sat Sep 27 2008 Ilya Evseev <evseev@altlinux.ru> 2.45-alt2
- updated to new version 2.45

* Tue Apr 29 2008 Ilya Evseev <evseev@altlinux.ru> 2.41-alt3
- enable ISC DHCPD reader, needed for libvirt/qemu

* Wed Apr  9 2008 Ilya Evseev <evseev@altlinux.ru> 2.41-alt2
- bugfix #15277

* Fri Feb 15 2008 Ilya Evseev <evseev@altlinux.ru> 2.41-alt1
- updated to new version 2.41

* Sun Sep  2 2007 Ilya Evseev <evseev@altlinux.ru> 2.40-alt1
- updated to new version 2.40

* Tue May  1 2007 Ilya Evseev <evseev@altlinux.ru> 2.39-alt1
- updated to new version 2.39

* Sat Feb 24 2007 Ilya Evseev <evseev@altlinux.ru> 2.38-alt1
- updated to new version 2.38
- specfile: better russian description

* Wed Feb  7 2007 Ilya Evseev <evseev@altlinux.ru> 2.37-alt1
- updated to new version 2.37
- cleanup specfile from obsoleted ALM22-related stuff

* Mon Jan 22 2007 Ilya Evseev <evseev@altlinux.ru> 2.36-alt1%release_tag
- updated to new version 2.36

* Thu Jan  4 2007 Ilya Evseev <evseev@altlinux.ru> 2.35-alt2%release_tag
- adopt build for modern Sisyphus without kernel-std-up

* Sun Oct 29 2006 Ilya Evseev <evseev@altlinux.ru> 2.35-alt1%release_tag
- updated to new version 2.35

* Tue Oct 17 2006 Ilya Evseev <evseev@altlinux.ru> 2.34-alt1%release_tag
- updated to new version 2.34

* Tue Aug  8 2006 Ilya Evseev <evseev@altlinux.ru> 2.33-alt1%release_tag
- updated to new version 2.33

* Tue Jul 25 2006 Ilya Evseev <evseev@altlinux.ru> 2.32-alt1%release_tag
- updated to new version 2.32

* Fri May 12 2006 Ilya Evseev <evseev@altlinux.ru> 2.31-alt1%release_tag
- updated to new version 2.31

* Thu Apr 20 2006 Ilya Evseev <evseev@altlinux.ru> 2.28-alt2%release_tag
- specfile bugfixes: added dependency from kernel headers

* Tue Apr 18 2006 Ilya Evseev <evseev@altlinux.ru> 2.28-alt1%release_tag
- updated to new version 2.28

* Fri Mar 17 2006 Ilya Evseev <evseev@altlinux.ru> 2.27-alt1%release_tag
- updated to new version 2.27

* Sun Jan 22 2006 Ilya Evseev <evseev@altlinux.ru> 2.26-alt1%release_tag
- updated to new version 2.26

* Sun Jan 15 2006 Ilya Evseev <evseev@altlinux.ru> 2.25-alt1%release_tag
- updated to new version 2.25

* Tue Nov 29 2005 Ilya Evseev <evseev@altlinux.ru> 2.24-alt1%release_tag
- update to new version 2.24
- new option 'localise-query' is now enabled by default
- some stuff from contrib/ is added to docs/.

* Tue Aug 30 2005 Ilya Evseev <evseev@altlinux.ru> 2.23-alt1%release_tag
- update to new version 2.23

* Mon Jul 11 2005 Ilya Evseev <evseev@altlinux.ru> 2.22-alt2%release_tag
- bugfix #7223: use '/sbin/ip route' instead 'sbin/route' in service script
- service script bugfix: m4 previously intercepts 'shift' as keyword

* Sun Apr  3 2005 Ilya Evseev <evseev@altlinux.ru> 2.22-alt1%release_tag
- Updated to version 2.22, patch #1 is no more needed

* Fri Mar 25 2005 Ilya Evseev <evseev@altlinux.ru> 2.21-alt1%release_tag
- Updated to version 2.21
- Added includes patch (P1)

* Tue Jan 25 2005 Ilya Evseev <evseev@altlinux.ru> 2.20-alt1%release_tag
- 2.20
- URL is changed back from mantainer site to author site

* Sat Dec 18 2004 Ilya Evseev <evseev@altlinux.ru> 2.19-alt1%release_tag
- version 2.19
- IMPORTANT bugfixes in service script

* Thu Nov 25 2004 Ilya Evseev <evseev@altlinux.ru> 2.18-alt1%release_tag
- version 2.18

* Wed Oct 27 2004 Ilya Evseev <evseev@altlinux.ru> 2.16-alt1%release_tag
- version 2.16

* Wed Sep 22 2004 Ilya Evseev <evseev@altlinux.ru> 2.15-alt1%release_tag
- version 2.15

* Sun Sep 12 2004 Ilya Evseev <evseev@altlinux.ru> 2.14-alt1%release_tag
- version 2.14

* Tue Sep  7 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt4%release_tag
- service script bugfixes:
   + domain name detection: added 'hostname --domain'
   + options are previously not passed to daemon
- sysconfig: added listening on 127.0.0.1 only for better security
- dnsmasq.conf: domain-needed and expand-hosts are enabled by default

* Sat Aug 28 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt3%release_tag
- more once attempt to fit hasher restrictions:
   + detection rule is changed again
   + removed 'BuildPreReq: initscripts'

* Fri Aug 27 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt2%release_tag
- added 'BuildPreReq: initscripts' for correct platform detection
  in build environment like hasher/sisyphus_check; changed detection rule.

* Sun Aug 22 2004 Ilya Evseev <evseev@altlinux.ru> 2.13-alt1%release_tag
- new release
- also update configuration file
- service script is generated separately
  for ALTLinux 2.2 (classic style) and 2.4beta (modern style)
- removed 'Requires: initscripts' for preventing problems with sisyphus_check

* Wed Aug  4 2004 Ilya Evseev <evseev@altlinux.ru> 2.10-alt2
- added 'Requires: initscripts' for preventing problems with automated building

* Tue Jul 29 2004 Ilya Evseev <evseev@altlinux.ru> 2.10-alt1
- initial build

## EOF ##
