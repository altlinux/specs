%def_with python3
%define oname gnocchiclient
%def_disable doc

Name: python-module-%oname
Version: 3.3.1
Release: alt1
Summary: Python client library for Gnocchi

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-sphinx_rtd_theme
BuildRequires: python-module-reno

BuildRequires: python-module-cliff >= 1.16.0
BuildRequires: python-module-ujson
BuildRequires: python-module-keystoneauth1 >= 2.0.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-futurist
BuildRequires: python-module-iso8601
BuildRequires: python-module-debtcollector
BuildRequires: python-module-monotonic


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6

BuildRequires: python3-module-cliff >= 1.16.0
BuildRequires: python3-module-ujson
BuildRequires: python3-module-keystoneauth1 >= 2.0.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-futurist
BuildRequires: python3-module-iso8601
BuildRequires: python3-module-debtcollector
BuildRequires: python3-module-monotonic

%description
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This is a client for OpenStack gnocchi API

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.
%package -n python3-module-%oname
Summary: Python client library for Gnocchi
Group: Development/Python3

%description -n python3-module-%oname
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This is a client for OpenStack gnocchi API

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack Gnocchi API Client
Group: Development/Documentation

%description doc
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This package contains auto-generated documentation.

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf gnocchiclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

%if_disabled doc
rm -f gnocchiclient/gendoc.py
%endif

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
mv %buildroot%_bindir/gnocchi %buildroot%_bindir/python3-gnocchi
%endif

%python_install

%if_enabled doc
export PATH=$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=.
export LANG=en_US.utf8
python setup.py build_sphinx

# Fix hidden-file-or-dir warnings
rm -rf doc/build/html/.doctrees doc/build/html/.buildinfo
%endif

%files
%doc README.rst
%doc LICENSE
%_bindir/gnocchi
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-gnocchi
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%if_enabled doc
%files doc
%doc doc/build/html
%endif

%changelog
* Thu Aug 10 2017 Alexey Shabalin <shaba@altlinux.ru> 3.3.1-alt1
- 3.3.1
- add tests packages
- disable build doc package

* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- initial build


