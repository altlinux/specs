%define oname fyzz
Name: python-module-%oname
Version: 0.1.0
Release: alt1
Summary: SPARQL parser
License: LGPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/fyzz/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-yapps2
BuildPreReq: python-module-logilab-common

%description
SPARQL parser written in Python using yapps.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
SPARQL parser written in Python using yapps.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
export PYTHONPATH=%buildroot%python_sitelibdir
pushd test/data
#tar -xf data-r2.tar.gz
popd
for i in test/*.py; do
	python $i
done

%files
%doc ChangeLog doc/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test

%files tests
%python_sitelibdir/*/test

%changelog
* Wed Nov 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus

