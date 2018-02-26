Name: tcptrace
Version: 6.6.7
Release: alt3

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Tool for analysis of TCP dump files
License: GPLv2+
Group: Monitoring

URL: http://www.tcptrace.org/
Source0: http://www.tcptrace.org/download/tcptrace-%version.tar.gz
Patch0: http://ftp.de.debian.org/debian/pool/main/t/tcptrace/tcptrace_6.6.7-3.diff.gz

# Automatically added by buildreq on Thu Feb 26 2009
BuildRequires: flex libpcap-devel

%description
tcptrace is a tool for analysis of TCP dump files. It can take as input the
files produced by several popular packet-capture programs, including tcpdump,
snoop, etherpeek, HP Net Metrix, and WinDump. tcptrace can produce several
different types of output containing information on each connection seen, such
as elapsed time, bytes and segments sent and recieved, retransmissions, round
trip times, window advertisements, throughput, and more. It can also produce a
number of graphs for further analysis.

%prep
%setup
%patch0 -p1

%build
%configure
# Needed define was not added on x86_64 due to naive libc version check
# (test for file in /lib (sic!) directory). Just add this define explicitly:
%make_build CCOPT="-D_BSD_SOURCE %optflags"

%install
install -d %buildroot%_bindir
install -p -m755 tcptrace xpl2gpl %buildroot%_bindir
install -pD -m644 tcptrace.man %buildroot%_man1dir/tcptrace.1

%files
%doc README.xpl2gpl
%_bindir/*
%_man1dir/*

%changelog
* Wed Mar 10 2010 Victor Forsiuk <force@altlinux.org> 6.6.7-alt3
- Added fix to get package built on x86_64.

* Thu Oct 27 2005 Victor Forsyuk <force@altlinux.ru> 6.6.7-alt2
- Fix compile error with flex 2.5.31.

* Tue Jan 04 2005 Victor Forsyuk <force@altlinux.ru> 6.6.7-alt1
- New version.

* Thu May 13 2004 Victor Forsyuk <force@altlinux.ru> 6.6.1-alt1
- Initial build for Sisyphus.
