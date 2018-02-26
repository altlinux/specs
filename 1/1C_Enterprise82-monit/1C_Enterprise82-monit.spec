Name: 1C_Enterprise82-monit
Version: 0.1
Release: alt1

Summary: Monit file for 1C Enterprise 8.2
Group: Networking/WWW
License: GPL

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

Requires: monit

BuildArch: noarch

%description
Monit file for 1C Enterprise 8.2

%prep
%setup

%install
mkdir -p %buildroot%_sysconfdir/monitrc.d/
install -m644 monitrc.d/* %buildroot%_sysconfdir/monitrc.d/

%files
%_sysconfdir/monitrc.d/*

%changelog
* Fri Mar 23 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus

