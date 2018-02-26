# $Id: hping2.spec,v 1.7 2004/02/13 10:37:33 homyakov Exp $

%define beta	rc2

Name:		hping2
Version:	2.0.0
Release:	alt4.%beta.qa2
Packager:	Igor Homyakov <homyakov at altlinux dot ru>

Provides:	hping = %version
Obsoletes:	hping

%define srcname	 %name-%beta

Summary: hping2 is a network tool able to send custom ICMP/UDP/TCP packets
Summary(ru_RU.KOI8-R): утилита для генерации ICMP/UDP/TCP пакетов
License: GPL
Group: Security/Networking
Url: http://www.hping.org
Source: hping%version-%beta.tar.gz
Patch:  hping2-rc2-alt-cleanup.patch

# Automatically added by buildreq on Wed Feb 11 2004
BuildRequires: libpcap-devel

%description
hping2 is a network tool able to send custom ICMP/UDP/TCP
packets and to display target replies like ping do with
ICMP replies. hping2 handle fragmentation, arbitrary packet
body and size and can be used in order to transfer files
under supported protocols. Using hping2 you are able at
least to perform the following jobs:

      - Test firewall rules
      - [spoofed] port scanning
      - Test net performance using differents protocols,
          packet size, TOS (type of service) and fragmentation.
      - Path MTU discovery
      - Files trasfering even between really fascist firewall rules.
      - Traceroute like under different protocols.
      - Firewalk like usage.
      - Remote OS fingerprint.
      - TCP/IP stack auditing.
      - A lot of others.

%description -l ru_RU.KOI8-R
%name позволяет вручную создавать ICMP/UDP/TCP пакеты, фрагментировать
их изменять заголовки и т.д. Может использоваться для различных задач
связанных с сетевой безопаснотью и работой стека TCP/IP
  - проверка работы межсетевых экранов
  - сканирование потров
  - тестирование производительности протоколов
  - исследование работы стека TCP/IP
  - удаленное определение операционной системы хоста
  - многое другое ...

%prep

%setup -q -n %srcname

%patch -p1

%build
%configure --force-libpcap

%make_build

%install
install -m700 -D %name        %buildroot%_sbindir/%name
install -m644 -D docs/%name.8 %buildroot%_man8dir/%name.8

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \;
# hack if it is installed as doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; || :

%files
%_sbindir/*
%_mandir/man8/*
%doc README INSTALL AUTHORS BUGS CHANGES KNOWN-BUGS NEWS TODO docs/
%doc docs/ utils/

%changelog
* Sat Nov 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.0-alt4.rc2.qa2
- NMU: pkg-contains-cvs-or-svn-control-dir as %%doc for hping2

* Fri Nov 06 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.0.0-alt4.rc2.1
- NMU (by repocop): the following fixes applied:
  * pkg-contains-cvs-or-svn-control-dir for hping2

* Fri Feb 13 2004 Igor Homyakov <homyakov at altlinux dot ru> 2.0.0-alt4.rc2
- add patch for remove gcc warningds
- fixed depend for libpcap0.7

* Wed Feb 11 2004 Igor Homyakov <homyakov at altlinux dot ru> 2.0.0-alt3.rc2
- rebuild with libpcap0.8

* Thu May 08 2003 Igor Homyakov <homyakov at altlinux dot ru> 2.0.0-alt2.rc2
- fixed bad URL to source tarbal
- spec cleanup
- strict permissions
- rename package to hping2

* Wed Nov 20 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.0.0-alt1.rc2
- rc2 

* Thu Feb 28 2002 Igor Homyakov <homyakov at altlinux dot ru> 2.0.0-alt1.rc1
- Build package for ALTLinux

