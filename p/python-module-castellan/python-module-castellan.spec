%define pypi_name castellan
%def_with python3

Name: python-module-%pypi_name
Version: 0.2.1
Release: alt1
Summary: Generic Key Manager interface for OpenStack
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name

Source: %name-%version.tar
BuildArch: noarch


BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-cryptography >= 1.0
BuildRequires: python-module-oslo.config >= 2.3.0
BuildRequires: python-module-oslo.context >= 0.2.0
BuildRequires: python-module-oslo.log >= 1.8.0
BuildRequires: python-module-oslo.policy >= 0.5.0
BuildRequires: python-module-oslo.serialization >= 1.4.0
BuildRequires: python-module-oslo.utils >= 2.0.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-cryptography >= 1.0
BuildRequires: python3-module-oslo.config >= 2.3.0
BuildRequires: python3-module-oslo.context >= 0.2.0
BuildRequires: python3-module-oslo.log >= 1.8.0
BuildRequires: python3-module-oslo.policy >= 0.5.0
BuildRequires: python3-module-oslo.serialization >= 1.4.0
BuildRequires: python3-module-oslo.utils >= 2.0.0
%endif

%description
Generic Key Manager interface for OpenStack

%package -n python3-module-%pypi_name
Summary: Generic Key Manager interface for OpenStack
Group: Development/Python3

%description -n python3-module-%pypi_name
Generic Key Manager interface for OpenStack


%package doc
Summary: Documentation for Generic Key Manager interface for OpenStack
Group: Development/Documentation

%description doc
Documentation for Generic Key Manager interface for OpenStack

%prep
%setup
# Remove bundled egg-info
rm -rf %pypi_name.egg-info

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

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif
# Delete tests

rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc html

%changelog
* Fri Oct 30 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2.1-alt1
- Initial build for Sisyphus

