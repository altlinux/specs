%define oname pandas

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.16.2
Release: alt1.1

Summary: Python Data Analysis Library
License: BSD
Group: Development/Python

Url: http://pandas.pydata.org/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
#BuildPreReq: libnumpy-devel python-module-Cython xvfb-run
#BuildPreReq: python-module-sphinx-devel python-modules-json ipython
#BuildPreReq: python-module-pytz python-module-dateutil
#BuildPreReq: python-module-nose python-module-setuptools-tests
#BuildPreReq: python-module-SQLAlchemy python-module-BeautifulSoup4
#BuildPreReq: python-module-numpy-tests python-module-numexpr
#BuildPreReq: python-module-scipy python-module-pymysql
#BuildPreReq: python-module-psycopg2 python-module-boto
#BuildPreReq: python-module-xlrd python-module-openpyxl
#BuildPreReq: python-module-xlsxwriter python-module-xlwt-future
#BuildPreReq: python-module-httplib2 python-module-oauth2client
#BuildPreReq: python-module-apiclient python-module-gflags
#BuildPreReq: python-module-tables python-module-rpy2
#BuildPreReq: python-module-scikits.statsmodels-tests
#BuildPreReq: gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel libnumpy-py3-devel python3-module-Cython
#BuildPreReq: python3-module-pytz python3-module-dateutil
#BuildPreReq: python3-module-nose python3-module-setuptools-tests
#BuildPreReq: python3-module-SQLAlchemy python3-module-BeautifulSoup4
#BuildPreReq: python3-module-numpy-tests python3-module-numexpr
#BuildPreReq: python3-module-scipy python3-module-pymysql
#BuildPreReq: python3-module-psycopg2 python-module-boto
#BuildPreReq: python3-module-xlrd python3-module-openpyxl
#BuildPreReq: python3-module-xlsxwriter python3-module-xlwt-future
#BuildPreReq: python3-module-httplib2 python3-module-oauth2client
#BuildPreReq: python3-module-apiclient python3-module-gflags
#BuildPreReq: python3-module-tables python3-module-rpy2
#BuildPreReq: python3-module-scikits.statsmodels-tests
%endif

%setup_python_module %oname
%py_requires pytz pandas.util.testing dateutil numpy sqlalchemy numexpr
%py_requires scipy boto bs4 xlrd openpyxl xlsxwriter xlwt httplib2 rpy2
%py_requires oauth2client apiclient gflags tables
%py_requires statsmodels.stats.multitest

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libstdc++-devel python-base python-devel python-module-Numeric python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-Pyro4 python-module-Scientific python-module-apiclient python-module-apsw python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-django python-module-docutils python-module-ecdsa python-module-enum34 python-module-fs python-module-functools32 python-module-future python-module-gdata python-module-genshi python-module-greenlet python-module-html5lib python-module-httplib2 python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jdcal python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-keyczar python-module-keyring python-module-markupsafe python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-numdifftools python-module-numexpr python-module-numexpr-tests python-module-numpy python-module-numpy-tests python-module-ordereddict python-module-pandas python-module-path python-module-pexpect python-module-pickleshare python-module-psycopg2 python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycrypto python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-rsa python-module-scipy python-module-serial python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-tables python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-twisted-core python-module-wx3.0 python-module-xlrd python-module-xlsxwriter python-module-xlwt-future python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-tkinter python-modules-unittest python-modules-wsgiref python3 python3-base python3-dev python3-module-Pygments python3-module-apiclient python3-module-apsw python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-cvxopt python3-module-django python3-module-docutils python3-module-ecdsa python3-module-enum34 python3-module-fs python3-module-future python3-module-genshi python3-module-greenlet python3-module-html5lib python3-module-httplib2 python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jdcal python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-keyczar python3-module-keyring python3-module-matplotlib python3-module-mpmath python3-module-nbconvert python3-module-nbformat python3-module-ndg-httpsclient python3-module-nose python3-module-ntlm python3-module-numdifftools python3-module-numpy python3-module-numpy-tests python3-module-pandas python3-module-pexpect python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pycrypto python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-rsa python3-module-scipy python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-tables python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-urllib3 python3-module-xlrd python3-module-xlwt-future python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: gcc-c++ libnumpy-devel python-module-Cython python-module-notebook python-module-numpy-testing python-module-objects.inv python3-module-Cython python3-module-notebook python3-module-numpy-testing rpm-build-python3 time

%description
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

%package -n python3-module-%oname
Summary: Python Data Analysis Library
Group: Development/Python3
%py3_requires pytz pandas.util.testing dateutil numpy sqlalchemy numexpr
%py3_requires scipy boto bs4 xlrd openpyxl xlsxwriter xlwt httplib2 rpy2
%py3_requires oauth2client apiclient gflags tables statsmodels
%py3_requires statsmodels.stats.multitest

%description -n python3-module-%oname
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

%package -n python3-module-%oname-tests
Summary: Tests for pandas
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%py3_requires numpy.ma.testutils pymysql psycopg2

%description -n python3-module-%oname-tests
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains tests for pandas.

%package tests
Summary: Tests for pandas
Group: Development/Python
Requires: %name = %EVR
%py_requires numpy.ma.testutils pymysql psycopg2

%description tests
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains tests for pandas.

%package docs
Summary: Documentation for pandas
Group: Development/Documentation
BuildArch: noarch

%description docs
pandas is an open source, BSD-licensed library providing
high-performance, easy-to-use data structures and data analysis tools
for the Python programming language.

This package contains documentation for pandas.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

sed -i 's|@PYPATH@|%buildroot%python_sitelibdir|' doc/make.py

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

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

pushd doc
./make.py html
popd

%check
xvfb-run python setup.py test
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/test*

%files docs
%doc doc/build/html
#doc doc/source
#doc examples

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.16.2-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.2-alt1
- Version 0.16.2

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.2-alt1
- Version 0.15.2

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.1-alt1
- Version 0.15.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt2
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1
- Version 0.14.1

* Thu Nov 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt3
- Applied repocop patch

* Wed Nov 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt2
- Fixed build

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.0-alt1
- Version 0.12.0

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.1-alt1
- Initial build for Sisyphus

