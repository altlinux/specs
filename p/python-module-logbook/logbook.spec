%define oname logbook

%def_with python3

Name: python-module-%oname
Version: 0.7.1
Release: alt1.dev.git20141012.1
Summary: A logging replacement for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Logbook/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mitsuhiko/logbook.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython python-module-sphinx-devel
#BuildPreReq: python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython
#BuildPreReq: python3-module-py
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-pluggy python-module-ptyprocess python-module-py python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: python-module-Cython python-module-alabaster python-module-html5lib python-module-notebook python-module-objects.inv python-module-setuptools-tests python3-module-Cython python3-module-html5lib python3-module-notebook python3-module-setuptools-tests rpm-build-python3 time

%description
An awesome logging implementation that is fun to use.

%package -n python3-module-%oname
Summary: A logging replacement for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
An awesome logging implementation that is fun to use.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
An awesome logging implementation that is fun to use.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
An awesome logging implementation that is fun to use.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
export USE_CYTHON=1
CFLAGS="%optflags" python scripts/travis_build.py
%python_build_debug

%if_with python3
pushd ../python3
CFLAGS="%optflags" python3 scripts/travis_build.py
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
%doc AUTHORS CHANGES *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.1-alt1.dev.git20141012.1
- NMU: Use buildreq for BR.

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.dev.git20141012
- Initial build for Sisyphus

