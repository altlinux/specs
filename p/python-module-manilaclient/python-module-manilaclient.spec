%define oname manilaclient

Name:       python-module-%oname
Version:    1.24.1
Release:    alt1
Summary:    Client Library for OpenStack Manila shared file system service API
License:    ASL 2.0
Group:      Development/Python
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-ipaddress >= 1.0.17
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-simplejson >= 3.5.1
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-docutils >= 0.11

# BuildRequires: python-module-openstackclient >= 3.12.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-docutils >= 0.11

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
There is a Python library for accessing the API (manilaclient module),
and a command-line script (manilac).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Client Library for OpenStack  Manila shared file system service API
Group: Development/Python3

%description -n python3-module-%oname
Client library and command line utility for interacting with Openstack
Manila API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack  Manila shared file system service API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Manila shared file system service API.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py


rm -rf ../python3
cp -a . ../python3


%build
%python_build

pushd ../python3
%python3_build
popd


%install
%python_install
mv %buildroot%_bindir/manila %buildroot%_bindir/manila.py2

pushd ../python3
%python3_install
popd

# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/manila.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/manila
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.24.1-alt1
- 1.24.1

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.21.0-alt1
- new version 1.21.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.14.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- Initial release for Sisyphus
