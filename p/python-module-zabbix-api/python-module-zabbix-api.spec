Name: python-module-zabbix-api
Version: 0.1
Release: alt1
Summary: Zabbix API

Group: Development/Python
License: GNU LGPL 2.1
Url: https://github.com/gescheit/scripts

Source: %name-%version.tar
Packager: Evgenii Terechkov <evg@altlinux.org>

BuildArch: noarch
BuildRequires: python-module-setuptools
Requires: python-modules-json

%description
Zabbix API

%prep
%setup

%build
cd zabbix
%python_build

%install
cd zabbix
%python_install

%files
%python_sitelibdir/zabbix_api*
%doc zabbix/README zabbix/examples zabbix/zabbix_rpc_test.py zabbix/zabbix_item_add_example.py

%changelog
* Sat Aug 31 2013 Terechkov Evgenii <evg@altlinux.org> 0.1-alt1
- Initial build for ALT Linux Sisyphus
