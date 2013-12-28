Summary: tool to ascii-print or forward sFlow datagrams
Name: sflowtool
Version: 3.30
Release: alt1
License: http://www.inmon.com/technology/sflowlicense.txt
Group: Monitoring
URL: http://inmon.com/technology/sflowTools.php
Source: http://inmon.com/bin/sflowtool-%{version}.tar.gz

%description
The sFlow toolkit provides command line utilities and scripts for analyzing
sFlow data. sflowtool interfaces to utilities such as tcpdump, Wireshark and Snort
for detailed packet tracing and analysis, NetFlow compatible collectors for IP
flow accounting, and provides text based output that can be used in scripts to
provide customized analysis and reporting and for integrating with other tools
such as Graphite or rrdtool.

%prep

%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%doc AUTHORS INSTALL NEWS ChangeLog README scripts

%changelog
* Sat Dec 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 3.30-alt1
- New version

* Sun Oct 14 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.28-alt1
- New version

* Mon Jul 23 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 3.27-alt1
- Build for ALT
