%define oname keystoneauth1
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.1.2
Release: alt1.1

Summary: Authentication Library for OpenStack Identity

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/keystoneauth1

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-os-service-types >= 1.2.0

%if_with check
BuildRequires: python3-module-lxml >= 4.2.0
BuildRequires: python3-module-oauthlib >= 0.6.2
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-mock >= 2.0.0
BuildRequires: python3-module-oslo.config >= 5.2.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-betamax >= 0.7.0
BuildRequires: python3-module-stestr >= 1.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-pycodestyle >= 2.0.0
BuildRequires: python3-module-flake8-import-order >= 0.17.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-reno >= 3.1.0
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-testresources >= 2.0.0
BuildRequires: python3-module-requests-kerberos >= 0.8.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-sphinxcontrib-apidoc
%endif

%description
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

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

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.2-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.1.2-alt1
- Automatically updated to 5.1.2.

* Fri Oct 21 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2.1
- Little spec fix.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Unified (thx for felixz@).
- Built without docs.

* Thu Jun 04 2020 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.
- Renamed spec file.
- Fix license.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 3.17.1-alt1
- Automatically updated to 3.17.1
- Build without python2.

* Sun Aug 18 2019 Grigory Ustinov <grenka@altlinux.org> 3.13.1-alt1
- Automatically updated to 3.13.1

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.18.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 2.18.0-alt1
- 2.18.0
- add test packages

* Wed Feb 01 2017 Alexey Shabalin <shaba@altlinux.ru> 2.12.3-alt1
- 2.12.3

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.12.2-alt1
- 2.12.2

* Tue Apr 12 2016 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- Initial package.
