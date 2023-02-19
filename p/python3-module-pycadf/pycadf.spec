%define oname pycadf
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.1.1
Release: alt1.1

Summary: CADF Library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/pycadf

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-pytz >= 2013.6
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-debtcollector >= 1.2.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-openstackdocstheme >= 2.2.1
BuildRequires: python3-module-sphinxcontrib-apidoc >= 0.2.0
%endif

%description
This library provides an auditing data model based on the
Cloud Auditing Data Federation specification, primarily for use by OpenStack.
The goal is to establish strict expectations about what auditors can expect
from audit notifications.

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

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%pyproject_build

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
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

# Move config files to proper location
install -d -m 755 %buildroot%_sysconfdir/%oname
mv %buildroot/usr/etc/%oname/*_api_audit_map.conf %buildroot%_sysconfdir/%oname

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%dir %_sysconfdir/%oname
%config(noreplace) %_sysconfdir/%oname/ceilometer_api_audit_map.conf
%config(noreplace) %_sysconfdir/%oname/cinder_api_audit_map.conf
%config(noreplace) %_sysconfdir/%oname/glance_api_audit_map.conf
%config(noreplace) %_sysconfdir/%oname/neutron_api_audit_map.conf
%config(noreplace) %_sysconfdir/%oname/nova_api_audit_map.conf
%config(noreplace) %_sysconfdir/%oname/swift_api_audit_map.conf
%config(noreplace) %_sysconfdir/%oname/trove_api_audit_map.conf
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1.1
- Moved on modern pyproject macros.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.10.0-alt1
- Automatically updated to 2.10.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.9.0-alt1
- Automatically updated to 2.9.0

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.8.0-alt1
- 2.8.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- add test packages

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem at altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add python3 module

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.5.1-alt1
- First build for ALT (based on Fedora 0.5.1-1.fc21.src)

