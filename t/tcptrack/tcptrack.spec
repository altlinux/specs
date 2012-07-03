Name: tcptrack
Version: 1.4.2
Release: alt1

Summary: A packet sniffer which displays TCP information like the 'top' command
License: GPLv2+
Group: Security/Networking

URL: http://www.rhythm.cx/~steve/devel/tcptrack
Source: http://www.rhythm.cx/~steve/devel/tcptrack/release/%version/source/%name-%version.tar.gz

# Automatically added by buildreq on Wed Oct 13 2010
BuildRequires: gcc-c++ libncurses-devel libpcap-devel

%description 
tcptrack is a sniffer which displays information about TCP connections it
sees on a network interface. It passively watches for connections on the
network interface, keeps track of their state and displays a list of
connections in a manner similar to the unix 'top' command. It displays
source and destination addresses and ports, connection state, idle time,
and bandwidth usage.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/tcptrack
%_man1dir/tcptrack.*

%changelog
* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 1.4.2-alt1
- 1.4.2

* Wed Oct 13 2010 Victor Forsiuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Wed Dec 17 2008 Sergei Epiphanov <serpiph@altlinux.ru> 1.3.0-alt3
- Fix build with gcc 4.3

* Mon Dec 15 2008 Victor Forsyuk <force@altlinux.org> 1.3.0-alt2
- Fix FTBFS with gcc43.

* Tue Jul 22 2008 Sergei Epiphanov <serpiph@altlinux.ru> 1.3.0-alt1
- New version

* Sat Jul 21 2007 Sergei Epiphanov <serpiph@altlinux.ru> 1.2.0-alt1
- Build for Sisyphus
