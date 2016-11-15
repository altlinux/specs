%def_with python3
%define oname gnocchiclient

Name: python-module-%oname
Version: 2.6.0
Release: alt1
Summary: Python client library for Gnocchi

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-gnocchiclient
Source: %name-%version.tar


BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno

BuildRequires: python-module-cliff >= 1.16.0
BuildRequires: python-module-osc-lib >= 0.3.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0
BuildRequires: python-module-keystoneauth1 >= 1.0.0
BuildRequires: python-module-futurist

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cliff >= 1.16.0
BuildRequires: python3-module-osc-lib >= 0.3.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
BuildRequires: python3-module-keystoneauth1 >= 1.0.0
BuildRequires: python3-module-futurist
%endif


%description
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This is a client for OpenStack gnocchi API

%if_with python3
%package -n python3-module-%oname
Summary: Python client library for Gnocchi
Group: Development/Python3

%description -n python3-module-%oname
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This is a client for OpenStack gnocchi API
%endif

%package doc
Summary: Documentation for OpenStack Gnocchi API Client
Group: Development/Documentation

%description doc
Gnocchi is a multi-tenant timeseries, metrics and resources database.
This package contains auto-generated documentation.

%prep
%setup

# Remove bundled egg-info
rm -rf gnocchiclient.egg-info

# Let RPM handle the requirements
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
mv %buildroot%_bindir/gnocchi %buildroot%_bindir/python3-gnocchi
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests


export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build -b html doc/source html

# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%files
%doc README.rst
%doc LICENSE
%_bindir/gnocchi
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%_bindir/python3-gnocchi
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Tue Nov 15 2016 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- initial build


