%define _unpackaged_files_terminate_build 1
%define oname grampg
Name: python-module-%oname
Version: 0.3.0
Release: alt1.1
Summary: Simple and flexible password generation library
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/grampg/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/84/6f/63cee4b51ee20b737606c3e682673f3d4c9697fae7147e9bc5beefa42e58/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-sphinx-devel

%py_provides %oname

%description
The grampg (cue to Grumpy Admin Password Generator, and pronounced
"grummpeegee") is a small python2 library which allows to generate
passwords according to (possibly complicated) user specs. The idea is
simple: build an instance, feed it your desired specifications, then
generate as many passwords as you want. Each password generated will be
independent of the others, except from the fact that all of them will
comply with the specs.

The objectives for the grampg are flexibility and easy of use. grampg
fulfills by providing a kind interface to the user: When building the
password generator the user writes the spec as if it were being
pronounced. In this fashion, a set of complex rules is expressed in a
declarative line.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The grampg (cue to Grumpy Admin Password Generator, and pronounced
"grummpeegee") is a small python2 library which allows to generate
passwords according to (possibly complicated) user specs. The idea is
simple: build an instance, feed it your desired specifications, then
generate as many passwords as you want. Each password generated will be
independent of the others, except from the fact that all of them will
comply with the specs.

The objectives for the grampg are flexibility and easy of use. grampg
fulfills by providing a kind interface to the user: When building the
password generator the user writes the spec as if it were being
pronounced. In this fashion, a set of complex rules is expressed in a
declarative line.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

