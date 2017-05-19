# this is where zabbix agent look for loadable modules:
%define moddir %_libdir/zabbix/modules

%define z_dir %_sysconfdir/zabbix
%define zlm_dir %z_dir/libzbxmodbus

Name: libzbxmodbus
Version: 0.5
Release: alt3
Summary: Loadable module to integrate Modbus (RTU and TCP) into Zabbix

Group: Monitoring
License: GPLv2
Url: https://github.com/v-zhuravlev/libzbxmodbus
Source0: %name-%version.tar
Patch0: %name-%version.patch

BuildRequires: zabbix-source >= 3.2.0 libmodbus-devel >= 3.1.1

# we need /etc/zabbix:
Requires: zabbix-common >= 3.2.5-alt2

%description
Loadable module to integrate Modbus (RTU and TCP) protocol into Zabbix

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure --enable-zabbix-3.2
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%moddir %buildroot%zlm_dir %buildroot%z_dir/zabbix_agentd.conf.d

echo "LoadModule=libzbxmodbus.so" > %buildroot%z_dir/zabbix_agentd.conf.d/%name.conf

mv %buildroot%_libdir/*.so %buildroot%moddir

%files
%z_dir/zabbix_agentd.conf.d/%name.conf
%dir %zlm_dir
%moddir/*.so

%doc README.md

%changelog
* Fri May 19 2017 Terechkov Evgenii <evg@altlinux.org> 0.5-alt3
- Update modules path

* Fri Jan 27 2017 Terechkov Evgenii <evg@altlinux.org> 0.5-alt2
- Build with zabbix 3.2

* Mon Nov 21 2016 Terechkov Evgenii <evg@altlinux.org> 0.5-alt1
- Initial build for ALT Linux Sisyphus
- v0.5-1-gaa2a57f
