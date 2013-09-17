%define oname kajiki
Name: python-module-%oname
Version: 0.4.4
Release: alt1
Summary: Really fast well-formed xml templates
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Kajiki/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel python-module-nine

%description
Kajiki quickly compiles Genshi-like syntax to *real python bytecode*
that renders with blazing-fast speed.

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

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

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

%changelog
* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1
- Version 0.4.4

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus

