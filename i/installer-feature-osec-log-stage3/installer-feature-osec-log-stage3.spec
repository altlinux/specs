Name: installer-feature-osec-log-stage3
Version: 0.1
Release: alt1

Summary: Installer stage3 osec hook
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
Packager: Mikhail Efremov <sem@altlinux.org>
BuildArch: noarch
Requires: alterator-logs osec-mailreport
Source: %name-%version.tar

%description
This package contains installer stage3 hook for
enabling osec's log.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri Feb 19 2010 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build
