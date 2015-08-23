%define oname pandas

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.16.2
Release: alt1

Summary: Python Data Analysis Library
License: BSD
Group: Development/Python

Url: http://pandas.pydata.org/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python
BuildPreReq: libnumpy-devel python-module-Cython xvfb-run
BuildPreReq: python-module-sphinx-devel python-modules-json ipython
BuildPreReq: python-module-pytz python-module-dateutil
BuildPreReq: python-module-nose python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-BeautifulSoup4
BuildPreReq: python-module-numpy-tests python-module-numexpr
BuildPreReq: python-module-scipy python-module-pymysql
BuildPreReq: python-module-psycopg2 python-module-boto
BuildPreReq: python-module-xlrd python-module-openpyxl
BuildPreReq: python-module-xlsxwriter python-module-xlwt-future
BuildPreReq: python-module-httplib2 python-module-oauth2client
BuildPreReq: python-module-apiclient python-module-gflags
BuildPreReq: python-module-tables python-module-rpy2
BuildPreReq: python-module-scikits.statsmodels-tests
BuildPreReq: gcc-c++
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python3-module-Cython
BuildPreReq: python3-module-pytz python3-module-dateutil
BuildPreReq: python3-module-nose python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-BeautifulSoup4
BuildPreReq: python3-module-numpy-tests python3-module-numexpr
BuildPreReq: python3-module-scipy python3-module-pymysql
BuildPreReq: python3-module-psycopg2 python-module-boto
BuildPreReq: python3-module-xlrd python3-module-openpyxl
BuildPreReq: python3-module-xlsxwriter python3-module-xlwt-future
BuildPreReq: python3-module-httplib2 python3-module-oauth2client
BuildPreReq: python3-module-apiclient python3-module-gflags
BuildPreReq: python3-module-tables python3-module-rpy2
BuildPreReq: python3-module-scikits.statsmodels-tests
%endif

%setup_python_module %oname
%py_requires pytz pandas.util.testing dateutil numpy sqlalchemy numexpr
%py_requires scipy boto bs4 xlrd openpyxl xlsxwriter xlwt httplib2 rpy2
%py_requires oauth2client apiclient gflags tables
%py_requires statsmodels.stats.multitest

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

