Name: desproxy
Version: 0.1.0
Release: alt0.2

Summary: desproxy - a TCP tunnel for HTTP proxies
License: GPL
Group: Networking/Other
Url: http://desproxy.sourceforge.net/

Source: %name-%version-pre1.tgz

Patch1: %name-autoconf.patch.bz2

%description
* Desproxy: a TCP tunnel for HTTP proxies. The original application.
* Desproxy-inetd: inetd version of desproxy , useful to launch desproxy
  as a daemon for sendmail, pop3 mail...
* Desproxy-dns: a dns forwarder. Supports UDP & TCP client requests,
  forwarding them to a dns server through the HTTP proxy.
* Desproxy-socks4server: a SOCKS Version 4 server.
* Desproxy-socks5server: a SOCKS Version 5 server.
* Socket2socket: useful tiny application to connect two sockets (useful
  to forward proxy requests, for example).

%prep
%setup
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall
%make_install install -C po DESTDIR=$RPM_BUILD_ROOT

%files
%_bindir/*
%doc doc/{Readme.*,News.html,GPL.html}
%_datadir/locale/*/LC_MESSAGES/%name.mo

%changelog
* Mon Oct 21 2002 Sviatoslav Sviridov <svd@altlinux.ru> 0.1.0-alt0.2
- Rebuild with gcc3.2

* Tue Apr 22 2002 Sviatoslav Sviridov <svd@lintec.minsk.by> 0.1.0-alt0.1
- First build for ALT Linux Sisyphus
