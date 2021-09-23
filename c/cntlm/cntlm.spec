Name: cntlm
Version: 0.92.3
Release: alt2

Summary: Fast NTLM authentication proxy with tunneling
License: GPL-2
Group: System/Servers
URL: http://cntlm.sourceforge.net/
Packager:	Lenar Shakirov <snejok@altlinux.org>

#Source: https://downloads.sourceforge.net/%name/%name-%version.tar.bz2
Source: %name-%version.tar

Source1: cntlm.init
Source2: cntlm.sysconfig
Source3: cntlm.tmpfiles
Source4: cntlm.service

Patch0: cntlm_makefile.patch

%description
Cntlm is a fast and efficient NTLM proxy, with support for TCP/IP tunneling,
authenticated connection caching, ACLs, proper daemon logging and behaviour
and much more. It has up to ten times faster responses than similar NTLM
proxies, while using by orders or magnitude less RAM and CPU. Manual page
contains detailed information.

%prep
%setup
%patch -p2
%__subst 's!\-o root \-g root \-m [[:digit:]]\+!!g' Makefile

%build
%configure
%make_build SYSCONFDIR=%_sysconfdir \
	BINDIR=%_bindir \
	MANDIR=%_mandir

%install
%makeinstall SYSCONFDIR=%buildroot/%_sysconfdir \
	BINDIR=%buildroot/%_bindir \
	MANDIR=%buildroot/%_mandir

install -D -m 755 %SOURCE1 %buildroot/%_initrddir/cntlmd
install -D -m 644 %SOURCE2 %buildroot/%_sysconfdir/sysconfig/cntlmd
install -D -m 644 %SOURCE3 %buildroot/%_tmpfilesdir/%name.conf
install -D -m 644 %SOURCE4 %buildroot/%_unitdir/cntlmd.service

mkdir -p %buildroot/run/%name

%files
%doc LICENSE README COPYRIGHT
%_bindir/cntlm
%_man1dir/cntlm.1*
%config(noreplace) %_sysconfdir/cntlm.conf
%config(noreplace) %_sysconfdir/sysconfig/cntlmd
%config %_initdir/cntlmd
%_tmpfilesdir/%name.conf
%_unitdir/cntlmd.service
%ghost %attr(0750,%name,%name) /run/%name

%pre
%_sbindir/useradd -s /sbin/nologin -m -r -k /var/empty -d /var/run/cntlm cntlm >/dev/null 2>&1 ||:

%post
%post_service cntlmd

%preun
%preun_service cntlmd

%changelog
* Mon Sep 13 2021 Pavel Nakonechnyi <zorg@altlinux.org> 0.92.3-alt2
- spec cleanup
- minor Makefile fixes
- add systemd service file and tmpfiles.d config
- fix run directory handling, see #36776

* Thu Apr 05 2012 Lenar Shakirov <snejok@altlinux.ru> 0.92.3-alt1
- New version

* Tue Dec 20 2011 Lenar Shakirov <snejok@altlinux.ru> 0.92-alt2
- Init script:
  + fixed condrestart: "restart" function doesn't exist
  + config file processing added
  + doesn't "noreplace" now

* Fri Dec 02 2011 Lenar Shakirov <snejok@altlinux.ru> 0.92-alt1
- New version

* Thu Feb 14 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.35.1-alt3
- Init script fixed

* Wed Feb 13 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.35.1-alt2
- Add user script corrected

* Tue Feb 12 2008 Maxim Ivanov <redbaron@altlinux.ru> 0.35.1-alt1
- Inital build for Sisyphus
