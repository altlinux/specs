%define oname aodhclient
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 3.0.0
Release: alt1.1

Summary: Python client library for OpenStack Aodh

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/aodhclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 1.4
BuildRequires: python3-module-cliff >= 1.14.0
BuildRequires: python3-module-osc-lib >= 1.0.1
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-osprofiler >= 1.4.0
BuildRequires: python3-module-keystoneauth1 >= 1.0.0
BuildRequires: python3-module-pyparsing

%if_with check
BuildRequires: python3-module-stestr
BuildRequires: python3-module-tempest
BuildRequires: python3-module-oslotest
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0
BuildRequires: python3-module-reno >= 1.6.2
%endif

%description
There's a Python API (the aodhclient module), and a command-line script
(installed as aodh). Each implements the entire OpenStack Aodh API.

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
%_bindir/aodh
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
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1.1
- Moved on modern pyproject macros.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.
- Unified.
- Build without check.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt2
- Unify documentation building.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 2.0.1-alt1
- Automatically updated to 2.0.1.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.
- Build without python2.

* Wed Aug 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0

* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.1.1-alt1
- 1.1.1

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0
- add test packages

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 0.7.0-alt1
- Initial release for Sisyphus
