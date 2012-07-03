Name: rarpd
Version: 1.1
Release: alt2.1

Summary: Reverse Address Resolution Protocol Daemon
License: MIT/X11
Group: Networking/Other

Url: ftp://ftp.dementia.org/pub/net-tools/
Source: %name-%version.tar.bz2
Patch0: %name-%version-libnet.diff
Patch1: %name-%version-printf.diff
Patch2: %name-alt-no-rpath.diff
Patch3: %name-%version-autoconf.diff
Patch4: %name-%version-fix-packet-growth-bug246891.diff
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libnet-devel libpcap-devel
Conflicts: iputils <= 20020927-alt4.1

%description
Rarpd listens on the Ethernet for broadcast packets asking for reverse
address resolution.  These packets are sent by hosts at boot time to
find out their IP addresses.

%prep
%setup -q
%patch0
%patch1
%patch2 -p2
%patch3
%patch4

%build
rm install.sh
aclocal -I cmulocal
automake -afc --foreign
autoconf -I cmulocal
CFLAGS="%optflags -Wall -fPIE -pie" \
%configure --with-libnet=%prefix
%make

%install
make DESTDIR=%buildroot install

%files
%doc AUTHORS TODO
%doc %_mandir/man?/*
%_sbindir/%name

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2.1
- Removed bad RPATH

* Wed May 23 2007 Michael Shigorin <mike@altlinux.org> 1.1-alt2
- added Conflicts: for iputils package still including rarpd

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 1.1-alt1
- built for ALT Linux; package imported from openSUSE 1.1-633
  + fixes unlimited packet growth,
    see http://secunia.com/advisories/25061/
  + the following suse folks worked on it:
    nadvornik (cz), mls (de), ro (de), mjancar (cz), adrian (de), vinil (cz)
  + thanks Dmitry Levin (ldv@) for direct link
- spec cleanup
