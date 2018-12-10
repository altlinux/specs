
%define oname aodhclient

Name:       python-module-%oname
Version:    1.1.1
Release:    alt1
Summary:    Python API and CLI for OpenStack Aodh
Group:      Development/Python
License:    ASL 2.0
Url:        http://docs.openstack.org/developer/%oname
Source:     https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-argparse
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-cliff >= 1.14.0
BuildRequires: python-module-osc-lib >= 1.0.1
BuildRequires: python-module-oslo.i18n >= 1.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-keystoneauth1 >= 1.0.0
BuildRequires: python-module-debtcollector
BuildRequires: python-module-pyparsing

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.11.0
BuildRequires: python-module-reno >= 1.6.2

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cliff >= 1.14.0
BuildRequires: python3-module-osc-lib >= 1.0.1
BuildRequires: python3-module-oslo.i18n >= 1.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 1.0.0
BuildRequires: python3-module-debtcollector
BuildRequires: python3-module-pyparsing

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.11.0
BuildRequires: python3-module-reno >= 1.6.2

%description
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary:    Python API and CLI for OpenStack Aodh
Group: Development/Python3

%description -n python3-module-%oname
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Aodh API Client
Group:  Development/Documentation

%description doc
This is a client library for Aodh built on the Aodh API. It
provides a Python API (the aodhclient module) and a command-line tool
(aodh).

%prep
%setup -n %oname-%version

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
mv %buildroot%_bindir/aodh %buildroot%_bindir/aodh.py2

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
%_bindir/aodh.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%_bindir/aodh
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc LICENSE html

%changelog
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
