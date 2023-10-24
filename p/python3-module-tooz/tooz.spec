%define oname tooz
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.2.0
Release: alt1

Summary: Coordination library for distributed systems

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/tooz

Source: %oname-%version.tar
Source1: %oname.watch

Patch: remove-distutils-for-python-3.12.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-stevedore >= 1.16.0
BuildRequires: python3-module-voluptuous >= 0.8.9
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-fasteners >= 0.7
BuildRequires: python3-module-tenacity >= 5.0.0
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-oslo.utils >= 4.7.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0

%if_with check
BuildRequires: python3-module-testtools >= 1.4.0
BuildRequires: python3-module-coverage >= 3.6
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-pifpaf >= 0.10.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-ddt >= 1.2.1
BuildRequires: python3-module-pre-commit >= 2.6.0
BuildRequires: python3-module-etcd3
BuildRequires: python3-module-etcd3gw
BuildRequires: python3-module-zake
BuildRequires: python3-module-sysv_ipc
BuildRequires: python3-module-pymemcache
BuildRequires: python3-module-pymysql
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0
%endif

%description
The Tooz project aims at centralizing the most common distributed
primitives like group membership protocol, lock service and leader
election by providing a coordination API helping developers to build
distributed applications.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for Coordination library
Group: Development/Documentation

%description doc
Documentation for Coordination library.
%endif

%prep
%setup -n %oname-%version
%patch -p2

# Remove bundled egg-info
rm -rfv %oname.egg-info

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

%check
export TOOZ_TEST_URL="ipc://"
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
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
* Wed Oct 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0.
- Spec refactoring.

* Mon Oct 16 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2.1
- Dropped build dependency on python3-module-reno.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2
- Fixed FTBFS.

* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.3.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Automatically updated to 2.3.0.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.67.1-alt1
- Automatically updated to 1.67.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.66.2-alt1
- Automatically updated to 1.66.2.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.64.2-alt1
- Automatically updated to 1.64.2

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.62.0-alt1
- 1.62.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.48.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.48.2-alt1
- 1.48.2

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.48.1-alt1
- 1.48.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.48.0-alt1
- 1.48.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.43.0-alt1
- 1.43.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1.34.0-alt1
- 1.34.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.24.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.24.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.24.0-alt1
- 1.24.0

* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.13.0-alt1
- Initial release
