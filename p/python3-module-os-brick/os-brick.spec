%define oname os-brick
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 6.2.0
Release: alt1.1

Summary: OpenStack Cinder brick library for managing local volume attaches

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-brick

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 5.8.0
BuildRequires: python3-module-oslo.concurrency >= 5.0.0
BuildRequires: python3-module-oslo.context >= 4.1.0
BuildRequires: python3-module-oslo.config >= 9.0.0
BuildRequires: python3-module-oslo.log >= 4.8.0
BuildRequires: python3-module-oslo.i18n >= 5.1.0
BuildRequires: python3-module-oslo.privsep >= 3.0.0
BuildRequires: python3-module-oslo.service >= 2.8.0
BuildRequires: python3-module-oslo.serialization >= 4.3.0
BuildRequires: python3-module-oslo.utils >= 6.0.0
BuildRequires: python3-module-os-win >= 5.7.0
BuildRequires: python3-module-requests >= 2.25.1
BuildRequires: python3-module-tenacity >= 6.3.1

%if_with check
BuildRequires: python3-module-hacking >= 4.1.0
BuildRequires: python3-module-coverage >= 5.5
BuildRequires: python3-module-ddt >= 1.4.1
BuildRequires: python3-module-testtools >= 2.4.0
BuildRequires: python3-module-stestr >= 3.2.1
BuildRequires: python3-module-oslo.vmware >= 4.0.0
BuildRequires: python3-module-castellan >= 3.10.0
BuildRequires: python3-module-doc8 >= 0.8.1
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-bandit >= 1.7.0
BuildRequires: python3-module-mypy >= 0.982
BuildRequires: python3-module-castellan-tests
BuildRequires: python3-module-oslotest >= 4.5.0
BuildRequires: python3-module-testscenarios >= 0.5.0
BuildRequires: python3-module-eventlet >= 0.30.1
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 0.8.0
BuildRequires: python3-module-openstackdocstheme
%endif

%description
This project containing classes that help with volume discovery and removal
from a host.

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
install -d -m 755 %buildroot%_sysconfdir/%oname/rootwrap.d
mv %buildroot/usr/etc/os-brick/rootwrap.d/*.filters %buildroot%_sysconfdir/%oname/rootwrap.d

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%dir %_sysconfdir/%oname
%dir %_sysconfdir/%oname/rootwrap.d
%config(noreplace) %_sysconfdir/%oname/rootwrap.d/*
%python3_sitelibdir/os_brick
%python3_sitelibdir/os_brick-%version.dist-info
%exclude %python3_sitelibdir/os_brick/tests

%files tests
%python3_sitelibdir/os_brick/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 6.2.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 6.2.0-alt1
- Automatically updated to 6.2.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 6.1.0-alt1
- Automatically updated to 6.1.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.2.0-alt1
- Automatically updated to 5.2.0.
- Unified (thx for felixz@).

* Tue Jun 16 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.2-alt1
- Automatically updated to 3.0.2.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 2.11.0-alt1
- Automatically updated to 2.11.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.10.0-alt1
- Automatically updated to 2.10.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Automatically updated to 2.8.2

* Tue Dec 18 2018 Alexey Shabalin <shaba@altlinux.org> 2.5.4-alt1
- 2.5.4

* Fri Oct 05 2018 Grigory Ustinov <grenka@altlinux.org> 2.5.3-alt1
- Autoupdated to 2.5.3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.11.0-alt1
- 1.11.0

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- Initial packaging
