%define oname oasa
Name: python-module-%oname
Version: 0.13.1
Release: alt1
Summary: Python library for manipulation of chemical formats that forms the base of BKChem
License: GPLv2+
Group: Development/Python
Url: http://bkchem.zirael.org/oasa_en.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-pycairo

%description
OASA is a free cheminformatics library written in Python.

%package tests
Summary: Tests for OASA
Group: Development/Python
Requires: %name = %version-%release

%description tests
OASA is a free cheminformatics library written in Python.

This package contains tests for OASA.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python test.py

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/tests.py*
%exclude %python_sitelibdir/%oname/unittests.py*

%files tests
%python_sitelibdir/%oname/tests.py*
%python_sitelibdir/%oname/unittests.py*

%changelog
* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1
- Initial build for Sisyphus

