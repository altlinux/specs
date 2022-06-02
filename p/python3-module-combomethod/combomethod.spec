%define oname combomethod

%def_with check

Name: python3-module-%oname
Version: 1.0.12
Release: alt1

Summary: Decorator indicating a method is both a class and an instance method

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/combomethod

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

%description
Python has instance methods, class methods (@classmethod),
and static methods (@staticmethod).
But it doesn't have a clear way to invoke a method on
either a class or its instances. With combomethod, it does.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test3 -vv

%files
%doc *.rst
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Thu Jun 02 2022 Grigory Ustinov <grenka@altlinux.org> 1.0.12-alt1
- Build new version.

* Sat Jul 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.10-alt2
- Frop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 21 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.10-alt1
- Initial build for ALT.
