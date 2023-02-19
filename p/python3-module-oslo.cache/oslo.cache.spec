%define oname oslo.cache
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.3.0
Release: alt1

Summary: Cache storage for OpenStack projects

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.cache

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-cache = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-dogpile.cache >= 1.1.5
BuildRequires: python3-module-oslo.config >= 8.1.0
BuildRequires: python3-module-oslo.i18n >= 5.0.0
BuildRequires: python3-module-oslo.log >= 4.2.1
BuildRequires: python3-module-oslo.utils >= 4.2.0

%if_with check
BuildRequires: python3-module-memcached >= 1.56
BuildRequires: python3-module-pymongo >= 3.0.2
BuildRequires: python3-module-etcd3gw >= 0.2.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-pifpaf >= 0.10.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-pymemcache >= 3.5.0
BuildRequires: python3-module-binary-memcached
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%py3_requires dogpile.cache

%description
oslo.cache aims to provide a generic caching mechanism for OpenStack projects
by wrapping the dogpile.cache library. The dogpile.cache library provides
support memoization, key value storage and interfaces to common caching backends
such as Memcached.

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
Provides: python3-module-oslo-cache-doc = %EVR

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
install -pDm 644 man/oslocache.1 %buildroot%_man1dir/oslocache.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/oslo_cache
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_cache/tests

%files tests
%python3_sitelibdir/oslo_cache/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslocache.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt2.1
- Little spec fix.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 2.11.0-alt1
- Automatically updated to 2.11.0.
- Unified (thx for felixz@).

* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt2
- Build without docs.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Automatically updated to 2.3.0.
- Unify documentation building.
- Fix license.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.38.1-alt1
- Automatically updated to 1.38.1.
- Added watch file.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.37.0-alt1
- Automatically updated to 1.37.0.
- Build without python2.

* Mon Apr 22 2019 Alexey Shabalin <shaba@altlinux.org> 1.30.3-alt1
- 1.30.3

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.30.2-alt1
- 1.30.2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.17.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.17.0-alt1
- 1.17.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- 0.7.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- First build for ALT
