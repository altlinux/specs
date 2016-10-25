%define pypi_name os-vif

%def_with python3

Name: python-module-%pypi_name
Version: 1.2.1
Release: alt1
Summary: A library for plugging and unplugging virtual interfaces in OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://www.openstack.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1

BuildRequires: python-module-netaddr >= 0.7.12
BuildRequires: python-module-oslo.config >= 3.14.0
BuildRequires: python-module-oslo.log >= 1.14.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.privsep >= 1.9.0
BuildRequires: python-module-oslo.versionedobjects >= 1.13.0
BuildRequires: python-module-stevedore >= 1.16.0


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-reno >= 0.1.1

BuildRequires: python3-module-netaddr >= 0.7.12
BuildRequires: python3-module-oslo.config >= 3.14.0
BuildRequires: python3-module-oslo.log >= 1.14.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.privsep >= 1.9.0
BuildRequires: python3-module-oslo.versionedobjects >= 1.13.0
BuildRequires: python3-module-stevedore >= 1.16.0
%endif

%description
A library for plugging and unplugging virtual interfaces in OpenStack.
Features:
- A base VIF plugin class that supplies a plug() and unplug() interface
- Versioned objects that represent a virtual interface and its components


%package doc
Summary: Documentation for OpenStack %pypi_name library
Group: Development/Documentation

%description doc
Documentation for OpenStack %pypi_name library

%if_with python3
%package -n python3-module-%pypi_name
Summary: A library for plugging and unplugging virtual interfaces in OpenStack
Group: Development/Python3

%description -n python3-module-%pypi_name
A library for plugging and unplugging virtual interfaces in OpenStack.
Features:
- A base VIF plugin class that supplies a plug() and unplug() interface
- Versioned objects that represent a virtual interface and its components

%endif

%prep
%setup
# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

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

python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

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

%files doc
%doc README.rst doc/build/html

%if_with python3
%files -n python3-module-%pypi_name
%python3_sitelibdir/*
%endif

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.1-alt1
- Initial packaging
