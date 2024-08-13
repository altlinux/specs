Name:    netbox-config-backup
Version: 2.0.1
Release: alt1

Summary: A configuration backup system using napalm
License: Apache-2.0
Group:   Networking/WWW
URL:     https://github.com/DanSheps/netbox-config-backup

AutoReqProv: yes, nopython

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
Requires: netbox
Requires: netbox-napalm-plugin
Requires: python3-module-dulwich
Requires: python3-module-napalm
Requires: python3-module-pydriller
Requires: python3-module-deepdiff

BuildArch: noarch

Source: %name-%version.tar
Source1: README
Source2: ncb-rq@.service

%description
A configuration backup system using netbox and napalm to backup devices into
a git repository.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_datadir/netbox
mkdir -p %buildroot%_datadir/netbox/netbox_config_backup
mv %buildroot%python3_sitelibdir/netbox_config_backup/* %buildroot%_datadir/netbox/netbox_config_backup
mkdir -p %buildroot%_defaultdocdir/netbox-config-backup
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/netbox-config-backup/README
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/ncb-rq@.service

%files
%_unitdir/ncb-rq@.service
%_datadir/netbox/netbox_config_backup
%_defaultdocdir/netbox-config-backup/README
%python3_sitelibdir/netbox_config_backup-%version.dist-info

%changelog
* Tue Aug 13 2024 Alexander Burmatov <thatman@altlinux.org> 2.0.1-alt1
- New 2.0.1 version.

* Mon May 20 2024 Alexander Burmatov <thatman@altlinux.org> 1.5.5-alt1
- New 1.5.5 version.

* Tue Mar 26 2024 Alexander Burmatov <thatman@altlinux.org> 1.5.4-alt1
- New 1.5.4 version.

* Thu Dec 14 2023 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt3
- Remove RuntimeDirectory from service file.

* Thu Dec 07 2023 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt2
- Fix service file.

* Sat Nov 11 2023 Alexander Burmatov <thatman@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.
