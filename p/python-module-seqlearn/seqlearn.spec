%define _unpackaged_files_terminate_build 1
%define oname seqlearn

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: Sequence learning toolkit for Python
License: MIT
Group: Development/Python
Url: http://larsmans.github.io/seqlearn/
Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/larsmans/seqlearn.git
Source0: https://pypi.python.org/packages/25/2c/95da36839f647a6b15da1fd10f68d755c7fca549c92aabb3ff734f5c682c/%{oname}-%{version}.tar.gz

BuildPreReq: libnumpy-devel
BuildPreReq: python-devel
BuildPreReq: python-module-Cython
BuildPreReq: python-module-nose
BuildPreReq: python-module-notebook
BuildPreReq: python-module-numpy-testing
BuildPreReq: python-module-pytest
BuildPreReq: python-module-scikit-learn
BuildPreReq: python-module-sphinx
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-scipy python-module-scikit-learn
#BuildPreReq: python-module-nose
#BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-Cython
BuildPreReq: python3-module-numpy-testing
BuildPreReq: python3-module-pytest
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-scipy python3-module-scikit-learn
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-numpydoc python-module-pexpect python-module-pluggy python-module-ptyprocess python-module-py python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-scipy python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-numpy python3-module-zope
#BuildRequires: libnumpy-devel python-module-Cython python-module-alabaster python-module-html5lib python-module-nose python-module-notebook python-module-numpy-testing python-module-objects.inv python-module-pytest python-module-scikit-learn python3-module-Cython python3-module-numpy-testing rpm-build-python3 python3-module-pytest

%description
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Sequence learning toolkit for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
seqlearn is a sequence classification toolkit for Python. It is designed
to extend scikit-learn and offer as similar as possible an API.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
rm -rf ../python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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
mv %oname %oname.bak
%make -C doc pickle
%make -C doc html
mv %oname.bak %oname

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
#if_with python3
%if 0
pushd ../python3
rm -fR build
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- automated PyPI update

* Mon Mar 28 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20150324.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sat Mar 26 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.git20150324.2
- NMU: Fixed BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20150324.1
- NMU: Use buildreq for BR.

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150324
- New snapshot

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140922
- Initial build for Sisyphus

