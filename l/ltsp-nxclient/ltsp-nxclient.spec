Name: ltsp-nxclient
Version: 0.1
Release: alt1

Summary: NXClient support for LTSP

License: Public Domain
Group: Development/Other
Url: http://wiki.etersoft.ru/RX

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define screendir %_datadir/ltsp/screen.d

# git-clone http://git.altlinux.org/people/lav/packages/ltsp-nxclient.git
# git-clone http://git.etersoft.ru/people/lav/packages/ltsp-nxclient.git
Source: %name-%version.tar

BuildArchitectures: noarch

Requires: nxclient

%description
This package contains LTSP module for support NXClient.

%prep
%setup

%install
mkdir -p %buildroot%screendir
install -m 644 nxclient nxclientx %buildroot%screendir/

%files
%_datadir/ltsp/screen.d/

%changelog
* Wed Sep 23 2009 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

