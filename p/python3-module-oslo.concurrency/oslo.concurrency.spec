%define oname oslo.concurrency

Name: python3-module-%oname
Version: 3.31.0
Release: alt1

Summary: OpenStack oslo.concurrency library

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

Provides: python3-module-oslo-concurrency = %EVR

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-fasteners >= 0.7.0
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc

%description
Oslo concurrency library has utilities for safely running multi-thread,
multi-process applications using locking mechanisms and for running
external processes.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for the Oslo concurrency handling library
Group: Development/Documentation
Provides: python-module-oslo-concurrency-doc = %EVR

%description doc
Documentation for the Oslo concurrency handling library.

%prep
%setup -n %oname-%version

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
%_bindir/lockutils-wrapper
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc html

%changelog
* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 3.31.0-alt1
- Automatically updated to 3.31.0.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.30.0-alt1
- Automatically updated to 3.30.0.
- Build without python2.

* Thu Dec 13 2018 Alexey Shabalin <shaba@altlinux.org> 3.27.0-alt1
- Build new version.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 24 2017 Alexey Shabalin <shaba@altlinux.ru> 3.18.0-alt1
- 3.18.0
- add test packages

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 3.14.0-alt1
- 3.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Mon Aug 24 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.7.0-alt1
- Initial release
