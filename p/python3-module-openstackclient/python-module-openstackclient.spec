%define oname openstackclient

%def_without docs

Name: python3-module-%oname
Version: 4.0.0
Release: alt2

Summary: OpenStack Command-line Client

Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-keystoneauth1 >= 3.6.2
BuildRequires: python3-module-openstacksdk >= 0.17.0
BuildRequires: python3-module-osc-lib >= 1.14.0
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
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for OpenStack Client
Group: Development/Documentation

%description doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

This package contains auto-generated documentation.
%endif

%prep
%setup -n python-%oname-%version

# We handle requirements ourselves, pkg_resources only bring pain
rm -rf requirements.txt test-requirements.txt

# Remove bundled egg-info
rm -rf *.egg-info

%build
%python3_build

%install
%python3_install

%if_with docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 -b html doc/source html
sphinx-build-3 -b man doc/source man

#install -p -D -m 644 man/openstack.1 %buildroot%_mandir/man1/openstack.1

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo
%endif

%files
%doc LICENSE README.rst
%_bindir/openstack
#%%_man1dir/openstack.1*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc html
%endif

%changelog
* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Build without docs.

* Fri Nov 01 2019 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- new version 4.0.0
- Build without python2.

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

