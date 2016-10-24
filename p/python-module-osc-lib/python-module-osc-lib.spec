%define pypi_name osc-lib

%def_with python3

Name: python-module-%pypi_name
Version: 1.2.0
Release: alt1
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/osc-lib
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-cliff >= 2.2.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-os-client-config >= 1.13.1
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-stevedore >= 1.17.1


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-reno >= 0.1.1
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.2.0
BuildRequires: python3-module-keystoneauth1 >= 2.10.0
BuildRequires: python3-module-os-client-config >= 1.13.1
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-simplejson >= 2.2.0
BuildRequires: python3-module-stevedore >= 1.17.1
%endif

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

%package doc
Summary: Documentation for OpenStack %pypi_name library
Group: Development/Documentation

%description doc
Documentation for OpenStack %pypi_name library

%if_with python3
%package -n python3-module-%pypi_name
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
Group: Development/Python3

%description -n python3-module-%pypi_name
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

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
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial packaging
