Packager: Denis Smirnov <mithraen@altlinux.ru>

Name: sipp
Version: 3.2
Release: alt1

Summary: SIPp -- test tool / traffic generator for the SIP
License: GPL
Group: System/Servers

Url: http://sipp.sf.net

Source: %name-%version.tar

# Automatically added by buildreq on Wed Mar 29 2006
BuildRequires: gcc-c++ libncurses-devel libpcap-devel libssl-devel

%description
SIPp is a free Open Source test tool / traffic generator for the SIP
protocol. It includes a few basic SipStone user agent scenarios (UAC
and UAS) and establishes and releases multiple calls with the INVITE
nd BYE methods. It can also reads custom XML scenario files describing
from very simple to complex call flows. It features the dynamic display
of statistics about running tests (call rate, round trip delay, and
message statistics), periodic CSV statistics dumps, TCP and UDP over
multiple sockets or multiplexed with retransmission management and
dynamically adjustable call rates.
emulate live users.

%prep
%setup 

%build
%make_build pcapplay_ossl

%install
install -D sipp %buildroot%_bindir/sipp

%files
%_bindir/sipp

%doc pcap sipp.dtd

%changelog
* Tue Oct 04 2011 Denis Smirnov <mithraen@altlinux.ru> 3.2-alt1
- 3.2

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 3.1-alt3
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 3.1-alt2
- rebuild with new openssl

* Sat Sep 19 2009 Denis Smirnov <mithraen@altlinux.ru> 3.1-alt1
- 3.1

* Wed Mar 29 2006 Denis Smirnov <mithraen@altlinux.ru> 1.1rc5-alt1
- first build for Sisyphus
