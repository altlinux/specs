%define oname oslo.messaging
%def_with check
%def_with docs

Name: python3-module-%oname
Epoch: 1
Version: 14.2.0
Release: alt1

Summary: OpenStack Oslo Messaging API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.messaging

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-messaging = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.37.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.service >= 1.24.0
BuildRequires: python3-module-oslo.middleware >= 3.31.0
BuildRequires: python3-module-oslo.metrics >= 0.2.1
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-cachetools >= 2.0.0
BuildRequires: python3-module-webob
BuildRequires: python3-module-yaml >= 3.12
BuildRequires: python3-module-amqp >= 2.5.2
BuildRequires: python3-module-kombu >= 4.6.6

%if_with check
BuildRequires: python3-module-kafka
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-pifpaf >= 2.2.0
BuildRequires: python3-module-confluent-kafka >= 1.3.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-eventlet >= 0.23.0
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-pre-commit >= 2.6.0
BuildRequires: python3-module-pyngus >= 2.2.0
BuildRequires: python3-module-greenlet >= 0.4.15
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 1.6.2
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
%endif

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The Oslo messaging API supports RPC and notifications over a number of
different messaging transports.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation
Provides: python3-module-oslo-messaging-doc = %EVR

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%if_with docs
# install man page
install -pDm 644 man/oslomessaging.1 %buildroot%_man1dir/oslomessaging.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/oslo-messaging-send-notification
%python3_sitelibdir/oslo_messaging
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_messaging/tests

%files tests
%python3_sitelibdir/oslo_messaging/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslomessaging.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 1:14.2.0-alt1
- Automatically updated to 14.2.0.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 1:14.0.0-alt1
- Automatically updated to 14.0.0.

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 1:12.14.0-alt1
- Automatically updated to 12.14.0.
- Build without check.
- Build without docs.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 1:12.1.0-alt1
- Automatically updated to 12.1.0.
- Renamed spec file.
- Unify documentation building.
- Fix license.

* Sat Oct 26 2019 Grigory Ustinov <grenka@altlinux.org> 1:8.1.2-alt1
- Build without python2.

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
