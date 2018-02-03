%define oname loremipsum

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.0.0
Release: alt1.b2.git20141031.1.1
Summary: A Lorem Ipsum text generator
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/loremipsum/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/monkeython/loremipsum.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-setuptools python-tools-pep8
BuildPreReq: python-module-flake8 python-module-testrepository
BuildPreReq: pylint python-module-hacking python-module-wheel
BuildPreReq: python-module-coverage python-module-coveralls
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-setuptools python3-tools-pep8
BuildPreReq: python3-module-flake8 python3-module-testrepository
BuildPreReq: pylint-py3 python3-module-hacking python3-module-wheel
BuildPreReq: python3-module-coverage python3-module-coveralls
%endif

%py_provides %oname

%description
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A Lorem Ipsum text generator
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains documentation for %oname.

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
pushd %oname
cp -fR samples serialization tests \
	%buildroot%python_sitelibdir/%oname/
popd

%if_with python3
pushd ../python3
%python3_install
pushd %oname
cp -fR samples serialization tests \
	%buildroot%python3_sitelibdir/%oname/
popd
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.b2.git20141031.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.b2.git20141031.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Dec 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.b2.git20141031
- Initial build for Sisyphus

