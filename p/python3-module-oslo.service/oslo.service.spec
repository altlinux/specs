%global oname oslo.service

%def_without docs

Name: python3-module-%oname
Version: 1.41.1
Release: alt1
Summary: Oslo service library
Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz
Source1: oslo.service.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-webob >= 1.7.1
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-greenlet >= 0.4.10
BuildRequires: python3-module-monotonic >= 0.6
BuildRequires: python3-module-oslo.utils >= 3.40.2
BuildRequires: python3-module-oslo.concurrency >= 3.25.0
BuildRequires: python3-module-oslo.config >= 5.1.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-PasteDeploy >= 1.5.0
BuildRequires: python3-module-routes >= 2.3.1
BuildRequires: python3-module-paste >= 2.0.2

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
Library for running OpenStack services

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Oslo service documentation
Group: Development/Documentation
%description doc
Documentation for oslo.service

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

%build
%python3_build

%if_with docs
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc html
%endif

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.41.1-alt1
- Automatically updated to 1.41.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.40.2-alt1
- Automatically updated to 1.40.2.
- Build without python2.
- Build without docs.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.40.0-alt1
- Automatically updated to 1.40.0

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.31.8-alt1
- 1.31.8

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 1.31.7-alt1
- 1.31.7

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.19.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jun 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.19.1-alt1
- 1.19.1

* Thu May 25 2017 Alexey Shabalin <shaba@altlinux.ru> 1.19.0-alt1
- 1.19.0

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- Initial package.
