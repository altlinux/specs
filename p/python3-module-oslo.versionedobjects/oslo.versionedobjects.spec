%define oname oslo.versionedobjects

Name: python3-module-%oname
Version: 1.37.0
Release: alt1
Summary: OpenStack oslo.versionedobjects library
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: oslo.versionedobjects.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.concurrency >= 3.26.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.messaging >= 5.29.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-netaddr >= 0.7.18
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-jsonschema >= 2.6.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
oslo.versionedobjects library deals with DB schema being at different versions
than the code expects, allowing services to be operated safely during upgrades.
It enables DB independent schema by providing an abstraction layer, which
allows us to support SQL and NoSQL Databases. oslo.versionedobjects is also
used in RPC APIs, to ensure upgrades happen without spreading version dependent
code across different services and projects.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo versionedobjects library
Group: Development/Documentation

%description doc
Documentation for the Oslo versionedobjects library.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc CONTRIBUTING.rst HACKING.rst LICENSE PKG-INFO README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.37.0-alt1
- Automatically updated to 1.37.0.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.36.1-alt1
- Automatically updated to 1.36.1.
- Build without python2.

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.36.0-alt1
- new version 1.36.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.33.3-alt1
- 1.33.3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.21.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Aug 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.21.1-alt1
- 1.21.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.21.0-alt1
- 1.21.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0

* Mon Jun 01 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial release
