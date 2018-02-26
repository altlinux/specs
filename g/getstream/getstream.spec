Name: getstream
Summary: DVB to multicast streamer
Version: 20120411
Release: alt1
License: GPL
Group: Networking/Other
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
# Automatically added by buildreq on Thu Nov 12 2009
BuildRequires: glib2-devel libevent1.4-devel

Packager: Alexei Takaseev <taf@altlinux.ru>

Url: http://silicon-verl.de/home/flo/projects/streaming/

%description
getstream is an DVB to multicast or unicast streamer
Features provided by getstream:
  * Full transponder streaming
  * DVB-T/C/S/S2 support (S2 only via multiproto API)
  * UDP or RTP multicast streaming
  * SAP/SDP Announcements (VLC Compatible) for multicast streams
  * HTTP streaming for unicast setups
  * High optimization for multiple transponders per machine

%prep
%setup -q
%patch0 -p1

%build
%make LIBDIR=%_lib

%install

install -pm0755 -D %name %buildroot%_bindir/%name
install -pm0755 -D %name.init %buildroot%_sysconfdir/rc.d/init.d/%name
install -pm0644 -D %name.conf %buildroot%_sysconfdir/
install -pm0644 -D %name.8 %buildroot%_mandir/man8/%name.8
mkdir -p %buildroot%_localstatedir/%name

%pre
/usr/sbin/useradd -G video -s /bin/false -r -c "user for getstream" -d /var/lib/getstream getstream &>/dev/null ||:

%files
%doc README configs
%_bindir/%name
%_mandir/*/*
%_sysconfdir/rc.d/init.d/%name
%config %attr(644,root,root) %_sysconfdir/getstream.conf
%dir %_localstatedir/%name

%changelog
* Sat May 26 2012 Alexei Takaseev <taf@altlinux.org> 20120411-alt1
- new version

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20100816-alt1.2
- Fixed built with new glib2

* Sat Jun 25 2011 Igor Vlasenko <viy@altlinux.ru> 20100816-alt1.1
- rebuilt with libevent2

* Tue Sep 28 2010 Anton Farygin <rider@altlinux.ru> 20100816-alt1
- new version

* Thu Nov 12 2009 Anton Farygin <rider@altlinux.ru> 20090226-alt1
- first build for Sisyphus
