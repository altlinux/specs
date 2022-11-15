%define oname tooz

Name: python3-module-%oname
Version: 2.3.0
Release: alt1.1
Summary: Coordination library for distributed systems
Group: Development/Python3
License: Apache-2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-stevedore >= 1.16.0
BuildRequires: python3-module-voluptuous >= 0.8.9
BuildRequires: python3-module-msgpack >= 0.4.0
BuildRequires: python3-module-fasteners >= 0.7
BuildRequires: python3-module-tenacity >= 3.2.1
BuildRequires: python3-module-futurist >= 1.2.0
BuildRequires: python3-module-oslo.utils >= 3.15.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
%endif
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-pymemcache
BuildRequires: python3-module-pymysql
BuildRequires: python3-module-sysv_ipc
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-kazoo
BuildRequires: python3-module-zake
BuildRequires: python3-module-stevedore >= 1.16.0

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%oname/drivers

%description
The Tooz project aims at centralizing the most common distributed
primitives like group membership protocol, lock service and leader
election by providing a coordination API helping developers to build distributed applications.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Coordination library
Group: Development/Documentation

%description doc
Documentation for Coordination library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

# disabling git call for last modification date from git repo
#sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python3 setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr build/sphinx/html/.buildinfo

%install
%python3_install

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc build/sphinx/html

%changelog
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
