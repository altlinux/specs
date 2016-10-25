%define pypi_name neutron-lib

%def_with python3

Name: python-module-%pypi_name
Version: 0.4.0
Release: alt1
Summary: OpenStack Neutron shared routines and utilities
Group: Development/Python
License: ASL 2.0
Url: http://launchpad.net/%pypi_name
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-SQLAlchemy >= 1.0.10
BuildRequires: python-module-debtcollector >= 1.2.0
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.context >= 2.9.0
BuildRequires: python-module-oslo.db >= 4.10.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.messaging >= 5.2.0
BuildRequires: python-module-oslo.policy >= 1.9.0
BuildRequires: python-module-oslo.service >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 1.3
BuildRequires: python3-module-SQLAlchemy >= 1.0.10
BuildRequires: python3-module-debtcollector >= 1.2.0
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.context >= 2.9.0
BuildRequires: python3-module-oslo.db >= 4.10.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.messaging >= 5.2.0
BuildRequires: python3-module-oslo.policy >= 1.9.0
BuildRequires: python3-module-oslo.service >= 1.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
%endif

%description
Neutron-lib is an OpenStack library project used by Neutron, Advanced Services,
and third-party projects to provide common functionality and remove duplication.

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStack Neutron shared routines and utilities
Group: Development/Python3

%description -n python3-module-%pypi_name
Neutron-lib is an OpenStack library project used by Neutron, Advanced Services,
and third-party projects to provide common functionality and remove duplication.
%endif

%package doc
Summary: Documentation for OpenStack Neutron shared routines and utilities
Group: Development/Documentation

%description doc
Documentation for OpenStack Neutron shared routines and utilities

%prep
%setup

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py

# generate html docs
python setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

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
%doc AUTHORS ChangeLog README.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Fri Oct 21 2016 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Fri Apr 15 2016 Alexey Shabalin <shaba@altlinux.ru> 0.0.1-alt1
- Initial package.
