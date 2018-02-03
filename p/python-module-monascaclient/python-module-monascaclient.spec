%def_with python3
%define oname monascaclient

Name:       python-module-%oname
Version:    1.5.0
Release:    alt1.1
Summary:    Python API and CLI for OpenStack Monasca
License:    ASL 2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz
Group:      Development/Python

BuildArch:  noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-d2to1
BuildRequires: python-module-argparse
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.middleware >= 3.0.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.service >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-keystoneclient >= 3.8.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-yaml >= 3.10.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-argparse
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.middleware >= 3.0.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-oslo.service >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-keystoneclient >= 3.8.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable  >= 0.7.1
BuildRequires: python3-module-yaml >= 3.10.0
%endif

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

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/monasca %buildroot%_bindir/python3-monasca
%endif

%python_install

# Build HTML docs and man page
#export PYTHONPATH="$( pwd ):$PYTHONPATH"
#sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
#rm -fr html/.doctrees html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/monasca
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-monasca
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

#%files doc
#%doc LICENSE html

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed May 31 2017 Alexey Shabalin <shaba@altlinux.ru> 1.5.0-alt1
- 1.5.0
- add test packages

* Tue Nov 22 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial release for Sisyphus
