Name: tunctl
Version: 1.5
Release: alt1
Epoch: 1

Summary: Tool to create and manage persistent TUN/TAP interfaces
License: GPL
Group: Networking/Other
Url: http://tunctl.sourceforge.net/

Source: %name-%version-%release.tar

Requires(pre): shadow-utils
BuildRequires: docbook-utils

%description
tunctl allows the host sysadmin to preconfigure a TUN/TAP device for
use by a particular user. That user may open and use the device, but
may not change any aspects of the host side of the interface.

%prep
%setup

%build
make CFLAGS="%optflags"

%install
install -pm0644 -D tun.rules %buildroot%_sysconfdir/udev/rules.d/90-tun.rules
install -pm0755 -D %name %buildroot%_sbindir/%name
install -pm0644 -D %name.8 %buildroot%_man8dir/%name.8

%pre
/usr/sbin/groupadd -r -f tun &>/dev/null

%files
%_sysconfdir/udev/rules.d/90-tun.rules
%_sbindir/%name
%_man8dir/%name.8*

%changelog
* Fri Mar 19 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:1.5-alt1
- 1.5 released

* Sun Oct 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 20060323-alt4
- dropped unneeded source tree parts and rebuilt

* Sun Jun 03 2007 Fr. Br. George <george@altlinux.ru> 20060323-alt3
- Fixed #11003 (mithraen@)

* Sun Apr 29 2007 Denis Smirnov <mithraen@altlinux.ru> 20060323-alt2
- Not remove group when uninstall
- Force groupadd when install (not crash at upgrade)

* Wed Apr 18 2007 Denis Smirnov <mithraen@altlinux.ru> 20060323-alt1
- Add requires(pre) to shadow-utils (need for %%pre section)

* Tue Jan 09 2007 Fr. Br. George <george@altlinux.ru> 20060323-alt0
- Initial build from MDV+Debian

* Sat Jan 06 2007 Olivier Blin <oblin@mandriva.com> 20060323-3mdv2007.0
+ Revision: 104685
- make /dev/net/tun owned by the tun group (#21113)
- make the tunctl package add a tun system group (part of #21113)
- move tunctl in a subpackage since it is often used without UML (description from Debian manpage)

* Wed Aug 09 2006 Olivier Thauvin <nanardon@mandriva.org> 20060323-2mdv2007.0
+ Revision: 54861
- patch0: fix build
- Import uml-utilities


* Tue Apr 4 2006 Tibor Pittich <Tibor.Pittich@mandriva.org>  20060323-1mdk
- 20060323
- remove suid bit on uml_net

* Thu Mar 16 2006 Tibor Pittich <Tibor.Pittich@mandriva.org> 20060216-1mdk
- new version

* Mon Apr 04 2005 Nicolas Lécureuil <neoclust@mandrake.org> 20040406-3mdk
- %%mkrel
- Fix summary

* Mon Apr 04 2005 Nicolas Lécureuil <neoclust@mandrake.org> 20040406-2mdk
-  Rebuild for Readline

* Tue Apr 13 2004 Stew Benedict <sbenedict@mandrakesoft.com> 20040406-1mdk
- 20040406

* Thu Jan  8 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20030903-3mdk
- DIRM fix

* Sat Nov 08 2003 Michael Scherer <scherer.michael@free.fr> 20030903-2mdk 
- BuildRequires ( libncurses-devel )

* Tue Oct 07 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20030903-1mdk
- 20030903

* Tue Aug 13 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20020729-0.1mdk
- 1st pre release

