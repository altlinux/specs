%define oname aiohttp

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.15.3
Release: alt5.git20150425
Summary: http client/server for asyncio
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiohttp/

# https://github.com/KeepSafe/aiohttp.git
Source: %name-%version.tar

%if_with python2
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: ca-certificates elfutils ipython3 python-base python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-dev python3-module-Pygments python3-module-asyncio python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-django python3-module-dns python3-module-docutils python3-module-enum34 python3-module-future python3-module-genshi python3-module-greenlet python3-module-gunicorn python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-mccabe python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-paste python3-module-pexpect python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface python3-pyflakes python3-tools-pep8 xz
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib  python3-module-Cython  python3-module-flake8 python3-module-html5lib python3-module-nose python3-module-notebook python3-module-setuptools-tests rpm-build-python3 time
BuildRequires: python-sphinx-objects.inv

#BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-trollius python-module-nose
#BuildPreReq: python-module-gunicorn 
BuildPreReq: python-module-gunicorn python-module-chardet
BuildPreReq: python3-module-objects
#BuildPreReq: python-module-flake8 python-module-coverage
#BuildPreReq: python-module-path 
#python-module-bumpversion
#BuildPreReq: python-module-Cython
BuildPreReq: python-module-sphinx-devel
%endif
#python-module-alabaster
%if_with python3
BuildRequires(pre): rpm-macros-sphinx
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): python3-devel
BuildRequires(pre): python-module-sphinx-devel 
BuildRequires(pre): python-module-sphinx 
#BuildRequires: python3-module-Cython python3-module-aiohttp python3-module-flake8 python3-module-html5lib python3-module-nose python3-module-notebook
BuildPreReq:  python3-module-setuptools
BuildPreReq:  python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio
BuildPreReq: python-sphinx-objects.inv
BuildPreReq: python3-module-trollius python3-module-nose
BuildPreReq: python3-module-gunicorn python3-module-chardet
#BuildPreReq: python3-module-flake8 python3-module-coverage
#BuildPreReq: python3-module-path 
#python3-module-bumpversion
#BuildPreReq: python3-module-Cython
%endif

%py_provides %oname
#%py_requires trollius chardet

%description
http client/server for asyncio (PEP-3156).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: http client/server for asyncio
Group: Development/Python3
%py3_provides %oname
#%py3_requires asyncio chardet

%description -n python3-module-%oname
http client/server for asyncio (PEP-3156).

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
http client/server for asyncio (PEP-3156).

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
http client/server for asyncio (PEP-3156).

This package contains documentation for %oname.

%prep
%setup

%if_with python3
rm -rf ../python3
cp -R . ../python3
%endif

%if_with python2
find -type f -name '*.py' -exec \
	sed -i 's|asyncio.streams|trollius.streams|g' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|import asyncio|import trollius|' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|from asyncio|from trollius|' '{}' +
%prepare_sphinx .
%endif
%if_with python3
find -type f -name '*.py' -exec \
	sed -i 's|asyncio.streams|trollius.streams|g' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|import asyncio|import trollius|' '{}' +
find -type f -name '*.py' -exec \
	sed -i 's|from asyncio|from trollius|' '{}' +
%prepare_sphinx .
%endif
ln -s ../objects.inv docs/

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif
%if_with python3
#export SPHINXBUILD=%_bindir/py3_sphinx-build
#%make -C docs pickle  SPHINXBUILD=%_bindir/py3_sphinx-build
#%make -C docs html SPHINXBUILD=%_bindir/py3_sphinx-build

%make -C docs pickle
%make -C docs html
%endif
%if_with python2
%make -C docs pickle
%make -C docs html
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -R docs/_build/pickle %buildroot%python_sitelibdir/%oname/

rm requirements*

%check
%if_with python2
python setup.py test
nosetests -s -v ./tests/
%endif
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
sed -i 's|flake8|python3-flake8|' Makefile
nosetests3 -s -v ./tests/
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*
%endif

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Thu Mar  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt5.git20150425
- (.spec) Safer build: cleanup ../python3/ before use.
  (Nevertheless, beware: using ../python3/ for the build is very dirty
  because it is not cleaned up automatically afterwards and can cause
  side-effects in other unsafe specs, similar to this one. This dirty
  use of ../python3/ is very wide-spread in Sisyphus packages.)
- (.spec) Fail if the maintainer's intentions are not fulfilled
  (because the sources or the build environment have changed since the
  spec was written): rm/cp without -f

* Thu Mar 03 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt4.git20150425.2
- Remove self dependence.

* Wed Mar 02 2016 Denis Medvedev <nbr@altlinux.org>  0.15.3-alt3.git20150425.2
- File "inv"  for sphynx is in python-sphinx-objects.inv. 

* Mon Feb 08 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt2.git20150425.2
- NMU: manual build

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.15.3-alt2.git20150425.1
- NMU: Use buildreq for BR.

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 0.15.3-alt2.git20150425
- rebuild with cleaned build requires

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.3-alt1.git20150425
- Version 0.15.3

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20150217
- Version 0.14.4

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1.git20150123
- Version 0.14.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2.git20141231
- Version 0.13.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.a0.git20141229
- Version 0.13.1a0

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20141129
- Version 0.11.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.a.git20141125
- Initial build for Sisyphus

