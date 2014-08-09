%define oname kajiki

%def_with python3

Name: python-module-%oname
Version: 0.4.4
Release: alt2
Summary: Really fast well-formed xml templates
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Kajiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-nine
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

%package -n python3-module-%oname
Summary: Really fast well-formed xml templates
Group: Development/Python3

%description -n python3-module-%oname
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

%package -n python3-module-%oname-tests
Summary: Tests for Kajiki, really fast well-formed xml templates
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

This package contains tests for Kajiki.

%package tests
Summary: Tests for Kajiki, really fast well-formed xml templates
Group: Development/Python
Requires: %name = %version-%release

%description tests
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

This package contains tests for Kajiki.

%package pickles
Summary: Pickles for Kajiki
Group: Development/Python

%description pickles
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

This package contains pickles for Kajiki.

%package docs
Summary: Documentation for Kajiki
Group: Development/Documentation

%description docs
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

This package contains documentation for Kajiki.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc PKG-INFO *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt2
- Added module for Python 3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Version 0.4.4

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus

