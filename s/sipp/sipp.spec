Packager: Denis Smirnov <mithraen@altlinux.ru>

Name: sipp
Version: 3.5.1
Release: alt1

Summary: SIPp -- test tool / traffic generator for the SIP
License: GPL
Group: System/Servers

Url: https://github.com/SIPp/sipp

Source: %name-%version.tar

# Automatically added by buildreq on Tue Dec 08 2015
# optimized out: gnu-config libcom_err-devel libkrb5-devel libstdc++-devel libtinfo-devel pkg-config
BuildRequires: gcc-c++ libgsl-devel liblksctp-devel libncurses-devel libpcap-devel libssl-devel

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
%configure \
  --enable-epoll \
  --with-pcap \
  --with-rtpstream \
  --with-openssl \
  --with-sctp \
  --with-gsl
    

%make_build

%install
install -D sipp %buildroot%_bindir/sipp

%files
%_bindir/sipp

%doc pcap sipp.dtd

%changelog
* Mon Mar 27 2017 Denis Smirnov <mithraen@altlinux.ru> 3.5.1-alt1
- 3.5.1

* Thu Dec 17 2015 Denis Smirnov <mithraen@altlinux.ru> 3.4.1-alt1
- 3.4.1

* Tue Dec 08 2015 Denis Smirnov <mithraen@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Wed Feb 27 2013 Denis Smirnov <mithraen@altlinux.ru> 3.3-alt1
- 3.3

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
