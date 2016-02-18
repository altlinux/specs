%define oname mozsci

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.git20150127.1
Summary: Data science tools from Moz
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mozsci/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/seomoz/mozsci.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests gcc-c++
#BuildPreReq: python-module-scipy libnumpy-devel python-modules-json
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-Cython python-module-simplejson
#BuildPreReq: python-module-scikit-learn python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-scipy libnumpy-py3-devel
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-Cython python3-module-simplejson
#BuildPreReq: python3-module-scikit-learn python3-module-six
%endif

%py_provides %oname
%py_requires scipy numpy simplejson json sklearn six

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libstdc++-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-scipy python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-scipy python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: gcc-c++ libnumpy-devel python-module-Cython python-module-html5lib python-module-nose python-module-notebook python-module-numpy-testing python-module-scikit-learn python-module-setuptools-tests python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-scikit-learn python3-module-setuptools-tests rpm-build-python3

%description
A grab bag of assorted Data science tools from Moz.

%package -n python3-module-%oname
Summary: Data science tools from Moz
Group: Development/Python3
%py3_provides %oname
%py3_requires scipy numpy simplejson json sklearn six

%description -n python3-module-%oname
A grab bag of assorted Data science tools from Moz.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md test
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md test
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.2-alt1.git20150127.1
- NMU: Use buildreq for BR.

* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20150127
- Initial build for Sisyphus

