%define oname openstackclient
%def_with python3

Name: python-module-%oname
Version: 3.8.1
Release: alt1.1
Summary: OpenStack Command-line Client
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

Requires: python-module-cliff >= 2.3.0
Requires: python-module-keystoneauth1 >= 2.18.0
Requires: python-module-openstacksdk >= 0.9.13
Requires: python-module-osc-lib >= 1.2.0
Requires: python-module-oslo.i18n >= 2.1.0
Requires: python-module-oslo.utils >= 3.18.0
Requires: python-module-glanceclient >= 2.5.0
Requires: python-module-keystoneclient >= 3.8.0
Requires: python-module-novaclient >= 6.0.0
Requires: python-module-cinderclient >= 1.6.0

Requires: python-module-neutronclient >= 2.6.0
Requires: python-module-requests >= 2.10.0
Requires: python-module-stevedore >= 1.16.0

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-cliff >= 2.3.0
BuildRequires: python-module-keystoneauth1 >= 2.18.0
BuildRequires: python-module-openstacksdk >= 0.9.13
BuildRequires: python-module-osc-lib >= 1.2.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-glanceclient >= 2.5.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-novaclient >= 6.0.0
BuildRequires: python-module-cinderclient >= 1.6.0
BuildRequires: python-module-neutronclient >= 2.6.0
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-stevedore >= 1.16.0

# for build doc
BuildRequires: python-module-mock
BuildRequires: python-module-requests-mock
BuildRequires: python-module-fixtures
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-os-client-config
BuildRequires: python-module-osprofiler >= 1.4.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-cliff >= 2.3.0
BuildRequires: python3-module-keystoneauth1 >= 2.18.0
BuildRequires: python3-module-openstacksdk >= 0.9.13
BuildRequires: python3-module-osc-lib >= 1.2.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-glanceclient >= 2.5.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-novaclient >= 6.0.0
BuildRequires: python3-module-cinderclient >= 1.6.0
BuildRequires: python3-module-neutronclient >= 2.6.0
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-stevedore >= 1.16.0
%endif

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

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/openstack %buildroot%_bindir/python3-openstack
%endif

%python_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html
sphinx-build -b man doc/source man

install -p -D -m 644 man/openstack.1 %buildroot%_mandir/man1/openstack.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/openstack
%python_sitelibdir/*
%_man1dir/openstack.1*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files doc
%doc html

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-openstack
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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

