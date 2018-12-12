%define oname openstackclient

Name: python-module-%oname
Version: 3.16.2
Release: alt1
Summary: OpenStack Command-line Client
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

Requires: python-module-cliff >= 2.3.0
Requires: python-module-keystoneauth1 >= 3.4.0
Requires: python-module-openstacksdk >= 0.11.2
Requires: python-module-osc-lib >= 1.10.0
Requires: python-module-oslo.i18n >= 3.15.3
Requires: python-module-oslo.utils >= 3.33.0
Requires: python-module-glanceclient >= 2.8.0
Requires: python-module-keystoneclient >= 3.17.0
Requires: python-module-novaclient >= 9.1.0
Requires: python-module-cinderclient >= 3.3.0
Requires: python-module-neutronclient >= 6.7.0
Requires: python-module-requests >= 2.10.0
Requires: python-module-stevedore >= 1.16.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-cliff >= 2.8.0
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-openstacksdk >= 0.11.2
BuildRequires: python-module-osc-lib >= 1.10.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-glanceclient >= 2.8.0
BuildRequires: python-module-keystoneclient >= 3.17.0
BuildRequires: python-module-novaclient >= 9.1.0
BuildRequires: python-module-cinderclient >= 3.3.0
BuildRequires: python-module-neutronclient >= 6.7.0
BuildRequires: python-module-requests >= 2.14.2
BuildRequires: python-module-stevedore >= 1.20.0

# for build doc
BuildRequires: python-module-sphinx
BuildRequires: python-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1

BuildRequires: python-module-mock
BuildRequires: python-module-requests-mock
BuildRequires: python-module-fixtures
BuildRequires: python-module-os-client-config >= 1.28.0
BuildRequires: python-module-osprofiler >= 1.4.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-openstacksdk >= 0.11.2
BuildRequires: python3-module-osc-lib >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-glanceclient >= 2.8.0
BuildRequires: python3-module-keystoneclient >= 3.17.0
BuildRequires: python3-module-novaclient >= 9.1.0
BuildRequires: python3-module-cinderclient >= 3.3.0
BuildRequires: python3-module-neutronclient >= 6.7.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-stevedore >= 1.20.0


# for build doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

BuildRequires: python3-module-mock
BuildRequires: python3-module-requests-mock
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-osprofiler >= 1.4.0

%description
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Client
Group: Development/Documentation

%description doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

This package contains auto-generated documentation.

%package -n python3-module-%oname
Summary: OpenStack Command-line Client
Group: Development/Python3

%description -n python3-module-%oname
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.


%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n python-%oname-%version

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf requirements.txt test-requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/openstack %buildroot%_bindir/openstack.py2

pushd ../python3
%python3_install
popd



export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/openstack.1 %buildroot%_mandir/man1/openstack.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/openstack.py2
%python_sitelibdir/*
%_man1dir/openstack.1*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files doc
%doc html

%files -n python3-module-%oname
%_bindir/openstack
%_man1dir/openstack.1*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 3.16.2-alt1
- 3.16.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.8.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 3.8.1-alt1
- 3.8.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 3.2.0-alt1
- 3.2.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.7.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.1-alt1
- 1.7.1
- add python3 package

* Wed Aug 26 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- Initial package

