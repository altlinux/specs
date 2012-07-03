# User and group name for ss5
%define ss5_user ss5
%define ss5_group ss5
# Home for ss5 user
%define ss5_home /dev/null
# Shell for ss5 user
%define ss5_shell /dev/null
# Default address to bind
%define ss5_bindaddr 127.0.0.1
# Default port to bind
%define ss5_bindport 1080

Name: ss5
Version: 3.6.4
Release: alt2.rel3.2

Summary: Full featured SOCKS4 and SOCKS5 server
Summary(ru_RU.UTF-8): Многофункциональный сервер SOCKS4 и SOCKS5
License: GPL
Group: System/Servers

Url: http://ss5.sourceforge.net/

Source: %name-%version.tar.gz
Source1: %name.init
Source2: %name.pam
Source3: %name.sysconfig
Source4: %name.conf

# Fix hardcoded peers file path
#Patch0: %name-peerspath.patch
# Pid file support
Patch1: %name-pidfilesupport.patch
# Improved signal handling
Patch2: %name-signalhandling.patch
# Added libraries to fix unresolved symbols
Patch3: %name-makefile.patch
# More correct daemonize
Patch4: %name-daemon.patch
# array index overflow
Patch5: ss5-3.6.4-CVE-2009-2368.patch

Requires: openldap pam
BuildRequires: openldap-devel pam-devel

%description
ss5 is a full featured socks server, which supports both SOCKS4 and SOCKS5 protocols,
that runs on Linux/Solaris platforms.

%description -l ru_RU.UTF-8
ss5 - это многофункциональный socks-сервер, который поддерживает протоколы
SOCKS4 и SOCKS5 и работает на платформах Linux/Solaris.

%prep
%setup -q
#%%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p2

%build
%configure  --with-configfile=%_sysconfdir/%name/%name.conf \
			--with-passwordfile=%_sysconfdir/%name/%name.passwd \
			--with-logfile=%_var/log/%name/%name.log \
			--with-profilepath=%_sysconfdir/%name \
			--with-libpath=%_libdir \
			--with-tracepath=%_var/log/%name \
			--with-defaultuser=%ss5_user \
			--with-defaultaddr=%ss5_bindaddr \
			--with-defaultport=%ss5_bindport \	

%make

%install
%__mkdir_p %buildroot%_sysconfdir/%name
%__mkdir_p %buildroot%_initdir
%__mkdir_p %buildroot%_sysconfdir/{sysconfig,pam.d}
%__mkdir_p %buildroot%_libdir/%name
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_var/run/%name
%__mkdir_p %buildroot%_var/log/%name
%__mkdir_p %buildroot%_man1dir
%__mkdir_p %buildroot%_man5dir

find . -type f -name *.so -exec %__install -m644 '{}' %buildroot%_libdir/%name/ \;
%__install -m755 src/%name %buildroot%_bindir/
%__install -m755 %SOURCE1 %buildroot%_initdir/%name
%__install -m640 %SOURCE2 %buildroot/%_sysconfdir/pam.d/%name
%__install -m640 %SOURCE3 %buildroot/%_sysconfdir/sysconfig/%name
%__install -m640 %SOURCE4 %buildroot%_sysconfdir/%name/
%__install -m644 man/Linux/*\.1\.* %buildroot%_man1dir/
%__install -m644 man/Linux/*\.5\.* %buildroot%_man5dir/

%pre
/usr/sbin/groupadd -r -f %ss5_group
/usr/sbin/useradd -r -g %ss5_group -d %ss5_home -M -s %ss5_shell -n -c "Socks5 server" %ss5_user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc/* conf/* ChangeLog INSTALL License SOLARIS.NOTES
%attr(0750,root,%ss5_group) %dir %_sysconfdir/%name
%attr(0640,root,%ss5_group) %config(noreplace) %_sysconfdir/%name/*
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_initdir/*
%_bindir/*
%attr(1770,root,%ss5_group) %dir %_var/run/%name
%attr(1770,root,%ss5_group) %dir %_var/log/%name
%_man1dir/*
%_man5dir/*
%_libdir/%name


%changelog
* Mon Oct 05 2009 Michael Shigorin <mike@altlinux.org> 3.6.4-alt2.rel3.2
- NMU: security fix for CVE-2009-2368 (array index overflow) (ALT #20701)
  + thanks crux@ for heads-up

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 3.6.4-alt2.rel3.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Mon Apr 14 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.4-alt2.rel3
- /var/run/ss5 and /var/log/ss5 perms changed to 1770 (thanks to vvk@)
- ss5 user's shell changed to /dev/null

* Sat Apr 12 2008 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.4-alt1.rel3
- New version
- New patch for more correct daemonize (misfeature: stderr output won't work anymore)
- Changed /var/run/ss5 and /var/log/ss5 perms to 0770,root:ss5

* Fri Oct 06 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.6.1-alt1
- Release
- Removed hardcoded path patch (fixed by upstrem)
- Reworked other patches
- Fixed unresolved symbols

* Fri Jun 23 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.5.9-alt2
- Fixed unresolved symbols

* Tue May 23 2006 Andrew Kornilov <hiddenman@altlinux.ru> 3.5.9-alt1
- New version
- Removed hardcoded-path patch (fixed by upstream)
- New hardcoded peers file patch
- New config file
- Spec cleanups (man dirs)
- Now use configure (added by upstream)
- Reworked signal handling and pidfile support patches
- Added logdir

* Thu Oct 27 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.0-alt4
- Reworked pidfile and signals handling support 

* Thu Oct 27 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.0-alt3
- Now use "ss5" user and group

* Sun Oct 23 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.0-alt2
- New patch for pid-file support

* Wed Oct 19 2005 Andrew Kornilov <hiddenman@altlinux.ru> 3.0-alt1
- First build for Sisyphus

