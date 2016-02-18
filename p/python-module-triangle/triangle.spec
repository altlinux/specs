%define oname triangle

%def_with python3

Name: python-module-%oname
Version: 2013.04.05
Release: alt1.git20141030.1
Summary: Python wrapper for libtriangle
License: LGPL
Group: Development/Python
Url: http://dzhelil.info/triangle/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/drufat/triangle.git
Source: %name-%version.tar

#BuildPreReq: libtriangle-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-matplotlib python-module-nose
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: python-module-matplotlib-sphinxext
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-matplotlib python3-module-nose
%endif

%py_provides %oname
%py_requires numpy matplotlib

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils fontconfig ipython ipython3 python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-notebook python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xz
BuildRequires: libtriangle-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-matplotlib-sphinxext python-module-nose python-module-numpy-testing python-module-objects.inv python-module-pytest python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing rpm-build-python3 time

%description
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper for libtriangle
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy matplotlib

%description -n python3-module-%oname
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Python Triangle is a python wrapper around Jonathan Richard Shewchuk's
two-dimensional quality mesh generator and delaunay triangulator
library.

This package contains documentation for %oname.

%prep
%setup

rm -fR c

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
pushd doc
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
nosetests3 -v
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2013.04.05-alt1.git20141030.1
- NMU: Use buildreq for BR.

* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2013.04.05-alt1.git20141030
- Initial build for Sisyphus

