%define oname combomethod

Name: python3-module-%oname
Version: 1.0.10
Release: alt2
Summary: Decorator indicating a method is both a class and an instance method
License: Apache-2.0
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/combomethod

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%description
Python has instance methods, class methods (@classmethod),
and static methods (@staticmethod).
But it doesn't have a clear way to invoke a method on
either a class or its instances. With combomethod, it does.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PYTHONPATH=$PWD
py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.10-alt2
- Frop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Initial build for ALT.
