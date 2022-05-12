Name: tcpflow
Version: 1.6.1
Release: alt1

Summary: Network traffic recorder
License: GPLv3
Group: Monitoring
Url: https://github.com/simsong/tcpflow

Source: %name-%version.tar
Source1: control-tcpflow

Requires: %name-control

BuildRequires: gcc-c++ boost-devel libcairo-devel libpcap-devel zlib-devel
BuildRequires: openssl-devel

Provides: tcpflow+ = %EVR
Conflicts: tcpflow+ < %EVR
Obsoletes: tcpflow+

%description
tcpflow is a program that captures data transmitted as part of TCP connections
(flows), and stores the data in a way that is convenient for protocol analysis
or debugging. A program like 'tcpdump' shows a summary of packets seen on the
wire, but usually doesn't store the data that's actually being transmitted. In
contrast, tcpflow reconstructs the actual data streams and stores each flow in
a separate file for later analysis.

%package control
Summary: Network traffic recorder control facility.
Group: Monitoring
Requires: control

%description control
This package contains control rules for tcpflow - network traffic recorder.
See control(8) for details.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
install -pD -m755 %SOURCE1 %buildroot%_controldir/%name
sed -i -e 's:__BINARY__:%_bindir/%name:' %buildroot%_controldir/%name

%pre
i/usr/sbin/groupadd -r -f netadmin ||:
%pre_control %name

%post
%post_control -s restricted %name

%files
%doc AUTHORS COPYING ChangeLog NEWS
%attr(700,root,root) %verify(not mode group) %_bindir/%name
%_man1dir/%name.1*

%files control
%config %_controldir/%name

%changelog
* Thu May 12 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.1-alt1
- 1.6.1 released

* Wed Sep 26 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1
- Updated to upstream version 1.4.5.

* Mon Nov 17 2014 Paul Wolneykien <manowar@altlinux.org> 1.4.4-alt1
- New/alternative tcpflow version. Initial build for ALT Linux.
- Freshed up to v1.4.4 with the help of cronbuild and update-source-functions.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.21-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Sep 02 2008 Afanasov Dmitry <ender@altlinux.org> 0.21-alt1
- initial build

* Thu Apr 22 1999 Ross Golder <rossigee@bigfoot.com>
- Wrote for version 0.12

