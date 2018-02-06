%define oname zake

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.2
Release: alt1.1
Summary: Testing utilities for the kazoo library
License: ASLv2.0
Group: Development/Python
Url: https://github.com/yahoo/Zake

# https://github.com/python-zk/kazoo.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-kazoo >= 1.3.1
BuildRequires: python-module-six
BuildRequires: python-module-nose
BuildRequires: python-module-testtools
BuildRequires: python-module-flake8


%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-kazoo >= 1.3.1
BuildRequires: python3-module-six
BuildRequires: python3-module-nose
BuildRequires: python3-module-testtools
BuildRequires: python3-module-flake8
%endif

%py_provides %oname

%description
A python package that works to provide a nice set of testing utilities for the kazoo library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A python package that works to provide a nice set of testing utilities for the kazoo library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Higher Level Zookeeper Client
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python package that works to provide a nice set of testing utilities for the kazoo library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A python package that works to provide a nice set of testing utilities for the kazoo library.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif


%check
python setup.py test
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*


%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2.2-alt1
- Initial build for Sisyphus
