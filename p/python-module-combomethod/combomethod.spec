%define oname combomethod

%def_with python3

Name: python-module-%oname
Version: 1.0.10
Release: alt1.1
Summary: Decorator indicating a method is both a class and an instance method
License: Apache License 2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/combomethod

Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%description
Python has instance methods, class methods (@classmethod),
and static methods (@staticmethod).
But it doesn't have a clear way to invoke a method on
either a class or its instances. With combomethod, it does.

%if_with python3
%package -n python3-module-%oname
Summary: Decorator indicating a method is both a class and an instance method
Group: Development/Python3

%description -n python3-module-%oname
Python has instance methods, class methods (@classmethod),
and static methods (@staticmethod).
But it doesn't have a clear way to invoke a method on
either a class or its instances. With combomethod, it does.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test3 -vv
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Initial build for ALT.
