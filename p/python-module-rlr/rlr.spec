%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname rlr

%def_with python3

Name: python-module-%oname
Version: 2.4
#Release: alt1.git20150507.1.1
Summary: Regularized Logistic Regression
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rlr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/rlr.git
Source0: https://pypi.python.org/packages/f5/ba/17477a212565149877891eb05b8728f91e3a9cb34b61e0858dea8620728c/%{oname}-%{version}.tar.gz

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel python-module-nose
#BuildPreReq: python-module-pylbfgs
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel python3-module-nose
#BuildPreReq: python3-module-pylbfgs
%endif

%py_provides %oname
%py_requires numpy pylbfgs

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ipython ipython3 python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface xz
BuildRequires: python-module-Cython python-module-html5lib python-module-nose python-module-notebook python-module-numpy-testing python-module-pylbfgs python-module-setuptools-tests python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-pylbfgs python3-module-setuptools-tests rpm-build-python3 time

%description
A Cython implementation of L2 regularized logistic regression.

%package -n python3-module-%oname
Summary: Regularized Logistic Regression
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy pylbfgs

%description -n python3-module-%oname
A Cython implementation of L2 regularized logistic regression.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
#cython rlr/lr.pyx
%python_build_debug

%if_with python3
pushd ../python3
#cython3 rlr/lr.pyx
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

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test build_ext -i
nosetests3 -v
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150507.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20150507.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20150507.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20150507
- Version 1.5

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141119
- Initial build for Sisyphus

