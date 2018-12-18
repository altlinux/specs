%global oname oslo.messaging

Name:       python-module-%oname
Epoch:      1
Version:    8.1.2
Release:    alt1
Summary:    OpenStack common messaging library

Group:      Development/Python
License:    ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

Provides:  python-module-oslo-messaging = %EVR
Obsoletes: python-module-oslo-messaging < %EVR
BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-futurist >= 1.2.0
BuildRequires: python-module-oslo.config >= 5.2.0
BuildRequires: python-module-oslo.context >= 2.9.0
BuildRequires: python-module-oslo.log >= 3.36.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.service >= 1.24.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-stevedore >= 1.20.0
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-monotonic >= 0.6
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-cachetools >= 2.0.0
BuildRequires: python-module-webob >= 1.7.1
BuildRequires: python-module-yaml >= 3.12
BuildRequires: python-module-amqp >= 1:2.3.0
BuildRequires: python-module-kombu >= 1:4.0.0
BuildRequires: python-module-fixtures >= 3.0.0
BuildRequires: python-module-futures >= 3.0
BuildRequires: python-module-tenacity >= 4.4.0
BuildRequires: python-module-oslo.middleware >= 3.31.0
BuildRequires: python-module-kafka

BuildRequires: python-module-sphinx >= 1.6.2
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.9.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-cachetools >= 2.0.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-amqp >= 1:2.3.0
BuildRequires: python3-module-kombu >= 1:4.0.0
BuildRequires: python3-module-fixtures
BuildRequires: python3-module-tenacity >= 4.4.0
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-kafka

BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0


%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.


%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: OpenStack oslo.messaging library
Group: Development/Python3
Provides: python3-module-oslo-messaging = %EVR
%add_python3_req_skip proton
%add_python3_req_skip pyngus

%description -n python3-module-%oname
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary:    Documentation for OpenStack common messaging library
Group:     Development/Documentation
Provides:  python-module-oslo-messaging-doc = %EVR
Obsoletes: python-module-oslo-messaging-doc < %EVR

%description doc
Documentation for the oslo.messaging library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
#rm -rf %oname.egg-info
# let RPM handle deps
#sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
#rm -rf {test-,}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd


# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install
mv %buildroot%_bindir/oslo-messaging-send-notification %buildroot%_bindir/oslo-messaging-send-notification.py2
mv %buildroot%_bindir/oslo-messaging-zmq-broker %buildroot%_bindir/oslo-messaging-zmq-broker.py2
mv %buildroot%_bindir/oslo-messaging-zmq-proxy %buildroot%_bindir/oslo-messaging-zmq-proxy.py2

pushd ../python3
%python3_install
popd

%files
%doc README.rst LICENSE
%_bindir/*.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/*
%exclude %_bindir/*.py2
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc html LICENSE

%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1:8.1.2-alt1
- 8.1.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:5.17.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1:5.17.2-alt1
- 5.17.2

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1:5.17.1-alt1
- 5.17.1
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1:5.10.1-alt1
- 5.10.1

* Wed Oct 26 2016 Alexey Shabalin <shaba@altlinux.ru> 1:5.10.0-alt2
- fix BR with epoch

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1:5.10.0-alt1
- 5.10.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1:4.6.1-alt1
- 4.6.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:2.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:2.5.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1:2.5.0-alt1
- 2.5.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.8.3-alt1
- 1.8.3

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0
- add python3 package

* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Jul 15 2014 Lenar Shakirov <snejok@altlinux.ru> 1.3.0.2-alt1
- First build for ALT (based on Fedora 1.3.0.2-4.fc21.src)
