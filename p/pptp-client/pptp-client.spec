Name:      pptp-client
Version:   1.7.2
Release:   alt2

Summary:   Point-to-Point Tunneling Protocol (PPTP) Client
License:   GPL
Url:       http://pptpclient.sourceforge.net

Group:     Networking/Other

Obsoletes: pptp-client <= 1.2.0 pptp-client-fe <= 1.2.0 pptp-client-fe-Tk <= 1.2.0

Packager:  Evgeny V. Shishkov <shev@altlinux.org>

Source0:   pptp-%version.tar.gz
Patch0:    pptp-1.7.2-compat.patch
Patch1:    pptp-1.7.2-declaration.patch
Patch2:    pptp-1.7.2-ip-path.patch
Patch3:    pptp-1.7.2-makefile.patch

PreReq: ppp etcnet

BuildRequires: perl-Pod-Parser

Conflicts: pptp-adsl net-scripts

%description
Client for the proprietary Microsoft Point-to-Point Tunneling
Protocol, PPTP.  Allows connection to a PPTP based VPN as used
by employers and some cable and ADSL service providers.

%description -l ru_RU.UTF-8
Клиент для работы по протоколу Point-to-Point Tunneling Protocol
(PPTP), разработанному Microsoft. Клиент позволяет соединяться с VPN
сетями, построенными на PPTP, которые используются в некоторых офисах
и у провайдеров домашних сетей и ADSL сервисов.

%prep

%setup -n pptp-%version

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build OPTIMIZE="%optflags"

%install
%make_install DESTDIR="%buildroot" install
%__install -d -m 750 %buildroot%_localstatedir/run/pptp

%files
%doc AUTHORS COPYING DEVELOPERS INSTALL NEWS README TODO USING
%doc ChangeLog Documentation/DESIGN.PPTP PROTOCOL-SECURITY
%attr(555,root,root) %_sbindir/pptp
%attr(555,root,root) %_sbindir/pptpsetup
%_mandir/man8/pptp.8*
%_mandir/man8/pptpsetup.8.*
%dir %attr(750,root,root) %_localstatedir/run/pptp/
%config(noreplace) /etc/ppp/options.pptp

%changelog
* Tue Nov 16 2010 Evgeny V. Shishkov <shev@altlinux.org> 1.7.2-alt2
- add perl-Pod-Parser in BuildRequires.

* Tue Sep 08 2009 Evgeny V. Shishkov <shev@altlinux.org> 1.7.2-alt1
- new version

* Sun Apr 16 2006 Yury A. Zotov <yz@altlinux.ru> 1.7.0-alt1
- new version
- README.rus is updated

* Mon Feb 21 2005 Yury A. Zotov <yz@altlinux.ru> 1.6.0-alt1
- new version
- howto-diagnosis.html updated

* Mon Aug 02 2004 Yury A. Zotov <yz@altlinux.ru> 1.5.0-alt1
- new version
- howto-diagnosis.html updated

* Sat May 01 2004 Yury A. Zotov <yz@altlinux.ru> 1.4.0-alt2
- misprints in README.rus correction

* Thu Feb 12 2004 Yury A. Zotov <yz@altlinux.ru> 1.4.0-alt1
- new version
- add support for ifup/ifdown
- documentation updated

* Sun Jun 22 2003 Yury A. Zotov <yz@altlinux.ru> 1.3.1-alt1
- new initscript conforming to new initscripts scheme
- pptp-command removed
- pptp-config is new configuring tool
- README.rus rewritten to describe recent changes
- pptp_fe and xpptp_fe removed

* Tue Mar 25 2003 Yury A. Zotov <yz@altlinux.ru> 1.2.0-alt2
- bug 0002419 fixed

* Fri Feb 21 2003 Yury A. Zotov <yz@altlinux.ru> 1.2.0-alt1
- new version
- package split: pptp-client, pptp-client-fe, pptp-client-fe-Tk
- init script updated for use with bind9

* Wed Oct 23 2002 Yury A. Zotov <yz@altlinux.ru> 1.1.0-alt5
- added section about routing aspects in README.rus

* Sun Oct 13 2002 Yury A. Zotov <yz@altlinux.ru> 1.1.0-alt4
- rebuild for gcc3.2
- updated howto-diagnosis.html

* Tue May 7 2002 Yury Zotov <yz@altlinux.ru> 1.1.0-alt3
- README.rus updated
- using %post_service and %preun_service
- pptptunnel.init added in "off" state by default
- spec file cleanup

* Fri Apr 12 2002 Yury Zotov <yz@altlinux.ru> 1.1.0-alt2
- added workaround for ignoring holdoff parameter in options-2Com
- added howto-diagnosis.html
- some cleanups

* Sun Mar 24 2002 Yury Zotov <yz@altlinux.ru> 1.1.0-alt1
- pptp-linux-1.1.0
- spec cleanup
- translation in russian

* Tue Feb 12 2002 Yury Zotov <yz@altlinux.ru> 1.0.3-alt4
- Packager field corrected

* Thu Dec 20 2001 Yury Zotov <yz@altlinux.ru> 1.0.3-alt3
- pptp-extras sinchronized with CVS
- added some documentation
- spec file cleanup

* Thu Nov 8 2001 Yury Zotov <yz@altlinux.ru> 1.0.3-alt2
- updates in pptptunnel script
- added /etc/pptp.d directory

* Wed Oct 31 2001 Yury Zotov <yz@altlinux.ru> 1.0.3-alt1
- new version

* Sun Mar 18 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.0.2-ipl6mdk
- Build for ALT

* Fri Nov 17 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-5mdk
- build for gcc-2.96

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-4mdk
- BM

* Thu Mar 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-3mdk
- fix group
- clean spec

* Thu Jan 06 2000 Lenny Cartier <lenny@mandrakesoft.com>
- add conflicts tag
- fix buildroot

* Tue Oct 11 1999 Lenny Cartier <lenny@mandrakesoft.com>
- Specfile adaptations
