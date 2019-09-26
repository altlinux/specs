%define  oname oslo.upgradecheck
%define  mname oslo_upgradecheck

Name:    python3-module-%oname
Version: 0.3.2
Release: alt1

Summary: Common code for writing OpenStack upgrade checks

License: MIT
Group:   Development/Python3
URL:     https://github.com/openstack/oslo.upgradecheck

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
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
* Thu Sep 26 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus.
