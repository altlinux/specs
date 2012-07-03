%define		privuser  ichat
%define		privgroup ichat
%define		privpath  /var/empty

Name:		ichatsrvd
Version:	0.24
Release: alt3.1.1
License:	Distributable
Group:		System/Servers
Source0:	%name-%version.tar.bz2
Source1:	%name-logrotate
Summary:	Intranet Chat server
Summary(ru_RU.CP1251): Чат-сервер Интранет
Url:		http://vaulter.narod.ru
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Patch0:		%name-%version-alt_dir_ld_flags.diff
Provides:	ichatsrv

BuildRequires: libssl-devel

%description
Intranet Chat server

%description -l ru_RU.CP1251
Чат-сервер Интранет

%prep
%setup -q
%patch0 -p1

%build
%make_build RELEASE=1 DEVASTATOR=1

%install
%__mkdir -p %buildroot%_logdir/%name
%__mkdir -p %buildroot/var/run/ichatsrvd
%__install -Dp -c -m0755 %name %buildroot%_sbindir/%name.bin
%__install -Dp -m0755 ichatsrv %buildroot%_initdir/%name
%__install -Dp -m0644 ichatsrv.conf %buildroot%_sysconfdir/%name/%name.conf
echo "" > %buildroot%_sysconfdir/%name/ichat_banlist
%__install -Dp -m 0640 %SOURCE1 %buildroot%_sysconfdir/logrotate.d/%name

%pre
/usr/sbin/groupadd -r -f %privgroup
/usr/sbin/useradd -r -s /dev/null -g %privgroup -d %privpath >/dev/null -c 'iChat daemon' %privuser >/dev/null 2>&1 ||:

%post
%post_service %name
service %name condrestart

%preun
service %name stop
/usr/sbin/userdel %privuser

%files
%doc README
%_sbindir/*
%_initdir/%name
%_sysconfdir/logrotate.d/%name
%attr(770,root,%privgroup) %_sysconfdir/%name
%attr(2660,root,%privgroup) %config(noreplace) %_sysconfdir/%name/ichat_banlist
%attr(2660,root,%privgroup) %config(noreplace) %_sysconfdir/%name/%name.conf
%dir %attr(2770,root,%privgroup) %_logdir/%name
%dir %attr(2770,root,%privgroup) /var/run/ichatsrvd

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.24-alt3.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.24-alt3.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Sun Mar 02 2008 Motsyo Gennadi <drool@altlinux.ru> 0.24-alt3
- fix logrotate
- add condrestart to initscript

* Thu Feb 28 2008 Motsyo Gennadi <drool@altlinux.ru> 0.24-alt2
- initial build for Sisyphus
- change owner for process to special pseudouser
- add logrotate

* Sat Jun 23 2007 Motsyo Gennadi <drool@altlinux.ru> 0.24-alt0.M40.1
- build for M40
- changed subst method to patch method
- fix as-needed

* Sat Nov 04 2006 Motsyo Gennadi <drool@altlinux.ru> 0.24-alt0.M24.4
- fix path for devastator log

* Sun Oct 08 2006 Motsyo Gennadi <drool@altlinux.ru> 0.24-alt0.M24.3
- rename %_bindir/%name to %_bindir/%name.bin
- fix and cleanup daemon
- DEVASTATOR enabled and run buildreq script
- fix and cleanup spec-file
- fix spec-file to Backports Policy

* Sun Aug 20 2006 Motsyo Gennadi <drool_linux@pisem.net> 0.24-alt2.drool
- fix daemon to ALT Linux 2.4 Master compatible

* Mon Aug 01 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.24-alt1.drool
- new version from Andrei Bairamov aka Vaulter

* Sat Jul 30 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.21-alt3.drool
- fix URL

* Mon Jul 18 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.21-alt2.drool
- fix $RPM_OPT_FLAGS

* Tue Jul 05 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.21-alt1.drool
- initial build for ALT Linux
