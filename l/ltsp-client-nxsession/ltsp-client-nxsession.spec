Name: ltsp-client-nxsession
Version: 0.2
Release: alt2

Summary: NX session for ALTSP client
License: Public domain
Group: Graphical desktop/Other

Url: http://www.altlinux.org/LTSP/NX
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

# ltsp-client dependency spoils mkimage
AutoReq: no
Requires: nxclient ratpoison procps xinit xsetroot
BuildArch: noarch

%description
This package might be installed into LTSP client chroot
to add "nx" session type.  To make use of it, something
like "SCREEN_08=nx" should be added to default or host
section of chroot's /etc/lts.conf.

%prep
%setup

%install
install -pDm755 start_nx %buildroot%_datadir/ltsp/start_nx
install -pDm755 nx %buildroot%_datadir/ltsp/screen.d/nx
install -pDm600 terminal.nxs %buildroot%_sysconfdir/ltsp/terminal.nxs

%files
%_datadir/ltsp/start_nx
%_datadir/ltsp/screen.d/nx
%config(noreplace) %_sysconfdir/ltsp/terminal.nxs

%changelog
* Mon Mar 15 2010 Michael Shigorin <mike@altlinux.org> 0.2-alt2
- disable automatic requires

* Sun Mar 14 2010 Michael Shigorin <mike@altlinux.org> 0.2-alt1
- renamed from ltsp-nxclient to ltsp-client-nxsession
  (as it happens lav@ has already packaged another implementation
  named exactly the same for M51; both approaches have some pros
  and should be merged someday)

* Sun Mar 14 2010 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release (based on scripts submitted by Mike Grozak)

