%define oname oslo.reports

Name: python3-module-%oname
Version: 1.31.1
Release: alt1

Summary: Openstack common reports library

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: oslo.reports.watch

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-jinja2 >= 2.10
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-psutil >= 3.2.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0

BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

OpenStack library for creating Guru Meditation Reports and other reports.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo common reports library
Group: Development/Documentation

%description doc
Documentation for the Oslo common reports library.

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
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html
%doc README.rst LICENSE

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.31.1-alt1
- Automatically updated to 1.31.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.30.0-alt1
- Automatically updated to 1.30.0.
- Build without python2.

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.28.0-alt1
- 1.28.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.17.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- 1.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT

