Name: pdnsd
Version: 1.2.9a
Release: alt1

Summary: A caching DNS proxy for small networks and dialup users
License: %gpl3plus
Group: System/Servers

Url: http://members.home.nl/p.a.rombouts/pdnsd/

# git://git.altlinux.org/gears/p/pdnsd.git
Source: %name-%version-%release.tar

BuildPreReq: %_bindir/mksock
BuildPreReq: rpm-build-licenses >= 0.7

%description
pdnsd is a proxy DNS daemon with permanent disk cache and the ability
to serve local records.

%prep
%setup -n %name-%version-%release

mv alt/README.ALT .

%build
%autoreconf
%configure \
	--with-default-id=%name \
	--with-random-device=/dev/urandom
%make_build

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot{%_cachedir/%name,%_var/run/%name}
rm -f contrib/Makefile*

install -pD -m755 alt/%name.init %buildroot%_initdir/%name
install -pD -m755 alt/%name.conf %buildroot%_sysconfdir/%name.conf
install -pD -m755 alt/%name.ip-up %buildroot%_sysconfdir/ppp/ip-up.d/0%name
install -pD -m755 alt/%name.tmpfiles.d %buildroot%_tmpfilesdir/%name.conf

touch %buildroot%_cachedir/%name/%name.cache
mksock %buildroot%_var/run/%name/socket

bzip -9 ChangeLog

%files
%doc AUTHORS Change* COPYING.BSD NEWS README* THANKS TODO doc/pdnsd.conf contrib doc/txt doc/html
%_sbindir/%{name}*
%_mandir/man?/%{name}*
%_tmpfilesdir/%name.conf
%config %_initdir/%name
%config %_sysconfdir/ppp/ip-up.d/0%name
%config(noreplace) %_sysconfdir/%name.conf
	%attr(700,root,%name) %dir %_var/run/%name
%ghost	%attr(600,root,%name) %_var/run/%name/socket
	%attr(700,root,%name) %dir %_cachedir/%name
%ghost	%attr(600,root,%name) %verify(not md5 mtime size) %config(noreplace) %_cachedir/%name/%name.cache

%pre
%_sbindir/groupadd -r -f %name >/dev/null 2>&1 ||:
%_sbindir/useradd -r -g %name -d /dev/null -s /dev/null -n %name >/dev/null 2>&1 ||:

%post
[ -s %_cachedir/%name/%name.cache ] ||
        echo -n -e "pd12\0\0\0\0" >%_cachedir/%name/%name.cache
chmod 0600 %_cachedir/%name/%name.cache
chown root:%name %_cachedir/%name/%name.cache

%post_service %name

%preun
%preun_service %name

%changelog
* Fri May 11 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.2.9a-alt1
- 1.2.9a
- rediffed patches
- updated home url
- add tmpfiles.d conf

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.2.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Sep 06 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.2.7-alt1
- 1.2.7-par
- use /dev/urandom as the RNG source
- compress ChangeLog

* Wed Sep 05 2007 Andrey Rahmatullin <wrar@altlinux.ru> 1.2.6-alt1
- 1.2.6-par

* Sun Dec 17 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.2.5-alt1
- 1.2.5-par
- spec cleanup
- update patches
- fix alt-sock_path.patch (#10099)
- fix README.ALT packaging (#5342)    

* Thu Oct 14 2004 Alexey Tourbin <at@altlinux.ru> 1.2-alt1
- updated to 1.2-par branch (by Paul Rombouts)
- updated patches
- built with recent autotools
- cryptic README.ALT

* Sat Aug 23 2003 Alexey Tourbin <at@altlinux.ru> 1.1.7a-alt6
- new init script according to new rc scheme
- cache.c:
  + s/alt-chroot-disk-cache.patch/cache.patch/
  + keep cache file stream always open
  + eliminate the use of fseek on writes (Paul Rombouts)
- main.c: command line parser reworked utilizing getopt_long(3)
- ipvers.h: remove stale glibc code
- configure.in: dropped some CFLAGS because they are in acconfig.h

* Sun May 11 2003 Alexey Tourbin <at@altlinux.ru> 1.1.7a-alt5
- fixed alt-chroot-disk-cache.patch that could lead to crash
- pdnsd is no longer maintained by its author; going to start my own CVS repo
- Sisyphus release (works fine for me)

* Mon Jan 27 2003 Alexey Tourbin <at@altlinux.ru> 1.1.7a-alt4
- doesnot build with automake-1.7; exact version specified for
  automake (1.6) and autoconf (2.5) in BuildPreReq
- minor fixes

* Wed Jan 22 2003 Alexey Tourbin <at@altlinux.ru> 1.1.7a-alt3
- major revision; new features added; works now out of the box
- alt patches: now able to work in empty chrooted environment
  + droppriv patches: global chroot_dir config option, chroot code
  + protoent, chroot patches: open resources before chroot
  + global-sock_path: control socket path configurable; not finished
    because can't link pdnsd-ctl against it
  + note that some features will not work when chrooted
- debian patches:
  + changeable_ip: manipulate server ip via control socket
  + so_reuseaddr: smoother restart
- default configuration file (supposed to be suitable for dialup):
  + chrooted to /var/empty
  + use {A,B}.ROOT-SERVERS.NET by default
  + changeble_ip enabled
- /etc/ppp/ip-up.d/0pdnsd: change server ip whenever peer DNS is available

* Fri Sep 20 2002 Alexey Tourbin <at@turbinal.org> 1.1.7a-alt2
- PLD patch applied which claims to fix SIGTERM handling for threads
- init script: sleep 2 after killproc (still thread problems)
- Sisyphus candidate

* Sun Jul 21 2002 Alexey Tourbin <at@turbinal.org> 1.1.7a-alt1
- 1.1.7a
- init script rewritten
- custom PPP init scheme suggested (pdnsd.conf.in and pdnsd.ip-up.local)
- ALT Linux adoptions

* Sun May 16 2001 Thomas Moestl <tmoestl@gmx.net>
- Make use of chkconfig for Red Hat (patch by Christian Engstler)
* Sun Mar 25 2001 Thomas Moestl <tmoestl@gmx.net>
- Merged SuSE fixes by Christian Engstler
* Fri Feb 09 2001 Thomas Moestl <tmoestl@gmx.net>
- Merged in a spec fix for mapage inclusion contributed by Sourav K.
  Mandal
* Sun Nov 26 2000 Thomas Moestl <tmoestl@gmx.net>
- Added some patches contributed by Bernd Leibing
* Tue Aug 15 2000 Thomas Moestl <tmoestl@gmx.net>
- Added the distro for configure
* Tue Jul 11 2000 Sourav K. Mandal <smandal@mit.edu>
- autoconf/automake modifications
