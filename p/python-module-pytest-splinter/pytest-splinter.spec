%define oname pytest-splinter

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.2.11
Release: alt1.git20150319.1
Summary: Splinter plugin for pytest testing framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-splinter/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pytest-dev/pytest-splinter.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-tox python-module-splinter
#BuildPreReq: python-module-detox python-module-mock
#BuildPreReq: python-module-pytest-localserver
#BuildPreReq: python-module-pytest-pep8 python-module-pytest-cov
#BuildPreReq: python-module-virtualenv python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-tox python3-module-splinter
#BuildPreReq: python3-module-detox python3-module-mock
#BuildPreReq: python3-module-pytest-localserver
#BuildPreReq: python3-module-pytest-pep8 python3-module-pytest-cov
#BuildPreReq: python3-module-virtualenv
%endif

%py_provides pytest_splinter

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-WSGIProxy2 python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-dns python-module-enum34 python-module-genshi python-module-greenlet python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pytest python-module-pytest-cache python-module-pytz python-module-restkit python-module-rlcompleter2 python-module-setuptools python-module-tox python-module-waitress python-module-webtest python-module-zope.cachedescriptors python-module-zope.event python-module-zope.exceptions python-module-zope.interface python-module-zope.schema python-module-zope.testing python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python-tools-pep8 python3 python3-base python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cryptography python3-module-cssselect python3-module-dns python3-module-enum34 python3-module-genshi python3-module-greenlet python3-module-html5lib python3-module-ntlm python3-module-paste python3-module-pip python3-module-psycopg2 python3-module-pycparser python3-module-pytest python3-module-pytest-cache python3-module-pytest-pep8 python3-module-pytz python3-module-setuptools python3-module-tox python3-module-virtualenv python3-module-waitress python3-module-webtest python3-module-wsgiproxy python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zope python3-module-zope.interface
BuildRequires: python-module-detox python-module-pbr python-module-pytest-cov python-module-pytest-localserver python-module-pytest-pep8 python-module-setuptools-tests python-module-unittest2 python-module-virtualenv python-module-zope.testbrowser python3-module-detox python3-module-pbr python3-module-pytest-cov python3-module-pytest-localserver python3-module-setuptools-tests python3-module-unittest2 python3-module-zope.testbrowser python3-tools-pep8 rpm-build-python3

%description
pytest spinter and selenium integration for anyone interested in browser
interaction in tests.

%package -n python3-module-%oname
Summary: Splinter plugin for pytest testing framework
Group: Development/Python3
%py3_provides pytest_splinter

%description -n python3-module-%oname
pytest spinter and selenium integration for anyone interested in browser
interaction in tests.

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
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.11-alt1.git20150319.1
- NMU: Use buildreq for BR.

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.11-alt1.git20150319
- Version 1.2.11

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.git20141019
- Initial build for Sisyphus

