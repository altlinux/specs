Name: netconsole
Version: 1.0
Release: alt2

Summary: service for logging kernel printk messages over UDP to remote syslog
License: DWTFYWTPL
Group: System/Configuration/Other

BuildArch: noarch

Source1: netconsole.init
Source2: netconsole.sysconfig
Source3: netconsole.service

%description
System administrator can use netconsole service to enable kernel messages
logging to remote syslog daemon.

See http://www.mjmwired.net/kernel/Documentation/networking/netconsole.txt
for details.

%install

mkdir -p %buildroot%_sysconfdir/sysconfig
install -pm640 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%_initdir %buildroot%_unitdir
install -pm755 %SOURCE1 %buildroot%_initdir/%name
install -pm644 %SOURCE3 %buildroot%_unitdir/%name.service

%post
%post_service netconsole

%preun
%preun_service netconsole

%files
%_initdir/netconsole
%_unitdir/netconsole.service
%config(noreplace) %_sysconfdir/sysconfig/netconsole

%changelog
* Tue Sep  1 2015 Terechkov Evgenii <evg@altlinux.org> 1.0-alt2
- Systemd unit file added

* Tue Nov 03 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt1
- Initial build for Sisyphus (initial idea and implementation: thresh@)
