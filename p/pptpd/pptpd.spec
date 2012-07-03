Name: pptpd
Version: 1.3.4
Release: alt7

Summary: A PPTP server daemon
Summary(ru_RU.KOI8-R): Сервер сетевых соединений PPTP
License: GPL
Group: System/Servers

Url: http://www.poptop.org

#http://heanet.dl.sourceforge.net/sourceforge/poptop/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: pptpd.init
Source2: pptpd.sysconfig
Patch0: %name-%version-%release.patch

Requires: ppp = 2.4.5

#BuildPreReq: rpm-build >= 4.0.4-alt10, autoconf_2.5, automake_1.9
BuildRequires: libwrap-devel
BuildRequires: ppp-devel = 2.4.5

#%%def_with libwrap

%description
PPTPd, Point-to-Point Tunnelling Protocol Daemon, offers out connections
to PPTP clients to become virtual members of the IP pool owned by the PPTP
server.  In effect, these clients become virtual members of the local
subnet, regardless of what their real IP address is.  A tunnel is built
between the PPTP server and client, and packets from the subnet are
wrapped and passed between server and client similar to other C/S
protocols.

%description -l ru_RU.KOI8-R
PPTPd, Point-to-Point Tunnelling Protocol Daemon, позволяет клиентским
PPTP-соедининениям получать адреса из IP-пула, управляемого сервером PPTP.
В результате эти клиенты могут стать виртуальными членами локальной подсети
независимо от их настоящего IP-адреса. Для этого формируется туннель между
клиентом и сервером, по которому транспортируются пакеты между локальной
подсетью и клиентом.

%prep
%setup
%patch0 -p1

%build
#%%set_autoconf_version 2.5
#%%set_automake_version 1.9
#%%configure %{subst_with libwrap}

# dirty hack for fix wtmp work on x86_64
sed -i -e "s,/usr/lib/pptpd/pptpd-logwtmp.so,%_libdir/pptpd/pptpd-logwtmp.so,g" pptpctrl.c

autoreconf -fisv
%configure \
	--with-libwrap \
	--enable-bcrelay
%make_build

%install
%makeinstall

install -pD -m644 samples/%name.conf %buildroot%_sysconfdir/%name.conf
install -pD -m644 samples/options.%name %buildroot%_sysconfdir/ppp/options.%name
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m600 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%config %_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/%name.conf
%config(noreplace) %_sysconfdir/ppp/options.%name
%_sbindir/*
%_mandir/man?/*
%_libdir/%name
%doc AUTHORS NEWS README* TODO samples tools ChangeLog* html

%changelog
* Wed Oct 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.4-alt7
- Relax dependency on ppp.

* Tue Oct 12 2010 Michael Shigorin <mike@altlinux.org> 1.3.4-alt6
- rebuilt with ppp-2.4.5-alt6

* Sat Jul 10 2010 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt5
- rebuild with ppp-2.4.5-alt5

* Tue Jan 26 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.4-alt4
- Set versioned dependency on ppp-devel.

* Tue Jan 19 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.4-alt3
- Rebuilt with ppp-2.4.5 (Closes: #22784).

* Mon May 12 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.4-alt2
- Updated default options.pptpd

* Thu May 03 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.4-alt1
- 1.3.4:
  + Security fix - remote DoS - malformed GRE packets can terminate PPTP
  connections (CVE-2007-0244)
  + Fix two release critical packet reordering bugs
  + Some other (see NEWS)
- Add dirty hack for fix wtmp work on x86_64 (re-Closes: #9817)
- Updated default options.pptpd

* Thu Apr 05 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.3-alt1
- 1.3.3
- Revert pptpd-1.3.2-alt-maxconn.patch because upstream introduces new feature -
  limiting connections number from configuration file
- Rebuild with new pppd (Closes: #11354)
- Switch to use .gear-tags

* Mon Nov 13 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.2-alt2
- Use system pppd.h header in logwtmp plugin, not own (reported by hiddenman@)
  (pptpd-1.3.2-alt-logwtmp_use_system_pppd.h.patch)

* Thu Aug 03 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.2-alt1
- 1.3.2
- Fix build on x86_64 (Closes: #9817)
- Fix some unresolved symbols in logwtmp (patch suggested by stalker@)
- Rediffed alt-maxconn patch
- Removed unnedded pptpd-1.3.0-cvs-pptpgre.c.patch

* Wed Jul 26 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.0-alt2
- Added patch from CVS (pptpd-1.3.0-cvs-pptpgre.c.patch) for fix some
  logging

* Sun Jul 09 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.3.0-alt1
- 1.3.0
- New packager

* Sun Dec 25 2005 Denis Ovsienko <pilot@altlinux.ru> 1.2.1-alt2
- fixing files section (#8727)

* Sat May 14 2005 Denis Ovsienko <pilot@altlinux.ru> 1.2.1-alt1
- switching to current stable version
- rediffed makefile patch

* Mon Feb 07 2005 Denis Ovsienko <pilot@altlinux.ru> 1.1.4-alt4.b4
- enhancements:
 + #5653 (maximum 255 connections)
 + #5977 (--pidfile works now)

* Mon May 31 2004 Denis Ovsienko <pilot@altlinux.ru> 1.1.4-alt3.b4
- moved strange scripts away from bindir and eliminated perl-base dependency

* Tue May 25 2004 Denis Ovsienko <pilot@altlinux.ru> 1.1.4-alt2.b4
- disabled dangerous patch

* Sat May 15 2004 Denis Ovsienko <pilot@altlinux.ru> 1.1.4-alt1.b4
- previous version was actually 1.1.4-b4
- Russian tags
- enabled libwrap support and broadcast relaying
- group changed to System/Servers

* Wed May 05 2004 Denis Ovsienko <pilot@altlinux.ru> 1.1.4-alt1.b2
- initscript adjusted for current requirements and fixed
- new stable version 1.1.4-b2
- patches adjusted for new version

* Wed Apr 23 2003 Dmitry V. Levin <ldv@altlinux.org> 1.1.3_20030409-alt1
- NMU: updated to 1.1.3-20030409, to fix exploitable buffer overflow,
  thanks to Timo Sirainen for reporting this issue.

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.3-alt1
- 1.1.3
- Rebuilt in new environment

* Mon Jun 17 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.2-alt1
- 1.1.2
- Added patches from ASP Linux
- Added /etc/sysconfig/pptpd file with args for pptpd
- Some spec cleanup

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.1.1-ipl2
- Rebuild for Sisyphus
- Fixed filelist
- Added %post & %postun scripts

* Sun Mar 18 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.1.1-ipl1
- First build for ALT
