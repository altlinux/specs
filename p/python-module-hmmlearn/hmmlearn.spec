%define oname hmmlearn

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.a.git20141117
Summary: Hidden Markov Models in Python, with scikit-learn like API
License: BSD
Group: Development/Python
Url: https://github.com/hmmlearn/hmmlearn
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hmmlearn/hmmlearn.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython python-module-scikit-learn
BuildPreReq: libnumpy-devel python-module-nose python-module-coverage
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
BuildPreReq: python-module-Pillow texlive-latex-recommended
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python3-module-scikit-learn
BuildPreReq: libnumpy-py3-devel python3-module-nose
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname

%description
HMMlearn is a set of algorithm for learning and inference of Hiden
Markov Models.

Historically, this code was present in scikit-learn, but unmaintained.
It has been orphaned and separated as a different package.

%package -n python3-module-%oname
Summary: Hidden Markov Models in Python, with scikit-learn like API
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
HMMlearn is a set of algorithm for learning and inference of Hiden
Markov Models.

Historically, this code was present in scikit-learn, but unmaintained.
It has been orphaned and separated as a different package.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
HMMlearn is a set of algorithm for learning and inference of Hiden
Markov Models.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
HMMlearn is a set of algorithm for learning and inference of Hiden
Markov Models.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%add_optflags -fno-strict-aliasing
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
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
rm -fR %oname
%make test-coverage
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
rm -fR %oname
%make test-coverage PYTHON=python3 NOSETESTS=nosetests3
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.a.git20141117
- Initial build for Sisyphus

