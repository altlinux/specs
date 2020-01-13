%define _unpackaged_files_terminate_build 1

%define oname grampg

Name: python3-module-%oname
Version: 0.3.0
Release: alt2

Summary: Simple and flexible password generation library
License: AGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/grampg/
BuildArch: noarch

Source0: https://pypi.python.org/packages/84/6f/63cee4b51ee20b737606c3e682673f3d4c9697fae7147e9bc5beefa42e58/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx-devel

%py3_provides %oname


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
Group: Development/Python3
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
%setup -q -n %oname-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

