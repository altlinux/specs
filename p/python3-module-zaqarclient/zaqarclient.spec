%define sname zaqarclient

Name: python3-module-%sname
Version: 1.12.0
Release: alt1

Summary: Client Library for OpenStack Zaqar Queueing API

Group: Development/Python3
License: ASL 2.0
Url: http://pypi.python.org/pypi/python-%sname

Source: %sname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-requests >= 2.14.2
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-stevedore >= 1.20.0
BuildRequires: python3-module-jsonschema >= 2.6.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-keystoneclient >= 2.0.0
BuildRequires: python3-module-osc-lib >= 1.8.0

%description
Python client to Zaqar messaging service API v1.

%package doc
Summary: Documentation for OpenStack Zaqar Queueing API Client
Group: Development/Documentation

%description doc
Python client to Zaqar messaging service API v1.

This package contains auto-generated documentation.

%prep
%setup -n %sname-%version

# Remove bundled egg-info
rm -rf *.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -rf {,test-}requirements.txt

%build
%python3_build

%install
%python3_install

export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build-3 -b html doc/source html

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%doc LICENSE
%python3_sitelibdir/*

%files doc
#%%doc html

%changelog
* Fri Dec 27 2019 Grigory Ustinov <grenka@altlinux.org> 1.12.0-alt1
- Automatically updated to 1.12.0.
- Added watch file.

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


