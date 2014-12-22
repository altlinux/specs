Name: servicectl
Version: 1.0
Release: alt2

Summary: Control systemd services in chroot environment
License: GPL
Group: System/Configuration/Boot and Init

Url: https://github.com/smaknsk/servicectl
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch

%define servicedir %_sysconfdir/servicectl

%description
Servicectl is a shell script to start/stop services on linux hosts
using systemd in chroot and SysVinit outside the chroot environment.
It uses systemd service files, e.g. nginx.service.

%prep
%setup
sed -i -e 's,^\(SYSTEMD_UNITS_PATH=\).*,\1/lib/systemd/system/,' \
       -e 's,^DIR=.*$,DIR=%servicedir,' servicectl serviced

%build

%install
install -pDm755 servicectl %buildroot%_sbindir/servicectl
install -pDm755 serviced   %buildroot%_sbindir/serviced
mkdir -p %buildroot%servicedir/enabled

%files
%servicedir/enabled
%_sbindir/*
%doc README*

%changelog
* Mon Dec 22 2014 Michael Shigorin <mike@altlinux.org> 1.0-alt2
- noarch indeed

* Mon Dec 22 2014 Michael Shigorin <mike@altlinux.org> 1.0-alt1
- built for ALT Linux

