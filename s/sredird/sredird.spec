Name: sredird
Version: 2.2.2
Release: alt2

Summary: RFC 2217-compliant serial port redirector
License: GPL
Group: Networking/Other

Url: http://www.ibiblio.org/pub/Linux/system/serial
Source0: %url/%name-%version.tar.gz
# Source0-md5:	e541e4b1cb9fa8fc8ff0e76bb1127cda
Source1: sredird.xinetd
Packager: Michael Shigorin <mike@altlinux.org>

Summary(pl):	Program przekierowuj±cy port szeregowy zgodny z RFC 2217

%description
sredird is a serial port redirector that is compliant with the RFC
2217 "Telnet Com Port Control Option" protocol. This protocol lets you
share a serial port through the network.

%description -l pl
sredird jest programem przekierowuj±cym port szeregowy zgodnym z RFC
2217 (Telnet Com Port Control Option protocol). Protokó³ ten pozwala
na udostêpnianie portu szeregowego przez sieæ.

%prep
%setup -q

%build
%make_build

%install
install -pD -m755 %name %buildroot%_sbindir/%name
install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/xinetd.d/sredir-tcp

%files
%_sbindir/%name
%_sysconfdir/xinetd.d/sredir-tcp
%doc README

%changelog
* Mon Jun 25 2007 Michael Shigorin <mike@altlinux.org> 2.2.2-alt2
- added xinetd configuration file, thanks luch@ (#12139)

* Thu Jan 25 2007 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- spec cleanup

