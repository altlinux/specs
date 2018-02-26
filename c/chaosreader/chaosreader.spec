Summary: Tool to fetch application data from snoop or tcpdump logs.
Name: chaosreader
Version: 0.94
Release: alt1
License: GPL
Group: Networking/Other
Packager: Boris Savelev <boris@altlinux.org>
Url: http://chaosreader.sourceforge.net
Source: http://download.sourceforge.net/sourceforge/chaosreader/%name%version

%description
Chaosreader is a freeware tool to fetch application data from snoop or tcpdump logs.
Supported protocols include TCP, UDP, IPv4, IPv6, ICMP, telnet, FTP, HTTP, SMTP, IRC, X11, VNC, etc
%prep

%install
mkdir -p %buildroot/%_bindir
install -m755 %SOURCE0 %buildroot/%_bindir/%name

%files
%_bindir/*

%changelog
* Tue Mar 10 2009 Boris Savelev <boris@altlinux.org> 0.94-alt1
- initial build

