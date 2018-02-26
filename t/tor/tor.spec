# hey Emacs, its -*- mode: rpm-spec; coding: cyrillic-cp1251; -*-

## Things users may want to change
#
# User (and group) name under which the Tor daemon runs
%define toruser _tor

# Root directory for chrooted environment, must not be
# same as real system root.
%define _tor_root %_localstatedir/%name

Name: tor
Version: 0.2.1.30
Release: alt1

Summary: Anonymizing overlay network for TCP (The onion router)
Group: System/Servers
License: BSD-like
Url: http://tor.eff.org/
Packager: Sviatoslav Sviridov <svd@altlinux.ru>

Source0: http://tor.eff.org/dist/%name-%version.tar
Source1: %name.init

# Automatically added by buildreq on Fri Jun 24 2011
# optimized out: fontconfig fonts-type1-urw ghostscript-classic libcom_err-devel libkrb5-devel tex-common texlive-base texlive-base-bin texlive-common texlive-latex-base texlive-latex-recommended
BuildRequires: ghostscript-common libevent-devel libssl-devel texlive-fonts-recommended texlive-generic-recommended transfig zlib-devel

%description
Tor is a connection-based low-latency anonymous communication system.
This package provides the "tor" program, which serves as both a client
and a relay node.

Applications connect to the local Tor proxy using the SOCKS
protocol. The local proxy chooses a path through a set of relays, in
which each relay knows its predecessor and successor, but no
others. Traffic flowing down the circuit is unwrapped by a symmetric
key at each relay, which reveals the downstream relay.

Warnings: Tor does no protocol cleaning.  That means there is a danger
that application protocols and associated programs can be induced to
reveal information about the initiator. Tor depends on Privoxy and
similar protocol cleaners to solve this problem. This is alpha code,
and is even more likely than released code to have anonymity-spoiling
bugs. The present network is very small -- this further reduces the
strength of the anonymity provided. Tor is not presently suitable
for high-stakes anonymity.

%prep
%setup
ln doc/spec/README doc/spec/README-spec

# Set default configuration values
sed -i 's:^#Log notice file.*:Log notice file %_var/log/%name/%name.log:' src/config/torrc.sample.in
sed -i 's:^#DataDirectory.*:DataDirectory %_var/cache/%name:' src/config/torrc.sample.in

%build
%configure
%make_build
%make -C doc/design-paper tor-design.pdf

# Perform unit test
%make check

%install
%makeinstall_std

install -pD -m755 %SOURCE1 %buildroot/%_initdir/%name
mv %buildroot/%_sysconfdir/%name/torrc.sample %buildroot/%_sysconfdir/%name/torrc
mkdir -p %buildroot%_tor_root
mkdir -p %buildroot%_var/{cache/%name,log/%name,run/%name}

mkdir -p %buildroot%_sysconfdir/logrotate.d
cat >%buildroot%_sysconfdir/logrotate.d/%name <<__EOF__
%_var/log/%name/*log {
	weekly
	rotate 5
	compress
	missingok
	notifempty
	sharedscripts
	postrotate
		%_initdir/%name condreload >/dev/null
	endscript
}
__EOF__

# Chroot config
#mkdir -p %buildroot%_tor_root{/lib,%_var/{nis,yp/binding,log},%_sysconfdir/%name}

%pre
/usr/sbin/groupadd -r -f %toruser
/usr/sbin/useradd -r -g %toruser -d %_tor_root -s /dev/null -c 'Tor user' %toruser >/dev/null 2>&1 ||:
if [ $1 -gt 1 ]; then
	chown %toruser:auth /etc/tcb/%toruser
	/usr/sbin/usermod -d %_tor_root %toruser
fi

%post
#%_sysconfdir/chroot.d/%name.all force
%post_service %name

%preun
%preun_service %name

#if [ $1 = 0 ]; then
#	rm -f %_tor_root/lib/* %_tor_root/var/yp/binding/*
#fi

%files
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/torrc
%config(noreplace) %_sysconfdir/%name/tor-tsocks.conf
%config %_sysconfdir/logrotate.d/%name
%_bindir/tor
%_bindir/torify
%_bindir/tor-resolve
%_bindir/tor-gencert
%_man1dir/*.1.*
%_initdir/%name
%dir %_datadir/%name
%_datadir/%name/geoip
%doc README AUTHORS LICENSE ChangeLog INSTALL doc/{HACKING,TODO} doc/spec/README-spec doc/design-paper/tor-design.pdf contrib/torify contrib/tor-tsocks.conf

%defattr(640,root,%toruser,2710)
%_tor_root
%defattr(640,root,%toruser,2770)
%_var/log/%name
%defattr(640,root,%toruser,2730)
%_var/run/%name
%defattr(640,%toruser,%toruser,2700)
%_var/cache/%name

%changelog
* Fri Jun 24 2011 Dmitry V. Levin <ldv@altlinux.org> 0.2.1.30-alt1
- Blindly updated 0.2.1.30 (fixes numerous bugs including CVE-2011-0427).
- Updated build dependencies.

* Tue Dec 07 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.1.27-alt2
- new version. Rebuilt with openssl-1.0b

* Fri Sep 24 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.1.26-alt2
- added torify

* Wed Jun 09 2010 Mykola Grechukh <gns@altlinux.ru> 0.2.1.26-alt1
- updated to 0.2.1.26

* Tue Jun 30 2009 Sviatoslav Sviridov <svd@altlinux.ru> 0.2.0.35-alt2
- Added directory /usr/share/tor to file list

* Mon Jun 29 2009 Sviatoslav Sviridov <svd@altlinux.ru> 0.2.0.35-alt1
- Updated to 0.2.0.35
- Packaged files:
  + /usr/bin/tor-gencert
  + /usr/share/tor/geoip

* Wed Sep 10 2008 Sviatoslav Sviridov <svd@altlinux.ru> 0.2.0.31-alt1
- Updated to 0.2.0.31

* Sun Sep 02 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.17-alt1
- Updated to 0.1.2.17

* Thu Aug 09 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.16-alt1
- Updated to 0.1.2.16
  + Major security fixes: close immediately after missing authentication 
    on control port; do not allow multiple authentication attempts.

* Tue Jul 24 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.15-alt1
- Updated to 0.1.2.15

* Sun May 27 2007 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.2.14-alt1
- Updated to 0.1.2.14
- Packaged more tor specs

* Sun Dec 17 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.26-alt1
- Updated to 0.1.1.26

* Sun Dec 10 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.25-alt1
- Updated to 0.1.1.25

* Tue Oct 10 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.24-alt1
- Updated to 0.1.1.24
- Removed doc files (disappeared in upstream): doc/CLIENTS, doc/FAQ,
  doc/tor-doc.css, doc/tor-doc.html

* Wed May 24 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.1.20-alt1
- Updated to 0.1.1.20 (first stable release of the 0.1.1.x branch)

* Sun Feb 19 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.17-alt1
- Updated to 0.1.0.17

* Wed Jan 04 2006 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.16-alt1
- Updated to 0.1.0.16

* Mon Oct 10 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.15-alt1
- Updated to 0.1.0.15

* Sat Aug 27 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.14-alt1
- Updated to 0.1.0.14

* Wed Jul 13 2005 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0.11-alt1
- First build for ALT Linux
- Known problems:
  + service is not being chrooted
