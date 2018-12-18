%define oname etcd3gw

Name: python-module-%oname
Version: 0.2.4
Release: alt1
Summary: etcd3 gateway Python Client

Group: Development/Python
License: ASL 2.0
Url: https://github.com/dims/etcd3-gateway
Source: %oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-urllib3 >= 1.15.1
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-futurist >= 0.11.0


BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx >= 4.7
BuildRequires: python-module-reno >= 1.8.0
#BuildRequires: python-module-openstackdocstheme

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-urllib3 >= 1.15.1
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-futurist >= 0.11.0


BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx >= 4.7
BuildRequires: python3-module-reno >= 1.8.0
#BuildRequires: python3-module-openstackdocstheme

%description
A python client for etcd3 grpc-gateway v3alpha API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: etcd3 gateway Python Client
Group: Development/Python3

%description -n python3-module-%oname
A python client for etcd3 grpc-gateway v3alpha API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for Cache storage for Openstack projects
Group: Development/Documentation

%description doc
Documentation for etcd3 gateway Python Client.


%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rf %oname.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd


# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install

pushd ../python3
%python3_install
popd



%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/examples

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python_sitelibdir/*/examples

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc html
%doc README.md LICENSE
%doc etcd3gw/examples

%changelog
* Mon Dec 17 2018 Alexey Shabalin <shaba@altlinux.org> 0.2.4-alt1
- Initial build

