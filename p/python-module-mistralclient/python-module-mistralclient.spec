
%define oname mistralclient

Name:       python-module-%oname
Version:    3.7.0
Release:    alt1
Summary:    Client Library for OpenStack Mistral Workflow Service API
License:    ASL 2.0
Group:      Development/Python
Url:        http://docs.openstack.org/developer/python-%oname
Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-stevedore >= 1.20.0

BuildRequires: python-module-oslotest >= 3.2.0
BuildRequires: python-module-requests-mock >= 1.2.0
BuildRequires: python-module-osprofiler >= 1.4.0
BuildRequires: python-module-tempest

# doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0

BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-tempest

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
There is a Python library for accessing the API (mistralclient module),
and a command-line script (mistral).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Client Library for OpenStack Mistral Workflow Service API
Group: Development/Python3

%description -n python3-module-%oname
Client library and command line utility for interacting with Openstack
MistralAPI.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Mistral Workflow Service API
Group:  Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Mistral Workflow Service API.

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

# Prevent doc build warnings from causing a build failure
sed -i '/warning-is-error/d' setup.cfg

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/mistral %buildroot%_bindir/mistral.py2

pushd ../python3
%python3_install
popd

# Build HTML docs and man page
python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/mistral.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/mistral
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE doc/build/html

%changelog
* Tue Dec 11 2018 Alexey Shabalin <shaba@altlinux.org> 3.7.0-alt1
- 3.7.0

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- new version 3.3.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 3.0.0-alt1
- 3.0.0
- add test packages

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- Initial release for Sisyphus
