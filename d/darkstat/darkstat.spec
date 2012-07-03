Summary: Network traffic analyzer
Name:    darkstat
Version: 3.0.707
Release: alt1
License: GPL
Group:   Monitoring
Url: http://dmr.ath.cx/net/darkstat/

Packager: Nick S. Grechukh <gns@altlinux.org>

Source: http://dmr.ath.cx/net/darkstat/darkstat-%version.tar.bz2

# Automatically added by buildreq on Wed Apr 02 2008
BuildRequires: libpcap-devel zlib-devel

%description
darkstat is a network traffic analyzer. It's basically a packet sniffer
which runs as a background process on a cable/DSL router and gathers
all sorts of useless but interesting statistics.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING* INSTALL LICENSE NEWS README THANKS
%_man1dir/darkstat.1*
%_sbindir/darkstat

%changelog
* Wed Apr 02 2008 Nick S. Grechukh <gns@altlinux.org> 3.0.707-alt1
- first build to sisyphus. TODO: steal nice initscript from debian

* Tue Oct 02 2007 Dag Wieers <dag@wieers.com> - 3.0.707-1
- Updated to release 3.0.707.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 3.0.619-1
- Updated to release 3.0.619.

* Mon Aug 07 2006 Dag Wieers <dag@wieers.com> - 3.0.540-1
- Updated to release 3.0.540.

* Tue Jun 20 2006 Dag Wieers <dag@wieers.com> - 3.0.471-1
- Updated to release 3.0.471.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 2.6-1
- Initial package. (using DAR)
