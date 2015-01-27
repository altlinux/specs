%define oname babelfish

%def_with python3

Name: python-module-%oname
Version: 0.5.5
Release: alt1.dev.git20150124
Summary: A module to work with countries and languages
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/babelfish/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Diaoul/babelfish.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Sphinx-PyPI-upload
BuildPreReq: python-module-sphinx-devel diaoul-sphinx-themes
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Sphinx-PyPI-upload
%endif

%py_provides %oname

%description
BabelFish is a Python library to work with countries and languages.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
BabelFish is a Python library to work with countries and languages.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A module to work with countries and languages
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
BabelFish is a Python library to work with countries and languages.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
BabelFish is a Python library to work with countries and languages.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
BabelFish is a Python library to work with countries and languages.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
BabelFish is a Python library to work with countries and languages.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

rm -fR docs/_themes
cp -fR %_datadir/diaoul-sphinx-themes docs/_themes
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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.5-alt1.dev.git20150124
- Version 0.5.5-dev

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.dev.git20140622
- Initial build for Sisyphus

