Name: sredird
Version: 2.2.2
Release: alt3

Summary: RFC 2217-compliant serial port redirector
License: GPL
Group: Networking/Other

Url: http://www.ibiblio.org/pub/Linux/system/serial
Source0: %url/%name-%version.tar.gz
# Source0-md5:	e541e4b1cb9fa8fc8ff0e76bb1127cda
Source1: sredird.xinetd

Patch1: sredird-2.2.2-Fix-segfault-if-insufficient-arguments-and-some-star.patch
Patch2: sredird-2.2.2-Re-raise-deadly-signals-instead-of-ignoring-them-Clo.patch
Patch3: sredird-2.2.2-rm-termio-h.patch

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
%autopatch -p1

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
* Wed Jun 17 2026 Andrew A. Vasilyev <andy@altlinux.org> 2.2.2-alt3
- NMU: fix FTBFS with new glibc, add patches from Debian

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.2-alt2.qa1
- NMU: rebuilt for debuginfo.

* Mon Jun 25 2007 Michael Shigorin <mike@altlinux.org> 2.2.2-alt2
- added xinetd configuration file, thanks luch@ (#12139)

* Thu Jan 25 2007 Michael Shigorin <mike@altlinux.org> 2.2.2-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- spec cleanup

