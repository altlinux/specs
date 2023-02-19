%define oname os-win
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 5.9.0
Release: alt1.1

Summary: Windows Hyper-V library for OpenStack projects

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-win

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-eventlet >= 0.22.0
BuildRequires: python3-module-oslo.concurrency >= 3.29.0
BuildRequires: python3-module-oslo.config >= 6.8.0
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 4.7.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-ddt >= 1.2.1
BuildRequires: python3-module-oslotest >= 3.8.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testscenarios >= 0.4
BuildRequires: python3-module-testtools >= 2.2.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
%endif

%description
Library contains Windows / Hyper-V code commonly used in the OpenStack
projects: nova, cinder, networking-hyperv. The library can be used in any
other OpenStack projects where it is needed.

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
%python3_sitelibdir/os_win
%python3_sitelibdir/os_win-%version.dist-info
%exclude %python3_sitelibdir/os_win/tests

%files tests
%python3_sitelibdir/os_win/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 5.9.0-alt1.1
- Moved on modern pyproject macros.

* Sat Feb 18 2023 Grigory Ustinov <grenka@altlinux.org> 5.9.0-alt1
- Automatically updated to 5.9.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 5.7.1-alt3
- Spec refactoring.

* Wed Oct 12 2022 Grigory Ustinov <grenka@altlinux.org> 5.7.1-alt2
- Added manual.

* Sat Oct 08 2022 Grigory Ustinov <grenka@altlinux.org> 5.7.1-alt1
- Automatically updated to 5.7.1.
- Unified.

* Tue Jun 16 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.2-alt1
- Automatically updated to 5.0.2.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1.
- Renamed spec file.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 4.3.2-alt1
- Automatically updated to 4.3.2.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 4.2.0-alt1
- Automatically updated to 4.2.0

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 4.0.1-alt1
- 4.0.1

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jul 18 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1
- 1.4.2

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.1-alt1
- 1.4.1
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.1-alt1
- Initial packaging
