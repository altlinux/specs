%define oname magnumclient

Name:       python-module-%oname
Version:    2.10.0
Release:    alt1
Summary:    Client Library for OpenStack Magnum Container Management API
Group:      Development/Python
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/python-%oname
Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-os-client-config >= 1.28.0
BuildRequires: python-module-osc-lib >= 1.8.0 python-module-osc-lib-tests
BuildRequires: python-module-prettytable >= 0.7.2
BuildRequires: python-module-cryptography >= 2.1
BuildRequires: python-module-decorator >= 3.4.0

# doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-reno
BuildRequires: python-module-openstackdocstheme >= 1.18.1


BuildRequires: python-module-oslo.log
BuildRequires: python-module-argparse
BuildRequires: python-module-mock
BuildRequires: python-module-subunit-tests
BuildRequires: python-module-openstackclient-tests

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-osc-lib >= 1.2.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-cryptography >= 1.0
BuildRequires: python3-module-decorator >= 3.4.0

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
There is a Python library for accessing the API (magnumclient module),
and a command-line script (magnum).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Client Library for OpenStack Magnum Container Management API
Group: Development/Python3

%description -n python3-module-%oname
Client library and command line utility for interacting with Openstack
Magnum API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack Magnum Container Management API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Magnum Container Management API.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_magnumclient.egg-info
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
mv %buildroot%_bindir/magnum %buildroot%_bindir/magnum.py2

pushd ../python3
%python3_install
popd


# Build HTML docs and man page
python3 setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.doctrees /build/sphinx/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/magnum.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/magnum
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE build/sphinx/html

%changelog
* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 2.9.1-alt1
- new version 2.9.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- add test packages

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt0.b1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt0.b1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt0.b1
- Initial release for Sisyphus

