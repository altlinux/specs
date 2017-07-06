# this is where zabbix agent look for loadable modules:
%define moddir %_libdir/zabbix/modules

%define z_dir %_sysconfdir/zabbix
%define module libzbxsockets

Name: zabbix-module-sockets
Version: 1.1.0
Release: alt2
Summary: A Zabbix loadable module to monitor Linux Sockets

Group: Monitoring
License: GPLv2
URL: https://github.com/cavaliercoder/zabbix-module-sockets
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: zabbix-source libdbus-devel checkpolicy policycoreutils

# we need /etc/zabbix:
Requires: zabbix-common >= 3.2.5-alt2

%description
zabbix-module-sockets is a loadable Zabbix module that enables Zabbix to monitor
the state of sockets on Linux systems.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --with-zabbix=%_includedir/zabbix
%make_build

%install
%makeinstall_std

%files
%z_dir/zabbix_agentd.conf.d/%module.conf
%moddir/%module.so
%doc README.md templates/*.xml

%changelog
* Thu Jul  6 2017 Terechkov Evgenii <evg@altlinux.org> 1.1.0-alt2
- v1.1.0-5-g9aa69e6

* Sat Jun 24 2017 Terechkov Evgenii <evg@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux Sisyphus
