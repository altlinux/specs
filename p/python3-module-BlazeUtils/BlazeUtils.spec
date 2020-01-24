%define oname BlazeUtils

Name: python3-module-%oname
Version: 0.6.1
Release: alt1

Summary: A collection of python utility functions and classes
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/BlazeUtils/
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-wrapt
# for tests
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest
BuildRequires: python3-module-SQLAlchemy

%py3_provides blazeutils


%description
BlazeUtils is a library to hold common tools for the Blaze library
family:

* BlazeWeb
* BaseBWA
* BlazeForm

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
BlazeUtils is a library to hold common tools for the Blaze library
family:

* BlazeWeb
* BaseBWA
* BlazeForm

This package contains tests for %oname.

%prep
%setup

rm -f blazeutils/tests/_bad_import_deeper.py

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing.*

%files tests
%python3_sitelibdir/*/testing.*


%changelog
* Fri Jan 24 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.1-alt1
- Version updated to 0.6.1
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- automated PyPI update

* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Initial build for Sisyphus

