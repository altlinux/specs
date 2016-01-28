%define oname nbconvert

%def_with python3
#def_disable check

Name: python-module-%oname
Version: 4.0.0
Release: alt2.1
Summary: Converting Jupyter Notebooks
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/nbconvert
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests pandoc
#BuildPreReq: python-module-mistune python-module-jinja2
#BuildPreReq: python-module-Pygments python-module-traitlets-tests
#BuildPreReq: python-module-jupyter_core python-module-nbformat
#BuildPreReq: python-module-nose python-module-ipykernel
#BuildPreReq: python-module-tornado python-module-jupyter_client
#BuildPreReq: python-module-ipython_genutils-tests
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-mistune python3-module-jinja2
#BuildPreReq: python3-module-Pygments python3-module-traitlets-tests
#BuildPreReq: python3-module-jupyter_core python3-module-nbformat
#BuildPreReq: python3-module-nose python3-module-ipykernel
#BuildPreReq: python3-module-tornado python3-module-jupyter_client
#BuildPreReq: python3-module-ipython_genutils-tests
%endif

%py_provides %oname
%py_requires mistune jinja2 pygments traitlets jupyter_core nbformat
%py_requires tornado jupyter_client

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ipython ipython3 python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-certifi python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-mistune python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-requests python-module-setuptools python-module-simplegeneric python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado python-module-tornado_xstatic python-module-traitlets python-module-urllib3 python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-Pygments python3-module-asyncio python3-module-babel python3-module-certifi python3-module-cffi python3-module-chardet python3-module-cssselect python3-module-decorator python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-markupsafe python3-module-matplotlib python3-module-mistune python3-module-nbconvert python3-module-nbformat python3-module-nose python3-module-numpy python3-module-path python3-module-pexpect python3-module-pickleshare python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-simplegeneric python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom python3-module-yieldfrom.http python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface python3-modules-sqlite3 xz
BuildRequires: pandoc python-module-alabaster python-module-html5lib python-module-ipython_genutils-tests python-module-notebook python-module-objects.inv python-module-pytest python-module-traitlets-tests python3-module-html5lib python3-module-ipython_genutils-tests python3-module-jinja2-tests python3-module-notebook python3-module-traitlets-tests rpm-build-python3 time

%description
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Converting Jupyter Notebooks
Group: Development/Python3
%py3_provides %oname
%py3_requires mistune jinja2 pygments traitlets jupyter_core nbformat
%py3_requires tornado jupyter_client

%description -n python3-module-%oname
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Jupyter nbconvert converts notebooks to various other formats via Jinja
templates.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

export PYTHONPATH=$PWD
export PATH=$PATH:%buildroot%_bindir
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export LC_ALL=en_US.UTF-8
export PYTHONPATH=$PWD
nosetests -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
nosetests3 -vv
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.0-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- Enabled check

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus

