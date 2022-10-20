%define _unpackaged_files_terminate_build 1

Name: netconsole
Version: 1.1
Release: alt1

Summary: service for logging kernel printk messages over UDP to remote syslog
License: WTFPL
Group: System/Configuration/Other
Url: https://www.altlinux.org/Netconsole

BuildArch: noarch

Source1: netconsole.init
Source2: netconsole.sysconfig
Source3: netconsole.service
Source4: netconsole-setup

%{?!_without_check:%{?!_disable_check:
BuildRequires: systemd-analyze
}}

%description
System administrator can use netconsole service to enable kernel messages
logging to remote syslog daemon.

See https://www.kernel.org/doc/Documentation/networking/netconsole.txt
for details.

%install
mkdir -p %buildroot%_sysconfdir/sysconfig
install -pm640 %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%_initdir %buildroot%_unitdir
install -pm755 %SOURCE1 %buildroot%_initdir/%name
install -pm644 %SOURCE3 %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_sbindir
install -Dpm755 %SOURCE4 %buildroot%_sbindir/netconsole-setup

%check
systemd-analyze verify %buildroot%_unitdir/%name.service
bash -n %buildroot%_initdir/%name
bash -n %buildroot%_sysconfdir/sysconfig/%name
bash -n %buildroot%_sbindir/netconsole-setup

%triggerin -- %name < 1.1
sed -i 's/^DEV=/SRCDEV=/' %_sysconfdir/sysconfig/%name

%post
%post_service netconsole

%preun
%preun_service netconsole

%files
%_sbindir/netconsole-setup
%_initdir/netconsole
%_unitdir/netconsole.service
%config(noreplace) %_sysconfdir/sysconfig/netconsole

%changelog
* Thu Oct 20 2022 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- spec: Fix License tag and update link in description.
- Streamline netconsole initialization.
- Add netconsole-setup helper tool.
- Update systemd service to start after network is up.

* Tue Sep  1 2015 Terechkov Evgenii <evg@altlinux.org> 1.0-alt2
- Systemd unit file added

* Tue Nov 03 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.0-alt1
- Initial build for Sisyphus (initial idea and implementation: thresh@)
