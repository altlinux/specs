%global oname zVMCloudConnector

Name: python3-module-%oname
Version: 1.4.0
Release: alt2.1
Summary: z/VM cloud management library in Python

Group: Development/Python3
License: Apache-2.0
Url: https://pypi.org/project/zVMCloudConnector
Source: %oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-jsonschema >= 2.3.0
BuildRequires: python3-module-netaddr >= 0.7.5
BuildRequires: python3-module-jwt >= 1.0.1
BuildRequires: python3-module-requests >= 2.6.0
BuildRequires: python3-module-routes >= 2.2
BuildRequires: python3-module-webob >= 1.2.3

%add_python3_self_prov_path %buildroot%python3_sitelibdir/zvmsdk/dist.py

%description
z/VM cloud connector is a development sdk for manage z/VM.
It provides a set of APIs to operate z/VM including guest, image, network, volume etc.

Just like os-win for nova hyperv driver and oslo.vmware for nova vmware driver,
z/VM cloud connector (zVMCloudConnector) is for nova z/vm driver
and other z/VM related openstack driver such as neutron, ceilometer.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
#rm -f test-requirements.txt requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.0-alt2.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Jun 02 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt2
- Drop python2 support.
- Fix url tag.
- Fix license tag.

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
