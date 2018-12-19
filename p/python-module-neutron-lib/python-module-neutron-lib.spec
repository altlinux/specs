%define oname neutron-lib

Name: python-module-%oname
Version: 1.18.0
Release: alt1
Summary: OpenStack Neutron shared routines and utilities
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-pecan >= 1.0.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-oslo.concurrency >= 3.26.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.context >= 2.19.2
BuildRequires: python-module-oslo.db >= 4.27.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.messaging >= 5.29.0
BuildRequires: python-module-oslo.policy >= 1.30.0
BuildRequires: python-module-oslo.service >= 1.24.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python-module-osprofiler >= 1.4.0
BuildRequires: python-module-webob >= 1.7.1
BuildRequires: python-module-weakrefmethod >= 1.0.2

# doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-os-api-ref >= 1.4.0
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-mock >= 2.0.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-pecan >= 1.0.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.db >= 4.27.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.policy >= 1.30.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.31.2
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-webob >= 1.7.1

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-os-api-ref >= 1.4.0
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-mock >= 2.0.0

%description
Neutron-lib is an OpenStack library project used by Neutron, Advanced Services,
and third-party projects to provide common functionality and remove duplication.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack Neutron shared routines and utilities
Group: Development/Python3

%description -n python3-module-%oname
Neutron-lib is an OpenStack library project used by Neutron, Advanced Services,
and third-party projects to provide common functionality and remove duplication.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Neutron shared routines and utilities
Group: Development/Documentation

%description doc
Documentation for OpenStack Neutron shared routines and utilities

%prep
%setup -n %oname-%version

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

# generate html docs
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc AUTHORS ChangeLog README.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/neutron_lib/fixture.py

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/neutron_lib/fixture.py

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/neutron_lib/fixture.py

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/neutron_lib/fixture.py

%files doc
%doc build/sphinx/html

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.18.0-alt1
- 1.18.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- add test packages

* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Fri Apr 15 2016 Alexey Shabalin <shaba@altlinux.ru> 0.0.1-alt1
- Initial package.
