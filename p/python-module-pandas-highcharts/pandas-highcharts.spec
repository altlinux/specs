%define _unpackaged_files_terminate_build 1
%define oname pandas-highcharts

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.5.2
Release: alt1
Summary: Easily build Highcharts plots with pandas.DataFrame objects
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pandas-highcharts/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gtnx/pandas-highcharts.git
Source0: https://pypi.python.org/packages/1a/70/fe7201bb6750e26dbf662d5b0f12fe6d41a4e3edf5e49314597913026bd1/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildRequires: python-devel python-module-setuptools-tests
#BuildRequires: python-module-pandas python-module-pytz
#BuildRequires: python-module-numpy ipython
#BuildRequires: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildRequires: python3-module-pandas python3-module-pytz
#BuildRequires: python3-module-numpy ipython3
#BuildRequires: python-tools-2to3
%endif

%py_provides pandas_highcharts
%py_requires pandas pytz json numpy IPython

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: ipython ipython3 python-base python-devel python-module-Numeric python-module-PyStemmer python-module-Pygments python-module-Pyro4 python-module-Scientific python-module-apsw python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-django python-module-docutils python-module-ecdsa python-module-enum34 python-module-fs python-module-functools32 python-module-future python-module-gdata python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-keyczar python-module-matplotlib python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-psycopg2 python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycrypto python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-scipy python-module-serial python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-twisted-core python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-yaml python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-modules-wsgiref python-tools-2to3 python3 python3-base python3-module-Pygments python3-module-apsw python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-cssselect python3-module-django python3-module-docutils python3-module-ecdsa python3-module-enum34 python3-module-fs python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jdcal python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-keyczar python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-ndg-httpsclient python3-module-ntlm python3-module-numpy python3-module-pexpect python3-module-psycopg2 python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pycrypto python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-scipy python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-urllib3 python3-module-xstatic python3-module-xstatic-term.js python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: python-module-apiclient python-module-coverage python-module-html5lib python-module-httplib2 python-module-jdcal python-module-keyring python-module-nose python-module-notebook python-module-numdifftools python-module-numpy-tests python-module-ordereddict python-module-pytest python-module-rsa python-module-tables python-module-xlrd python-module-xlwt python3-module-apiclient python3-module-coverage python3-module-cvxopt python3-module-html5lib python3-module-httplib2 python3-module-keyring python3-module-mpmath python3-module-nose python3-module-notebook python3-module-numdifftools python3-module-numpy-tests python3-module-rsa python3-module-tables python3-module-xlrd python3-module-xlwt rpm-build-python3 time

%description
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%add_python_req_skip core

%description tests
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Easily build Highcharts plots with pandas.DataFrame objects
Group: Development/Python3
%py3_provides pandas_highcharts
%py3_requires pandas pytz json numpy IPython

%description -n python3-module-%oname
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
pandas-highcharts is a Python package which allows you to easily build
Highcharts plots with pandas.DataFrame objects.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python -m unittest -v pandas_highcharts.tests
%if_with python3
pushd ../python3
python3 setup.py test
python3 -m unittest -v pandas_highcharts.tests
popd
%endif

%files
%doc *.rst *.ipynb
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *.ipynb
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- automated PyPI update

* Sat May 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt2.git20150228
- NMU: rebuild with xlwt

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.0-alt1.git20150228.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.0-alt1.git20150228.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150228
- Initial build for Sisyphus

