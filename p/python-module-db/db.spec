%define oname db

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.2
Release: alt1.git20150317.1.1
Summary: A db package that doesn't suck
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/db.py/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/yhat/db.py.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-prettytable python-module-pandas
#BuildPreReq: python-module-pybars3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-prettytable python3-module-pandas
#BuildPreReq: python3-module-pybars3
%endif

%py_provides %oname
%py_requires prettytable pandas pybars3

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: ipython ipython3 python-base python-devel python-module-Numeric python-module-PyStemmer python-module-Pygments python-module-Pyro4 python-module-Scientific python-module-apsw python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-django python-module-docutils python-module-ecdsa python-module-enum34 python-module-fs python-module-functools32 python-module-future python-module-gdata python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-keyczar python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-psycopg2 python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycrypto python-module-pycurl python-module-pygobject3 python-module-pymeta3 python-module-pyparsing python-module-pytz python-module-scipy python-module-serial python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-twisted-core python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-Pygments python3-module-apsw python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-django python3-module-docutils python3-module-ecdsa python3-module-enum34 python3-module-fs python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jdcal python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-keyczar python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-ndg-httpsclient python3-module-ntlm python3-module-numpy python3-module-pexpect python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pycrypto python3-module-pygobject3 python3-module-pymeta3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-scipy python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-urllib3 python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: python-module-apiclient python-module-coverage python-module-html5lib python-module-httplib2 python-module-jdcal python-module-keyring python-module-nose python-module-notebook python-module-numdifftools python-module-numpy-tests python-module-ordereddict python-module-pybars3 python-module-pytest python-module-rsa python-module-tables python-module-xlrd python-module-xlwt-future python3-module-apiclient python3-module-coverage python3-module-cvxopt python3-module-html5lib python3-module-httplib2 python3-module-keyring python3-module-mpmath python3-module-nose python3-module-notebook python3-module-numdifftools python3-module-numpy-tests python3-module-pybars3 python3-module-rsa python3-module-tables python3-module-xlrd python3-module-xlwt-future rpm-build-python3

%description
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

db.py uses `pandas` to manage data, so if you're already using pandas,
db.py should feel pretty natural. It's also fully compatible with the
IPython Notebook, so not only is db.py extremely functional, it's also
pretty.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A db package that doesn't suck
Group: Development/Python3
%py3_provides %oname
%py3_requires prettytable pandas pybars3

%description -n python3-module-%oname
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

db.py uses `pandas` to manage data, so if you're already using pandas,
db.py should feel pretty natural. It's also fully compatible with the
IPython Notebook, so not only is db.py extremely functional, it's also
pretty.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
db.py is an easier way to interact with your databases. It makes it
easier to explore tables, columns, views, etc. It puts the emphasis on
user interaction, information display, and providing easy to use helper
functions.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export LC_ALL=en_US.UTF-8
nosetests -v
%if_with python3
pushd ../python3
nosetests3 -v
popd
%endif

%files
%doc CHANGES.txt *.rst docs/* examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt *.rst docs/* examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150317.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150317.1
- NMU: Use buildreq for BR.

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150317
- Version 0.4.2

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20150208
- Initial build for Sisyphus

