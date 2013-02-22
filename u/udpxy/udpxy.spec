Name: udpxy
Version: 1.0.23
Release: alt1

Summary: UDP-to-HTTP multicast traffic relay daemon

Group: Networking/Other
License: GPLv3+
Url: http://sourceforge.net/projects/udpxy/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/udpxy/udpxy/Chipmunk-1.0/%name.%{version}-0-prod.tar

Source1: udpxy.service
Source44: import.info
Source45: udpxy.init
Source46: udpxy.sysconfig

%description
udpxy is a UDP-to-HTTP multicast traffic relay daemon:
it forwards UDP traffic from a given multicast subscription
to the requesting HTTP client.

%prep
%setup -n %name.%version-0-prod
%__subst "s|CFLAGS += -W -Wall -Werror --pedantic|CFLAGS += %optflags|g" Makefile

%build
%make_build

%install
%__subst "s|INSTALLROOT := /usr/local|INSTALLROOT := %buildroot/usr|g" Makefile
%__subst 's|ln -s $(INSTALLROOT)/bin/$(EXEC)|ln -s $(EXEC)|g' Makefile

%make_install install

install -D -p -m 0644 %SOURCE1 %buildroot%_unitdir/%name.service
install -D -m 755 %SOURCE45 %buildroot%_initdir/%name
install -D -m 644 %SOURCE46 %buildroot%_sysconfdir/sysconfig/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README CHANGES
#udpxy-manual-RU.rtf
%_bindir/%name
%_bindir/udpxrec
%_unitdir/%name.service
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Fri Feb 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.23-alt1
- new version 1.0.23 (with rpmrb script)

* Fri Feb 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.21-alt4
- cleanup spec for ALT Linux rules

* Sat Feb 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt3_2
- cleaned up depandencies

* Sat Feb 18 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt2_2
- added sys V init script

* Fri Feb 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.21-alt1_2
- converted for Sisyphus

