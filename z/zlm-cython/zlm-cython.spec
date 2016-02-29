# this is where zabbix agent look for loadable modules:
%define moddir %_libdir/modules

%define z_dir %_sysconfdir/zabbix
%define zlm_dir %z_dir/zlm-cython

Name: zlm-cython
Version: 0.1
Release: alt2
Summary: Zabbix Loadable Module which embedding Python interpreter in Zabbix server proxy or an agent

Group: Development/Python
License: GPLv2
Url: https://github.com/vulogov/zlm-cython
Source0: %name-%version.tar
Patch0: %name-alt.patch

BuildRequires: python-dev python-module-Cython zabbix-source libxml2-devel libelf-devel libcurl-devel libnet-snmp-devel

# we need /etc/zabbix:
Requires: zabbix-common

%description
ZLM-python is a Zabbix Loadable Module which embedding Python
interpreter in Zabbix server proxy or an agent. You can create the
snippets of the Python code, which will be executed inside the Zabbix
execution context, giving you access to internal Zabbix core functions
and serious performance gain.

%prep
%setup
%patch0 -p1

cd src
./BUILD.sh

%build

%install
mkdir -p %buildroot%moddir %buildroot%zlm_dir %buildroot%z_dir/zabbix_agentd.conf.d
cd src
install -pm 644 zlm_python.so %buildroot%moddir/zlm_python.so
touch %buildroot%zlm_dir/zlm_python.ini
install -pm 644 python.cfg %buildroot%moddir/python.cfg
ln -sf "../../..%zlm_dir/pymodules" %buildroot%moddir/pymodules
ln -sf "../../..%zlm_dir/pydaemons" %buildroot%moddir/pydaemons
ln -sf "../../..%zlm_dir/zlm_python.ini" %buildroot%moddir/zlm_python.ini
cp -var pydaemons %buildroot%zlm_dir
cp -var pymodules %buildroot%zlm_dir

echo "LoadModule=zlm_python.so" > %buildroot%z_dir/zabbix_agentd.conf.d/%name.conf

%files
%z_dir/zabbix_agentd.conf.d/%name.conf
%dir %zlm_dir
%dir %zlm_dir/pydaemons
%dir %zlm_dir/pymodules
%dir %zlm_dir/pymodules/lib
%config(noreplace) %zlm_dir/zlm_python.ini
%zlm_dir/py*/*.py
%zlm_dir/py*/lib/*.py
%moddir/*

%doc ROADMAP.md README.md doc/*.pdf

%changelog
* Mon Feb 29 2016 Terechkov Evgenii <evg@altlinux.org> 0.1-alt2
- git-20160229 (with experimental fix for https://github.com/vulogov/zlm-cython/issues/4)

* Thu Feb 25 2016 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
