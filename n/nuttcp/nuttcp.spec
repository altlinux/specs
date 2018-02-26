Name: nuttcp
Version: 6.1.2
Release: alt2
Summary: TCP/UDP network testing tool 
Group: Monitoring
License: GPLv2
Packager: Andrew Clark <andyc@altlinux.org>
Url: http://www.lcp.nrl.navy.mil/nuttcp/
Source0: http://www.lcp.nrl.navy.mil/nuttcp/%name-%version.tar.bz2
Patch0: xinetd.patch

%description
nuttcp is a network performance measurement tool intended for
use by network and system managers. Its most basic usage is
to determine the raw TCP (or UDP) network layer throughput by
transferring memory buffers from a source system across an
interconnecting network to a destination system, either
transferring data for a specified time interval, or alternatively
transferring a specified number of bytes. In addition to reporting
the achieved network throughput in Mbps, nuttcp also provides
additional useful information related to the data transfer
such as user, system, and wall-clock time, transmitter and
receiver CPU utilization, and loss percentage (for UDP transfers).

%prep
%setup -q
%patch0 -p2

%build
%make 

%install
mkdir -p %buildroot%_bindir
install -pD -m 755 %_builddir/%name-%version/%name-%version %buildroot%_bindir/%name
mkdir -p %buildroot%_man8dir
install -pD -m 644 %_builddir/%name-%version/%name.8 %buildroot%_man8dir/
mkdir -p %buildroot%_sysconfdir/xinetd.d/
install -pD -m 640 %_builddir/%name-%version/xinetd.d/%name %buildroot%_sysconfdir/xinetd.d/

%files
%doc examples.txt LICENSE nuttcp.cat nuttcp.html README
%_bindir/*
%_man8dir/*
%config(noreplace) %_sysconfdir/xinetd.d/%name

%changelog
* Sat Dec 25 2010 Andrew Clark <andyc@altlinux.org> 6.1.2-alt2
- xinet.d path fixes (#24755)

* Fri Dec 11 2009 Andrew Clark <andyc@altlinux.org> 6.1.2-alt1
- initial build for ALT.

