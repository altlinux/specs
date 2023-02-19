%define oname oslo.policy
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.1.0
Release: alt1

Summary: OpenStack Oslo Policy library

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/oslo.policy

Source: %oname-%version.tar
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
BuildRequires: python3-module-yaml >= 3.12

%if_with check
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-requests-mock >= 1.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 2.0.0
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
The Oslo Policy library provides support for RBAC policy enforcement across all
OpenStack services.

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
install -pDm 644 man/oslopolicy-checker.1 %buildroot%_man1dir/oslopolicy-checker.1
install -pDm 644 man/oslopolicy-list-redundant.1 %buildroot%_man1dir/oslopolicy-list-redundant.1
install -pDm 644 man/oslopolicy-policy-generator.1 %buildroot%_man1dir/oslopolicy-policy-generator.1
install -pDm 644 man/oslopolicy-sample-generator.1 %buildroot%_man1dir/oslopolicy-sample-generator.1
%endif

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
%python3_sitelibdir/oslo_policy
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/oslo_policy/tests

%files tests
%python3_sitelibdir/oslo_policy/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/oslopolicy-checker.1.xz
%_man1dir/oslopolicy-list-redundant.1.xz
%_man1dir/oslopolicy-policy-generator.1.xz
%_man1dir/oslopolicy-sample-generator.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

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
