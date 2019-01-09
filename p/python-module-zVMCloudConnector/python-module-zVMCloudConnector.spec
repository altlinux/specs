%global oname zVMCloudConnector

Name: python-module-%oname
Version: 1.4.0
Release: alt1
Summary: z/VM cloud management library in Python

Group: Development/Python
License: ASL 2.0
Url: http://github.com/powervm/pypowervm
Source: %oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-jsonschema >= 2.3.0
BuildRequires: python-module-netaddr >= 0.7.5
BuildRequires: python-module-jwt >= 1.0.1
BuildRequires: python-module-requests >= 2.6.0
BuildRequires: python-module-routes >= 2.2
BuildRequires: python-module-webob >= 1.2.3

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-jsonschema >= 2.3.0
BuildRequires: python3-module-netaddr >= 0.7.5
BuildRequires: python3-module-jwt >= 1.0.1
BuildRequires: python3-module-requests >= 2.6.0
BuildRequires: python3-module-routes >= 2.2
BuildRequires: python3-module-webob >= 1.2.3

%description
z/VM cloud connector is a development sdk for manage z/VM.
It provides a set of APIs to operate z/VM including guest, image, network, volume etc.

Just like os-win for nova hyperv driver and oslo.vmware for nova vmware driver,
z/VM cloud connector (zVMCloudConnector) is for nova z/vm driver
and other z/VM related openstack driver such as neutron, ceilometer.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: z/VM cloud management library in Python
Group: Development/Python3

%description -n python3-module-%oname
z/VM cloud connector is a development sdk for manage z/VM.
It provides a set of APIs to operate z/VM including guest, image, network, volume etc.

Just like os-win for nova hyperv driver and oslo.vmware for nova vmware driver,
z/VM cloud connector (zVMCloudConnector) is for nova z/vm driver
and other z/VM related openstack driver such as neutron, ceilometer.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n %oname-%version

# Let RPM handle the dependencies
#rm -f test-requirements.txt requirements.txt

# Remove bundled egg info
rm -rf *.egg-info

cp -fR . ../python3

%build
%python_build


pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
