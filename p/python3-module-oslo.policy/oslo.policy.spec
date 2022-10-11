%define oname oslo.policy
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 3.12.1
Release: alt1

Summary: RBAC policy enforcement library for OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://docs.openstack.org/oslo.policy/latest

Source: %name-%version.tar
Source1: %oname.watch

BuildArch: noarch

Provides: python3-module-oslo-policy = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-oslo.config >= 6.0.0
BuildRequires: python3-module-oslo.context >= 2.22.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-oslo.utils >= 3.40.0
BuildRequires: python3-module-pyaml >= 5.1

%if_with check
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
%endif

%if_with docs
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
BuildRequires: python3-module-yaml >= 3.12
%endif

%description
summary.

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
Provides: python3-module-oslo-policy-doc = %EVR

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup

# Remove bundled egg-info
rm -rfv %oname.egg-info

%build
%python3_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%python3_install

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/oslopolicy-checker
%_bindir/oslopolicy-convert-json-to-yaml
%_bindir/oslopolicy-list-redundant
%_bindir/oslopolicy-policy-generator
%_bindir/oslopolicy-policy-upgrade
%_bindir/oslopolicy-sample-generator
%_bindir/oslopolicy-validator
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%endif

%changelog
* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 3.12.1-alt1
- Automatically updated to 3.12.1.
- Unified (thx for felixz@).

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.
- Fix license.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1
- Automatically updated to 2.4.1.
- Added watch file.
- Renamed spec file.

* Fri Sep 20 2019 Grigory Ustinov <grenka@altlinux.org> 2.3.2-alt1
- new version 2.3.2.
- Build without python2.

* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 1.38.1-alt1
- 1.38.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.18.0-alt1
- 1.18.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.11.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Oct 28 2015 Alexey Shabalin <shaba@altlinux.ru> 0.11.0-alt1
- 0.11.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- Initial release
