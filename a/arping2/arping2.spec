%define origname arping
%define libnet_ver 2

Name: arping2
Version: 2.12
Release: alt1

Summary: Layer2 Ethernet pinger
License: GPL
Group: Networking/Other

# git://github.com/ThomasHabets/arping.git
Url: http://www.habets.pp.se/synscan/programs.php?prog=arping
Source: http://www.habets.pp.se/synscan/files/arping-%version.tar.gz
Source100: %name.watch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Wed Oct 08 2008
BuildRequires: libnet%{libnet_ver}-devel libpcap-devel

%description
Arping is an utility to find out whether a specific IP address
on the LAN is 'taken' and what MAC address owns it.

Sure, you *could* just use 'ping' to find out if it's taken and
even if the computer blocks ping (and everything else) you still
get an entry in your ARP cache.

But what if you aren't on a routable net? Or the host blocks ping
(all ICMP even)?  Then you're screwed. Or you use arping.
Which might not yield realistic result as well.

%prep
%setup -n %origname-%version

%build
%configure
%make_build

%install
%makeinstall_std
# due to arping in iputils as of 2011
mv %buildroot%_sbindir/{%origname,%name}
mv %buildroot%_man8dir/{%origname,%name}.8

%files
%doc LICENSE README extra/arping-scan-net.sh
%_sbindir/%name
%_man8dir/*

%changelog
* Mon Jul 02 2012 Michael Shigorin <mike@altlinux.org> 2.12-alt1
- new version (watch file uupdate)

* Wed Feb 29 2012 Michael Shigorin <mike@altlinux.org> 2.11-alt1
- 2.11

* Tue Feb 28 2012 Michael Shigorin <mike@altlinux.org> 2.10-alt1
- 2.10

* Sat Jan 22 2011 Michael Shigorin <mike@altlinux.org> 2.09-alt3
- renamed manpage either

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 2.09-alt2
- FTBFS (libpcap-1.x finally arrived)
- packaged manpage

* Fri Apr 02 2010 Michael Shigorin <mike@altlinux.org> 2.09-alt1
- 2.09

* Wed Oct 08 2008 Michael Shigorin <mike@altlinux.org> 2.08-alt1
- built for ALT Linux (based on DAG spec for 2.06)

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com>- 2.06-1
- Initial package. (using DAR)
