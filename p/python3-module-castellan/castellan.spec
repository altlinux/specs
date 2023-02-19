%define oname castellan
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.1.0
Release: alt1.1

Summary: Generic Key Manager interface for OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/castellan

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cryptography >= 2.7
BuildRequires: python3-module-oslo.config >= 6.4.0
BuildRequires: python3-module-oslo.context >= 2.19.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-requests >= 2.18.0
BuildRequires: python3-module-hacking >= 3.0.1

%if_with check
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-barbicanclient
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-bandit >= 1.6.0
BuildRequires: python3-module-pifpaf >= 0.10.0
BuildRequires: python3-module-pyflakes >= 2.1.1
BuildRequires: python3-module-requests-mock >= 1.2.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
BuildRequires: python3-module-sphinxcontrib-rsvgconverter
%endif

%description
%summary.

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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Spec refactoring.

* Tue Oct 11 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Fri Oct 07 2022 Grigory Ustinov <grenka@altlinux.org> 3.11.0-alt1
- Automatically updated to 3.11.0.
- Unified (thx for felixz@).

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.
- Fix license.
- Build with docs.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Automatically updated to 1.3.1.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Automatically updated to 1.2.2

* Thu Dec 06 2018 Alexey Shabalin <shaba@altlinux.org> 0.19.0-alt1
- 0.19.0

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0
- add tests packages

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- Initial build for Sisyphus

