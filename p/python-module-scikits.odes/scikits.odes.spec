%define mname scikits
%define oname %mname.odes

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 2.1.0
Release: alt1.git20150417.1
Summary: Ordinary differential equation anddifferential algebraic equation solvers
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikits.odes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bmcage/odes.git
Source: %name-%version.tar

#BuildPreReq: gcc-c++ gcc-fortran libsundials-devel liblapack-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-scipy python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-scipy python3-module-nose
%endif

%py_provides %oname
%py_requires %mname numpy scipy

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libgfortran-devel libnumpy-devel libopenblas-devel libquadmath-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xz
BuildRequires: gcc-fortran liblapack-devel libnumpy-py3-devel libsundials-devel python-module-Cython python-module-html5lib python-module-nose python-module-notebook python-module-numpy-testing python-module-scipy python-module-setuptools-tests python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-scipy python3-module-setuptools-tests rpm-build-python3 time

%description
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires nose

%description tests
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Ordinary differential equation anddifferential algebraic equation solvers
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname numpy scipy

%description -n python3-module-%oname
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires nose

%description -n python3-module-%oname-tests
Odes is a scikit toolkit for scipy to add some extra ode solvers.
Present are

1. sundials python interface tocvode, ida
2. ddaspk
3. lsodi

At present it provides dae solvers you can use, extending the
capabilities offered in scipy.integrade.ode.

This package contains tests for %oname.

%prep
%setup

for i in sundials cvode cvodes ida idas kinsol nvector
do
	rm -fR scikits/odes/sundials/$i
	ln -s %_includedir/sundials-double/$i scikits/odes/sundials/
done

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags %optflags_shared -fno-strict-aliasing
%add_optflags -I%_includedir/openblas
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

%check
python setup.py test
export PYTHONPATH=%buildroot%python_sitelibdir
pushd ~
nosetests -v
popd
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ~
nosetests3 -v
popd
popd
%endif

%files
%doc README docs/src/examples
%python_sitelibdir/%mname/odes
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/odes/tests

%files tests
%python_sitelibdir/%mname/odes/tests

%if_with python3
%files -n python3-module-%oname
%doc README docs/src/examples
%python3_sitelibdir/%mname/odes
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%mname/odes/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/%mname/odes/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:2.1.0-alt1.git20150417.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.1.0-alt1.git20150417
- Version 2.1.0

* Sat Feb 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.2-alt1.git20150123
- Initial build for Sisyphus

