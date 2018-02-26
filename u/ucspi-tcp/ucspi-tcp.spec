Name: ucspi-tcp
Version: 0.88
Release: alt1

Summary: partial replacement for inetd+tcpd
License: Public domain
Group: System/Configuration/Networking
Url: http://cr.yp.to/%name.html

Source: http://cr.yp.to/%name/%name-%version.tar
Packager: Boris Gulay <boresexpress@altlinux.org>

Patch: %name-%version.errno.patch
Patch1: %name-%version.nobase.patch
Patch2: %name-%version.a_record.patch
Patch3: %name.check.setgroup.patch
Patch4: %name.HOME.patch

%description
tcpserver and tcpclient are easy-to-use command-line tools for building
TCP client-server applications.

tcpserver waits for incoming connections and, for each connection, runs
a program of your choice. Your program receives environment variables
showing the local and remote host names, IP addresses, and port numbers.

tcpserver offers a concurrency limit to protect you from running out of
processes and memory. When you are handling 40 (by default) simultaneous
connections, tcpserver smoothly defers acceptance of new connections.

tcpserver also provides TCP access control features, similar to
tcp-wrappers/tcpd\'s hosts.allow but much faster. Its access control
rules are compiled into a hashed format with cdb, so it can easily deal
with thousands of different hosts.

This package includes a recordio tool that monitors all the input and
output of a server.

tcpclient makes a TCP connection and runs a program of your choice. It
sets up the same environment variables as tcpserver.

This package includes several sample clients built on top of tcpclient:
who@, date@, finger@, http@, tcpcat, and mconnect.

tcpserver and tcpclient conform to UCSPI, the UNIX Client-Server Program
Interface, using the TCP protocol. UCSPI tools are available for several
different networks.

This rpm applies the following patches:

0: errno; to correct an incompatibility in errno declaration
1: nobase; the default rbl base is not avaialble noncommercially anymore
2: a_record; many rbl databases provide now A records instead of txt

%prep
%setup
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p2

%build
%make_build prog

%install
for F in tcpserver tcprules tcprulescheck argv0 recordio tcpclient who@ date@ finger@ http@ tcpcat mconnect mconnect-io addcr delcr fixcrio rblsmtpd
do
	install -Dp -m 755 $F %buildroot%_bindir/$F
done

%files
%doc TODO VERSION CHANGES README*
%_bindir/tcpserver
%_bindir/tcprules
%_bindir/tcprulescheck
%_bindir/argv0
%_bindir/recordio
%_bindir/tcpclient
%_bindir/who@
%_bindir/date@
%_bindir/finger@
%_bindir/http@
%_bindir/tcpcat
%_bindir/mconnect
%_bindir/mconnect-io
%_bindir/addcr
%_bindir/delcr
%_bindir/fixcrio
%_bindir/rblsmtpd

%changelog
* Sat Jan 23 2010 Boris Gulay <boresexpress@altlinux.org> 0.88-alt1
- first build for ALT Linux
