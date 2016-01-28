%define mname scikits
%define oname %mname.statsmodels

%def_with python3
%def_disable check

Name: python-module-%oname
Epoch: 1
Version: 0.7.0
Release: alt2.git20150731.1
Summary: Statistical computations and models for use with SciPy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/statsmodels/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/statsmodels/statsmodels.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-scipy python-module-pandas
#BuildPreReq: python-module-patsy python-module-matplotlib
#BuildPreReq: python-module-cvxopt python-module-nose
#BuildPreReq: python-module-coverage python-module-zmq
#BuildPreReq: python-module-sphinx-devel pandoc xvfb-run
#BuildPreReq: python-module-matplotlib-sphinxext ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
#BuildPreReq: python3-module-scipy python3-module-pandas
#BuildPreReq: python3-module-patsy python3-module-matplotlib
#BuildPreReq: python3-module-cvxopt python3-module-nose
#BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires numpy scipy pandas patsy matplotlib cvxopt
%py_requires statsmodels.stats.multitest
%add_python_req_skip models

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ca-certificates elfutils fontconfig ipython ipython3 libnumpy-devel python-base python-devel python-module-Numeric python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-Pyro4 python-module-Scientific python-module-apiclient python-module-apsw python-module-babel python-module-certifi python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-cvxopt python-module-cycler python-module-dateutil python-module-decorator python-module-django python-module-docutils python-module-ecdsa python-module-enum34 python-module-fs python-module-functools32 python-module-future python-module-gdata python-module-genshi python-module-greenlet python-module-html5lib python-module-httplib2 python-module-ipykernel python-module-ipython_genutils python-module-jdcal python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-keyczar python-module-keyring python-module-markupsafe python-module-matplotlib python-module-mistune python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-nose python-module-notebook python-module-ntlm python-module-numdifftools python-module-numexpr python-module-numexpr-tests python-module-numpy python-module-numpy-tests python-module-ordereddict python-module-pandas python-module-path python-module-patsy python-module-pexpect python-module-pickleshare python-module-psycopg2 python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycrypto python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-requests python-module-rsa python-module-scikits.statsmodels python-module-scipy python-module-serial python-module-setuptools python-module-simplegeneric python-module-simplejson python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-tables python-module-terminado python-module-tornado python-module-tornado_xstatic python-module-traitlets python-module-twisted-core python-module-urllib3 python-module-wx3.0 python-module-xlrd python-module-xlsxwriter python-module-xlwt-future python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-tkinter python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-apiclient python3-module-apsw python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-cvxopt python3-module-cycler python3-module-dateutil python3-module-django python3-module-docutils python3-module-ecdsa python3-module-enum34 python3-module-fs python3-module-future python3-module-genshi python3-module-greenlet python3-module-html5lib python3-module-httplib2 python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jdcal python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-keyczar python3-module-keyring python3-module-matplotlib python3-module-mpmath python3-module-nbconvert python3-module-nbformat python3-module-ndg-httpsclient python3-module-nose python3-module-ntlm python3-module-numdifftools python3-module-numexpr python3-module-numpy python3-module-numpy-tests python3-module-pandas python3-module-patsy python3-module-pexpect python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pycrypto python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-rsa python3-module-scikits.statsmodels python3-module-scipy python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-sphinx python3-module-tables python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-urllib3 python3-module-xlrd python3-module-xlsxwriter python3-module-xlwt-future python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: fonts-bitmap-misc libnumpy-py3-devel python-module-Cython python-module-alabaster python-module-ipyparallel python-module-matplotlib-sphinxext python-module-numpy-testing python-module-objects.inv python-module-pandas-tests python3-module-Cython python3-module-notebook python3-module-numexpr-tests python3-module-numpy-testing python3-module-pandas-tests rpm-build-python3 time

%description
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip rpy

%description tests
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Statistical computations and models for use with SciPy
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy pandas patsy matplotlib cvxopt
%py3_requires statsmodels.stats.multitest
%add_python3_req_skip models

%description -n python3-module-%oname
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR
%add_python3_req_skip rpy

%description -n python3-module-%oname-tests
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python
%add_python_req_skip load_macrodata var_plots

%description pickles
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Statsmodels is a Python package that provides a complement to scipy for
statistical computations including descriptive statistics and estimation
and inference for statistical models.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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
for i in $(find %buildroot%python_sitelibdir -name '*test*') \
	$(find %buildroot%python_sitelibdir -name '*xamp*')
do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done

%if_with python3
pushd ../python3
%python3_install
for i in $(find %buildroot%python3_sitelibdir -name '*test*') \
	$(find %buildroot%python3_sitelibdir -name '*xamp*')
do
	echo $i |sed 's|%buildroot\(.*\)|%%exclude \1\*|' >>%oname.notests
	echo $i |sed 's|%buildroot\(.*\)|\1\*|' >>%oname.tests
done
popd
%endif

python setup.py build_ext -i
export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
xvfb-run python setup.py test
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test
popd
%endif

%files -f %oname.notests
%doc *.md *.rst README_l1.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files tests -f %oname.tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc examples docs/*.pdf docs/build/html

%if_with python3
%files -n python3-module-%oname -f ../python3/%oname.notests
%doc *.md *.rst README_l1.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/*/*/example*
%exclude %python3_sitelibdir/*/*/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests -f ../python3/%oname.tests
%python3_sitelibdir/*/*/*/*/example*
%python3_sitelibdir/*/*/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:0.7.0-alt2.git20150731.1
- NMU: Use buildreq for BR.

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150731
- New snapshot

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150323
- New snapshot

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt2.git20150216
- Added requires statsmodels.stats.multitest

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.7.0-alt1.git20150216
- Initial build for Sisyphus

