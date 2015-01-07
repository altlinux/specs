%define oname jsonutil
Name: python-module-%oname
Version: 1.0.3
Release: alt1
Summary: Deserializes decimals to Decimal instead of to float
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonutil/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-simplejson
BuildPreReq: python-module-twisted-core-test

%py_provides %oname

%description
A wrapper around simplejson which deserializes decimals to Decimal
instead of to float.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR python-module-twisted-core-test

%description tests
A wrapper around simplejson which deserializes decimals to Decimal
instead of to float.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc CREDITS *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%changelog
* Wed Jan 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus

