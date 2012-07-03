Name: httptunnel
Version: 3.0.5
Release: alt2

Url: http://www.nocrew.org/software/httptunnel.html

Summary: bidirectional virtual data over HTTP-proxy
License: GPL
Group: Networking/Other

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

Patch1: %name-%version.bind.patch
Patch2: %name-%version.debug.patch

%description
httptunnel creates a bidirectional virtual data path tunnelled in HTTP
requests.  The requests can be sent via an HTTP proxy if so desired.

This can be useful for users behind restrictive firewalls.  If WWW
access is allowed through an HTTP proxy, it's possible to use
httptunnel and, say, telnet or PPP to connect to a computer outside
the firewall.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%doc AUTHORS COPYING ChangeLog DISCLAIMER FAQ HACKING NEWS README TODO

%changelog
* Wed Nov 19 2008 Denis Smirnov <mithraen@altlinux.ru> 3.0.5-alt2
- cleanup spec

* Thu Feb 12 2004 Denis Smirnov <mithraen@altlinux.ru> 3.0.5-alt1
- Patch for binding at specified address
- First build for ALT Linux Sisyphus
