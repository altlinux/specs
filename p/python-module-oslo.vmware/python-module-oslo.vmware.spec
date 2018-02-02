%define oname oslo.vmware
%def_with python3

Name: python-module-%oname
Version: 2.17.1
Release: alt1.1
Summary: Oslo VMware library for OpenStack projects
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

Provides: python-module-oslo-vmware = %EVR

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-netaddr >= 0.7.13
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-yaml >= 3.10.0
BuildRequires: python-module-lxml >= 2.3
BuildRequires: python-module-suds-jurko >= 0.6
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-urllib3 >= 1.15.1
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.17.1
BuildRequires: python3-module-netaddr >= 0.7.13
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-yaml >= 3.10.0
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-suds-jurko >= 0.6
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-requests >= 2.8.1
BuildRequires: python3-module-urllib3 >= 1.15.1
BuildRequires: python3-module-lxml >= 2.3

%endif

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Oslo VMware library for OpenStack projects
Group: Development/Python3
Provides: python3-module-oslo-vmware = %EVR

%description -n python3-module-%oname
The oslo.i18n library contain utilities for working with internationalization
(i18n) features, especially translation for text strings in an application
or library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack common VMware library
Group: Development/Documentation

%description doc
Documentation for OpenStack common VMware library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
#rm -rf %oname.egg-info
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

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif


%files
%doc README.rst LICENSE
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%files doc
%doc html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 2.17.1-alt1
- 2.17.1

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.17.0-alt1
- 2.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.14.0-alt1
- 2.14.0

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.21.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.21.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1.21.0-alt1
- 1.21.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.1-alt1
- 0.11.1

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Fri Mar 06 2015 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- initial build
