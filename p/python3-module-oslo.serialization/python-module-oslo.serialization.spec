%define oname oslo.serialization

Name: python3-module-%oname
Version: 2.29.2
Release: alt1
Summary: OpenStack oslo.serialization library
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python3-module-oslo-serialization = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-msgpack >= 0.5.2
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-pytz >= 2013.6

# doc
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1

%description
The OpenStack Oslo serialization handling library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo serialization handling library
Group: Development/Documentation
Provides: python-module-oslo-serialization-doc = %EVR

%description doc
Documentation for the Oslo serialization handling library.

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
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 2.29.2-alt1
- Automatically updated to 2.29.2.
- Build without python2.

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 2.29.1-alt1
- new version 2.29.1

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 2.27.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.16.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 2.16.0-alt1
- 2.16.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.13.0-alt1
- 2.13.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.4.0-alt1
- Initial release
