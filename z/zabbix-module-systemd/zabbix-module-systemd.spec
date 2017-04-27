# this is where zabbix agent look for loadable modules:
%define moddir %_libdir/zabbix/modules

%define z_dir %_sysconfdir/zabbix
%define module libzbxsystemd

Name: zabbix-module-systemd
Version: 1.0.0
Release: alt2
Summary: systemd monitoring module for Zabbix

Group: Monitoring
License: GPLv2
URL: https://github.com/cavaliercoder/zabbix-module-systemd
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: zabbix-source libdbus-devel checkpolicy policycoreutils

# we need /etc/zabbix:
Requires: zabbix-common >= 3.2.5-alt2

%description
zabbix-module-systemd is a loadable Zabbix module that enables Zabbix to query
the systemd D-Bus API for native and granular service monitoring.

%prep
%setup
%patch -p1
# fix up FTBFS on non-x86_64:
subst 's|/usr/lib64|%_libdir|g' configure.ac

%build
%autoreconf
%configure --with-zabbix=%_includedir/zabbix
%make_build

%install
%makeinstall_std

%files
%z_dir/zabbix_agentd.conf.d/%module.conf
%moddir/%module.so
%doc README.md

%changelog
* Thu Apr 27 2017 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt2
- Fix FTBFS on non-x86_64
- Update modules path (see ALT#33418)

* Mon Apr 24 2017 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt1
- 1.0.0-4-gf0beaef

* Sun Apr 23 2017 Terechkov Evgenii <evg@altlinux.org> 1.0.0-alt1
- 1.0.0-2-gb8fc86f
