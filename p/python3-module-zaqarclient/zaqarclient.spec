%define oname zaqarclient

Name: python3-module-%oname
Version: 1.13.1
Release: alt2

Summary: Client Library for OpenStack Zaqar Queueing API

Group: Development/Python3
License: Apache-2.0
Url: http://pypi.python.org/pypi/python-%oname

Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneclient >= 2.0.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-openstackdocstheme

%description
Python client to Zaqar messaging service API.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Zaqar Queueing API Client
Group: Development/Documentation

%description doc
Python client to Zaqar messaging service API.

This package contains documentation for %oname.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf *.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

%build
%python3_build

export PYTHONPATH="$PWD"

# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python3_install

# install man page
install -p -D -m 644 man/python-zaqarclient.1 %buildroot%_man1dir/zaqarclient.1

%files
%doc *.rst LICENSE
%_man1dir/zaqarclient*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Fri Jun 19 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt2
- Unify documentation building.
- Add tests subpackage.

* Fri May 15 2020 Grigory Ustinov <grenka@altlinux.org> 1.13.1-alt1
- Automatically updated to 1.13.1.

* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.12.0-alt1
- Automatically updated to 1.12.0.

* Fri Oct 25 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt2
- Build without python2.
- Build without docs=(.

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.0-alt1
- Initial build.


