%define oname blazarclient
%def_with check
# There is still empty doc directory
%def_without docs

Name: python3-module-%oname
Version: 3.5.0
Release: alt1.1

Summary: Client for OpenStack Reservation Service

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-blazarclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-cliff >= 2.8.0
BuildRequires: python3-module-prettytable
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.log >= 3.36.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-osc-lib >= 1.3.0

%if_with check
BuildRequires: python3-module-hacking >= 1.1.0
BuildRequires: python3-module-pyflakes >= 2.1.1
BuildRequires: python3-module-oslotest >= 3.2.0
BuildRequires: python3-module-fixtures >= 3.0.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-coverage >= 4.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%description
It provides a Python API (the blazarclient module) and a command-line script
(blazar).

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
%_bindir/blazar
%python3_sitelibdir/%oname
%python3_sitelibdir/python_blazarclient-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1.1
- Moved on modern pyproject macros.

* Mon Oct 10 2022 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.

* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Just rebuild with TODO in spec.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.
- Renamed spec file.

* Fri Oct 18 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.1-alt1
- Automatically updated to 2.2.1.
- Build without python2.
- Cleanup spec.

* Mon Jan 14 2019 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- Initial build.
