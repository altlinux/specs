%define oname ipyparallel

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 4.1.0
Release: alt1.dev.git20150819.1.1
Summary: Interactive Parallel Computing with IPython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ipyparallel
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ipython/ipyparallel.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-ipython_genutils python-module-decorator
#BuildPreReq: python-module-zmq ipython python-module-nose
#BuildPreReq: python-module-jupyter_client python-module-ipykernel
#BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-ipython_genutils python3-module-decorator
#BuildPreReq: python3-module-zmq ipython3 python3-module-nose
#BuildPreReq: python3-module-jupyter_client python3-module-ipykernel
%endif

%py_provides %oname
%py_requires ipython_genutils decorator zmq IPython jupyter_client
%py_requires ipykernel

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ipython python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python3 python3-base
BuildRequires: python-module-alabaster python-module-html5lib python-module-nose python-module-notebook python-module-objects.inv python-module-pytest python3-module-zope rpm-build-python3 time

%description
Use multiple instances of IPython in parallel, interactively.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Use multiple instances of IPython in parallel, interactively.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Interactive Parallel Computing with IPython
Group: Development/Python3
%py3_provides %oname
%py3_requires ipython_genutils decorator zmq IPython jupyter_client
%py3_requires ipykernel

%description -n python3-module-%oname
Use multiple instances of IPython in parallel, interactively.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Use multiple instances of IPython in parallel, interactively.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Use multiple instances of IPython in parallel, interactively.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Use multiple instances of IPython in parallel, interactively.

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
	mv $i ip-$i.py3
done
popd
%endif

%python_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ip-$i
done
popd

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
iptest2 --coverage xml ipyparallel.tests
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
iptest3 --coverage xml ipyparallel.tests
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

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/build/html

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.dev.git20150819.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.0-alt1.dev.git20150819.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1.dev.git20150819
- Initial build for Sisyphus

