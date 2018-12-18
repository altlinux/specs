%define oname os-vif

%def_with docs

Name: python-module-%oname
Version: 1.11.1
Release: alt1
Summary: A library for plugging and unplugging virtual interfaces in OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/os_vif-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-netaddr >= 0.7.18
BuildRequires: python-module-oslo.concurrency >= 3.20.0
BuildRequires: python-module-oslo.config >= 5.1.0
BuildRequires: python-module-oslo.log >= 3.30.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.privsep >= 1.23.0
BuildRequires: python-module-oslo.versionedobjects >= 1.28.0
BuildRequires: python-module-pyroute2 >= 0.4.21
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-stevedore >= 1.20.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-openstackdocstheme


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-oslo.concurrency >= 3.20.0
BuildRequires: python3-module-oslo.config >= 5.1.0
BuildRequires: python3-module-oslo.log >= 3.30.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.privsep >= 1.23.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.28.0
BuildRequires: python3-module-pyroute2 >= 0.4.21
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme

%description
A library for plugging and unplugging virtual interfaces in OpenStack.
Features:
- A base VIF plugin class that supplies a plug() and unplug() interface
- Versioned objects that represent a virtual interface and its components

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack %oname library
Group: Development/Documentation

%description doc
Documentation for OpenStack %oname library

%package -n python3-module-%oname
Summary: A library for plugging and unplugging virtual interfaces in OpenStack
Group: Development/Python3

%description -n python3-module-%oname
A library for plugging and unplugging virtual interfaces in OpenStack.
Features:
- A base VIF plugin class that supplies a plug() and unplug() interface
- Versioned objects that represent a virtual interface and its components

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n os_vif-%version
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%if_with docs
python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.buildinfo
%endif

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with docs
%files doc
%doc README.rst build/sphinx/html
%endif

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- 1.11.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- Initial packaging
