%define oname osc-lib

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.1
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-cliff >= 2.3.0
BuildRequires: python-module-keystoneauth1 >= 2.16.0
BuildRequires: python-module-os-client-config >= 1.22.0
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-stevedore >= 1.17.1
BuildRequires: python-module-requests-mock >= 1.1

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-cliff >= 2.2.0
BuildRequires: python3-module-keystoneauth1 >= 2.16.0
BuildRequires: python3-module-os-client-config >= 1.22.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-simplejson >= 2.2.0
BuildRequires: python3-module-stevedore >= 1.17.1
%endif

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package doc
Summary: Documentation for OpenStack %oname library
Group: Development/Documentation

%description doc
Documentation for OpenStack %oname library

%package -n python3-module-%oname
Summary: OpenStackClient (aka OSC) is a command-line client for OpenStack
Group: Development/Python3

%description -n python3-module-%oname
OpenStackClient (aka OSC) is a command-line client for OpenStack.
osc-lib is a package of common support modules for writing OSC plugins.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.


%prep
%setup -n %oname-%version
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

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files doc
%doc README.rst doc/build/html

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 30 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.0-alt1
- 1.3.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial packaging
