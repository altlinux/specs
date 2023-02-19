%define oname magnumclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 4.1.0
Release: alt1

Summary: OpenStack Client library for Magnum API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-magnumclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-os-client-config >= 1.28.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-cryptography >= 3.0
BuildRequires: python3-module-decorator >= 3.4.0

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-bandit >= 1.1.0
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-openstackclient-tests
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-testscenarios >= 0.4
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-reno
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
There is a Python library for accessing the API (magnumclient module),
and a command-line script (magnum).

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
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

# install bash completion
install -pDm 644 tools/magnum.bash_completion \
  %buildroot%_sysconfdir/bash_completion.d/magnum.bash_completion

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%_bindir/magnum
%python3_sitelibdir/%oname
%python3_sitelibdir/python_magnumclient-%version-py%_python3_version.egg-info
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/magnum.bash_completion
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.1.0-alt1
- Automatically updated to 4.1.0.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt2
- Fixed unowned dir.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 2.15.0-alt1
- Automatically updated to 2.15.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 2.12.0-alt1
- Automatically updated to 2.12.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 2.10.0-alt1
- Updated to 2.10.0.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 2.9.1-alt1
- new version 2.9.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.5.0-alt1
- 2.5.0
- add test packages

* Wed Apr 12 2017 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt0.b1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
 (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt0.b1.1
- NMU: Use buildreq for BR.

* Mon Nov 02 2015 Alexey Shabalin <shaba@altlinux.ru> 1.0.0-alt0.b1
- Initial release for Sisyphus

