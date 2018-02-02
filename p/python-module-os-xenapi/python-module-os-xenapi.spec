%define oname os-xenapi

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.1
Summary: XenAPI library for OpenStack projects
Group: Development/Python
License: ASL 2.0
Url: http://www.citrix.com
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.8
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 0.1.1
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-eventlet >= 0.18.2
BuildRequires: python-module-oslo.concurrency >= 3.8.0
BuildRequires: python-module-oslo.log >= 3.11.0
BuildRequires: python-module-oslo.utils >= 3.18.0
BuildRequires: python-module-oslo.i18n >= 2.1.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.8
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-eventlet >= 0.18.2
BuildRequires: python3-module-oslo.concurrency >= 3.8.0
BuildRequires: python3-module-oslo.log >= 3.11.0
BuildRequires: python3-module-oslo.utils >= 3.18.0
BuildRequires: python3-module-oslo.i18n >= 2.1.0
%endif

%description
XenAPI library for OpenStack projects.

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
Summary: Windows Hyper-V library for OpenStack projects
Group: Development/Python3

%description -n python3-module-%oname
XenAPI library for OpenStack projects.

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
rm -rf %buildroot%python_sitelibdir/*/dom0

%if_with python3
pushd ../python3
%python3_install
rm -rf %buildroot%python3_sitelibdir/*/dom0
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 06 2017 Alexey Shabalin <shaba@altlinux.ru> 0.1.1-alt1
- Initial packaging
