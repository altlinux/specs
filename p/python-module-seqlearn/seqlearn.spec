%define oname seqlearn

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140922
Summary: Sequence learning toolkit for Python
License: MIT
Group: Development/Python
Url: http://larsmans.github.io/seqlearn/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/larsmans/seqlearn.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-scipy python-module-scikit-learn
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-scikit-learn
%endif

%py_provides %oname

%description
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Sequence learning toolkit for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
mv %oname %oname.bak
%make -C doc pickle
%make -C doc html
mv %oname.bak %oname

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
#if_with python3
%if 0
pushd ../python3
rm -fR build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140922
- Initial build for Sisyphus

