%define  oname oslo.upgradecheck
%define  mname oslo_upgradecheck

Name:    python3-module-%oname
Version: 1.0.1
Release: alt1

Summary: Common code for writing OpenStack upgrade checks

License: MIT
Group:   Development/Python3
URL:     https://github.com/openstack/oslo.upgradecheck

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr

BuildArch: noarch

Source:  %mname-%version.tar

%description
%summary

%prep
%setup -n %mname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%mname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.
- Renamed spec file.

* Thu Sep 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus.
