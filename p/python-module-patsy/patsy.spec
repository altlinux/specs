%define oname patsy

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.1

Summary: A Python package for describing statistical models and for building design matrices
License: BSD
Group: Development/Python
Url: http://patsy.readthedocs.org/en/latest/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-sphinx-devel
#BuildPreReq: libnumpy-devel python-module-matplotlib ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: fontconfig ipython python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-notebook python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base
BuildRequires: python-module-alabaster python-module-html5lib python-module-ipyparallel python-module-numpy-testing python-module-objects.inv python3-module-setuptools rpm-build-python3 time

#BuildRequires: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%description
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

%package tests
Summary: Tests for patsy
Group: Development/Python
Requires: %name = %EVR

%description tests
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains tests for patsy.

%package pickles
Summary: Pickles for patsy
Group: Development/Python

%description pickles
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains pickles for patsy.

%package docs
Summary: Documentation for patsy
Group: Development/Documentation

%description docs
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains documentation for patsy.

%if_with python3
%package -n python3-module-%oname
Summary: A Python package for describing statistical models and for building design matrices
Group: Development/Python3

%description -n python3-module-%oname
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

%package -n python3-module-%oname-tests
Summary: Tests for patsy
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A Python package for describing statistical models and for building
design matrices. It is closely inspired by and compatible with the
'formula' mini-language used in R and S.

This package contains tests for patsy.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
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

%make -C doc pickle
%make -C doc html

%install
%python_build_install

%if_with python3
pushd ../python3
%python3_build_install
popd
%endif

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc *.rst TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test_*

%files tests
%python_sitelibdir/*/test_*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test_*
%exclude %python3_sitelibdir/*/__pycache__/test_*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test_*
%python3_sitelibdir/*/__pycache__/test_*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Thu Oct 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

