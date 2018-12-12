%define oname monascaclient

Name:       python-module-%oname
Version:    1.12.1
Release:    alt1
Summary:    Python API and CLI for OpenStack Monasca
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/python-%oname
Source:     https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-osc-lib >= 1.8.0
BuildRequires: python-module-oslo.serialization >= 2.18.0
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-prettytable >= 0.7.2
BuildRequires: python-module-yaml >= 3.12

BuildRequires: python-module-sphinx >= 1.6.5
BuildRequires: python-module-reno >= 2.5.0
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-doc8 >= 0.6.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-osc-lib >= 1.8.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable >= 0.7.2
BuildRequires: python3-module-yaml >= 3.12

BuildRequires: python3-module-sphinx >= 1.6.5
BuildRequires: python3-module-reno >= 2.5.0
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-doc8 >= 0.6.0

%description
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

The Monasca Client was written using the OpenStack Heat Python client as a framework.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Python API and CLI for OpenStack Monasca
Group: Development/Python3

%description -n python3-module-%oname
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

The Monasca Client was written using the OpenStack Heat Python client as a framework.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Monasca API Client
Group:  Development/Documentation

%description doc
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API the monascaclient module and a command-line tool
monasca.

%prep
%setup -n python-%oname-%version

# Let RPM handle the dependencies
rm -f {,test-}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/monasca %buildroot%_bindir/monasca.py2

pushd ../python3
%python3_install
popd

# Build HTML docs and man page
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/monasca.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/monasca
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- Updated to 1.12.1.
- Added building docs.

* Fri Jul 20 2018 Grigory Ustinov <grenka@altlinux.org> 1.10.0-alt1
- new version 1.10.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- add test packages

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial release for Sisyphus
