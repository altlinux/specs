%define oname gensim

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.10.3
Release: alt1.git20141117
Summary: Python framework for fast Vector Space Modelling
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/gensim/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/piskvorky/gensim.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scipy python-module-six
BuildPreReq: python-module-Pyro4 libnumpy-devel
BuildPreReq: python-module-simserver
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy python3-module-six
BuildPreReq: python3-module-Pyro4 libnumpy-py3-devel
%endif

%py_provides %oname
%py_requires simserver

%description
Gensim is a Python library for topic modelling, document indexing and
similarity retrieval with large corpora. Target audience is the natural
language processing (NLP) and information retrieval (IR) community.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Gensim is a Python library for topic modelling, document indexing and
similarity retrieval with large corpora. Target audience is the natural
language processing (NLP) and information retrieval (IR) community.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python framework for fast Vector Space Modelling
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Gensim is a Python library for topic modelling, document indexing and
similarity retrieval with large corpora. Target audience is the natural
language processing (NLP) and information retrieval (IR) community.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Gensim is a Python library for topic modelling, document indexing and
similarity retrieval with large corpora. Target audience is the natural
language processing (NLP) and information retrieval (IR) community.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Gensim is a Python library for topic modelling, document indexing and
similarity retrieval with large corpora. Target audience is the natural
language processing (NLP) and information retrieval (IR) community.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Gensim is a Python library for topic modelling, document indexing and
similarity retrieval with large corpora. Target audience is the natural
language processing (NLP) and information retrieval (IR) community.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/src/

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
%make -C docs/src pickle
%make -C docs/src html

cp -fR docs/src/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/src/_build/html/*

%files tests
%python_sitelibdir/*/test

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test
%endif

%changelog
* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.git20141117
- Version 0.10.3

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt2.git20140918
- Added necessary requirements

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.2-alt1.git20140918
- Initial build for Sisyphus

